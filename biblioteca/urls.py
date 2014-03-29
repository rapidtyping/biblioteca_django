from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biblioteca.views.home', name='home'),
    url(r'^', include('inicio.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^autor/', include('autores.urls')),

    #Para que podamos ver las fotos
    # En realidad para que el navegador pueda acceder
    # a la url de nuestra imagen

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    				{'document_root': settings.MEDIA_ROOT, }),


)
