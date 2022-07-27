from django.contrib import admin
from .models import Peliculas,Director

class PeliculasAdministrador(admin.ModelAdmin):
    list_display = ['id','nombre','descipcion']

class DirectorAdmin(admin.ModelAdmin):
    list_display= ['id','nombre','apellido','pelicula']

admin.site.register(Peliculas,PeliculasAdministrador)
admin.site.register(Director,DirectorAdmin)
# Register your models here.
