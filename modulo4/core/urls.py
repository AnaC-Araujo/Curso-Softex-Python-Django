from django.urls import path
from . import views # O '.' importa as 'views' do app atual

urlpatterns = [
    path('', views.home, name='home'),
    path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
    path('dona', views.dona, name='dona'),
    path('register/', views.register, name='register'),
]
