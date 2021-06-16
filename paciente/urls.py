from django.urls import path
from .views import CrearPaciente


urlpatterns=[
    path('crear_paciente/',CrearPaciente.as_view(),name='crear_paciente'),
]