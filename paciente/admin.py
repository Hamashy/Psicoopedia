from django.contrib import admin


from paciente.models import Paciente, Practicante

# Register your models here.

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Practicante)
class PracticanteAdmin(admin.ModelAdmin):
    pass
