from django.db import models
from django.contrib.auth.models import User

class Artigo(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artigos')
    texto = models.TextField()
    fotografia = models.ImageField(upload_to='artigos/', blank=True, null=True)
    link = models.URLField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='artigos_gostados')

    def __str__(self):
        return f"{self.autor.username} – {self.data_criacao.strftime('%d/%m/%Y')}"

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username} em {self.artigo}"