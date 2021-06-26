from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from fichas.forms import FichaForm
from .models import ficha


class ListadoFicha(ListView):
    model = ficha
    template_name = 'fichas/listar_ficha.html'
    context_object_name = 'fichas'
    queryset = ficha.objects.all()


class CrearFicha(CreateView):
    model = ficha
    form_class = FichaForm
    template_name = 'fichas/crear_ficha.html'
    success_url = reverse_lazy('fichas:listar_ficha')


class EditarFicha(UpdateView):
    model = ficha
    template_name = 'fichas/crear_ficha.html'
    form_class = FichaForm
    success_url = reverse_lazy('fichas:listar_ficha')

class EliminarFicha(DeleteView):
    model = ficha
    success_url = reverse_lazy('fichas:listar_ficha')


