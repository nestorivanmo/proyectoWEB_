from django.db import models

# Create your models here.

class Cliente(models.Model):
    #id_cliente = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre + ' - ' + self.usuario

class Pedidos(models.Model):
    #id_pedido
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField
    status = models.CharField(max_length=20)