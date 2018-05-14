from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    passwd = models.CharField(max_length=20)
    correo = models.CharField(max_length=200, default=" ")
    telefono = models.CharField(max_length=20, default=" ")
    def __str__(self):
        return self.nombre + ' - ' + self.usuario + ' - ' + self.correo + ' - ' + self.telefono
    def _get_pk_val(self, meta=None):
        return reverse('padmex:url', kwargs={'pk': self.pk})

class Producto(models.Model):
    nombreProd = models.CharField(max_length=200)
    descripcionProd = models.CharField(max_length=2000)
    precio = models.CharField(max_length=20)
    imagen = models.CharField(max_length=200, default="")
    def __str__(self):
        return self.nombreProd + ' - ' + self.precio



class Pedido(models.Model):
    cliente_FK = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(
        default = timezone.now
    )
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.cliente_FK.nombre + ' - ' + self.fecha.strftime('%Y-%M-%d') + ' - ' + self.status

class Detalle(models.Model):
    pedido_FK = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_FK = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=20)
    def __str__(self):
        return  self.producto_FK.nombreProd + ' - ' + self.cantidad

class Cita(models.Model):
    cliente_FK = models.ForeignKey(User, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=30, default=" ")
    contenido = models.TextField(default=" ")
    telefono = models.CharField(max_length=30,default= "")
    correo = models.EmailField(default="")
    fecha = models.DateTimeField(
        default=timezone.now
    )
    status = models.CharField(max_length=20, default="Por atender")
    def __str__(self):
        return self.asunto + ' - cliente: ' + self.cliente_FK.username + ' - ' + self.cliente_FK.email