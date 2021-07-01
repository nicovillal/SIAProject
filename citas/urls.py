from django.urls import path
from .views import CrearCita, ListadoCita,EditarCita,EliminarCita
from django.contrib.auth.decorators import login_required


urlpatterns=[
    path('crear_cita/',login_required(CrearCita.as_view()),name='crear_cita'),
    path('listar_cita/',login_required(ListadoCita.as_view()),name='listar_cita'),
    path('editar_cita/<int:pk>',login_required(EditarCita.as_view()), name='editar_cita'),
    path('eliminar_cita/<int:pk>', login_required(EliminarCita.as_view()), name='eliminar_cita'),
]