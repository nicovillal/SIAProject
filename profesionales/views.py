from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from profesionales.forms import ProfesionalForm
from .models import profesionale


# Create your views here.

class ListadoProfesional(ListView):
    model = profesionale
    template_name = 'profesionales/listar_profesional.html'
    context_object_name = 'profesionales'
    queryset = profesionale.objects.all()


class CrearProfesional(CreateView):
    model = profesionale
    form_class = ProfesionalForm
    template_name = 'profesionales/crear_profesional.html'
    success_url = reverse_lazy('profesionales:listar_profesional')


class EditarProfesional(UpdateView):
    model = profesionale
    template_name = 'profesionales/crear_profesional.html'
    form_class = ProfesionalForm
    success_url = reverse_lazy('profesionales:listar_profesional')

class EliminarProfesional(DeleteView):
    model = profesionale
    success_url = reverse_lazy('profesionales:listar_profesional')
from django.shortcuts import render

# Create your views here.
