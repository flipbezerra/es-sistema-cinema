from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from aplicativo.models import Filme, Assentos
from aplicativo.forms import FilmesModelForm, SessaoModelForm, AssentoModelForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
# Create your views here.

def index(request):
    context = {
    'filmes': Filme.objects.all()
    }
    return render(request, 'index.html', context)

def index_auth(request):
    context = {
    'filmes': Filme.objects.all()
    }
    if request.user.is_authenticated:
        return render(request, 'index_auth.html')
    else:
        return redirect(index)
    
def administrador(request):

    if request.user.is_superuser:
        return render(request, 'administrador.html')
    else:
        return redirect(index_auth)

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Usuário conectado!')
            return redirect(index)
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    #linha alterada
    return render(request, 'logar.html', context)

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, 'Usuário cadastrado!')
            form = UserCreationForm()
        else:
            messages.error(request, 'Usuário não cadastrado!')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    # linha alterada
    return render(request, 'cadastro.html', context)

def filmes(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FilmesModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Filme adicionado com sucesso!')
                form = FilmesModelForm()
            else:
                messages.error(request, 'Erro! Filme não pôde ser adicionado.!')
        else:
            form = FilmesModelForm()
        context = {
            'form': form
        }
        return render(request, 'filmes.html', context)
    else:
        return redirect(index)

def sessoes(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SessaoModelForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Sessão criada com sucesso.')
                form = SessaoModelForm()
            else:
                messages.error(request, 'Erro! Sessão não pôde ser criada.')
        else:
            form = SessaoModelForm()
        context = {
            'form': form
        }
        return render(request, 'sessoes.html', context)
    else:
        return redirect(index)

def assentos(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AssentoModelForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Assento adicionado!')
            else:
                messages.error(request, 'Erro! Assento não pôde ser adicionado.')
        else:
            form = AssentoModelForm()
        context = {
            'form': form,
            'assento': Assentos.objects.all()
        }
        return render(request, 'assentos.html', context)
    else:
        return redirect(index)
