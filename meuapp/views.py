
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import connection
from .models import (
    Estudante, Professor, Aula, Classe,
    V_tela_estudante, 
)
from .forms import EstudanteForm, ProfessorForm, ResponsavelForm, AulaForm

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

def adicionar_aula(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_aulas')
    else:
        form = AulaForm()
    return render(request, 'adicionar_aula.html', {'form': form})


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

def excluir_aula(request, pk):
    aula = get_object_or_404(Aula, pk=pk)
    aula.delete()
    return redirect('lista_aulas')


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

def editar_aula(request, pk):
    aula = get_object_or_404(Aula, pk=pk)
    if request.method == 'POST':
        form = AulaForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
            return redirect('lista_aulas')
    else:
        form = AulaForm(instance=aula)
    return render(request, 'editar_aula.html', {'form': form})
# --- Views de Listagem ---

def lista_estudantes(request):
    estudantes = V_tela_estudante.objects.all()
    return render(request, 'lista_estudantes.html', {'estudantes': estudantes})

def lista_professores(request):
    # Consulta todos os professores diretamente
    professores = Professor.objects.all()
    
    return render(request, 'lista_professores.html', {'professores': professores})

def lista_classe(request):
    classes = Classe.objects.all()
    return render(request, 'lista_classe.html', {'classes': classes})

def lista_aulas(request):
    aulas = Aula.objects.all()
    return render(request, 'lista_aulas.html', {'aulas': aulas})


# --- Outras Views ---

def chamada(request):
    # Obter todas as classes da base de dados
    classes = Classe.objects.all()

    # Obter o id da classe selecionada (se houver)
    idclasse = request.GET.get('idclasse')

    if idclasse:
        alunos = Estudante.objects.filter(idclasse=idclasse)

    else:
        alunos = Estudante.objects.all()

    # Renderizar o template passando as classes e os alunos
    return render(request, 'chamada.html', {'classes': classes, 'alunos': alunos})

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html', {
        'total_estudantes': Estudante.objects.count(),
        'total_professores': Professor.objects.count(),
        'total_aulas': Aula.objects.count(),
        'total_classe': Classe.objects.count(),
    })
    
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


def visualizar_classe(request, idclasse):
    classe = get_object_or_404(Classe, pk=idclasse)  # Obtém a classe com o ID fornecido
    professores = Professor.objects.filter(idclasse=idclasse)  # Filtra os professores da classe
    alunos = Estudante.objects.filter(idclasse=idclasse)  # Filtra os alunos da classe

    # Consulta SQL para pegar as aulas associadas à classe específica
    query = """
    SELECT a.id, a.nome
    FROM aula a
    JOIN classe c ON a.id = c.idaula
    WHERE c.classe = %s;
    """
    aulas = Aula.objects.raw(query, [classe.classe])

    return render(request, 'visualizar_classe.html', {
        'classe': classe,
        'professores': professores,
        'alunos': alunos,
        'aulas': aulas,
    })