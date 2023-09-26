from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from consultorio.models import Consultorio



@admin.register(Consultorio)
class ConsultorioAdmin(admin.ModelAdmin):
    pass