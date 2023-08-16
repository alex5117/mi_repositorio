from django.db import models

# Create your models here.
class stock_limpieza(models.Model):

    producto = models.CharField(max_length = 40)
    precio = models.IntegerField()
    envase = models.CharField(max_length = 40)
    stock = models.IntegerField()

class stock_comida(models.Model):
    producto = models.CharField(max_length = 40)
    precio = models.IntegerField()
    bolsa = models.CharField(max_length = 40)
    stock = models.CharField(max_length = 40)

class stock_veneno(models.Model):
    producto = models.CharField(max_length = 40)
    precio = models.IntegerField()
    envase = models.CharField(max_length = 40)
    stock = models.CharField(max_length = 40)

class stock_pago(models.Model):
    efectivo = models.IntegerField()
    uala = models.IntegerField()
    mercado_pago = models.IntegerField()
    banco_provincia = models.IntegerField()
