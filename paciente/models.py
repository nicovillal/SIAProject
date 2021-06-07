from django.db import models


# Create your models here.

class paciente(models.Model):
    id_registro = models.AutoField(primary_key=True)
    rut_paciente = models.CharField(max_length=12)
    dni_extranjero = models.CharField(max_length=9)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    fecha_nac = models.DateField(verbose_name="Fecha de nacimiento: Ejemplo 05/05/1995")
    direccion = models.CharField(max_length=30, verbose_name="Dirección")
    num_casa = models.CharField(max_length=6, verbose_name="Número de casa")
    telefono = models.CharField(max_length=9, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo Electrónico")

    def __str__(self):
        return self.nombres + " " + self.apellidos
