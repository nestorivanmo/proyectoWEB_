from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    passwd = models.CharField(max_length=20)
    correo = models.CharField(max_length=200, default=" ")
    telefono = models.CharField(max_length=20, default=" ")
    def __str__(self):
        return self.nombre + ' - ' + self.usuario + ' - ' + self.correo + ' - ' + self.telefono

class Producto(models.Model):
    nombreProd = models.CharField(max_length=200)
    descripcionProd = models.CharField(max_length=2000)
    precio = models.CharField(max_length=20)
    imagen = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.nombreProd + ' - ' + self.precio

class Pedido(models.Model):
    cliente_FK = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(
        default = timezone.now
    )
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.cliente_FK + ' - ' + self.fecha + ' - ' + self.status

class Detalle(models.Model):
    pedido_FK = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_FK = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=20)
    def __str__(self):
        return self.pedido_FK + ' - ' + self.producto_FK + ' - ' + self.cantidad

class Cita(models.Model):
    cliente_FK = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(
        default=timezone.now
    )
    status = models.CharField(max_length=20, default="Por atender")
    def __str__(self):
        return self.cliente_FK + ' - ' + self.fecha + ' - ' + self.status