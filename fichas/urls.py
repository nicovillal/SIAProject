from django.urls import path
from .views import CrearFicha,ListadoFicha,EditarFicha,EliminarFicha


urlpatterns=[
    path('crear_ficha/',CrearFicha.as_view(),name='crear_ficha'),
    path('listar_ficha/', ListadoFicha.as_view(),name='listar_ficha'),
    path('editar_ficha/<int:pk>',EditarFicha.as_view(), name='editar_ficha'),
    path('eliminar_ficha/<int:pk>', EliminarFicha.as_view(), name='eliminar_ficha'),


]