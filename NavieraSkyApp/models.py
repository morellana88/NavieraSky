from django.db import models
from django.urls import reverse


class Contenedores(models.Model):

    codigo = models.CharField(max_length=25)
    bahia = models.CharField(max_length=255)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.codigo

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('detalle-contenedor', args=[str(self.id)])
