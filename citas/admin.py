from django.contrib import admin
from citas.models import cita


class citasAdmin(admin.ModelAdmin):
    list_display = ("id_reserva", "paciente", "profesional", "fecha_cita", "estado", "motivo_anulacion")


admin.site.register(cita, citasAdmin)
