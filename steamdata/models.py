class Game:
    """
    Representa um jogo da Steam.
    """
    def __init__(self, id, name, year, is_free, price, genre):
        self.id = id
        self.name = name
        self.year = year
        self.is_free = is_free
        self.price = price
        self.genre = genre
