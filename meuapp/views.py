from .models import Estudante
from .models import Usuario
from .forms import EstudanteForm  # Supondo que você tenha um formulário para o estudante
from django.shortcuts import render, get_object_or_404


def editar_estudante(request, id):
    estudante = get_object_or_404(Estudante, pk=id)

    if request.method == 'POST':
        form = EstudanteForm(request.POST, instance=estudante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudantes')  # Redireciona para a lista de estudantes após salvar
    else:
        form = EstudanteForm(instance=estudante)

    return render(request, 'editar_estudante.html', {'form': form, 'estudante': estudante})

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def lista_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'lista_estudantes.html', {'estudantes': estudantes})


def lista_aulas(request):
    return render(request, 'lista_aulas.html')

def lista_professores(request):
    professores = Usuario.objects.all()
    return render(request, 'lista_professores.html', {'professores': professores})
def lista_classes(request):
    return render(request, 'lista_classes.html')

