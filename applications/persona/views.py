from django.shortcuts import render
from  django.views.generic import ListView
# models
from .models import Empleado

class ListAllEmplados(ListView):
    template_name =  'persona/list_all.html'
    model = Empleado
    # puede acceder a los datos del modelo mediante 'context_object_name' o 'object_list'
    # context_object_name = 'data'
    
