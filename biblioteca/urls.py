from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    # INICIO
    url(r'^', include('inicio.urls')),

    #AUTORES
    url(r'^autor/', include('autores.urls')),
    
    #LIBROS
    url(r'^libros/', include('libros.urls')),
    
    

    #Para que podamos ver las fotos
    # En realidad para que el navegador pueda acceder
    # a la url de nuestra imagen

    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    				{'document_root': settings.MEDIA_ROOT, }),


)
