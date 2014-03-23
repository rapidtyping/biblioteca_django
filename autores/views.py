#from django.shortcuts import render
from django.views.generic import CreateView
from .models import Autor
# Create your views here.

class RegistrarAutor(CreateView):
    template_name = 'autores/registrarAutor.html'
    model = Autor
