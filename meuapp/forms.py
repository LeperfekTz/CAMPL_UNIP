from django import forms
from .models import estudante

class estudanteForm(forms.ModelForm):
    class Meta:
        model = estudante
        fields = ['nome', 'email', 'telefone', 'cpf', 'rg', 'nis', 'observacao', 'grupoprioridade', 'registro', 'encaminhamento', 'URLimagem', 'rua', 'bairro', 'cidade', 'estado', 'cep']
