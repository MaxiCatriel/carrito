from django.db import models

# Create your models here.
class Producto(models.Model):
    
    nombre = models.CharField(max_length=64)    
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)
    # Categoria es una ForeignKey a la clase "Categoria"
    categoria = models.CharField(max_length=32)  

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    
    