from django.urls import path
from .views import CrearUsuario, ListadoUsuario, EditarUsuario, EliminarUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('crear_usuario/', login_required(CrearUsuario.as_view()), name='crear_usuario'),
    path('listar_usuario/', login_required(ListadoUsuario.as_view()), name='listar_usuario'),
    path('editar_usuario/<int:pk>',login_required(EditarUsuario.as_view()), name='editar_usuario'),
    path('eliminar_usuario/<int:pk>',login_required(EliminarUsuario.as_view()), name='eliminar_usuario'),
]
