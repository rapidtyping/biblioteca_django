from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    pais   = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
#   Se debe instalar la libreria PIL 8(Ver tut 06 django de devcodelab)
#    foto = models.ImageField(upload_to='foto_autor')
