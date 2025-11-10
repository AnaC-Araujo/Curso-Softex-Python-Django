from django.contrib import admin
from .models import Tarefa
from .models import Execucao 
# Register your models here.
admin.site.register(Tarefa)
admin.site.register(Execucao)
