from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^wall$', views.wall),
    url(r'^msgprocess$', views.msgprocess),
    url(r'^comments/(?P<id>[0-9])$', views.cmtprocess),
    url(r'^logout$', views.logout),
]