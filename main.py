from steamdata.loader import GameLoader
from steamdata.queries import GameQueries, QueryError
from steamdata.exceptions import DataLoadError

def main():
    print('==== Análise de Jogos Steam ====')
    arquivo = input('Deseja usar a amostra ou o CSV completo? (amostra/completo) ').strip().lower()

    if arquivo == 'amostra':
        arquivo = 'samples/sample_20.csv'
    else:
        arquivo = 'steam_games.csv'

    try:
        games = GameLoader.load_from_csv(arquivo)
        print(f'Total de jogos carregados: {len(games)}\n')
    except DataLoadError as e:
        print(f'Erro ao carregar dados: {e}')
        return

    # 1. Percentual de jogos gratuitos e pagos
    try:
        percentuais = GameQueries.percentual_gratuitos_e_pagos(games)
        print(f'Percentual de jogos gratuitos: {percentuais['gratuitos']:.2f}%')
        print(f'Percentual de jogos pagos: {percentuais['pagos']:.2f}%\n')
    except QueryError as e:
        print(f'Erro na consulta de percentuais: {e}')

    # 2. Ano(s) com mais lançamentos
    try:
        anos = GameQueries.ano_com_mais_lancamentos(games)
        anos_str = ', '.join(map(str, anos))
        print(f'\nAno(s) com mais lançamentos: {anos_str}.')
    except QueryError as e:
        print(f'Erro na consulta de anos: {e}')

    # 3. Média de preço por gênero
    try:
        medias = GameQueries.media_de_preco_por_genero(games)
        print('\nMédia de preço por gênero:')
        for genero, media in medias.items():
            print(f"  {genero}: US$ {media:.2f}")
    except QueryError as e:
        print(f'Erro na consulta de médias: {e}')

if __name__ == '__main__':
    main()