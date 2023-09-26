from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from paciente.models import Paciente, Practicante


class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class PracticanteSerializer(ModelSerializer):
    class Meta:
        model = Practicante
        fields = '__all__'