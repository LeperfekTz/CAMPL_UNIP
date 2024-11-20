from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=50)

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

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'estudante'  # Nome da tabela no banco de dados

class Professor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='professor')  # Relacionamento com Usuario
    telefone = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario.nome

    class Meta:
        db_table = 'professor'  # Nome da tabela no banco de dados

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



class Responsavel(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30, unique=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    idestudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, related_name='responsavel')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'responsavel'  # Nome da tabela no banco de dados


class Classe(models.Model):
    classe = models.CharField(max_length=10)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, related_name='classes')  # Relacionamento com estudante
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='classes')  # Relacionamento com professor
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.classe} - {self.estudante.nome}"

    class Meta:
        db_table = 'classe'  # Nome da tabela no banco de dados


class Aula(models.Model):
    nome = models.CharField(max_length=25)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='aulas')  # Relacionamento com professor
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'aula'  # Nome da tabela no banco de dados

