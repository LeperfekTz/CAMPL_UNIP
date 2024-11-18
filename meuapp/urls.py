from django.urls import path
from .views import lista_estudantes
from .views import pagina_inicial
from .views import lista_estudantes
from .views import lista_professores
from .views import lista_classes
from .views import lista_aulas

urlpatterns = [
    path('', lista_estudantes, name='lista_estudantes'),
    path('pagina_inicial/', pagina_inicial, name='pagina_inicial'),
    path('lista_estudantes/', lista_estudantes, name='lista_estudantes'),
    path('lista_professores/', lista_professores, name='lista_professores'),
    path('lista_classes/', lista_classes, name='lista_classes'),
    path('lista_aulas/', lista_aulas, name='lista_aulas'),
]
