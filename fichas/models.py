from django.db import models
from paciente.models import paciente
from profesionales.models import profesionale


# Create your models here.

class ficha(models.Model):
    paciente = models.ForeignKey('paciente.paciente', on_delete=models.CASCADE)
    profesional = models.ForeignKey('profesionales.profesionale', on_delete=models.CASCADE)
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    receta = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
