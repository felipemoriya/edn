# 4) Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.

import json

arquivo_json = 'pessoa.json'

pessoa = {
    "nome": "João Silva",
    "idade": 30,
    "cidade": "São Paulo"
}

with open(arquivo_json, 'w', encoding='utf-8') as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=4)
    print(f"Dados salvos em {arquivo_json}")

with open(arquivo_json, 'r', encoding='utf-8') as f:
    dados_lidos = json.load(f)
    print("\nDados lidos do arquivo:")
    print(dados_lidos)

import json

arquivo_json = 'pessoa.json'

pessoa = {
    "nome": "João Silva",
    "idade": 30,
    "cidade": "São Paulo"
}

with open(arquivo_json, 'w', encoding='utf-8') as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=4)
    print(f"Dados salvos em {arquivo_json}")

with open(arquivo_json, 'r', encoding='utf-8') as f:
    dados_lidos = json.load(f)
    print("\nDados lidos do arquivo:")
    print(dados_lidos)