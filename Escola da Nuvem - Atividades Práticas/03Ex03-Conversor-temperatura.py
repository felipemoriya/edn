def converter_temperatura(valor, origem, destino):
    if origem == "C":
        temp_c = valor
    elif origem == "F":
        temp_c = (valor - 32) * 5/9
    elif origem == "K":
        temp_c = valor - 273.15
    else:
        return "Unidade de origem inválida."
    if destino == "C":
        return temp_c
    elif destino == "F":
        return (temp_c * 9/5) + 32
    elif destino == "K":
        return temp_c + 273.15
    else:
        return "Unidade de destino inválida."


    valor = float(input("Digite o valor da temperatura: "))
    origem = input("Digite a unidade de origem (C, F ou K): ").upper()
    destino = input("Digite a unidade de destino (C, F ou K): ").upper()

    resultado = converter_temperatura(valor, origem, destino)

    if isinstance(resultado, float):
        print(f"{valor}°{origem} é igual a {resultado:.2f}°{destino}")
    else:
        print(resultado)