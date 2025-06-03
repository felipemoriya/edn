# Crie um programa que permita a um professor registrar as notas de uma turma. 
# O programa deve continuar solicitando notas até que o professor digite 'fim'. 
# Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. 
# No final, deve exibir a média da turma. Notas = [] -> len(Notas)


notas = []

while True:
    entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f}")
    print(f"Total de notas válidas registradas: {len(notas)}")
else:
    print("\nNenhuma nota válida foi registrada.")




