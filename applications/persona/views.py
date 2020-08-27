from django.shortcuts import render
# Nos permite invocar rutas
from django.urls import reverse_lazy

from  django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView
)
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
        # obtener valores pasados en un form asegurado con 'csrf_token'
        palabra_clave = self.request.GET.get('termino','')
        
        return Empleado.objects.filter(
            first_name = palabra_clave
        )

class ListarEmpleadoByWorks(ListView):
    """ Listar Empleado por ocupacion/trabajo """

    # Declarar plantilla
    template_name = 'persona/filter_by_works.html'
    # Añadir paginacion
    paginate_by= 5
    # Añadir ordenamiento
    ordering = 'first_name'

    def get_queryset(self):
        # Obtenemos el parametro pasado por URL
        trabajo = self.kwargs['your_work']

        return  Empleado.objects.filter(
            job=trabajo
        )

class ListarHabilidadesEmpleados(ListView):
    """ Listar habilidades de un empleado """

    template_name = 'persona/habilidades.html'
    context_object_name = 'dataEmpleado'

    def get_queryset(self):
        try:
            # Obtener parametro
            id_empleado =  self.kwargs['key']
            # Obtener el empleado
            empleado = Empleado.objects.get(id=id_empleado)
            # Retornar sus habilidades, es una relacion Many to Many
            return empleado.habilidades.all()
        except ValueError:
            return []



class EmpleadoDetailView(DetailView):
    # En DetailView indicar el modelo a trabajar obligatoriamente
    model = Empleado
    # Declarar plantilla
    template_name =  'persona/detail_empleado.html'

    # Nos permite enviar variables extras al template, campos que no estan en nuestro modelo
    def get_context_data(self, **kwargs):
        
        context = super(EmpleadoDetailView, self ).get_context_data(**kwargs)
        # or this
        # context =  super().get_context_data(**kwargs)
        context['title'] = 'Detalle del empleado '
        return context

class SuccessViewEmpleadoCreateView(TemplateView):
    # Definir template
    template_name = 'persona/success_add_employee.html'

class EmpleadoCreateView(CreateView):

    # Definir template
    template_name = 'persona/add_employee.html'
    # Definir el modelo a utilizar es obligatorio
    model = Empleado
    # Definir campos de nuestro modelo que queremos trabajar
    # Pude indicar que se trabaje con todos los campos del modelo, asi
    # fields = (__all__)
    # Pude indicar determinados compos del modelo con los que trabajar
    # fields = ['first_name','last_name','job']
    fields = ('__all__')

    # Definir la ruta de rediccion cuando el registro se agrego correctamente, con '.' se cargara la misma pagina
    # success_url = '/success-add-employe'
    success_url = reverse_lazy('persona_app:success-employe')

    # Definir variables extras a pasar al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar empleado'
        return context


