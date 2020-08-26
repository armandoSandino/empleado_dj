from django.shortcuts import render
from  django.views.generic import ListView
# models
from .models import Empleado

class ListAllEmplados(ListView):
    template_name =  'persona/list_all.html'
    model = Empleado
    # puede acceder a los datos del modelo mediante 'context_object_name' o 'object_list'
    # context_object_name = 'data'
    
class  ListByAreaEmpleado(ListView):
    """ Listar todos los empleados de un area de la empresa """
    template_name = 'persona/list_all.html' 
    # filtrar empleado por departamento
    queryset = Empleado.objects.filter(
        departamento__short_name ='AC'
    ) 
