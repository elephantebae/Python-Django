from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<name>[A-Za-z_]+)$', views.process)
]
