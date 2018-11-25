from django.shortcuts import render

# Create your views here.
from NavieraSkyApp.models import Contenedores


def index(request):
    contenedores = Contenedores.objects.all().count()

    context = {
        'contenedores': contenedores,
    }

    return render(request, 'index.html', context=context)
