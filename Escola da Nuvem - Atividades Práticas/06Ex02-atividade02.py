 # *Exercicio 2*: # Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
# O programa deve exibir o nome, email e país do usuário gerado."

import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("=== Perfil de Usuário Gerado ===")
        print(f"Nome : {nome}")
        print(f"Email: {email}")
        print(f"País : {pais}")
    else:
        print("Erro ao acessar a API. Código de status:", response.status_code)

if __name__ == "__main__":
    gerar_usuario()