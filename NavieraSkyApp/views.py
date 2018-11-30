from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView

# Create your views here.
from NavieraSkyApp.models import Contenedor


def index(request):
    contenedores = Contenedor.objects.all().count()

    context = {
        'contenedores': contenedores,
    }

    return render(request, 'index.html', context=context)


class ContenedorListView(ListView):
    model = Contenedor
    context_object_name = 'contenedores'
    template_name = 'contenedores/contenedores_list.html'


class ContenedorLDetailView(DetailView):
    # model = get_object_or_404(Contenedores, pk=pk=primary_key)
    model = Contenedor
    context_object_name = 'contenedores_detail'
    template_name = 'contenedores/contenedor_detail.html'
