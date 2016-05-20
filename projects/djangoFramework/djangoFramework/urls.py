from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    url(r'debtors/', include('debtors.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^search/', include('haystack.urls')),
]

