from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from paciente.models import Paciente, Practicante
from paciente.api.serializers import PacienteSerializer, PracticanteSerializer




class PacienteApiViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAdminUser]


class PracticanteApiViewSet(ModelViewSet):
    queryset = Practicante.objects.all()
    serializer_class = PracticanteSerializer
    permission_classes = [IsAdminUser]
    