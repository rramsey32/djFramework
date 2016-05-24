from django.conf.urls import url

from . import views

app_name = 'debtors'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<debtor_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<crime_id>[0-9]+)/crime/$', views.crime, name='crime'),
    url(r'^contact/', views.contact),

]

