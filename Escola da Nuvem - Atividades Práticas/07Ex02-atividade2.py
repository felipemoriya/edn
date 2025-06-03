# 2) Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

import csv

arquivo_csv = 'pessoas.csv'

dados_pessoas = [
    {"Nome": "João", "Idade": 30, "Cidade": "São Paulo"},
    {"Nome": "Maria", "Idade": 25, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carlos", "Idade": 40, "Cidade": "Belo Horizonte"}
]

with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as f:
    nomes_colunas = ["Nome", "Idade", "Cidade"]
    escritor_csv = csv.DictWriter(f, fieldnames=nomes_colunas)

    escritor_csv.writeheader()  # Escreve o cabeçalho
    escritor_csv.writerows(dados_pessoas)  # Escreve os dados

print(f"Dados escritos com sucesso no arquivo '{arquivo_csv}'!")

# Dados escritos com sucesso no arquivo 'pessoas.csv'!