# -*- encoding:utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
#cap8 parte2
from django.template import RequestContext    
#cap8 parte2 - Con esto ya carga los archivos estáticos    
#class index(TemplateView):
#    template_name = 'inicio/index.html'

#cap8 parte2 - Otra forma de renderizar PERO FALTA
#              un parámetro para que cargue los estáticos
#class index(TemplateView):

#    def get(self, request, *args, **kwargs):
#        return render_to_response('inicio/index.html')

#cap8 parte2 - Explicación: Al no usar TemplateView se debe
#               agregar el RequestContext(request)
class index(TemplateView):

    def get(self, request, *args, **kwargs):
        return render_to_response('inicio/index.html',
                        context_instance = RequestContext(request))



    
class index2(TemplateView):
    template_name = 'inicio/index2.html'
