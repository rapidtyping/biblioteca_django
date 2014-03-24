# -*- encoding: utf-8 -*-
#from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from .models import Autor
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class RegistrarAutor(CreateView):
    template_name = 'autores/registrarAutor.html'
    model = Autor
    success_url = reverse_lazy('reportar_autor')

# class ReportarAutor(TemplateView):
#     template_name = 'autores/reportarAutor.html'

# Devolverá una lista de objetos
class ReportarAutor(ListView):
	template_name = 'autores/reportarAutor.html'
	# El modelo del cual se extraerá información
	model = Autor
	# cambiar el nombre por defecto 'object_list'
	context_object_name = 'autores'
