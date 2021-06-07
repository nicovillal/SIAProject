from django.db import models


# Create your models here.

class profesionale(models.Model):
    KINE = '0'
    ENFERMERA = '1'
    TENS = '2'
    PROFESION_4 = '3'

    PROFESION_CHOICES = [(KINE, 'Kinesiologo'),
                         (ENFERMERA, 'Enfermera'),
                         (TENS, 'Tens'),
                         (PROFESION_4, 'Profesión 4'),
                         ]

    rut_profesional = models.CharField(max_length=12)
    nombres = models.CharField(max_length=150, verbose_name="Nombres", null=False, blank=False)
    apellidos = models.CharField(max_length=150, verbose_name="Apellidos", null=False, blank=False)
    fecha_nac = models.DateField(verbose_name="Fecha de nacimiento: Ejemplo 05/05/1995", null=False, blank=False)
    direccion = models.CharField(max_length=100, verbose_name="Dirección", null=False, blank=False)
    num_casa = models.CharField(max_length=6, verbose_name="Número de casa", null=False, blank=False)
    telefono = models.CharField(max_length=9, verbose_name="Teléfono", null=False, blank=False)
    email = models.EmailField(verbose_name="Correo Electrónico", null=False, blank=False)
    profesion = models.CharField(max_length=11, choices=PROFESION_CHOICES, default=None, null=True)

    def __str__(self):
        return self.nombres + " " + self.apellidos
