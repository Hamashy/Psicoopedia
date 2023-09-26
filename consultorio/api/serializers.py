from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from consultorio.models import Consultorio  # Asegúrate de importar tu modelo Consultorio aquí\


class ConsultorioSerializer(ModelSerializer):
    class Meta:
        model = Consultorio
        fields = ['id', 'nombre', 'descripcion'] 
