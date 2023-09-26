from rest_framework.routers import DefaultRouter

# from psicoopedia.paciente.api.views import PacienteApiViewSet

from .views import PacienteApiViewSet, PracticanteApiViewSet





router_paciente = DefaultRouter()
router_practicante = DefaultRouter()

router_paciente.register(prefix='pacientes', basename='pacientes', viewset=PacienteApiViewSet)

router_practicante.register(prefix='practicantes', basename='practicantes', viewset=PracticanteApiViewSet)


