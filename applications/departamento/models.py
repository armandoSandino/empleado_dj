from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, default='', blank= False)
    short_name = models.CharField('Nombre corto', max_length=20, default='', blank=False)
    anulate = models.BooleanField('Anulado', default=False, blank=False)

    def __str__(self):
        return self.name
