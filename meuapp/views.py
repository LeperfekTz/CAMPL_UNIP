from .models import estudante, professor, aula, classe, usuario, responsavel
from .forms import estudanteForm  # Supondo que você tenha um formulário para o estudante
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages


def editar_estudante(request, id):
    estudantes = get_object_or_404(estudante, pk=id)

    if request.method == 'POST':
        form = estudanteForm(request.POST, instance=estudantes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudante atualizado com sucesso!')
            return redirect('lista_estudantes')  # Redireciona para a lista de estudantes após salvar
        
    else:

        form = estudanteForm(instance=estudantes)


    return render(request, 'editar_estudante.html', {'form': form, 'estudante': estudantes})


def editar_professor(request, id):
    Professor = get_object_or_404(professor, pk=id)
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
    total_estudantes = estudante.objects.count()
    total_professores = professor.objects.count()
    total_aulas = aula.objects.count()
    total_classe = classe.objects.count()
    return render(request, 'pagina_inicial.html', {
        'total_estudantes': total_estudantes,
        'total_professores': total_professores,
        'total_aulas': total_aulas,
        'total_classe': total_classe
        })

def lista_estudantes(request):
    estudantes = estudante.objects.all()
    responsaveis = responsavel.objects.all()
    return render(request, 'lista_estudantes.html', {
        'estudantes': estudantes,
        'responsaveis': responsaveis
        })


def lista_aulas(request):
    return render(request, 'lista_aulas.html')

def lista_professores(request):
    professores = usuario.objects.all()
    return render(request, 'lista_professores.html', {'professores': professores})
def lista_classes(request):
    return render(request, 'lista_classes.html')

