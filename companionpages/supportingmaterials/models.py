from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, render_to_response
import autocomplete_light, logging, logging.config

from model_utils.choices import Choices
from model_utils.models import StatusModel, TimeStampedModel
from taggit.managers import TaggableManager
from django.conf.urls.static import static

from members.models import Member

RESEARCH_CHOICES = (
	("32", "Biological Sciences"),
	("27" , "Neuroscience"),
	("44" , "Cognitive neuroscience"),
	("45" , "Computational neuroscience"),
	("46" , "Developmental neuroscience"),
	("47" , "Neuroimaging"),
	("48" , "Neuroinformatics"),
	("49" , "Neurophysiology"),
	("50" , "Systems neuroscience"),
	("33", "Chemistry"),
	("34", "Computer and Information Sciences"),
	("35", "Engineering"),
	("36", "Geosciences"),
	("37", "Mathematics"),
	("38", "Medical Research"),
	("41", "Other Computational Sciences"),
	("39", "Physics"),
	("40", "Social Sciences"),
	("4" , "Econometrics"),
	("85" , "Asymptotic Theory"),
	("82" , "Bayesian Analysis"),
	("84" , "Bootstrap and Monte Carlo"),
	("94" , "Classification Methods"),
	("91" , "Duration analysis"),
	("76" , "Econometric modeling"),
	("79" , "Financial Econometrics"),
	("78" , "Forecasting"),
	("81" , "Hypothesis Testing"),
	("80" , "Microeconometrics"),
	("95" , "Neural Networks"),
	("93" , "Nonlinear econometrics"),
	("86" , "Nonparametric econometrics"),
	("87" , "Panel data models"),
	("89" , "Qualitative choice models"),
	("92" , "Regime switching models"),
	("83" , "Simultaneous equation methods"),
	("88" , "Spatial econometrics"),
	("77" , "Time-Series"),
	("90" , "Truncated and Censored Models"),
	("43" , "Economics"),
	("2" , "Agricultural, Environmental, and Energy Economics"),
	("3" , "Development and Transition Economics"),
	("5" , "Economic Theory"),
	("6" , "Experimental Economics"),
	("74" , "Experiments"),
	("70" , "Financial Economics"),
	("73" , "Game Theory"),
	("8" , "Game Theory and Decision Science"),
	("72" , "General Equilibrium"),
	("10" , "Health Economics and Management"),
	("12" , "Industrial Organization"),
	("14" , "Innovation and Entrepreneurship"),
	("16" , "International Economics"),
	("17" , "Labor Economics"),
	("18" , "Law and Economics"),
	("19" , "Macroeconomics"),
	("21" , "Microeconomics"),
	("22" , "Monetary Economics"),
	("75" , "Optimization"),
	("25" , "Public Economics and Public Choice"),
	("71" , "Real Estate"),
	("30" , "Urban, Spatial, and Regional Economics"),
	("7" , "Finance"),
	("69" , "Alternative Investments"),
	("61" , "Asset Management"),
	("53" , "Asset Pricing"),
	("54" , "Banking and Risk Management"),
	("52" , "Behavioral Finance"),
	("57" , "Corporate Finance"),
	("55" , "Derivatives"),
	("65" , "Energy and Commodities"),
	("51" , "Financial Econometrics"),
	("68" , "Financing"),
	("62" , "Fixed Income"),
	("58" , "Governance"),
	("66" , "Household Finance"),
	("64" , "International Finance"),
	("56" , "Investment"),
	("60" , "Mergers and Acquisitions"),
	("63" , "Microstructure"),
	("26" , "Real Estate"),
	("67" , "Real Option"),
	("59" , "Valuation"),
	("42" , "Management"),
	("1" , "Accounting"),
	("9" , "General Management"),
	("11" , "Human Resources Management"),
	("13" , "Information Systems"),
	("15" , "Insurance and Actuarial Science"),
	("20" , "Marketing"),
	("23" , "Operations Research"),
	("24" , "Organizational Behavior"),
	("28" , "Strategy"),
	("29" , "Technology and Operations Management"),
	("31", "Statistics"),
)

TYPE_CHOICES= (
	('1','Published Paper'),
	('2','Working Paper'),
	('3','Methods Paper'),
	('4','Negative Results'),
	('5','Public Tool'),
)

class Article(StatusModel, TimeStampedModel):
    doi = models.CharField(max_length=500, blank=True, verbose_name="DOI or PMID")
    article_url = models.URLField(blank=True, verbose_name="Paper URL")
    document = models.FileField(upload_to='papers', blank=True, verbose_name="Upload Paper")
    title = models.CharField(max_length=500)
    paper_type = models.CharField(max_length=45,blank=False,choices=TYPE_CHOICES,default='NULL')
    journal = models.CharField(blank=True, max_length=500)
    pub_date = models.DateField(verbose_name="Date")
    volume = models.CharField(max_length=50, verbose_name="Volume")
    issue = models.CharField(max_length=50,verbose_name="Issue")
    pages = models.CharField(max_length=50, verbose_name="Pages")
    abstract_text = models.TextField(max_length=2000)
    corresponding_author = models.ForeignKey(Member)
    keywords = models.CharField(blank=True, max_length=500)
    research_area = models.CharField(max_length=100,choices=sorted(RESEARCH_CHOICES, key=lambda x: x[1]), verbose_name="Primary research field")
    research_area_2 = models.CharField(max_length=100,choices=sorted(RESEARCH_CHOICES, key=lambda x: x[1]),verbose_name="Secondary research field")
    authors = models.CharField(max_length=500, verbose_name="Author 1")
    coders = models.CharField(max_length=500, verbose_name="Coder 1")
    STATUS=Choices('active', 'inactive')
    slug = models.SlugField(unique=True)
    tags = TaggableManager()
    legacy_id = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('rmc_companionpage', args=(self.id) )

    class Meta(object):
        ordering = ['title']
        verbose_name = (u'companion page')
        verbose_name_plural = (u'companion pages')
        
class Collaborator(TimeStampedModel):
    member = models.ForeignKey(Member, null=True, blank=True,
            help_text=_(u'Member account for a collaborator who is also a RunMyCode member'))
    name = models.TextField(max_length=200, help_text=_(u'The name of a collaborator'))
    coder = models.BooleanField()
    author = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta(object):
        ordering = ['name']
        verbose_name = _(u'collaborator')
        verbose_name_plural = _(u'collaborators')
        
class SupportingMaterial(StatusModel, TimeStampedModel):
    STATUS = Choices('active', 'inactive')
    companion_article = models.ForeignKey(Article)
    name = models.CharField(max_length=500)
    archive_file = models.FileField(upload_to='materials', blank=True)
    explanatory_text = models.TextField(max_length=5000, blank=True)
    materials_url = models.URLField(blank=True, help_text=_(u'URL to the supporting material. For example, '
                                                            u'if this is source code, this would be a url '
                                                            u'to to the code repository.'))
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.name
        
autocomplete_light.register(Article,
    search_fields=['doi','journal']
	#autocomplete_js_attributes = {'placeholder': 'Other model name ?'}
)

def upload_file(request):
	CompanionForm(request.POST) #UploadFileForm(request.POST)
	if request.method == 'POST':
        	form = CompanionForm() #UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
	else:
		form = CompanionForm( extra=request.POST.get('extra_author_count')) #UploadFileForm()
	return render_to_response('create.html', {'form': form})

def create_companion(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        paper = Article()
        paper.save()

