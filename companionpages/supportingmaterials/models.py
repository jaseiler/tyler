from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, render_to_response

from model_utils.choices import Choices
from model_utils.models import StatusModel, TimeStampedModel
from taggit.managers import TaggableManager
from django.conf.urls.static import static

from members.models import Member
from .forms import UploadFileForm, CompanionForm, Article

@receiver(post_save, sender=User)
def create_companion(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        paper = Article()
        paper.save()
        
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
        
def handle_uploaded_file(request):
    """ stub """
    # maybe this didn't get checked in yet?
    pass

def search_doi(request):
	#http://doi.crossref.org/servlet/query?pid=jas2385@columbia.edu&format=info&id={{DOI}}
	return render_to_response('create.html', {'form': form})

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
