from django.contrib import admin
from .models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'resumen', 'imagen_portadas')
    # Recuerda terminar con una coma la tupla de un elemento
    list_filter = ('autor',)
    search_fields = ('nombre' , 'autor__nombre')
    # El primer item de la lista debe diferir de 'list_display'
    # por ello ponemos id en 'list_display'
    list_editable = ('nombre', 'resumen')
    # Crea una nueva estructura para agregar autores
    filter_horizontal = ('autor',)
    
        
    def imagen_portadas(self, libro):
        url = libro.traer_url_portadas()
        tag = "<img src='%s' >" % url
        return tag
        
    imagen_portadas.allow_tags = True
admin.site.register(Libro, LibroAdmin)
