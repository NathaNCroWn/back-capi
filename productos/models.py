from django.db import models

class Producto(models.Model):
    productoNombre= models.CharField(max_length=150)
    productoImg= models.ImageField(upload_to='productoimg/')
    productoDescripcion= models.TextField()
    productoDescripcionSimple= models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=0, blank=True,)
