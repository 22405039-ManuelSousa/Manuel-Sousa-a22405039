from django.urls import path
from . import views

urlpatterns = [
    path('', views.artigos_view, name='artigos'),
    path('criar/', views.artigo_criar, name='artigo_criar'),
    path('<int:pk>/editar/', views.artigo_editar, name='artigo_editar'),
    path('<int:pk>/like/', views.artigo_like, name='artigo_like'),
    path('<int:pk>/comentar/', views.comentario_criar, name='comentario_criar'),
    path('registo/', views.registo_autor, name='registo_autor'),
    path('<int:pk>/avaliar/', views.artigo_avaliar, name='artigo_avaliar'),
]