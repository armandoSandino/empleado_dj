from django.shortcuts import render
# imports models
from .models import Prueba
#
from django.views.generic import (
    TemplateView, ListView, CreateView
)

# vistas basadas en clases, nos permiten utilizar vistas genericas como
"""
TemplateView
ListView
CreateView
UpdateView
"""
class PruebaView(TemplateView):
    template_name = 'home/home.html'


class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumero'
    queryset = ['one', 'two', 'three',4,5]

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model  =  Prueba
    context_object_name = 'lista'

class CreateViewPrueba(CreateView):
    template_name = 'home/agregar.html'
    model = Prueba
    fields = ['titulo', 'subtitulo', 'cantidad']