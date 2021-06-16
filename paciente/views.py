from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from paciente.forms import PacienteForm
from .models import paciente
# Create your views here.


class Inicio(TemplateView):
    template_name = 'index.html'






class CrearPaciente(CreateView):
    model = paciente
    form_class = PacienteForm
    template_name = 'paciente/crear_paciente.html'
    success_url = reverse_lazy('paciente:listar_paciente')