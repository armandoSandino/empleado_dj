from django.contrib import admin
from .models import Empleado, Habilidades


admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job',
        'departamento',
    )

admin.site.register(Empleado, EmpleadoAdmin)
