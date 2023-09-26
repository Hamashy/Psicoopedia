from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from paciente.models import Paciente
from paciente.api.serializers import PacienteSerializer




class PacienteApiViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAdminUser]
    