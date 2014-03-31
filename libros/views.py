# -*- encoding:utf-8 -*-
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Libro, Autor


class BuscarView(TemplateView):
    
    # cap13 - Función que se activará al enviar el formulario
    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        libros = Libro.objects.filter(nombre__contains=buscar)
        if libros:
            print "Pregunto por un libro"
        else:
            autores = Autor.objects.filter(nombre__contains=buscar) 
            print autores 
        return render(request, 'libros/buscar.html',
            {'autores':autores, 'autor':True})
