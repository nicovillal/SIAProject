from django.contrib import admin
from paciente.models import paciente


# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        "rut_paciente", "dni_extranjero", "nombres", "apellidos", "fecha_nac", "direccion", "num_casa", "telefono",
        "email")


admin.site.register(paciente, PacienteAdmin)
