from django.db import models


# Create your models here.

class profesionale(models.Model):
    KINE = 'Kinesíologo'
    TENS = 'Técnico en Enfermería'
    OTRO = 'Otro'

    PROFESION_CHOICES = [(KINE, 'Kinesíologo'),
                         (TENS, 'Técnico en Enfermería'),
                         (OTRO, 'Otro'),
                         ]

    rut_profesional = models.CharField(max_length=12)
    nombres = models.CharField(max_length=150, verbose_name="Nombres", null=False, blank=False)
    apellidos = models.CharField(max_length=150, verbose_name="Apellidos", null=False, blank=False)
    fecha_nac = models.DateField(verbose_name="Fecha de nacimiento: Ejemplo 05/05/1995", null=False, blank=False)
    direccion = models.CharField(max_length=100, verbose_name="Dirección", null=False, blank=False)
    num_casa = models.CharField(max_length=6, verbose_name="Número de casa", null=False, blank=False)
    telefono = models.CharField(max_length=9, verbose_name="Teléfono", null=False, blank=False)
    email = models.EmailField(verbose_name="Correo Electrónico", null=False, blank=False)
    profesion = models.CharField(max_length=25, choices=PROFESION_CHOICES, default=None, null=True)

    def __str__(self):
        return self.nombres + " " + self.apellidos
