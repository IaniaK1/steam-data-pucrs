from steamdata.loader import GameLoader

games = GameLoader.load_from_csv('steam_games.csv')
print(f'Total de jogos carregados: {len(games)}')
print('Primeiro jogo:', vars(games[0]))
