from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from citas.forms import CitaForm
from .models import cita


class ListadoCita(ListView):
    model = cita
    template_name = 'citas/listar_cita.html'
    context_object_name = 'citas'
    queryset = cita.objects.all()


class CrearCita(CreateView):
    model = cita
    form_class = CitaForm
    template_name = 'citas/crear_cita.html'
    success_url = reverse_lazy('citas:listar_cita')


class EditarCita(UpdateView):
    model = cita
    template_name = 'citas/crear_cita.html'
    form_class = CitaForm
    success_url = reverse_lazy('citas:listar_cita')

class EliminarCita(DeleteView):
    model = cita
    success_url = reverse_lazy('citas:listar_cita')
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
