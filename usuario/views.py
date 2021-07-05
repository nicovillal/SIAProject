from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from usuario.forms import FormularioLogin, FormUsuario
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from usuario.models import Usuario
from django.shortcuts import render
from django.db.models import Q


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuario/listar_usuario.html'
    paginate_by = 10
    form_class = FormUsuario

    def get_queryset(self):
        parametro = self.request.GET.get("buscar", None)
        print(parametro)
        queryset = Usuario.objects.filter(is_active=True)
        if parametro:
            queryset = Usuario.objects.filter(
                Q(username__icontains=parametro) |
                Q(nombres__icontains=parametro) |
                Q(apellidos__icontains=parametro)
            ).distinct()
            print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        contexto = {'object_list': self.get_queryset(), 'form': self.form_class}
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class CrearUsuario(CreateView):
    model = Usuario
    form_class = FormUsuario
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuario')


class EditarUsuario(UpdateView):
    model = Usuario
    template_name = 'usuario/crear_usuario.html'
    form_class = FormUsuario
    success_url = reverse_lazy('usuario:listar_usuario')


class EliminarUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario:listar_usuario')
