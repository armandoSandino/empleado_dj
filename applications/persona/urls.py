from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmplados.as_view() ),
    path('lista-by-area/', views.ListByAreaEmpleado.as_view())
]