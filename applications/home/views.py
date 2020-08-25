from django.shortcuts import render
#
from django.views.generic import TemplateView, ListView

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
