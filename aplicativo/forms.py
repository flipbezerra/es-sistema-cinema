from django import forms
from GerenciaCinema import settings
from aplicativo.models import Filme, Cartaz, Assentos

class FilmesModelForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['cartaz', 'nome', 'sinopse', 'categoria', 'classificacao', 'duracao', 'capa']
        widgets = {
            'duracao': forms.TextInput(attrs={'placeholder': '0h00m'})
        }

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
