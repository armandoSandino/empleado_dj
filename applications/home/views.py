from django.shortcuts import render
#
from django.views.generic import TemplateView

# vistas basadas en clases, nos permiten utilizar vistas genericas como
"""
TemplateView
ListView
CreateView
UpdateView
"""
class PruebaView(TemplateView):
    template_name = 'home/home.html'
