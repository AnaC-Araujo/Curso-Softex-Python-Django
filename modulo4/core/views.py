from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tarefa
from .models import Execucao
from .forms import TarefaForm

# Create your views here.
def home(request):
   
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = TarefaForm() 

    # return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em')
    todas_as_tarefas = Tarefa.objects.all()
    todas_as_execucao = Execucao.objects.all()

    context = {
        'nome_usuario':'Ana',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        'tarefas' : todas_as_tarefas,
        'execucoes' : todas_as_execucao,
        'form' : form,
    }
    return render(request, 'home.html', context)

def dona(request):
    return HttpResponse("<h1>Olá, Ana! Tudo bem?!</h1>")

def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.concluida = True
        tarefa.save() 
    return redirect('home')

def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
    return redirect('home')