from django.urls import path
from .views import TarefaListCreateAPIView
from .views import ContagemTarefasAPIView
from .views import EstatisticasTarefasAPIView
from .views import DetalheTarefaAPIView
from .views import ConcluirTarefaLoteAPIView
from .views import MinhaView
from .views import LogoutView
from .views import MeView
from .views import ChangePasswordView
from .views import UserStatsView
from .views import TarefaRetrieveUpdateDestroyAPIView
from .views import RegisterView

app_name = 'core'
urlpatterns = [
    path('tarefas/', TarefaListCreateAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/contagem/', ContagemTarefasAPIView.as_view(), name='contagem-tarefas'),
    path('tarefas/estatisticas/', EstatisticasTarefasAPIView.as_view(), name='estatisticas-tarefas'),
    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyAPIView.as_view(), name='detalhe-tarefa'),
    path('tarefas/<int:pk>/duplicar/', DetalheTarefaAPIView.as_view()),
    path('tarefas/concluir-todas/', ConcluirTarefaLoteAPIView.as_view()),
    path('teste/', MinhaView.as_view(), name= 'teste-autenticacao'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='usuario-autenticado'),
    path('change-password/', ChangePasswordView.as_view(), name='alterar-senha'),
    path('stats/', UserStatsView.as_view(), name='estatisticas-usuario'),
    path('register/', RegisterView.as_view(), name='register'),
]
