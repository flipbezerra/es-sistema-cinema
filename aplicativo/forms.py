from django import forms
from GerenciaCinema import settings
from aplicativo.models import Filme, Sessao, Assentos

class FilmesModelForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'sinopse', 'classificacao', 'duracao', 'capa', 'trailer']
        widgets = {
            'duracao': forms.TextInput(attrs={'placeholder': '0h00m'})
        }

class SessaoModelForm(forms.ModelForm):
    class Meta:
        model = Sessao
        fields = ['filme', 'dataCartaz']
        widgets = {
            'dataCartaz': forms.DateInput(format=settings.DATETIME_INPUT_FORMATS,
                                          attrs={'placeholder': 'Ex: 01/01/2000 00:00'})
        }

class AssentoModelForm(forms.ModelForm):
    class Meta:
        model = Assentos
        fields = ['ocupado', 'sessao']
        widgets = {
            'ocupado': forms.HiddenInput(),
        }
