from django.shortcuts import render
# Nos permite invocar rutas
from django.urls import reverse_lazy

from  django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
# models
from .models import Empleado
from django.http import HttpResponseRedirect

class InitView(TemplateView):
    """ Pagina de inicio """
    template_name = 'index.html'

class ListAllEmplados(ListView):
    template_name =  'persona/list_all.html'
    # Agregar paginacion
    # cuando se agrega paginacion genera implicitamente un objeto 'page_obj' y un 'paginator'
    paginate_by = 5
    # Ordenar resultados
    ordering = 'first_name'
    # Definir el modelo
    # model = Empleado

    # Definir variable que nos servira para acceder a la lista de empleados resultante
    context_object_name = 'listaEmpleado'

    # puede acceder a los datos del modelo mediante 'context_object_name' o 'object_list'
    # context_object_name = 'data'
    def get_queryset(self):
        # obtener valores pasados en un form asegurado con 'csrf_token'
        palabra_clave = self.request.GET.get('termino','')
        # __icontains busca la existencia de una cadena en otra, como funcionaria un 'like'
        return Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )


class ListaEmpladosAdmin(ListView):
    template_name =  'persona/lista_empleados.html'
    # Agregar paginacion
    # cuando se agrega paginacion genera implicitamente un objeto 'page_obj' y un 'paginator'
    paginate_by = 10
    # Ordenar resultados
    ordering = 'first_name'
    # Definir el modelo
    model = Empleado

    # Definir variable que nos servira para acceder a la lista de empleados resultante
    context_object_name = 'listaEmpleado'


class  ListByAreaEmpleado(ListView):
    """ Listar todos los empleados de un area de la empresa """
    
    # Definir template
    template_name = 'persona/list_by_area.html' 
    # Definir lista de datos a manipular desde la vista
    context_object_name = 'listEmployee'

    def get_context_data(self, **kwargs):

        context = super(ListByAreaEmpleado, self).get_context_data(**kwargs)
        context['title'] = 'Empleados en el area de ' + self.kwargs['termino'] 
        return context

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
    # Puede indicar determinados compos del modelo con los que trabajar
    fields = ['first_name','last_name','job', 'departamento', 'habilidades']
    # fields = ('__all__')

    # Definir la ruta de rediccion cuando el registro se agrego correctamente, con '.' se cargara la misma pagina
    # success_url = '/success-add-employe'
    success_url = reverse_lazy('persona_app:empleados-admin')

    # Definir variables extras a pasar al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar empleado'
        return context

    # validar datos a procesar para el modelo
    def form_valid(self, form):
        
        # Obtener los valores de los campos en el formulario
        # empleado = form.save()
        empleado = form.save(commit=False)
        # Actualizando el campo full_name
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        # Guadar los cambios
        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):

    # Definir plantilla
    template_name = 'persona/update_employee.html'
    # Definir Modelo
    model = Empleado
    # Definir campos a trabajar
    fields = ['first_name','last_name','job', 'departamento', 'habilidades']
    # Definir url de redireccion 
    success_url = reverse_lazy('persona_app:empleados-admin')

    # Definir variables extras a pasar al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Actualizar empleado'
        return context

    # Realizar algun proceso previo al guardado de datos o validaciones de datos
    # Tanto el 'post' como el 'form_valid' pueden realizar la misma tarea si ese es el caso.
    # Primeramente cuando se realiza el request a la ruta que implementa el UpdateView se ejeucta el 'post' antes del 'form_valid'    
    def form_valid(self, form):
        # Obtener valores
        employee = form.save(commit=False)
        # Actualiza determinados campos explicitamente
        full = [employee.first_name,' ', employee.last_name]
        employee.full_name = ''.join(full)
        # Guarda los cambios
        employee.save()
        return super(EmpleadoUpdateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Obtener los valores del form desde el request
        # print(request.POST), print(request.POST['first_name'])
        return super().post(request, *args, **kwargs)

class EmpleadoDeteleView(DeleteView):

    # Definir template
    template_name = 'persona/delete_employee.html'
    # Definir modelo
    model = Empleado
    # Definir ruta de redireccionamiento
    # success_url = reverse_lazy('persona_app:success-employe')

    # Definir variables extras a pasar al template
    def get_context_data(self, **kwargs):
        context =  super(EmpleadoDeteleView, self).get_context_data(**kwargs)
        context['title_delete'] = 'Borrar empleado'
        return context

    def delete(self,request,*args,**kwargs):
        # Obtener el registro a borrar
        self.object = self.get_object()
        # success_url = self.get_success_url()
        # Ruta de redireccionamiento
        success_url = reverse_lazy('persona_app:empleados-admin')
        # Borrar el registro
        self.object.delete()
        return HttpResponseRedirect(success_url)

    
