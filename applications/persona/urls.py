from django.contrib import admin
from django.urls import path
from . import views

# Variable con la que invocaremos rutas desde codigo utilizando 'reverse_lazy'
app_name = 'persona_app'

urlpatterns = [
    # Inicio
    path('', views.InitView.as_view(), name='inicio'),
    path('listar-todo-empleados/', views.ListAllEmplados.as_view(), name='all-employe' ),
    path('buscar-empleado/', views.ListarEmpleadoByKword.as_view() ),
    path('listar-by-work/<your_work>/', views.ListarEmpleadoByWorks.as_view() ),
    path('listar-habilidad-empleado/<key>/', views.ListarHabilidadesEmpleados.as_view()),
    # Esta ruta es equivalente a la posterior
    # path('lista-by-area/<termino>/', views.ListByAreaEmpleado.as_view())
    path('lista-by-area/<str:termino>/', views.ListByAreaEmpleado.as_view()),
    
    # Implementando DetailView el 'pk' es importante aqui
    path('ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='detail-employe' ),
    # Implementando CreateView
    path('agregar-empleado/', views.EmpleadoCreateView.as_view() ),
    # Ruta para mostrar mensaje de usuario agregado
    path('success-add-employe/', views.SuccessViewEmpleadoCreateView.as_view(), name='success-employe'),
    # Implementando UpdateView, el pk es importante aqui
    path('actualizar-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='update-employe'),
    # Implementando DeleteView, el pk es importante
    path('borrar-empleado/<int:pk>/', views.EmpleadoDeteleView.as_view(), name='delete-employe')
]