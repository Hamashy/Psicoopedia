from django.db import models

from consultorio.models import Consultorio
from paciente.models import Paciente, Practicante

# Create your models here.


class Cita(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    estado_cita = models.CharField(max_length=255)
    id_practicante = models.ForeignKey(Practicante, on_delete=models.CASCADE)
    
    







# class Cita(models.Model):
#     id_paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citas_paciente')
#     id_consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE, related_name='citas_consultorio')
#     fecha = models.DateTimeField()
#     estado_cita = models.CharField(max_length=255)
#     id_practicante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citas_practicante')
    
#     def __str__(self):
#         return f"Cita de {self.id_paciente.username} el {self.fecha}"
