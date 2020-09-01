from django.shortcuts import render
from django.urls import reverse_lazy
# Form
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
# Model
from applications.persona.models import Empleado
from .models import Departamento

from django.views.generic import ListView

class NewRegisterDepartmentView(FormView):
    # Definir tamplate
    template_name = 'departamento/new_department.html'
    # Definir el formulario a implementar
    form_class = NewDepartamentoForm
    # Definir ruta de redireccionamiento
    # success_url = '/'
    success_url = reverse_lazy('department_app:all-department')
    

    def get_context_data(self, **kwargs):
        context = super(NewRegisterDepartmentView, self).get_context_data(**kwargs)
        context['title'] = 'Registrar nuevo departamento'
        return context
    

    def form_valid(self, form):
        # Aacceder a los valores de los campos del formulario
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        
        # Crear un registro de departamento para obtener su referencia y agregarlo como llave foranea en Empleado
        depart = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname']
        )
        depart.save()

        # Crear un registro en base al modelo Empleado
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            full_name= ''.join([nombre,apellido]),
            job='1',
            departamento=depart
        )
        return super(NewRegisterDepartmentView, self).form_valid(form)



class ListAllDepartment(ListView):
    """ Listar todo  """
    template_name = 'departamento/list_all.html'
    
    # Definir variable que nos servira para acceder a la lista de empleados resultante
    # puede acceder a los datos del modelo mediante 'context_object_name' o 'object_list'
    # context_object_name = 'data'
    context_object_name = 'listDepartment'

    # Agregar paginacion
    # cuando se agrega paginacion genera implicitamente un objeto 'page_obj' y un 'paginator'
    paginate_by=4
    ordering = 'name'

    # Nos permite enviar variables extras al template, campos que no estan en nuestro modelo
    def get_context_data(self, **kwargs):
        context = super(ListAllDepartment, self).get_context_data(**kwargs)
        context['titulo'] = 'Todos los departamentos'

        return context

    def get_queryset(self):
        # obtener valores pasados en un form asegurado con 'csrf_token'
        search_term = self.request.GET.get('termino','')
         # __icontains busca la existencia de una cadena en otra, como funcionaria un 'like'
        return Departamento.objects.filter(
            name__icontains = search_term
        )
