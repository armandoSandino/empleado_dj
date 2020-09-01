from django.contrib import admin

#registrar mi modelo para verlo desde la interfaz de administracion
from .models import Prueba

admin.site.register(Prueba)