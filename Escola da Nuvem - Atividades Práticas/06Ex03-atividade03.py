# *Exercicio 3*: # Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,
# utilizando a API ViaCEP.
# O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
# pip install requests

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        if "erro" in dados:
            print("CEP não encontrado. Verifique se o CEP está correto.")
        else:
            logradouro = dados.get("logradouro", "N/A")
            bairro = dados.get("bairro", "N/A")
            cidade = dados.get("localidade", "N/A")
            estado = dados.get("uf", "N/A")

            print("=== Informações do Endereço ===")
            print(f"Logradouro: {logradouro}")
            print(f"Bairro    : {bairro}")
            print(f"Cidade    : {cidade}")
            print(f"Estado    : {estado}")
    else:
        print("Erro ao consultar a API ViaCEP.")

def main():
    cep = input("Digite o CEP (apenas números): ").strip()
    if len(cep) == 8 and cep.isdigit():
        consultar_cep(cep)
    else:
        print("CEP inválido. Certifique-se de digitar 8 números.")

if __name__ == "__main__":
    main()
