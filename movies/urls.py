from django.urls import path
from movies.views import ListaPeliculasView, DetallePeliculaView

urlpatterns = [
    path('', ListaPeliculasView.as_view(), name='lista_peliculas'),
    path('pelicula/<int:pk>/', DetallePeliculaView.as_view(),
         name='detalle_pelicula'),
]
