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