from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('lista_estudantes/', views.lista_estudantes, name='lista_estudantes'),
    path('lista_professores/', views.lista_professores, name='lista_professores'),
    path('lista_aulas/', views.lista_aulas, name='lista_aulas'),
    path('chamada/', views.chamada, name='chamada'),
    path('lista_classe/', views.lista_classe, name='lista_classe'),
    path('classes/<int:idclasse>/', views.visualizar_classe, name='visualizar_classe'),    
    path('editar_estudante/<int:id>/', views.editar_estudante, name='editar_estudante'),
    path('editar_professor/<int:id>/editar', views.editar_professor, name='editar_professor'),
    path('adicionar_professor/adicionar/', views.adicionar_professor, name='adicionar_professor'),
    path('adicionar-estudante-responsavel/', views.adicionar_estudante_responsavel, name='adicionar_estudante_responsavel'),
    path('excluir_professor/excluir/<int:professor_id>/', views.excluir_professor, name='excluir_professor'),
    path('excluir_estudante/excluir/<int:estudante_id>/', views.excluir_estudante, name='excluir_estudante'),
    path('avaliacao/', views.avaliacao, name='avaliacao'),
    path('aulas/', views.lista_aulas, name='lista_aulas'),
    path('adicionar_aula/', views.adicionar_aula, name='adicionar_aula'),
    path('editar_aula/<int:pk>/', views.editar_aula, name='editar_aula'),
    path('excluir_aula/<int:pk>/', views.excluir_aula, name='excluir_aula'),


    
]