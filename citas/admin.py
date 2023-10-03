from django.contrib import admin

from citas.models import Cita

# Register your models here.

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    pass