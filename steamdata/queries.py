class GameQueries:
    @staticmethod
    def percentual_gratuitos_e_pagos(games):
        total = len(games)
        if total == 0:
            return {"gratuitos": 0, "pagos": 0}
        gratuitos = sum(1 for game in games if game.is_free)
        pagos = total - gratuitos
        return {"gratuitos": gratuitos / total * 100, "pagos": pagos / total * 100}
    
    @staticmethod
    def ano_com_mais_lancamentos(games):
        anos = {}
        for game in games:
            ano = game.year
            anos[ano] = anos.get(ano, 0) + 1
        if not anos:
            return None
        max_lanc = max(anos.values())
        anos_max = [ano for ano, qtd in anos.items() if qtd == max_lanc]
        return anos_max
    
    @staticmethod
    def media_de_preco_por_genero(games):
        precos = {}
        for game in games:
            for genero in game.genre:
                precos[genero] = precos.get(genero, []) + [game.price]
        medias = {genero: sum(precos[genero]) / len(precos[genero]) for genero in precos}
        return medias