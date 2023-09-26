from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from consultorio.models import Consultorio

from consultorio.api.serializers import ConsultorioSerializer

class ConsultorioApiViewSet(ModelViewSet):
    queryset = Consultorio.objects.all()
    serializer_class = ConsultorioSerializer
    permission_classes = [IsAdminUser]






    
