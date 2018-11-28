from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.numgen),
    url(r'^reset', views.delete)
]