import requests
import json
import os

schoolYear = '202526'
course = 260  # LEI

os.makedirs('data/files', exist_ok=True)

# Buscar informação do curso
url_curso = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'

payload = {
    'language': 'PT',
    'courseCode': course,
    'schoolYear': schoolYear
}
headers = {'content-type': 'application/json'}

response = requests.post(url_curso, json=payload, headers=headers)
curso = response.json()

# Guardar JSON do curso
with open(f'data/files/ULHT{course}-PT.json', 'w', encoding='utf-8') as f:
    json.dump(curso, f, indent=4, ensure_ascii=False)

print(f"Curso: {curso.get('courseName', '')}")
print(f"Total de UCs: {len(curso.get('courseFlatPlan', []))}")

# Buscar informação de cada UC
url_uc = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'

for uc in curso.get('courseFlatPlan', []):
    codigo = uc['curricularIUnitReadableCode']

    payload_uc = {
        'language': 'PT',
        'curricularIUnitReadableCode': codigo,
    }

    response_uc = requests.post(url_uc, json=payload_uc, headers=headers)
    uc_dados = response_uc.json()

    with open(f'data/files/{codigo}-PT.json', 'w', encoding='utf-8') as f:
        json.dump(uc_dados, f, indent=4, ensure_ascii=False)

    print(f"  UC guardada: {codigo}")

print("Concluído!")