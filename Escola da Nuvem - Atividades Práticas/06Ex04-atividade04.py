# *Exercicio 4:*# Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL).
# O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP),
# e o programa deve exibir o valor atual, máximo e mínimo da cotação,
# além da data e hora da última atualização.
# Utilize a API da AwesomeAPI para obter os dados de cotação.​
# pip install requests

import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        chave = f"{moeda}BRL"

        if chave in dados:
            info = dados[chave]
            nome = info['name']
            valor_atual = info['bid']
            valor_maximo = info['high']
            valor_minimo = info['low']
            data = info['create_date']

            print("=== Cotação Atual ===")
            print(f"Moeda         : {nome}")
            print(f"Valor atual   : R$ {valor_atual}")
            print(f"Valor máximo  : R$ {valor_maximo}")
            print(f"Valor mínimo  : R$ {valor_minimo}")
            print(f"Última atualização: {data}")
        else:
            print(f"Moeda '{moeda}' não encontrada ou não suportada.")
    else:
        print("Erro ao acessar a API da AwesomeAPI.")

def main():
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip()
    if moeda:
        consultar_cotacao(moeda)
    else:
        print("Código da moeda não pode estar vazio.")

if __name__ == "__main__":
    main()