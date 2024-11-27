from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('lista_estudantes/', views.lista_estudantes, name='lista_estudantes'),
    path('lista_professores/', views.lista_professores, name='lista_professores'),
    path('lista_classes/', views.lista_classes, name='lista_classes'),
    path('lista_aulas/',views.lista_aulas, name='lista_aulas'),
    path('editar_estudante/<int:id>/', views.editar_estudante, name='editar_estudante'),
    path('editar_professor/<int:id>/editar', views.editar_professor, name='editar_professor'),
    path('editar_classe/<int:id>/', views.editar_classe, name='editar_classe'),
    path('editar_aula/<int:id>/', views.editar_aula, name='editar_aula'),
    path('adicionar_professor/adicionar/', views.adicionar_professor, name='adicionar_professor'),
    path('adicionar-estudante-responsavel/', views.adicionar_estudante_responsavel, name='adicionar_estudante_responsavel'),
    path('excluir_professor/excluir/<int:professor_id>/', views.excluir_professor, name='excluir_professor'),
    path('excluir_estudante/excluir/<int:estudante_id>/', views.excluir_estudante, name='excluir_estudante'),

    
]