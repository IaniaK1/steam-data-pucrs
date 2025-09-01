"""
Gera uma amostra aleatória de 20 jogos a partir do arquivo steam_games.csv, 
ignorando as 20 primeiras linhas de dados (após o cabeçalho), conforme solicitado no enunciado do trabalho.

A amostra é salva no arquivo samples/sample_20.csv, incluindo o cabeçalho original.

Uso:
    Basta executar este script uma vez para criar a amostra que será utilizada nos testes automatizados.

Atenção:
    - O resultado é utilizado para validar manualmente e automaticamente as respostas das queries.
"""

import csv
import random

with open('steam_games.csv', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    header = reader[0]
    data = reader[21:] # Aqui eu pulei o cabeçalho e as 20 primeiras linhas como pede o enunciado
    sample = random.sample(data, 20)

with open('samples/sample_20.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(sample)
