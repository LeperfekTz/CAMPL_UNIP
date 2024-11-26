
from django import forms
from .models import Estudante, Usuario, Responsavel, Classe

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome', 'email', 'telefone', 'cpf', 'rg', 'nis', 'observacao', 'grupoprioridade', 'registro', 'encaminhamento', 'URLimagem', 'rua', 'bairro', 'cidade', 'estado', 'cep']

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
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'rua', 'bairro', 'cidade', 'estado', 'cep']
