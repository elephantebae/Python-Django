from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^books$', views.showbooks),
    url(r'^add$', views.addbook),
    url(r'^logout$', views.logout),
    url(r'^addprocess$', views.addbookprocess)
] 