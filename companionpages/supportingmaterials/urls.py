from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from . import views
from .forms import CompanionForm

urlpatterns = patterns('',
    url(r'^$', views.CompanionArticleListView.as_view(), name='rmc_companionpages'),
#    url(r'^create/$', TemplateView.as_view(template_name='supportingmaterials/create.html'), {'form':CompanionForm}, name='rmc_create'),
	url(r'^create/$', views.CreateView.as_view(), {'form':CompanionForm}, name='rmc_create'),
	url(r'^create/doi/$', views.search, name='rmc_create_doi'),
    url(r'^(?P<pk>\d+)/$', views.CompanionArticleDetailView.as_view(), name='rmc_companionpage'),
)
