from django.contrib import admin
from fichas.models import ficha


class FichaAdmin(admin.ModelAdmin):
    list_display = ("paciente", "profesional", "diagnostico", "tratamiento","costo", "receta", "fecha", "hora")


admin.site.register(ficha, FichaAdmin)
