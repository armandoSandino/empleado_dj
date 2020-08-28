from django.shortcuts import render
from django.urls import reverse_lazy
# Form
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
# Model
from applications.persona.models import Empleado
from .models import Departamento

class NewRegisterDepartmentView(FormView):
    # Definir tamplate
    template_name = 'departamento/new_department.html'
    # Definir el formulario a implementar
    form_class = NewDepartamentoForm
    # Definir ruta de redireccionamiento
    success_url = '/'


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
