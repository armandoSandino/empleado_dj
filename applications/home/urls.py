from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.PruebaView.as_view() ) ,
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('agregar-prueba/', views.CreateViewPrueba.as_view())
]