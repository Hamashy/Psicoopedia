from rest_framework.routers import DefaultRouter

# from psicoopedia.paciente.api.views import PacienteApiViewSet

from .views import PacienteApiViewSet





router_paciente = DefaultRouter()

router_paciente.register(prefix='pacientes', basename='pacientes', viewset=PacienteApiViewSet)


