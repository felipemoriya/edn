# *Exercicio1:* Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória. ​

import random
import string

def gerar_senha(tamanho):
    # Conjunto de caracteres: letras, dígitos e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Geração da senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    try:
        tamanho = int(input("Informe o tamanho da senha desejada: "))
        if tamanho <= 0:
            print("Por favor, informe um número maior que zero.")
        else:
            senha = gerar_senha(tamanho)
            print(f"Senha gerada: {senha}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()

#Informe o tamanho da senha desejada: 
#4
#Senha gerada: x6MZ