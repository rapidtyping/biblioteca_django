#from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Autor
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class RegistrarAutor(CreateView):
    template_name = 'autores/registrarAutor.html'
    model = Autor
    success_url = reverse_lazy('reportar_autor')

class ReportarAutor(TemplateView):
    template_name = 'autores/reportarAutor.html'

