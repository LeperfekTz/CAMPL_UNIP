from django.contrib import admin
from .models import estudante  # Certifique-se de que Estudante está definido corretamente no models.py

# Customizando a exibição do modelo Estudante no Django Admin
@admin.register(estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'telefone', 'cidade', 'estado', 'dataCriacao')  # Colunas exibidas na lista
    search_fields = ('nome', 'email', 'cpf')  # Campos que podem ser pesquisados
    list_filter = ('estado', 'cidade', 'dataCriacao')  # Filtros laterais
    ordering = ('nome',)  # Ordenação padrão
    date_hierarchy = 'dataCriacao'  # Navegação por datas

