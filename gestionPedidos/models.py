from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombrecito")
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank = True, null=True)
    tfno = models.CharField(max_length=7)


class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.FloatField()

    def __str__(self) :
        return 'el nombre es %s la seccion es %s y su precio es %s'%(self.nombre, self.seccion, self.precio)
    

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entrega = models.BooleanField()

