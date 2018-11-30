from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView, FormView, RedirectView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
from NavieraSkyApp.models import Contenedor, Salida, Ingreso, Producto, Cliente

from .forms import LoginForm


@login_required
def Home(request):
    contenedores = Contenedor.objects.all().count()
    salidas = Salida.objects.all().count()
    ingresos = Ingreso.objects.all().count()
    productos = Producto.objects.all().count()
    clientes = Cliente.objects.all().count()

    context = {
        'contenedores': contenedores,
        'salidas': salidas,
        'ingresos': ingresos,
        'productos': productos,
        'clientes': clientes,

    }

    return render(request, 'index.html', context=context)


class LoginView(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('home')
    template_name = 'registration/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)
