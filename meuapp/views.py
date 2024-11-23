from .models import Estudante, Professor, Aula, Classe, Usuario, V_tela_estudante
from .forms import EstudanteForm, ProfessorForm, ResponsavelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import redirect
from django.contrib import messages
from django.db import transaction

def adicionar_estudante_responsavel(request):
    if request.method == 'POST':
        estudante_form = EstudanteForm(request.POST)
        responsavel_form = ResponsavelForm(request.POST)

        # Valida os dois formulários
        if estudante_form.is_valid() and responsavel_form.is_valid():
            # Salva o estudante primeiro
            estudante = estudante_form.save()

            # Cria o responsável, associando o estudante
            responsavel = responsavel_form.save(commit=False)
            responsavel.idestudante = estudante  # Associa o estudante criado
            responsavel.save()  # Agora salva o responsável

            # Redireciona para a lista de responsáveis ou outra página
            return redirect('lista_estudantes')

    else:
        estudante_form = EstudanteForm()
        responsavel_form = ResponsavelForm()

    return render(request, 'adicionar_estudante_responsavel.html', {
        'estudante_form': estudante_form,
        'responsavel_form': responsavel_form,
    })



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
    # Obtém o professor pelo ID ou retorna 404 se não encontrado
    professor = get_object_or_404(Professor, pk=id)

    # Se o método da requisição for POST, significa que o formulário foi enviado
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            # Salva as alterações no professor
            form.save()
            messages.success(request, 'Professor atualizado com sucesso!')
            return redirect('lista_professores')  # Redireciona para a lista de professores
    else:
        # Caso contrário, cria o formulário com os dados atuais do professor
        form = ProfessorForm(instance=professor)

    # Renderiza a página de edição com o formulário
    return render(request, 'editar_professor.html', {'form': form, 'professor': professor})

def editar_classe(request):
    # Lógica para editar a classe
    return render(request, 'editar_classe.html')

def editar_aula(request):
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
