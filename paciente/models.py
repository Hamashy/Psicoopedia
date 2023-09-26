from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()
    genero=models.CharField(max_length=100)
    telefono = models.IntegerField()
    zona_residencia = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=100)
    rh = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre
