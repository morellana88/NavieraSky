from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView

# Create your views here.
from NavieraSkyApp.models import Contenedores


def index(request):
    contenedores = Contenedores.objects.all().count()

    context = {
        'contenedores': contenedores,
    }

    return render(request, 'index.html', context=context)


class ContenedorListView(ListView):
    model = Contenedores
    context_object_name = 'contenedores_list'
    template_name = 'contenedores/contenedores_list.html'


class ContenedorLDetailView(DetailView):
    # model = get_object_or_404(Contenedores, pk=pk=primary_key)
    model = Contenedores
    context_object_name = 'contenedores_detail'
    template_name = 'contenedores/contenedor_detail.html'
