from django.db import models

class Peliculas(models.Model):
    nombre = models.CharField(max_length=50)
    descipcion = models.CharField(max_length=500)
    def __str__(self) -> str:
        return f'{self.nombre}'

class Director(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=30)
    pelicula = models.ForeignKey(Peliculas,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'
# Create your models here.
