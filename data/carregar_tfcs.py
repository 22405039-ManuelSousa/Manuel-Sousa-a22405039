import json
from portfolio.models import TFC

with open('data/tfcs-24-25.json', encoding='utf-8') as f:
    tfcs = json.load(f)

for item in tfcs:
    TFC.objects.create(
        titulo=item['titulo'],
        aluno=item['aluno'][0],
        orientador=item['orientador'][0] if item['orientador'] else '',
        ano=2025,
    )

print(f"{len(tfcs)} TFCs carregados!")

# correr com python manage.py shell < data/carregar_tfcs.py