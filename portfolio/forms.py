from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao

class ProjetoForm(forms.ModelForm): 
    class Meta: 
        model = Projeto
        fields = ['titulo', 'descricao', 'imagem', 'video', 'github', 'deploy', 'unidade_curricular', 'tecnologias', 'destaque']

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'categoria', 'logo', 'url', 'nivel']

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'tipo', 'nivel', 'descricao', 'tecnologias', 'projetos']

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['nome', 'tipo', 'data_inicio', 'data_fim', 'tecnologias', 'competencias']