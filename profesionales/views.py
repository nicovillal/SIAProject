from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from profesionales.forms import ProfesionalForm
from .models import profesionale
from django.shortcuts import render
from django.db.models import Q


# Create your views here.

class ListadoProfesional(ListView):
    model = profesionale
    template_name = 'profesionales/listar_profesional.html'
    paginate_by = 10
    form_class=ProfesionalForm

    def get_queryset(self):
        parametro = self.request.GET.get("buscar", None)
        print(parametro)
        queryset = profesionale.objects.all()
        if parametro:
            queryset = profesionale.objects.filter(
                Q(rut_profesional__icontains=parametro)|
                Q(nombres__icontains=parametro) |
                Q(apellidos__icontains=parametro)|
                Q(email__icontains=parametro) |
                Q(profesion__icontains=parametro)
            ).distinct()
            print(queryset)
        return queryset


    def get_context_data(self, **kwargs):
        contexto = {'profesionales': self.get_queryset(), 'form': self.form_class}
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


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
