from django.db import models

# Create your models here.
class Consultorio(models.Model):
    nombre = models.CharField(max_length=100)  # Campo de texto para el nombre del consultorio
    descripcion = models.TextField()  # Campo de texto largo para la descripción del consultorio

    def __str__(self):
        return self.nombre
