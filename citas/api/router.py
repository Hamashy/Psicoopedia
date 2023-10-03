from rest_framework.routers import DefaultRouter

from citas.views import CitaApiViewSet


router_cita = DefaultRouter()

router_cita.register(prefix='citas', basename='citas', viewset=CitaApiViewSet)