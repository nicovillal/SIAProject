from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from paciente.forms import PacienteForm
from .models import paciente
from django.shortcuts import render
from django.db.models import Q


# Create your views here.


class Inicio(TemplateView):
    template_name = 'index.html'


class ListadoPaciente(ListView):
    model = paciente
    template_name = 'paciente/listar_paciente.html'
    paginate_by= 10
    form_class=PacienteForm

    def get_queryset(self):
        parametro = self.request.GET.get("buscar", None)
        print(parametro)
        queryset = paciente.objects.all()
        if parametro:
            queryset = paciente.objects.filter(
                Q(nombres__icontains=parametro)|
                Q(apellidos__icontains=parametro)|
                Q(rut_paciente__icontains=parametro)|
                Q(dni_extranjero__icontains=parametro)
            ).distinct()
            print(queryset)
        return queryset


    def get_context_data(self, **kwargs):
        contexto = {'pacientes': self.get_queryset(), 'form': self.form_class}
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


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
