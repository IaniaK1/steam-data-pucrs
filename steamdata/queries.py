from .exceptions import QueryError

class GameQueries:
    """
    Classe utilitária para realizar consultas (queries) sobre uma lista de objetos Game.
    """


    @staticmethod
    def percentual_gratuitos_e_pagos(games):
        """
        Calcula o percentual de jogos gratuitos e pagos na lista fornecida.

        Args:
            games (list): Lista de objetos Game.

        Returns:
            dict: Dicionário com as chaves 'gratuitos' e 'pagos', contendo os percentuais de cada categoria.

        Raises:
            QueryError: Se a lista de jogos estiver vazia.
        """
        if not games:
            raise QueryError('A lista de jogos está vazia. Não é possível calcular percentuais.')
        total = len(games)
        gratuitos = sum(1 for game in games if game.is_free)
        pagos = total - gratuitos
        return {'gratuitos': gratuitos / total * 100, 'pagos': pagos / total * 100}
    
    @staticmethod
    def ano_com_mais_lancamentos(games):
        """
        Retorna o(s) ano(s) com maior número de lançamentos de jogos.

        Args:
            games (list): Lista de objetos Game.

        Returns:
            list: Lista com o(s) ano(s) que tiveram mais lançamentos.

        Raises:
            QueryError: Se a lista de jogos estiver vazia ou se algum jogo não tiver ano definido.
        """
        if not games:
            raise QueryError('A lista de jogos está vazia. Não é possível calcular o ano com mais lançamentos.')
        anos = {}
        for game in games:
            if game.year is None:
                raise QueryError(f'Jogo sem ano de lançamento definido: {game.name}')
            ano = game.year
            anos[ano] = anos.get(ano, 0) + 1
        if not anos:
            raise QueryError('Nenhum ano de lançamento encontrado nos jogos.')
        max_lanc = max(anos.values())
        anos_max = [ano for ano, qtd in anos.items() if qtd == max_lanc]
        return anos_max
    
    @staticmethod
    def media_de_preco_por_genero(games):
        """
        Calcula a média de preço dos jogos agrupados por gênero.

        Args:
            games (list): Lista de objetos Game.

        Returns:
            dict: Dicionário onde as chaves são os gêneros e os valores são as médias de preço (arredondadas para 2 casas decimais).

        Raises:
            QueryError: Se a lista de jogos estiver vazia ou se não houver gêneros para calcular.
        """
        if not games:
            raise QueryError('A lista de jogos está vazia. Não é possível calcular médias de preço por gênero.')
        precos = {}
        for game in games:
            for genero in game.genre:
                precos[genero] = precos.get(genero, []) + [game.price]
        if not precos:
            raise QueryError('Nenhum gênero encontrado para calcular médias de preço.')
        medias = {genero: round(sum(precos[genero]) / len(precos[genero]), 2) for genero in precos}
        return medias
    