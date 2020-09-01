from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, default='', blank= False)
    short_name = models.CharField('Nombre corto', max_length=20, default='',unique=True, blank=False)
    anulate = models.BooleanField('Anulado', default=False, blank=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'All department'
        ordering = ['-name']
        unique_together = ('name', 'short_name') 

    def __str__(self):
        return self.name
