from django.db import models


class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    url_lusofona = models.URLField(blank=True)
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)

    def __str__(self):
        return self.nome


class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    ects = models.IntegerField(default=180)
    
    def __str__(self):
        return f"{self.sigla} – {self.nome}"


class UnidadeCurricular(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE,
                                     related_name='unidades_curriculares')
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20, blank=True)
    ano = models.IntegerField(default=4)
    semestre = models.IntegerField(default=2)
    docentes = models.ManyToManyField(Docente, blank=True, related_name='unidades_curriculares')
    obrigatoria = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sigla or self.nome} ({self.ano}º Ano, {self.semestre}º Sem)"


class Tecnologia(models.Model):
    CATEGORIA_CHOICES = [
        ('linguagem', 'Linguagem de Programação'),
        ('framework', 'Framework'),
        ('bd', 'Base de Dados'),
        ('devops', 'DevOps / Infraestrutura'),
        ('ferramenta', 'Ferramenta'),
        ('design', 'Design / Frontend'),
        ('outro', 'Outro'),
    ]
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='outro')
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    url = models.URLField(blank=True)
    nivel = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.nome}"


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    video = models.URLField(blank=True)
    github = models.URLField(blank=True)
    deploy = models.URLField(blank=True)
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.SET_NULL,
                                            null=True, blank=True, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='projetos')
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class TFC(models.Model):
    titulo = models.CharField(max_length=300)
    aluno = models.CharField(max_length=200)
    orientador = models.CharField(max_length=200, blank=True)
    ano = models.PositiveIntegerField()
    interesse = models.IntegerField(default=10)
    destaque = models.BooleanField(default=False)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='tfcs')
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.SET_NULL,
                                      null=True, blank=True, related_name='tfcs')

    def __str__(self):
        return f"{self.ano}"


class Competencia(models.Model):
    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20)
    nivel = models.CharField(max_length=20)
    descricao = models.TextField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='competencias')
    projetos = models.ManyToManyField(Projeto, blank=True, related_name='competencias')

    def __str__(self):
        return f"{self.nome}"


class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='formacoes')
    competencias = models.ManyToManyField(Competencia, blank=True, related_name='formacoes')

    def __str__(self):
        return f"{self.nome}"


class MakingOf(models.Model):
    titulo = models.CharField(max_length=200)
    entidade_relacionada = models.CharField(max_length=50)
    descricao = models.TextField()
    decisoes = models.TextField(blank=True)
    erros = models.TextField(blank=True)
    uso_ia = models.TextField(blank=True)
    foto_caderno = models.ImageField(upload_to='makingof/', blank=True, null=True)
    der = models.ImageField(upload_to='makingof/der/', blank=True, null=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='making_of')
    tecnologia = models.ForeignKey(Tecnologia, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='making_of')
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.SET_NULL,
                                            null=True, blank=True, related_name='making_of')

    def __str__(self):
        return f"{self.titulo}"


class Conquista(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20)
    data = models.DateField(blank=True, null=True)
    projetos = models.ManyToManyField(Projeto, blank=True, related_name='conquistas')
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name='conquistas')

    def __str__(self):
        return f"{self.titulo}"