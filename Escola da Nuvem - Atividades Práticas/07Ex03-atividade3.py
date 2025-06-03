# 3) Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

import csv

arquivo_csv = 'pessoas.csv'

try:
    with open(arquivo_csv, mode='r', encoding='utf-8') as f:
        leitor_csv = csv.DictReader(f)
        
        print("Dados do arquivo CSV:\n")
        for linha in leitor_csv:
            nome = linha['Nome']
            idade = linha['Idade']
            cidade = linha['Cidade']
            print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
except FileNotFoundError:
    print(f"Arquivo '{arquivo_csv}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")


# Nome,Idade,Cidade
# João,30,São Paulo
# Maria,25,Rio de Janeiro
# Carlos,40,Belo Horizonte