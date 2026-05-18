from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Avg
from .models import Artigo, Comentario, Avaliacao
from .forms import ArtigoForm, ComentarioForm, AvaliacaoForm

def artigos_view(request):
    artigos = Artigo.objects.select_related('autor').prefetch_related('comentarios', 'likes').annotate(media_rating=Avg('avaliacoes__valor')).order_by('-data_criacao')
    autor = request.user.is_authenticated and request.user.groups.filter(name='bloggers').exists()
    return render(request, 'artigos/artigos.html', {'artigos': artigos, 'autor': autor})

@login_required
def artigo_criar(request):
    if not request.user.groups.filter(name='bloggers').exists():

        return redirect('artigos')
    form = ArtigoForm(request.POST, request.FILES)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos')
    return render(request, 'artigos/artigo_form.html', {'form': form})

@login_required
def artigo_editar(request, pk):
    artigo = Artigo.objects.get(pk=pk)
    if artigo.autor != request.user:
        return redirect('artigos')
    form = ArtigoForm(request.POST, request.FILES, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigos')
    return render(request, 'artigos/artigo_form.html', {'form': form})

@login_required
def artigo_like(request, pk):
    artigo = Artigo.objects.get(pk=pk)
    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigos')

def comentario_criar(request, pk):
    artigo = Artigo.objects.get(pk=pk)
    form = ComentarioForm(request.POST)
    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.artigo = artigo
        if request.user.is_authenticated:
            comentario.autor = request.user
        else:
            comentario.nome = form.cleaned_data['nome'] or 'Anónimo'
        comentario.save()
    return redirect('artigos')

def registo_autor(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        grupo, _ = Group.objects.get_or_create(name='bloggers')
        grupo.user_set.add(user)
        login(request, user)
        return redirect('artigos')
    return render(request, 'artigos/registo_autor.html', {'form': form})

def artigo_avaliar(request, pk):
    artigo = Artigo.objects.get(pk=pk)
    form = AvaliacaoForm(request.POST)
    if form.is_valid():
        avaliacao = form.save(commit=False)
        avaliacao.artigo = artigo
        avaliacao.save()
    return redirect('artigos')