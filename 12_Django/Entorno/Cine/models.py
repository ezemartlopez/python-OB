from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=35,help_text='Nombre de la pelicula')
    descripcion = models.TextField(max_length=500,help_text='Descripcion de la pelicula')
    def __str__(self) -> str:
        return self .titulo
    def title(self):
        return self.titulo
    def desc(self):
        return self.descripcion

class Director(models.Model):
    name = models.CharField(max_length=64,help_text='Ingrese el nombre del director')
    peliculas = models.ManyToManyField(Pelicula)
    def __str__(self):
        return self.name

    def info(self):
        string = ''
        for pelicula in self.peliculas.all():
            string+=f'Titulo: {pelicula.title()}\n\tdescripcion: {pelicula.desc()}\n'
        return string


