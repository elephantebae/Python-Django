from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^shows/new$', views.addnewshows),
url(r'^createprocess$', views.createprocess),
url(r'^shows/(?P<id>[0-9]$)',views.showing),
url(r'^shows$',views.show),
url(r'^shows/(?P<id>[0-9])/edit$', views.edit),
url(r'^updateprocess/(?P<id>[0-9])$', views.updateprocess),
url(r'^shows/(?P<id>[0-9])/delete$', views.delete)
]