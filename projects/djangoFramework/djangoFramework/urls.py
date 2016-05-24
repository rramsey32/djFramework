from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    url(r'debtors/', include('debtors.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^debtors/search/', RedirectView.as_view(pattern_name='search/')),
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
]
