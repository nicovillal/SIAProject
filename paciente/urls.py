from django.urls import path
from .views import CrearPaciente, ListadoPaciente,EditarPaciente,EliminarPaciente
from django.contrib.auth.decorators import login_required


urlpatterns=[
    path('crear_paciente/',login_required(CrearPaciente.as_view()),name='crear_paciente'),
    path('listar_paciente/', login_required(ListadoPaciente.as_view()),name='listar_paciente'),
    path('editar_paciente/<int:pk>',login_required(EditarPaciente.as_view()), name='editar_paciente'),
    path('eliminar_paciente/<int:pk>', login_required(EliminarPaciente.as_view()), name='eliminar_paciente'),
]