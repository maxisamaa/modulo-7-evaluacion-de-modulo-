from django.db import models
from categorias.models import Categoria



class Producto(models.Model): # tiene una relacion de uno es a muchos con usuarios , siempre el muchos es el que recibe la clave foranea
    nombre=models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=8,decimal_places=2)
    descripcion=models.TextField()
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name='productos')
    def __str__(self):
        return self.nombre 
    

class Detalles(models.Model):
    producto=models.OneToOneField(Producto,on_delete=models.CASCADE,related_name='detalles')
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    alto=models.DecimalField(max_digits=5,decimal_places=2)
    largo=models.DecimalField(max_digits=5,decimal_places=2) # a pelicula se le adjudica un nuevo atributo llamado comentarios , que esta enlazado a Comentarios mediante clave foranea
    ancho=models.DecimalField(max_digits=5,decimal_places=2)
    fecha_ingreso=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"
    
