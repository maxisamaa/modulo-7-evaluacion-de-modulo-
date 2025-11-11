from django.db import models
from productos.models import Producto  # Asegúrate de ajustar el import según tu estructura real

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    productos = models.ManyToManyField(Producto, related_name='etiquetas', blank=True) # producto tiene ahora el atributo etiquetas 

    def __str__(self):
        return self.nombre
    
class ProductoEtiqueta(models.Model):
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    etiqueta = models.ForeignKey('Etiqueta', on_delete=models.CASCADE)