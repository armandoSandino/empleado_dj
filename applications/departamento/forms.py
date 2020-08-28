from django import forms

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    departamento = forms.CharField(max_length=50, required=True)
    shortname = forms.CharField(max_length=50, required=True)
