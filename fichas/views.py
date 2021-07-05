from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from fichas.forms import FichaForm
from .models import ficha
from django.shortcuts import render
from django.db.models import Q


class ListadoFicha(ListView):
    model = ficha
    template_name = 'fichas/listar_ficha.html'
    paginate_by = 10
    form_class = FichaForm

    def get_queryset(self):
        parametro = self.request.GET.get("buscar", None)
        print(parametro)
        queryset = ficha.objects.all()
        if parametro:
            queryset = ficha.objects.filter(
                Q(paciente__nombres__icontains=parametro) |
                Q(paciente__apellidos__icontains=parametro) |
                Q(profesional__nombres__icontains=parametro) |
                Q(profesional__apellidos__icontains=parametro)
            ).distinct()
            print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        contexto = {'fichas': self.get_queryset(), 'form': self.form_class}
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


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
