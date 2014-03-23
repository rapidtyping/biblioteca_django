from django.conf.urls import patterns, include, url
from .views import RegistrarAutor

urlpatterns = patterns('',
    url(r'^registrar/$', RegistrarAutor.as_view(),  name="registrar_autor")

)
