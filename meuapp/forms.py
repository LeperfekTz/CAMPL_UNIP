
from django import forms
from .models import Estudante, Professor, Responsavel, Classe

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome', 'email', 'telefone', 'cpf', 'rg', 'nis', 'observacao', 'grupoprioridade', 'registro', 'encaminhamento', 'URLimagem', 'rua', 'bairro', 'cidade', 'estado', 'cep', 'idclasse']

class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = ['nomeResp', 'telefoneResp']
        
class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['classe']  # Campos do modelo que serão exibidos no formulário

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'email', 'telefone', 'rua', 'bairro', 'cidade', 'estado', 'cep', 'cnpj', 'idclasse']
