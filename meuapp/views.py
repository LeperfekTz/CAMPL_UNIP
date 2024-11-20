from .models import Estudante, Professor, Aula, Classe, Usuario, V_tela_estudante
from .forms import EstudanteForm  # Supondo que você tenha um formulário para o estudante
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages


def editar_estudante(request, id):
    estudantes = get_object_or_404(Estudante, pk=id)

    if request.method == 'POST':
        form = EstudanteForm(request.POST, instance=estudantes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudante atualizado com sucesso!')
            return redirect('lista_estudantes')  # Redireciona para a lista de estudantes após salvar
        
    else:

        form = EstudanteForm(instance=estudantes)


    return render(request, 'editar_estudante.html', {'form': form, 'estudante': estudantes})

def editar_professor(request, id):
    Professor = get_object_or_404(Professor, pk=id)
    # Lógica para editar o professor
    return render(request, 'editar_professor.html', {'professor': Professor})

def editar_classe(request, id):
    # Lógica para editar a classe
    return render(request, 'editar_classe.html')

def editar_aula(request, id):
    # Lógica para editar a aula
    return render(request, 'editar_aula.html')

def pagina_inicial(request):
    # Consulta para contar todos os estudantes
    total_estudantes = Estudante.objects.count()
    total_professores = Professor.objects.count()
    total_aulas = Aula.objects.count()
    total_classe = Classe.objects.count()
    return render(request, 'pagina_inicial.html', {
        'total_estudantes': total_estudantes,
        'total_professores': total_professores,
        'total_aulas': total_aulas,
        'total_classe': total_classe
        })

def lista_estudantes(request):
    estudantes = V_tela_estudante.objects.all()
    return render(request, 'lista_estudantes.html', {'estudantes': estudantes})


def lista_aulas(request):
    return render(request, 'lista_aulas.html')

def lista_professores(request):
    professores = Usuario.objects.all()
    return render(request, 'lista_professores.html', {'professores': professores})
def lista_classes(request):
    return render(request, 'lista_classes.html')

def estudantes_view(request):
    estudantes = Estudante.objects.all().select_related('responsavel')
    return render(request, 'estudantes.html', {'estudantes': estudantes})