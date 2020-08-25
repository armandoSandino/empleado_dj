from django.db import models

from applications.departamento.models import Departamento

class Empleado(models.Model):
    """ Modelo para tabla  empleado """

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO')
    )

    first_name = models.CharField('Nombres', max_length=60, blank=False)
    last_name = models.CharField('Apellidos', max_length=60, blank=False)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name