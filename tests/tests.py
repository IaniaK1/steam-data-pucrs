import unittest
from steamdata.loader import GameLoader
from steamdata.queries import GameQueries, QueryError

class TestGameQueries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Carrega a amostra uma única vez para todos os testes
        cls.games = GameLoader.load_from_csv('samples/sample_20.csv')

    def test_percentual_gratuitos_e_pagos(self):
        esperado = {'gratuitos': 20.0, 'pagos': 80.0}
        resultado = GameQueries.percentual_gratuitos_e_pagos(self.games)
        self.assertEqual(resultado, esperado)

    def test_ano_com_mais_lancamentos(self):
        esperado = [2022, 2019, 2023, 2014, 2018]
        resultado = GameQueries.ano_com_mais_lancamentos(self.games)
        self.assertCountEqual(resultado, esperado)  # Não importa a ordem

    def test_media_de_preco_por_genero(self):
        esperado = {
            'Indie': 5.7, 'Racing': 7.99, 'Simulation': 15.1, 'Sports': 11.49, 'Undefined': 0.0,
            'Adventure': 12.78, 'Casual': 5.8, 'Action': 11.49, 'Strategy': 15.85, 'RPG': 2.49,
            'Early Access': 8.32, 'Free to Play': 0.0, 'Massively Multiplayer': 5.99
        }
        resultado = GameQueries.media_de_preco_por_genero(self.games)
        for genero in esperado:
            self.assertAlmostEqual(resultado.get(genero, 0), esperado[genero], places=2)

    def test_percentual_lista_vazia(self):
        with self.assertRaises(QueryError):
            GameQueries.percentual_gratuitos_e_pagos([])

    def test_ano_lista_vazia(self):
        with self.assertRaises(QueryError):
            GameQueries.ano_com_mais_lancamentos([])

    def test_media_lista_vazia(self):
        with self.assertRaises(QueryError):
            GameQueries.media_de_preco_por_genero([])

if __name__ == '__main__':
    unittest.main()