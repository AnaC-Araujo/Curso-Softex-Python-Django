from django.urls import path
from . import views # O '.' importa as 'views' do app atual

# Quando a URL for a raiz (''), chame a função 'home' de 'views.py'
urlpatterns = [
    path(
        '', 
        views.home, 
        name='home'),
    path(
        'dona', 
        views.dona, 
        name='dona'),
]
