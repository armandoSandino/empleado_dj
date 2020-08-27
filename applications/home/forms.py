from django import forms
#Models
from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        # Definir modelo a utilizar
        model = Prueba
        # Definir campos del modelo a utilizar
        # fields = ('__all__')
        fields = ('titulo', 'subtitulo', 'cantidad',)
        # Personalizar estilo,atributos 
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class': 'caja',
                    'title': 'Ingrese un titulo'
                }
            ),
            'subtitulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Debe ingreser un titulo',
                    'class': 'caja',
                    'title': 'Favor ingrese un subtitulo'
                }
            ),
            'cantidad': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese una cantidad',
                    'class': 'caja',
                    'title': 'Favor ingrese una cantidad'
                }
            )
        }
    # Agregar validacion para el campo 'cantidad' simpre debes especificar la palabra clave 'clean'
    def clean_cantidad(self):
        # Obtener el valor del campo
        dato = self.cleaned_data['cantidad']
        if dato < 10:
            # mostrar mensaje informativo en el form
            raise forms.ValidationError('Ingrese una cantidad mayor a 10')
                
        return dato
