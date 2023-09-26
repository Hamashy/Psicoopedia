from django.contrib import admin


from paciente.models import Paciente

# Register your models here.

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass
