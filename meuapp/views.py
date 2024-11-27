from .models import Estudante, Professor, Aula, Classe, Usuario, V_tela_estudante, EstudanteClasse, Presenca
from .forms import EstudanteForm, ProfessorForm, ResponsavelForm, ClasseForm
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse


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

def adicionar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            # Salva o usuário primeiro
            usuario = form.save(commit=False)
            usuario.papel = 'professor'  # Define o papel como 'professor'
            
            # Salva o usuário no banco para garantir que tenha um ID
            usuario.save()

            # Agora, cria o Professor e associa ao usuário
            if Professor.objects.filter(usuario=usuario).exists():
                messages.error(request, 'Este usuário já está associado a um professor.')
                return redirect('adicionar_professor')  # Redireciona para a página de adição de professor

            # Cria o novo Professor associado ao Usuario salvo
            Professor.objects.create(usuario=usuario)
            
            messages.success(request, 'Professor adicionado com sucesso!')
            return redirect('lista_professores')
    else:
        form = ProfessorForm()

    return render(request, 'adicionar_professor.html', {'form': form})

def excluir_estudante(request, estudante_id):
    if request.method == 'POST':
        estudante = get_object_or_404(Estudante, id=estudante_id)
        estudante.delete()
        messages.success(request, f"Estudante {estudante.nome} excluído com sucesso!")
        return redirect('lista_estudantes')  # Substitua pelo nome correto da URL
    return redirect('lista_estudantes')

def excluir_professor(request, professor_id):
    try:
        # Buscando o professor com o id fornecido
        professor = Professor.objects.get(id=professor_id)
        usuario = professor.usuario
        # Verificando se o professor está associado a alguma classe
        aulas = professor.classes.all()

        # Verificando se há aulas associadas ao professor
        if aulas.exists():
            # Se o professor estiver associado a aulas, podemos ou excluir as aulas ou tratá-las de outra forma
            messages.error(request, 'Este professor está associado a aulas e não pode ser excluído.')
            return redirect('lista_professores')

        professor.delete()
        usuario.delete()  # Depois exclui o usuário associado

        
        messages.success(request, 'Professor excluído com sucesso!')
        return redirect('lista_professores')

    except Professor.DoesNotExist:
        # Caso o professor não exista, exiba uma mensagem de erro
        messages.error(request, 'Professor não encontrado.')
        return redirect('lista_professores')

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
    # Obter o professor e o usuário relacionado
    professor = get_object_or_404(Professor, pk=id)
    usuario = professor.usuario  # Obtemos o usuário associado ao professor

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Professor atualizado com sucesso!')
            return redirect('lista_professores')
    else:
        form = ProfessorForm(instance=usuario)

    return render(request, 'editar_professor.html', {'form': form, 'professor': professor})

def editar_classe(request):
    # Lógica para editar a classe
    return render(request, 'editar_classe.html')
def adicionar_classe(request):
    # Se a requisição for POST, processa o formulário
    if request.method == "POST":
        form = ClasseForm(request.POST)
        if form.is_valid():
            # Salva a nova classe no banco de dados
            form.save()
            return redirect('lista_classes')  # Redireciona para a lista de classes
    else:
        form = ClasseForm()

    return render(request, 'adicionar_classe.html', {'form': form})

def adicionar_estudante_na_classe(request, classe_id):
    classe = get_object_or_404(Classe, id=classe_id)  # Obtém a classe
    estudantes = Estudante.objects.all()  # Obtém todos os estudantes cadastrados

    if request.method == "POST":
        estudante_selecionados = request.POST.getlist('estudante')  # Obtém os estudante selecionados
        classe.idestudante.set(estudante_selecionados)  # Atribui os estudante à classe
        classe.save()  # Salva a atualização da classe
        return redirect('lista_classes')  # Redireciona para a lista de classes

    return render(request, 'adicionar_estudante_na_classe.html', {'classe': classe, 'estudantes': estudantes})

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
    professores = Professor.objects.select_related('usuario').all()
    return render(request, 'lista_professores.html', {'professores': professores})


# View corrigida para passar as classes e não os estudantes
def lista_classes(request):
    # Receber o `idclasse` via POST ou GET
    id_classe = request.POST.get('idclasse', None)

    if id_classe:
        estudantes = EstudanteClasse.objects.filter(idclasse=id_classe)
    else:
        estudantes = EstudanteClasse.objects.all()

    return render(request, 'lista_classes.html', {'estudantes': estudantes})

def buscar_alunos_por_classe(request):
    id_classe = request.GET.get('idclasse')
    alunos = EstudanteClasse.objects.filter(idclasse=id_classe).values(
        'id', 'nome', 'email', 'telefone', 'idclasse__nome'
    )
    return JsonResponse(list(alunos), safe=False)




def estudantes_view(request):
    estudantes = Estudante.objects.all().select_related('responsavel')
    return render(request, 'estudantes.html', {'estudantes': estudantes})




