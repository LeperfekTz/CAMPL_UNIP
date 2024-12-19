from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import (
    Estudante, Professor, Aula, Classe,
    V_tela_estudante, v_tela_classeEstudante, Avaliacao
)
from .forms import EstudanteForm, ProfessorForm, ResponsavelForm, ClasseForm

# --- Views de Adição ---

def adicionar_estudante_responsavel(request):
    if request.method == 'POST':
        estudante_form = EstudanteForm(request.POST)
        responsavel_form = ResponsavelForm(request.POST)

        if estudante_form.is_valid() and responsavel_form.is_valid():
            estudante = estudante_form.save()
            responsavel = responsavel_form.save(commit=False)
            responsavel.idestudante = estudante
            responsavel.save()
            return redirect('lista_estudantes')
    else:
        estudante_form = EstudanteForm()
        responsavel_form = ResponsavelForm()

    return render(request, 'adicionar_estudante_responsavel.html', {
        'estudante_form': estudante_form,
        'responsavel_form': responsavel_form,
    })

def adicionar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor = form.save(commit=False)  # Cria a instância do Professor sem salvar ainda

            # Verificar se o professor já existe (exemplo usando o email)
            if Professor.objects.filter(email=professor.email).exists():
                messages.error(request, 'Este email já está associado a um Professor.')
                return redirect('adicionar_professor')

            professor.save()  # Agora salva o professor no banco de dados

            messages.success(request, 'Professor adicionado com sucesso!')
            return redirect('lista_professores')  # Redireciona para a lista de professores
    else:
        form = ProfessorForm()  # Caso seja GET, cria um novo formulário vazio

    return render(request, 'adicionar_professor.html', {'form': form})


# --- Views de Exclusão ---


def excluir_estudante(request, estudante_id):
    estudante = get_object_or_404(Estudante, id=estudante_id)  # Obtém o estudante ou retorna 404
    estudante.delete()  # Exclui o estudante do banco de dados
    messages.success(request, "Estudante excluído com sucesso!")  # Mensagem de sucesso
    return redirect('lista_estudantes')  # Redireciona para a página de lista de estudantes

def excluir_professor(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    # Excluir o Professor
    professor.delete()
    messages.success(request, 'Professor excluído com sucesso!')
    return redirect('lista_professores')


# --- Views de Edição ---

def editar_estudante(request, id):
    estudante = get_object_or_404(Estudante, pk=id)
    if request.method == 'POST':
        form = EstudanteForm(request.POST, instance=estudante)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudante atualizado com sucesso!')
            return redirect('lista_estudantes')
    else:
        form = EstudanteForm(instance=estudante)

    return render(request, 'editar_estudante.html', {'form': form, 'estudante': estudante})

def editar_professor(request, id):
    professor = get_object_or_404(Professor, pk=id)  # Obter a instância do Professor

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)  # Preencher o formulário com os dados do professor
        if form.is_valid():
            form.save()  # Salvar as alterações no banco de dados
            messages.success(request, 'Professor atualizado com sucesso!')
            return redirect('lista_professores')  # Redirecionar após a atualização
    else:
        form = ProfessorForm(instance=professor)  # Preencher o formulário com os dados do professor para o GET

    return render(request, 'editar_professor.html', {'form': form, 'professor': professor})


# --- Views de Listagem ---

def lista_estudantes(request):
    estudantes = V_tela_estudante.objects.all()
    return render(request, 'lista_estudantes.html', {'estudantes': estudantes})

def lista_professores(request):
    # Consulta todos os professores diretamente
    professores = Professor.objects.all()
    
    return render(request, 'lista_professores.html', {'professores': professores})


def lista_classes(request):
    # Obter todas as classes da base de dados
    classes = Classe.objects.all()

    # Obter o id da classe selecionada (se houver)
    id_classe = request.GET.get('idclasse')

    # Filtrar alunos se id_classe for fornecido
    if id_classe:
        alunos = Estudante.objects.filter(idclasse_id=id_classe)

    else:
        alunos = Estudante.objects.all()

    # Renderizar o template passando as classes e os alunos
    return render(request, 'lista_classes.html', {'classes': classes, 'alunos': alunos})

def lista_aulas(request):
    aulas = Aula.objects.all()
    return render(request, 'lista_aulas.html', {'aulas': aulas})
# --- Outras Views ---

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html', {
        'total_estudantes': Estudante.objects.count(),
        'total_professores': Professor.objects.count(),
        'total_aulas': Aula.objects.count(),
        'total_classe': Classe.objects.count(),
    })



def buscar_alunos_por_classe(request):
    id_classe = request.GET.get('id')  # Obtém o id da classe do parâmetro GET
    if id_classe:
        # Filtra os alunos com base no id da classe
        estudante = v_tela_classeEstudante.objects.filter(id=id_classe).values(
            'id', 'nome', 'email', 'cpf'
        )
        return JsonResponse(list(estudante), safe=False)  # Retorna os dados em formato JSON
    else:
        return JsonResponse({'error': 'Classe não encontrada'}, status=400)  # Caso o id da classe não seja fornecido
    
def marcar_presenca(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        aluno_id = data.get('aluno_id')
        presente = data.get('presente')

        aluno = Estudante.objects.get(id=aluno_id)
        aluno.presente = presente  # Supondo que você tenha um campo 'presente' no seu modelo
        aluno.save()

        return JsonResponse({'status': 'sucesso'})
    
def avaliacao(request):
    idclasse = request.GET.get('idclasse')  # Obtém o ID da classe selecionada
    
    if idclasse:
        # Obtém os estudantes e as aulas da classe selecionada
        professores = Professor.objects.filter(idclasse=idclasse)
        estudantes = Estudante.objects.filter(idclasse=idclasse)
        aulas = Aula.objects.all()
    else:
        professores = Professor.objects.all()
        estudantes = Estudante.objects.all()
        aulas = Aula.objects.all()

    classes = Classe.objects.all()

    return render(request, 'avaliacao.html', {
        'classes': classes,
        'estudantes': estudantes,
        'aulas': aulas,
        'professores': professores,
    })