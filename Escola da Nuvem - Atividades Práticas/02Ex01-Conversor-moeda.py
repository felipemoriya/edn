valor_reais = float(input("Digite o valor em reais (R$): "))
taxa_dolar = float(input("Digite a taxa do dólar (R$): "))
taxa_euro = float(input("Digite a taxa do euro (R$): "))

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Valor convertido em dólares: US$ {valor_dolar:.2f}")
print(f"Valor convertido em euros: € {valor_euro:.2f}")