from django.contrib import admin
from .models import Empleado, Habilidades


admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    # lista de campos a mostrar en el administrador
    list_display = (
        'id',
        'first_name',
        'last_name',
        'job',
        'departamento',
        'full_name',
    )
    # agregar valor al campo que no existe en mi modelo 'full_name'
    def full_name(self, obj ):
        #operaciones necesarias
        
        return obj.first_name + ' ' + obj.last_name

    # agregar/habilitar buscador, puede especificar laos campos por los que buscar
    search_fields = ('first_name',)
    # agregar/hablitar filtros para los campos
    list_filter = ('job','habilidades',)
    # agregar filtro horizontal unicamente para las relaciones many to many
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)
