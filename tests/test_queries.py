from steamdata.loader import GameLoader
from steamdata.queries import GameQueries

games = GameLoader.load_from_csv('samples/sample_20.csv')

percentuais = GameQueries.percentual_gratuitos_e_pagos(games)
print(f'Percentuais: {percentuais}')

anos = GameQueries.ano_com_mais_lancamentos(games)
print(f'Ano(s) com mais lançamentos: {anos}')

medias = GameQueries.media_de_preco_por_genero(games)
print(f'Médias de preço por gênero: {medias}')
