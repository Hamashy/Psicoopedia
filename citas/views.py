from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from citas.api.serializers import CitaSerializer
from citas.models import Cita

# Create your views here.


class CitaApiViewSet(ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes = [IsAdminUser]