from django.contrib import admin
from .models import Estudante
# Customizando a exibição do modelo Estudante no Django Admin
@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'telefone', 'cidade', 'estado', 'dataCriacao')  # Colunas exibidas na lista
    search_fields = ('nome', 'email', 'cpf')  # Campos que podem ser pesquisados
    list_filter = ('estado', 'cidade', 'dataCriacao')  # Filtros laterais
    ordering = ('nome',)  # Ordenação padrão
    date_hierarchy = 'dataCriacao'  # Navega o por datas

