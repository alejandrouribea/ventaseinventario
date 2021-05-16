from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=50)
    precioCompra=models.IntegerField(verbose_name= "Precio compra")
    precioVenta=models.IntegerField(verbose_name= "Precio venta")
    existencia=models.IntegerField(verbose_name= "Existencia")
    
    def __str__(self):
        return self.nombre + self.descripcion

