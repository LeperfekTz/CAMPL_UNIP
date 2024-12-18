from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import (
    Estudante, Professor, Aula, Classe, Usuario, 
    V_tela_estudante, v_tela_classeEstudante
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
            usuario = form.save(commit=False)
            usuario.papel = 'professor'
            usuario.save()

            if Professor.objects.filter(usuario=usuario).exists():
                messages.error(request, 'Este usuário já está associado a um professor.')
                return redirect('adicionar_professor')

            Professor.objects.create(usuario=usuario)
            messages.success(request, 'Professor adicionado com sucesso!')
            return redirect('lista_professores')
    else:
        form = ProfessorForm()

    return render(request, 'adicionar_professor.html', {'form': form})

def adicionar_classe(request):
    if request.method == "POST":
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_classes')
    else:
        form = ClasseForm()

    return render(request, 'adicionar_classe.html', {'form': form})

def adicionar_estudante_na_classe(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)
    estudantes = Estudante.objects.all()

    if request.method == "POST":
        estudante_selecionados = request.POST.getlist('estudante')
        classe.estudantes.set(estudante_selecionados)
        classe.save()
        return redirect('lista_classes')

    return render(request, 'adicionar_estudante_na_classe.html', {
        'classe': classe,
        'estudantes': estudantes,
    })

# --- Views de Exclusão ---

def excluir_objeto(request, model_class, object_id, redirect_url):
    obj = get_object_or_404(model_class, id=object_id)
    obj.delete()
    messages.success(request, f'{model_class.__name__} excluído com sucesso!')
    return redirect(redirect_url)

def excluir_estudante(request, estudante_id):
    estudante = get_object_or_404(Estudante, id=estudante_id)  # Obtém o estudante ou retorna 404
    estudante.delete()  # Exclui o estudante do banco de dados
    messages.success(request, "Estudante excluído com sucesso!")  # Mensagem de sucesso
    return redirect('lista_estudantes')  # Redireciona para a página de lista de estudantes

def excluir_professor(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)

    # Verificar se o professor está associado a qualquer classe ou aula
    if Aula.objects.filter(professor=professor).exists():
        messages.error(request, 'Este professor está associado a classes ou aulas e não pode ser excluído.')
        return redirect('lista_professores')

    # Excluir o usuário associado, se não estiver sendo usado em outros lugares
    if professor.usuario:
        professor.usuario.delete()

    # Excluir o professor
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
    professor = get_object_or_404(Professor, pk=id)
    usuario = professor.usuario

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Professor atualizado com sucesso!')
            return redirect('lista_professores')
    else:
        form = ProfessorForm(instance=usuario)

    return render(request, 'editar_professor.html', {'form': form, 'professor': professor})

# --- Views de Listagem ---

def lista_estudantes(request):
    estudantes = V_tela_estudante.objects.all()
    return render(request, 'lista_estudantes.html', {'estudantes': estudantes})

def lista_professores(request):
    professores = Professor.objects.select_related('usuario').all()
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
    # Obter o id da classe da query string (se presente)
    classe_id = request.GET.get('classe_id', None)
    professores = Professor.objects.all()

    # Se houver um id de classe na URL, filtra os estudantes e professores
    if classe_id:
        estudantes = Estudante.objects.filter(idclasse_id=classe_id)  # Usar idclasse_id para filtrar
    else:
        # Caso não haja um filtro, pega todos os estudantes e professores
        estudantes = Estudante.objects.all()
    
    # Passa os dados para o template
    return render(
        request,
        'avaliacao.html',
        {
            'estudantes': estudantes,
            'professores': professores,
            'classes': Classe.objects.all(),
        }
    )
