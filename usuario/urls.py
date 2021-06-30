from django.urls import path
from .views import CrearUsuario, ListadoUsuario, EditarUsuario, EliminarUsuario

urlpatterns = [
    path('crear_usuario/', CrearUsuario.as_view(), name='crear_usuario'),
    path('listar_usuario/', ListadoUsuario.as_view(), name='listar_usuario'),
    path('editar_usuario/<int:pk>', EditarUsuario.as_view(), name='editar_usuario'),
    path('eliminar_usuario/<int:pk>', EliminarUsuario.as_view(), name='eliminar_usuario'),
]
