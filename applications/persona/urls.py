from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmplados.as_view() ),
    path('buscar-empleado/', views.ListarEmpleadoByKword.as_view() ),
    path('listar-by-work/<your_work>/', views.ListarEmpleadoByWorks.as_view() ),
    path('listar-habilidad-empleado/<key>/', views.ListarHabilidadesEmpleados.as_view()),
    # Esta ruta es equivalente a la posterior
    # path('lista-by-area/<termino>/', views.ListByAreaEmpleado.as_view())
    path('lista-by-area/<str:termino>/', views.ListByAreaEmpleado.as_view())
]