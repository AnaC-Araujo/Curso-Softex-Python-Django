from django.db import models

# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200) #equivale a TEXT no SQL
    concluida = models.BooleanField(default=False) #equivale a bool
    criada_em = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.titulo
    
class Execucao(models.Model):
    nome = models.CharField(max_length=200) 
    concluido = models.BooleanField(default=False)
    local =models.CharField(max_length=200) 
    hora = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.nome