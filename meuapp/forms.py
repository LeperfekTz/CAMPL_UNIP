from django import forms
from .models import Estudante

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome', 'email', 'telefone', 'cpf', 'rg', 'nis', 'observacao', 'grupoprioridade', 'registro', 'encaminhamento', 'URLimagem', 'rua', 'bairro', 'cidade', 'estado', 'cep']
