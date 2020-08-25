from django.contrib import admin
from django.urls import path

def message(self):
    print('== llamada a la ruta de persona ==')

urlpatterns = [
    path('persona', message)
]