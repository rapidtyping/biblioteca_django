from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    pais   = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    foto = models.ImageField(upload_to='foto_autor')
# Con ImageField se creara una carpeta foto_autor para estas imagenes     
    def __unicode__(self):
        return self.nombre
