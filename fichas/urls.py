from django.urls import path
from .views import CrearFicha,ListadoFicha,EditarFicha,EliminarFicha
from django.contrib.auth.decorators import login_required


urlpatterns=[
    path('crear_ficha/',login_required(CrearFicha.as_view()),name='crear_ficha'),
    path('listar_ficha/', login_required(ListadoFicha.as_view()),name='listar_ficha'),
    path('editar_ficha/<int:pk>',login_required(EditarFicha.as_view()), name='editar_ficha'),
    path('eliminar_ficha/<int:pk>', login_required(EliminarFicha.as_view()), name='eliminar_ficha'),


]