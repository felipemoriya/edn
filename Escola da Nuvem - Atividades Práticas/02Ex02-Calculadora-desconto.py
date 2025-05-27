nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o preço original (R$): "))
percentual_desconto = float(input("Digite a porcentagem de desconto (%): "))

valor_desconto = preco_original * (percentual_desconto / 100)

preco_final = preco_original - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")