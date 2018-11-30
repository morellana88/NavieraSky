from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Contenedor(models.Model):

    codigo = models.CharField(max_length=25)
    bahia = models.CharField(max_length=255)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return '{} -- {}'.format(self.codigo, self.bahia)

    def get_absolute_url(self):
        return reverse('contenedores', args=[str(self.id)])


class Cliente(models.Model):
    nombres  = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    pais = CountryField(blank_label='(select country)', default='SV')
    telefono = models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    def get_absolute_url(self):
        return reverse('clientes', args=[str(self.id)])


class Salida(models.Model):
    placa = models.CharField(max_length=25)
    contenedor = models.ForeignKey('Contenedor', on_delete=models.SET_NULL, null=True, default=None)
    motorista = models.ForeignKey('Motorista', on_delete=models.SET_NULL, null=True, default=None)
    cantidad = models.IntegerField()
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True, default=None)
    fecha_salida = models.DateField()

    def __str__(self):
        return "{} -- {}".format(self.contenedor, self.fecha_salida)

    def get_absolute_url(self):
        return reverse('salidas', args=[str(self.id)])


class Ingreso(models.Model):
    placa = models.CharField(max_length=25)
    contenedor = models.ForeignKey('Contenedor', on_delete=models.SET_NULL, null=True, default=None)
    motorista = models.ForeignKey('Motorista', on_delete=models.SET_NULL, null=True, default=None)
    cantidad = models.IntegerField()
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True, default=None)
    fecha_ingreso = models.DateTimeField()

    def __str__(self):
        return "{} -- {}".format(self.contenedor, self.fecha_ingreso)

    def get_absolute_url(self):
        return reverse('ingresos', args=[str(self.id)])


class Motorista(models.Model):
    nombres  = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    pais = CountryField(blank_label='(select country)', default='SV')
    telefono = models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)

    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)

    def get_absolute_url(self):
        return reverse('motoristas', args=[str(self.id)])


class Producto(models.Model):
    codigo = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=255)
    precio = models.FloatField()
    existencia = models.IntegerField(default=None)

    def __str__(self):
        return "{} -- {}".format(self.codigo, self.nombre)

    def get_absolute_url(self):
        return reverse('productos', args=[str(self.id)])
