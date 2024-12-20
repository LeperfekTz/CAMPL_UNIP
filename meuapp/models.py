from django.db import models


# Modelo de Estudante
class Estudante(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
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
    idclasse = models.ForeignKey(
        'Classe',
        on_delete=models.SET_NULL,
        db_column='idclasse',
        blank=True,
        null=True,
        related_name='estudantes'
    )

    class Meta:
        db_table = 'estudante'

    def __str__(self):
        return self.nome


# Modelo de Classe
class Classe(models.Model):
    classe = models.CharField(max_length=10, null=True, blank=True)
    aula = models.ForeignKey('Aula', on_delete=models.CASCADE, db_column='idaula', related_name='classes')
    dataCriacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'classe'

    def __str__(self):
        return f"Classe: {self.classe}"


# Modelo de Aula
class Aula(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)


    class Meta:
        db_table = 'aula'

    def __str__(self):
        return self.nome


# Modelo de Usuário
class Professor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=20)
    rua = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    idclasse = models.ForeignKey('Classe', on_delete=models.CASCADE, db_column='idclasse', blank=True, null=True)

    
    dataCriacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'professor'

    def __str__(self):
        return self.nome

# Modelo de Responsável
class Responsavel(models.Model):
    idestudante = models.ForeignKey(
        Estudante,
        on_delete=models.CASCADE,
        db_column='idestudante'
    )
    nomeResp = models.CharField(max_length=50)
    telefoneResp = models.CharField(max_length=30)

    class Meta:
        db_table = 'responsavel'


# Modelo de View Estudante
class V_tela_estudante(models.Model):
    id = models.IntegerField(primary_key=True)
    NOME = models.CharField(max_length=50)
    EMAIL = models.CharField(max_length=50)
    CPF = models.CharField(max_length=30)
    RESPONSAVEL = models.CharField(max_length=50)
    TELEFONE = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'V_tela_estudante'


# Modelo de View Classe Estudante

class Avaliacao(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    aula = models.CharField(max_length=255)
    status = models.CharField(max_length=30)
    comentario = models.TextField()

    class Meta:
        managed = False
        db_table = 'avaliacao'



    def __str__(self):
        return f"Avaliação de {self.aluno} por {self.professor}"