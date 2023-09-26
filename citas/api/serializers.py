from rest_framework.serializers import ModelSerializer

from citas.models import Cita





class CitaSerializer(ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'