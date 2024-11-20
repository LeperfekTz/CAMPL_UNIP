from django.db import models

class usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'usuario'  # Nome da tabela no banco de dados


class estudante(models.Model):
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
        return self.usuario.nome

    class Meta:
        db_table = 'estudante'  # Nome da tabela no banco de dados


class professor(models.Model):
    usuario = models.OneToOneField(usuario, on_delete=models.CASCADE, related_name='professor')  # Relacionamento com Usuario
    telefone = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario.nome

    class Meta:
        db_table = 'professor'  # Nome da tabela no banco de dados


class responsavel(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30, unique=True)
    estudante = models.ForeignKey(estudante, on_delete=models.CASCADE, related_name='responsaveis')  # Relacionamento com estudante
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'responsavel'  # Nome da tabela no banco de dados


class classe(models.Model):
    classe = models.CharField(max_length=10)
    estudante = models.ForeignKey(estudante, on_delete=models.CASCADE, related_name='classes')  # Relacionamento com estudante
    professor = models.ForeignKey(professor, on_delete=models.CASCADE, related_name='classes')  # Relacionamento com professor
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.classe} - {self.estudante.nome}"

    class Meta:
        db_table = 'classe'  # Nome da tabela no banco de dados


class aula(models.Model):
    nome = models.CharField(max_length=25)
    professor = models.ForeignKey(professor, on_delete=models.CASCADE, related_name='aulas')  # Relacionamento com professor
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'aula'  # Nome da tabela no banco de dados
