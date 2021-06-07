from django.contrib import admin
from profesionales.models import profesionale


class ProfesinalAdmin(admin.ModelAdmin):
    list_display = (
    "rut_profesional", "nombres", "apellidos", "fecha_nac", "direccion", "num_casa", "telefono", "email")


admin.site.register(profesionale, ProfesinalAdmin)