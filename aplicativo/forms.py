from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from GerenciaCinema import settings
from aplicativo.models import Filme, Cartaz, Assentos


class FilmesModelForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['cartaz', 'nome', 'sinopse', 'categoria', 'classificacao', 'duracao', 'capa']
        widgets = {
            'duracao': forms.TextInput(attrs={'placeholder': '0h00m'})
        }

class RegistroClienteModelForm(UserCreationForm):
    first_name = forms.CharField(label='Nome', max_length=32)
    last_name = forms.CharField(label='Sobrenome', max_length=32)
    email = forms.EmailField(max_length=32)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CartazModelForm(forms.ModelForm):
    class Meta:
        model = Cartaz
        fields = ['dataCartaz', 'assentos']
        widgets = {
            'dataCartaz': forms.DateInput(format=settings.DATETIME_INPUT_FORMATS,
                                          attrs={'placeholder': 'Ex:. 01/01/2000 00:00'})
        }

class AssentoModelForm(forms.ModelForm):
    class Meta:
        model = Assentos
        fields = []
