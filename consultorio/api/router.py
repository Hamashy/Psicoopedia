from django.db import router
from rest_framework.routers import DefaultRouter

from consultorio.api.views import ConsultorioApiViewSet



router_consultorio = DefaultRouter()

router_consultorio.register(prefix='consultorios', basename='consultorios', viewset=ConsultorioApiViewSet)




