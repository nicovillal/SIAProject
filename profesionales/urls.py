from django.urls import path
from .views import CrearProfesional, ListadoProfesional,EditarProfesional,EliminarProfesional
from django.contrib.auth.decorators import login_required


urlpatterns=[
    path('crear_profesional/',login_required(CrearProfesional.as_view()),name='crear_profesional'),
    path('listar_profesional/',login_required( ListadoProfesional.as_view()),name='listar_profesional'),
    path('editar_profesional/<int:pk>',login_required(EditarProfesional.as_view()), name='editar_profesional'),
    path('eliminar_profesional/<int:pk>', login_required(EliminarProfesional.as_view()), name='eliminar_profesional'),
]