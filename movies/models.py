from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Pelicula(models.Model):
    # Géneros de películas (opciones predefinidas)
    GENEROS = [
        ('ACC', 'Acción'),
        ('COM', 'Comedia'),
        ('DRA', 'Drama'),
        ('SCI', 'Ciencia Ficción'),
        ('TER', 'Terror'),
        ('ANI', 'Animación'),
        ('AVT', 'Aventura'),
        ('FAN', 'Fantasía'),
        ('ROM', 'Romance'),
        ('DOC', 'Documental'),
    ]

    # Campos del modelo
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    año_lanzamiento = models.PositiveIntegerField(
        verbose_name="Año de lanzamiento",
        # Años válidos entre 1900 y 2100
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    genero = models.CharField(
        max_length=3,
        choices=GENEROS,
        verbose_name="Género"
    )
    duracion = models.PositiveIntegerField(
        verbose_name="Duración (minutos)",
        help_text="Duración en minutos"
    )
    calificacion = models.FloatField(
        verbose_name="Calificación",
        # Calificación entre 0 y 10
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="Calificación entre 0.0 y 10.0"
    )
    imagen_portada = models.ImageField(
        upload_to='peliculas/portadas/',
        verbose_name="Imagen de portada",
        blank=True,
        null=True
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    # Método para representar el objeto como una cadena
    def __str__(self):
        return self.titulo

    # Metadata adicional
    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        # Ordenar por fecha de creación (más reciente primero)
        ordering = ['-fecha_creacion']
