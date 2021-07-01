from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from paciente.forms import PacienteForm
from .models import paciente


# Create your views here.


class Inicio(TemplateView):
    template_name = 'index.html'


class ListadoPaciente(ListView):
    model = paciente
    template_name = 'paciente/listar_paciente.html'
    context_object_name = 'pacientes'
    queryset = paciente.objects.all()
    paginate_by: 10


class CrearPaciente(CreateView):
    model = paciente
    form_class = PacienteForm
    template_name = 'paciente/crear_paciente.html'
    success_url = reverse_lazy('paciente:listar_paciente')


class EditarPaciente(UpdateView):
    model = paciente
    template_name = 'paciente/crear_paciente.html'
    form_class = PacienteForm
    success_url = reverse_lazy('paciente:listar_paciente')

class EliminarPaciente(DeleteView):
    model = paciente
    success_url = reverse_lazy('paciente:listar_paciente')
