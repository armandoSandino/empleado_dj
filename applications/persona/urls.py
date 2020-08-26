from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmplados.as_view() ),
    # Esta ruta es equivalente a la posterior
    # path('lista-by-area/<termino>/', views.ListByAreaEmpleado.as_view())
    path('lista-by-area/<str:termino>/', views.ListByAreaEmpleado.as_view())
]