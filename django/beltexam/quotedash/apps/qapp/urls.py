from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^quotes$', views.quotes),
    url(r'^addquote$', views.addquotes),
    url(r'^showuser/(?P<id>[0-9])$', views.showuser),
    url(r'^logout$', views.logout),
    url(r'^user/(?P<id>[0-9])$', views.edituser),
    url(r'^editprocess/(?P<id>[0-9])$', views.editprocess),
    url(r'^deletequote/(?P<id>[0-9])$', views.deletequote),
    url(r'^liked/(?P<id>[0-9])$', views.likes),
]