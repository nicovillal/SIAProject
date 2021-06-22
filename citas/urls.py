from django.urls import path
from .views import CrearCita, ListadoCita,EditarCita,EliminarCita


urlpatterns=[
    path('crear_cita/',CrearCita.as_view(),name='crear_cita'),
    path('listar_cita/', ListadoCita.as_view(),name='listar_cita'),
    path('editar_cita/<int:pk>',EditarCita.as_view(), name='editar_cita'),
    path('eliminar_cita/<int:pk>', EliminarCita.as_view(), name='eliminar_cita'),
]