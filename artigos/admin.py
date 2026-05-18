from django.contrib import admin
from .models import Artigo, Comentario, Avaliacao
admin.site.register(Avaliacao)
admin.site.register(Artigo)
admin.site.register(Comentario)
