from django.contrib import admin
from django.urls import path
# Views
from . import views

app_name = 'prueba_app'

urlpatterns = [
    path('home/', views.PruebaView.as_view() ) ,
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('agregar-prueba/', views.PruebaCreateView.as_view(), name='add-test'),
    path('resume-foundation/', views.ResumeFoundationTemplateView.as_view(), name='re-found' )
]