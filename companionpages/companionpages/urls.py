from django.conf.urls import patterns, include, url

<<<<<<< HEAD
import autocomplete_light
#autocomplete_light.registry.autocomplete_model_base = YourAutocompleteModelBase
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()
=======
from compendia.views import ArticleDetailView

>>>>>>> upstream/master

admin.autodiscover()

urlpatterns = patterns(
    '',
<<<<<<< HEAD
    url(r'^$', HomeView.as_view(), name='rmc_home'),
    url(r'^members/edit', 'profiles.views.edit_profile', {'form_class': MemberForm,}, name='rmc_edit'),
    url(r'^members/', include('profiles.urls')),
    # profiles/create/ named profiles_create_profile
    # profiles/edit/ named profiles_edit_profile
    # profiles/username named profiles_profile_detail
    # profiles/ named profiles_profile_list
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact/', ContactView.as_view(template_name='contact.html'),
        name='envelope-contact'),
    url(r'^faq/', FaqView.as_view(), name='rmc_faq'),
    url(r'^news/', include('news.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^companionpages', include('supportingmaterials.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),

=======
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
>>>>>>> upstream/master
)

urlpatterns += patterns(
    'django.contrib.flatpages.views',
<<<<<<< HEAD
    url(r'^about/', 'flatpage', {'url': '/about/'}, name='rmc_about'),
    url(r'^terms/', 'flatpage', {'url': '/terms/'}, name='rmc_terms'),
    url(r'^privacy/', 'flatpage', {'url': '/privacy/'}, name='rmc_privacy'),
=======
    url(r'^terms/', 'flatpage', {'url': '/terms/'}, name='terms'),
    url(r'^privacy/', 'flatpage', {'url': '/privacy/'}, name='privacy'),
>>>>>>> upstream/master
)
