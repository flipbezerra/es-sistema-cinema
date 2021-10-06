from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from aplicativo.models import Filme, Assentos
from aplicativo.forms import FilmesModelForm, ClienteModelForm, RegistroClienteModelForm, CartazModelForm, \
    AssentoModelForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

def index_auth(request):
    if request.user.is_authenticated:
        return render(request, 'index_auth.html')
    else:
        return redirect(index)

def filme_list(request):
    context = {
        'filmes': Filme.objects.all()
    }
    return render(request, 'filme_list.html', context)

def registrar(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistroClienteModelForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect(index)
            else:
                messages.error(request, 'Erro no cadastro do Usuário!')
        else:
            form = RegistroClienteModelForm

        context = {
            'form': form
        }
        return render(request, 'registrar.html', context)
    else:
        return redirect(index)

def filmes(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FilmesModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Filme registrado com sucesso!')
                form = FilmesModelForm()
            else:
                messages.error(request, 'Filme não registrado!')
        else:
            form = FilmesModelForm()
        context = {
            'form': form
        }
        return render(request, 'filmes.html', context)
    else:
        return redirect(index)


def cliente(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ClienteModelForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Cliente cadastrado com sucesso!')
                form = ClienteModelForm()
            else:
                messages.error(request, 'Cliente não cadastrado!')
        else:
            form = ClienteModelForm()
        context = {
            'form': form
        }
        return render(request, 'cliente.html', context)
    else:
        return redirect(index)


def cartaz(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CartazModelForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Cartaz criado com sucesso!')
                form = CartazModelForm()
            else:
                messages.error(request, 'Cartaz não criado!')
        else:
            form = CartazModelForm()
        context = {
            'form': form
        }
        return render(request, 'cartaz.html', context)
    else:
        return redirect(index)

def assento(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AssentoModelForm(request.POST)
            if form.is_valid():

                messages.success(request, 'Assentos Reservados!')
            else:
                messages.error(request, 'Erro!')
        else:
            form = AssentoModelForm()
        context = {
            'form': form,
            'assento': Assentos.objects.all()
        }
        return render(request, 'assento.html', context)
    else:
        return redirect(filme_list)
