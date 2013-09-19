from django import forms
from django.forms import ModelForm, RadioSelect, ChoiceField
from model_utils.models import StatusModel, TimeStampedModel
from model_utils.choices import Choices
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views import generic

from django.db import models
from members.models import Member
from taggit.managers import TaggableManager
from .models import Article

class CompanionForm(ModelForm):
	class Meta:
		model = Article
		extra_author_count = models.CharField()
		exclude = ['status','modified','status_changed','slug','legacy_id','tags',]
		#fields = ['doi','corresponding_author', 'title', 'abstract_text','document', 'journal','article_url']
		widgets = {
            'doi' : forms.TextInput(attrs = {'placeholder': 'will autocomplete paper info','style':'width:200px;'}),
            'article_url' : forms.TextInput(attrs = {'placeholder': 'will autocomplete paper info','style':'width:200px; '}),
            'title' : forms.TextInput(attrs = {'placeholder': 'Title of the publication','style':'width:90%;'}),
            'journal' : forms.TextInput(attrs = {'placeholder': 'journal name','style':'width:400px;'}),
            'document' : forms.FileInput(attrs = {'style':'width:400px; float:right;'}),
            'paper_type' : RadioSelect(),
            'pub_date' : forms.DateInput(format=['%m %Y'], attrs = {'placeholder': 'month year','style':'width:100px;'}),
            'volume' : forms.TextInput(attrs = {'placeholder': 'vol','style':'width:100px;'}),
            'issue' : forms.TextInput(attrs = {'placeholder': 'issue#','style':'width:100px;'}),
            'pages' : forms.TextInput(attrs = {'placeholder': '1550-1487','style':'width:100px;'}),
            'abstract_text': forms.Textarea(attrs = {'placeholder':'abstract for this project does not need to match paper abstract','style':"width: 95%; height: 200px; padding: 5px; margin-bottom: 15px;border-radius:6px;"}),
            'keywords' : forms.TextInput(attrs = {'placeholder': 'blackholes, MCMC, finite element','style':'width:80%;'}),
            'authors' : forms.TextInput(attrs = {'placeholder': 'John Smith','style':'width:50%;'}),
			'extra_author_count': forms.HiddenInput(),
        }
    	def __init__(self, *args, **kwargs):
    		super(CompanionForm, self).__init__(*args, **kwargs)
    		extra_fields = kwargs.pop('extra', 0)
    		#self.fields['extra_author_count'].initial = extra_fields
    		for index in range(extra_fields):
    			self.fields['extra_author_{index}'.format(index=index)] = \
                	models.CharField(max_length=500)
                	
def myview(request):
	if request.method == 'POST':
		form = CompanionForm(request.POST, extra=request.POST.get('extra_author_count'))
	else:
		form = CompanionForm()
	return render(request, "create.html", { 'form': form })     

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()