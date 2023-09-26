from rest_framework import serializers
from consultorio.models import Consultorio  # Asegúrate de importar tu modelo Consultorio aquí\
from rest_framework.serializers import ModelSerializer



class ConsultorioSerializer(ModelSerializer):
    class Meta:
        model = Consultorio
        fields = ['id', 'nombre', 'descripcion'] 
