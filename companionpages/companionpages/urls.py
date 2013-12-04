from django.conf.urls import patterns, include, url

import autocomplete_light
#autocomplete_light.registry.autocomplete_model_base = YourAutocompleteModelBase
autocomplete_light.autodiscover()

from django.contrib import admin
from compendia.views import ArticleDetailView


admin.autodiscover()

urlpatterns = patterns(
    '',
    #url(r'^$', HomeView.as_view(), name='rmc_home'),
    #url(r'^contact/', ContactView.as_view(template_name='contact.html'),
        name='envelope-contact'),
    #url(r'^faq/', FaqView.as_view(), name='rmc_faq'),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^api/v1/', include('api.urls')),
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^compendia/', include('compendia.urls', namespace="compendia")),
    url(r'^search/', include('haystack.urls')),
    # don't ask some urls got listed in a grant with this url scheme. it can never break.
    url(r'^2013-11/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='bitterlegacy'),
    url(r'^', include('home.urls', namespace="home")),
)

urlpatterns += patterns(
    'django.contrib.flatpages.views',
    url(r'^terms/', 'flatpage', {'url': '/terms/'}, name='terms'),
    url(r'^privacy/', 'flatpage', {'url': '/privacy/'}, name='privacy'),
)
