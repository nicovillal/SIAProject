from django.db import models
from paciente.models import paciente
from profesionales.models import profesionale


# Create your models here.

class cita(models.Model):
    ACTIVA = '0'
    INACTIVA = '1'

    ESTADO_CHOICES = [(ACTIVA, 'Activa'), (INACTIVA, 'Inactiva'), ]

    id_reserva = models.AutoField(primary_key=True)
    paciente = models.ForeignKey('paciente.paciente', on_delete=models.CASCADE)
    profesional = models.ForeignKey('profesionales.profesionale', on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default=None, null=True)
    motivo_anulacion = models.CharField(max_length=100, null=True)
