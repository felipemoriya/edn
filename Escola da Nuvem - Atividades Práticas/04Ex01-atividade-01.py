# Desenvolva uma calculadora em Python que realize as quatro operações básicas 
# (adição, subtração, multiplicação e divisão) entre dois números. 
# A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

# A calculadora deve solicitar ao usuário que insira dois números e uma operação.
# As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
# O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
# Trate os seguintes erros:
# Entrada inválida (não numérica) para os números
# Divisão por zero
#Operação inválida
# Use try/except para capturar e tratar os erros apropriadamente.
# Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
# Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.

def calcular():
    while True:
        try:
 
            num1 = input("Digite o primeiro número: ")
            num1 = float(num1)
            
            num2 = input("Digite o segundo número: ")
            num2 = float(num2)
            
            operacao = input("Digite a operação (+, -, *, /): ")
            
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Não é possível dividir por zero.")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida. Use apenas +, -, * ou /.")

            print(f"Resultado: {resultado}")
            break

        except ValueError as ve:
            print(f"Erro: {ve}. Tente novamente.\n")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}. Tente novamente.\n")

calcular()