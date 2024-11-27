
from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    senha = models.CharField(max_length=50)
    URLimagem = models.URLField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20)
    rua = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=20)
    idclasse = models.ManyToManyField('Classe', related_name='professores', blank=True)
    papel = models.CharField(
        max_length=20,
        choices=[
            ('professor', 'Professor'),
            ('gerente', 'Gerente'),
            ('integracao', 'Integração'),
            ('emprego', 'Emprego'),
        ]
    )
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    
    class Meta:
        db_table = 'usuario'  # Nome da tabela no banco de dados


class Estudante(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    cpf = models.CharField(max_length=30, unique=True)
    rg = models.CharField(max_length=30, unique=True)
    nis = models.CharField(max_length=100, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    grupoprioridade = models.CharField(max_length=20, blank=True, null=True)
    registro = models.CharField(max_length=50)
    encaminhamento = models.CharField(max_length=30, blank=True, null=True)
    telefone = models.CharField(max_length=20, unique=True)
    URLimagem = models.CharField(max_length=100, blank=True, null=True)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=20)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    idclasse = models.ManyToManyField('Classe', related_name='estudantes', blank=True)

    def __str__(self):
        
        return self.nome

    class Meta:
        db_table = 'estudante'  # Nome da tabela no banco de dados

class Professor(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,  # Exclui o usuário quando o professor for excluído
        db_column='idusuario',     # Nome da coluna no banco de dados
        related_name='professor',  # Permite acessar o professor diretamente pelo usuario.professor
    )
    dataCriacao = models.DateTimeField(auto_now_add=True)  # Registra automaticamente a data de criação

    class Meta:
        db_table = 'professor'  # Nome da tabela no banco de dados

    def __str__(self):
        return f"Professor: {self.usuario.nome}"  # Exibe o nome do professor

class V_tela_estudante(models.Model):
    id = models.IntegerField(primary_key=True)
    NOME = models.CharField(max_length=50)
    EMAIL = models.CharField(max_length=50)
    CPF = models.CharField(max_length=30)
    RESPONSAVEL = models.CharField(max_length=50)
    TELEFONE = models.CharField(max_length=20)

    class Meta:
        managed = False  # Não deixe o Django gerenciar esta tabela
        db_table = 'V_tela_estudante'  # Nome da sua view ou tabela

class v_tela_classeEstudante(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)

    class Meta:
        managed = False  # Indica que essa tabela/visão é apenas leitura
        db_table = 'v_tela_classeEstudante'  # Nome da sua view no banco

class Responsavel(models.Model):
    idestudante = models.ForeignKey(
        'Estudante',  # Refere-se ao modelo Estudante
        on_delete=models.CASCADE,  # Comportamento em caso de exclusão
        db_column='idestudante'  # Nome da coluna na tabela do banco de dados
    )
    nomeResp = models.CharField(max_length=50)
    telefoneResp = models.CharField(max_length=30)


    class Meta:
        db_table = 'responsavel'  # Nome da tabela no banco de dados

class Aula(models.Model):
    nome = models.CharField(max_length=25)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, db_column='idprofessor')
    dataCriacao = models.DateTimeField(auto_now_add=True)

    # Novo campo dia com as opções de dias da semana
    dia_choices = [
        ('Segunda', 'Segunda'),
        ('Terça', 'Terça'),
        ('Quarta', 'Quarta'),
        ('Quinta', 'Quinta'),
        ('Sexta', 'Sexta'),
    ]
    dia = models.CharField(max_length=7, choices=dia_choices)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'aula'  # Nome da tabela no banco de dados



class Classe(models.Model):
    classe = models.CharField(max_length=10, null=True, blank=True)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, db_column='idaula', related_name='classes')
    idclasse = models.ManyToManyField(Estudante, related_name='classes', blank=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.classe} - {self.estudante.nome}"

    class Meta:
        db_table = 'classe'  # Nome da tabela no banco de dados


class Presenca(models.Model):
    estudante = models.OneToOneField(
        v_tela_classeEstudante,  # Relaciona com a view VTelaClasseEstudante
        on_delete=models.CASCADE,  # O que acontece se o estudante for excluído
        primary_key=True,  # Define estudante como a chave primária
    )
    presenca = models.BooleanField(default=False)  # Campo de presença
