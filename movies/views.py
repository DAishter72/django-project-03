from django.views.generic import ListView, DetailView
from movies.models import Pelicula


class ListaPeliculasView(ListView):
    model = Pelicula  # Modelo que se va a listar
    template_name = 'peliculas/list_pelis.html'  # Plantilla para el listado
    context_object_name = 'peliculas'  # Nombre del objeto en la plantilla
    # Ordenar por fecha de creación (más reciente primero)
    ordering = ['-fecha_creacion']


class DetallePeliculaView(DetailView):
    model = Pelicula  # Modelo que se va a detallar
    template_name = 'peliculas/det_pelis.html'  # Plantilla para los detalles
    context_object_name = 'pelicula'  # Nombre del objeto en la plantilla
