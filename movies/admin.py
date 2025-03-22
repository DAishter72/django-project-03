from django.contrib import admin
from movies.models import Pelicula

# Register your models here.


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'año_lanzamiento', 'genero',
                    'calificacion', 'fecha_creacion')
    list_filter = ('genero', 'año_lanzamiento')
    search_fields = ('titulo', 'descripcion')
    ordering = ('-fecha_creacion',)
