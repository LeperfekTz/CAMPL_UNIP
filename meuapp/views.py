from django.shortcuts import render
from .models import Estudante


def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def lista_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'lista_estudantes.html', {'estudantes': estudantes})


def lista_aulas(request):
    return render(request, 'lista_aulas.html')

def lista_professores(request):
    return render(request, 'lista_professores.html')

def lista_classes(request):
    return render(request, 'lista_classes.html')

