from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, unique=True, default="")
    cpf = models.CharField(max_length=30, unique=True, default="")
    rg = models.CharField(max_length=30, unique=True, default="")
    nis = models.CharField(max_length=100, blank=True, null=True, default="")
    observacao = models.CharField(max_length=100, blank=True, null=True, default="")
    grupoprioridade = models.CharField(max_length=20, blank=True, null=True, default="")
    registro = models.CharField(max_length=50, default="Desconhecido")
    encaminhamento = models.CharField(max_length=30, blank=True, null=True, default="")
    telefone = models.CharField(max_length=20, unique=True, default="")
    URLimagem = models.CharField(max_length=100, blank=True, null=True)
    rua = models.CharField(max_length=50, default="")
    bairro = models.CharField(max_length=50, default="")
    cidade = models.CharField(max_length=30, default="")
    estado = models.CharField(max_length=2, default="")
    cep = models.CharField(max_length=20, default="")
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'estudante'  # Nome da tabela no banco de dados

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'usuario'  # Nome da tabela no banco de dados