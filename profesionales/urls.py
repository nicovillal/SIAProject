from django.urls import path
from .views import CrearProfesional, ListadoProfesional,EditarProfesional,EliminarProfesional


urlpatterns=[
    path('crear_profesional/',CrearProfesional.as_view(),name='crear_profesional'),
    path('listar_profesional/', ListadoProfesional.as_view(),name='listar_profesional'),
    path('editar_profesional/<int:pk>',EditarProfesional.as_view(), name='editar_profesional'),
    path('eliminar_profesional/<int:pk>', EliminarProfesional.as_view(), name='eliminar_profesional'),
]