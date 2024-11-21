from django import forms
from .models import Estudante, Professor

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome', 'email', 'telefone', 'cpf', 'rg', 'nis', 'observacao', 'grupoprioridade', 'registro', 'encaminhamento', 'URLimagem', 'rua', 'bairro', 'cidade', 'estado', 'cep']



class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['usuario', 'telefone']  # Certifique-se de que 'telefone' está listado aqui
