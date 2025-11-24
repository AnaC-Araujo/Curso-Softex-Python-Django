from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tarefa
from .models import Execucao
from .forms import TarefaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
   
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
                tarefa = form.save(commit=False)
                tarefa.user = request.user
                tarefa.save()
                return redirect('home')
    else:
        form = TarefaForm() 

    # return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    todas_as_tarefas = Tarefa.objects.filter(user=request.user).order_by('-criada_em')
    todas_as_tarefas = Tarefa.objects.all()
    todas_as_execucao = Execucao.objects.all()

    context = {
        'nome_usuario': request.user.username,
        'tecnologias': ['Autenticação', 'ForeignKey', 'Login'],
        'tarefas' : todas_as_tarefas,
        'execucoes' : todas_as_execucao,
        'form' : form,
    }
    return render(request, 'home.html', context)

@login_required
def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':
        tarefa.concluida = True
        tarefa.save() 
    return redirect('home')

@login_required
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':
        tarefa.delete()
    return redirect('home')

def dona(request):
    return HttpResponse("<h1>Olá, Ana! Tudo bem?!</h1>")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            return redirect('home') 
    else:
        form = UserCreationForm() 
        
    context = {'form': form}
    return render(request, 'register.html', context)