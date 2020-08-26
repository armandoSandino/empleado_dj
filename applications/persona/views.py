from django.shortcuts import render
from  django.views.generic import ListView
# models
from .models import Empleado

class ListAllEmplados(ListView):
    template_name =  'persona/list_all.html'
    # Agregar paginacion
    paginate_by = 5
    # Ordenar resultados
    ordering = 'first_name'
    
    model = Empleado
    # puede acceder a los datos del modelo mediante 'context_object_name' o 'object_list'
    # context_object_name = 'data'
    
class  ListByAreaEmpleado(ListView):
    """ Listar todos los empleados de un area de la empresa """
    template_name = 'persona/list_all.html' 
    # filtrar empleado por departamento
    """
    queryset = Empleado.objects.filter(
        departamento__short_name ='AC'
    )
    """

    def get_queryset(self):
        # mediante 'self.kwargs['parametro']' podemos recibir parametros pasados por url a una ruta
        term = self.kwargs['termino']

        lista = Empleado.objects.filter(
            departamento__short_name=term
        )
        return  lista


class ListarEmpleadoByKword(ListView):
    """  Listar empleado por palabra clave """

    template_name = 'persona/by_kword.html'
    context_object_name = 'me_data'

    def get_queryset(self):
        # obtener valores pasados en un form mediante 'request'
        palabra_clave = self.request.GET.get('termino','')
        
        return Empleado.objects.filter(
            first_name = palabra_clave
        )