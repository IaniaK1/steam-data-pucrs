import csv
from .models import Game
from .exceptions import DataLoadError

class GameLoader:
    """
    Responsável por carregador jogos a partir de um arquivo CSV.
    """
    @staticmethod
    def load_from_csv(filepath):
        games = []
        try:
            with open(filepath, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    game = Game(
                        id=int(row['AppID']),
                        name=row['Name'],
                        year=int(row['Release date'][-4:]) if row['Release date'] else None,
                        is_free=float(row['Price']) == 0.0 if row['Price'] else False,
                        price=float(row['Price']) if row['Price'] else 0.0,
                        genre=row['Genres'].split(',')
                    )
                    games.append(game)
        except Exception as e:
            raise DataLoadError(f"Erro ao carregar jogos: {e}")
        return games