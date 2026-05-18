from django import forms
from .models import Artigo, Comentario, Avaliacao

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['texto', 'fotografia', 'link']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'texto']

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['valor']