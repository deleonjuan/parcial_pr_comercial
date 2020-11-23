from django.db import models

class Pelicula(models.Model):
    ROMANCE = 'romance'
    ACCION = 'accion'
    COMEDIA = 'comedia'
    TERROR = 'terror'
    SIFI = 'sifi'
    ANIMACION = 'animacion'
    MUSICAL = 'musical'

    GENEROS = (
        (ROMANCE, 'romance'),
        (ACCION, 'accion'),
        (COMEDIA, 'comedia'),
        (TERROR, 'terror'),
        (SIFI, 'sifi'),
        (ANIMACION, 'animacion'),
        (MUSICAL, 'musical')
    )

    titulo = models.CharField(max_length=255, default='')
    descripcion = models.TextField()
    portada = models.TextField()
    estreno = models.CharField(max_length=5)
    genero = models.CharField(max_length=10, choices=GENEROS, default=ROMANCE)