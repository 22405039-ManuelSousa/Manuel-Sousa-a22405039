import os
from django.core.files import File
from django.conf import settings

from portfolio.models import Docente, Tecnologia, Projeto, MakingOf
from artigos.models import Artigo

OLD_MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')

def migrar_campo(obj, campo, label):
    field = getattr(obj, campo)
    if not field or not field.name:
        return
    local_path = os.path.join(OLD_MEDIA_ROOT, field.name)
    if os.path.exists(local_path):
        with open(local_path, 'rb') as f:
            field.save(os.path.basename(local_path), File(f), save=True)
        print(f"Migrado {label}: {obj}")
    else:
        print(f"Ficheiro nao encontrado localmente: {local_path}")

for obj in Docente.objects.all():
    migrar_campo(obj, 'foto', 'Docente')

for obj in Tecnologia.objects.all():
    migrar_campo(obj, 'logo', 'Tecnologia')

for obj in Projeto.objects.all():
    migrar_campo(obj, 'imagem', 'Projeto')

for obj in MakingOf.objects.all():
    migrar_campo(obj, 'foto_caderno', 'MakingOf foto')
    migrar_campo(obj, 'der', 'MakingOf der')

for obj in Artigo.objects.all():
    migrar_campo(obj, 'fotografia', 'Artigo')
