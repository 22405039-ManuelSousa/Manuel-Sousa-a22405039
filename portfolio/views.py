from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
from .models import (Docente, Licenciatura, UnidadeCurricular, Tecnologia,
                     Projeto, TFC, Competencia, Formacao, MakingOf, Conquista)

def landing_view(request):
    return render(request, 'landing.html')

def videos_view(request):
    return render(request, 'videos.html')

def docentes_view(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes.html', {'docentes': docentes})

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'licenciaturas.html', {'licenciaturas': licenciaturas})

def unidades_curriculares_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all()
    return render(request, 'unidades_curriculares.html', {'ucs': ucs})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    gestor = request.user.groups.filter(name='gestor-portfolio').exists()
    return render(request, 'tecnologias.html', {'tecnologias': tecnologias, 'gestor': gestor})

def projetos_view(request):
    projetos = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias').all()
    gestor = request.user.groups.filter(name='gestor-portfolio').exists()
    return render(request, 'projetos.html', {'projetos': projetos, 'gestor': gestor})

def tfcs_view(request):
    tfcs = TFC.objects.select_related('licenciatura').prefetch_related('tecnologias').all()
    return render(request, 'tfcs.html', {'tfcs': tfcs})

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias', 'projetos').all()
    gestor = request.user.groups.filter(name='gestor-portfolio').exists()
    return render(request, 'competencias.html', {'competencias': competencias, 'gestor': gestor})

def formacoes_view(request):
    formacoes = Formacao.objects.prefetch_related('tecnologias', 'competencias').all()
    gestor = request.user.groups.filter(name='gestor-portfolio').exists()
    return render(request, 'formacoes.html', {'formacoes': formacoes, 'gestor': gestor})

def makingof_view(request):
    makingof = MakingOf.objects.select_related('projeto', 'tecnologia', 'unidade_curricular').all()
    return render(request, 'makingof.html', {'makingof': makingof})

def conquistas_view(request):
    conquistas = Conquista.objects.prefetch_related('projetos', 'tecnologias').all()
    return render(request, 'conquistas.html', {'conquistas': conquistas})

@login_required
def projeto_criar(request): 
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm()
    return render(request, 'projeto_form.html', {'form': form})

@login_required
def projeto_editar(request, pk):
    projeto = Projeto.objects.get(pk=pk)  
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():     
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'projeto_form.html', {'form': form})

@login_required
def projeto_apagar(request, pk):
    projeto = Projeto.objects.get(pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'projeto_confirmar_apagar.html', {'projeto': projeto})        

@login_required
def tecnologia_criar(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm()
    return render(request, 'tecnologia_form.html', {'form': form})

@login_required
def tecnologia_editar(request, pk):
    tecnologia = Tecnologia.objects.get(pk=pk)
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)
    return render(request, 'tecnologia_form.html', {'form': form})

@login_required
def tecnologia_apagar(request, pk):
    tecnologia = Tecnologia.objects.get(pk=pk)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'tecnologia_confirmar_apagar.html', {'tecnologia': tecnologia})

@login_required
def competencia_criar(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm()
    return render(request, 'competencia_form.html', {'form': form})

@login_required
def competencia_editar(request, pk):
    competencia = Competencia.objects.get(pk=pk)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'competencia_form.html', {'form': form})

@login_required
def competencia_apagar(request, pk):
    competencia = Competencia.objects.get(pk=pk)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'competencia_confirmar_apagar.html', {'competencia': competencia})

@login_required
def formacao_criar(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm()
    return render(request, 'formacao_form.html', {'form': form})

@login_required
def formacao_editar(request, pk):
    formacao = Formacao.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormacaoForm(request.POST, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm(instance=formacao)
    return render(request, 'formacao_form.html', {'form': form})

@login_required
def formacao_apagar(request, pk):
    formacao = Formacao.objects.get(pk=pk)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'formacao_confirmar_apagar.html', {'formacao': formacao})

def sobre_view(request):
    return render(request, 'sobre.html')

