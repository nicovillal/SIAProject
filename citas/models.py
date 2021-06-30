from django.db import models
from paciente.models import paciente
from profesionales.models import profesionale


# Create your models here.

class cita(models.Model):
    ACTIVA = 'Activa'
    INACTIVA = 'Inactiva'

    ESTADO_CHOICES = [(ACTIVA, 'Activa'), (INACTIVA, 'Inactiva'), ]

    id_reserva = models.AutoField(primary_key=True)
    paciente = models.ForeignKey('paciente.paciente', on_delete=models.CASCADE)
    profesional = models.ForeignKey('profesionales.profesionale', on_delete=models.CASCADE)
    fecha_cita = models.DateField(blank=True, null=True)
    hora_cita = models.TimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default=None, null=True)
    motivo_anulacion = models.CharField(max_length=100, null=True)
from django.db import models

# Create your models here.
