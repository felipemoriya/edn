distancia = float(input("Digite a distância percorrida (em km): "))
combustivel = float(input("Digite a quantidade de combustível gasto (em litros): "))

consumo_medio = distancia / combustivel

print("\nDados da viagem:")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")