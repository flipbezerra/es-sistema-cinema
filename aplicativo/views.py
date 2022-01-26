"""from django.shortcuts import render, redirect
from django.views import generic
from . import models
from .models import SetMovie, MovieMaster
from . import forms
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from aplicativo.models import BookedSeatsModel
from django.http import JsonResponse
# Create your views here.

## Página de login do admin
class LoiginAdmin(View):
    template_name = "aplicativo/admin_login.html"

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name)

    def post(self,request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            superusers = User.objects.get(username = username)
            print("-------------------------------------")
            print(superusers.username)
            print(superusers.is_superuser)
            print("--------------------------------------")
            if superusers.is_superuser == True:
                login(request, user)
                return redirect('../dashboard/')

        else:
            return render(request, self.template_name)


def adminLogout(request):
    logout(request)
    return redirect('../login/')


# Admin dashboard
class Dashboard(generic.ListView):
    model_add = models.MovieMaster
    model_set = models.SetMovie
    movies = MovieMaster.objects.filter(setmovie__isnull=False).distinct()
    # context_object_name = 'moviesss'
    model = MovieMaster

    template_name = "aplicativo/dashboard.html"

    def get_context_data(self, **kwargs):
        movies = MovieMaster.objects.filter(setmovie__isnull=False).distinct()
        context = super().get_context_data(**kwargs)
        context['movies'] = movies
        return context


# Adiciona os filmes
class AddMovies(generic.CreateView):  
    form_class = forms.AddMovieForm
    model = models.MovieMaster
    template_name = "aplicativo/addmovies.html"
    # fields = '__all__'

# Define os filmes como visiveis para o cliente
class SetMovies(generic.CreateView):
    form_class = forms.SetMovieForm
    model = models.SetMovie
    # context_object_name = 'movies'
    # def post(self, request, *args, **kwargs): 
    #     if request.method == 'POST':
    #         request.POST['']
    #         models.MovieGraphCount(m_name=)
    
    template_name = "aplicativo/setmovies.html"
"""