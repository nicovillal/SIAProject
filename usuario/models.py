from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def _create_user(self, username, nombres, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            nombres=nombres,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, nombres, email,password=None, **extra_fields):
        return self._create_user(username, nombres, email, password, False, False, **extra_fields)

    def create_superuser(self, username,  nombres, email, password=None, **extra_fields):
        return self._create_user(username,  nombres,email, password, True, True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(verbose_name="Nombre de Usuario",unique=True, max_length= 100)
    nombres = models.CharField(max_length=40,blank=True, null=True)
    apellidos = models.CharField(max_length=40, blank=True, null=True)
    telefono = models.CharField(max_length=9, verbose_name="Teléfono", blank=True, null=True)
    email = models.EmailField(verbose_name="Correo Electrónico",unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD='username'
    REQUIRED_FIELDS =['nombres','apellidos','telefono','email']

    def __str__(self):
        return f'{self.nombres}, {self.apellidos}, {self.telefono},{self.email}'
