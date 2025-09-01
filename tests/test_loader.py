from steamdata.loader import GameLoader

games = GameLoader.load_from_csv('samples/sample_20.csv')
print(f'Total de jogos carregados: {len(games)}')
print('Primeiro jogo:', vars(games[0]))
