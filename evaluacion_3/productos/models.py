from pickle import FALSE, TRUE
from tokenize import blank_re
from django.db import models

# Create your models here.
class Productos(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    disponible = models.BooleanField()
    precio = models.IntegerField(null=True)
    imagen = models.ImageField(upload_to="static", null=True)

    def __int__(self):
        return self.codigo

class Boleta(models.Model):
    idboleta = models.IntegerField()
    nombreProd = models.CharField(max_length=30)
    detalle = models.CharField(max_length=30)
    fecha = models.DateField()
    valor= models.IntegerField()
    Total = models.IntegerField()

class cliente(models.Model):
    idcliente = models.IntegerField()
    nombre = models.CharField(max_length=30)
    registro = models.BooleanField()
    correoCliente = models.EmailField()

class usuario(models.Model):
    nombreUsuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    suscripcion = models.BooleanField()
    logueado = models.BooleanField(default = 0)
