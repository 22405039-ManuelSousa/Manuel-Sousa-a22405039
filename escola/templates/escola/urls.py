from django.urls import path
from . import views

urlpatterns = [
    path('escola/', views.cursos_view, name='cursos'),
    path('escola/', views.professores_view, name='professores'),
    path('escola/', views.alunos_view, name='alunos'),
]
