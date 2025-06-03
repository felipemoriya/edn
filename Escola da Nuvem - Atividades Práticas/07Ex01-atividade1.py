# 1) Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de execução constantes. 

import csv
import statistics

dados = [
    {"modelo": "ModeloA", "tempo_execucao": 120},
    {"modelo": "ModeloB", "tempo_execucao": 150},
    {"modelo": "ModeloC", "tempo_execucao": 130},
    {"modelo": "ModeloD", "tempo_execucao": 110},
    {"modelo": "ModeloE", "tempo_execucao": 140}
]

tempos = [item["tempo_execucao"] for item in dados]

media = statistics.mean(tempos)
desvio_padrao = statistics.pstdev(tempos)  # pstdev = desvio padrão populacional

print(f"Média dos tempos de execução: {media:.2f} segundos")
print(f"Desvio padrão dos tempos de execução: {desvio_padrao:.2f} segundos")

# Média dos tempos de execução: 130.00 segundos
# Desvio padrão dos tempos de execução: 14.14 segundos