from django.urls import path
from .views import CrearPaciente, ListadoPaciente,EditarPaciente,EliminarPaciente


urlpatterns=[
    path('crear_paciente/',CrearPaciente.as_view(),name='crear_paciente'),
    path('listar_paciente/', ListadoPaciente.as_view(),name='listar_paciente'),
    path('editar_paciente/<int:pk>',EditarPaciente.as_view(), name='editar_paciente'),
    path('eliminar_paciente/<int:pk>', EliminarPaciente.as_view(), name='eliminar_paciente'),
]