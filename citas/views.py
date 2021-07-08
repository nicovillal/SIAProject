from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from citas.forms import CitaForm
from .models import cita
from django.shortcuts import render
from django.db.models import Q


class ListadoCita(ListView):
    model = cita
    template_name = 'citas/listar_cita.html'
    paginate_by=1
    form_class=CitaForm


    def get_queryset(self):
        parametro = self.request.GET.get("buscar", None)
        print(parametro)
        queryset = cita.objects.all()
        if parametro:
            queryset = cita.objects.filter(
                Q(paciente__nombres__icontains=parametro)|
                Q(paciente__apellidos__icontains=parametro) |
                Q(profesional__nombres__icontains=parametro)|
                Q(profesional__apellidos__icontains=parametro) |
                Q(fecha_cita__icontains=parametro)|
                Q(hora_cita__icontains=parametro)|
                Q(estado__icontains=parametro)|
                Q(motivo_anulacion__icontains=parametro)
            ).distinct()
            print(queryset)
        return queryset


    def get_context_data(self, **kwargs):
        contexto = {'citas': self.get_queryset(), 'form': self.form_class}
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class CrearCita(CreateView):
    model = cita
    form_class = CitaForm
    template_name = 'citas/crear_cita.html'
    success_url = reverse_lazy('citas:listar_cita')
    print(form_class)


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
