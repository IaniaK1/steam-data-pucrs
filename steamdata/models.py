class Game:
    """
    Representa um jogo da Steam.
    """
    def __init__(self, id, name, year, is_free, price, genre):
        self.id = id
        self.name = name
        self.year = year
        self.is_free = is_free # Criei para facilitar a consulta, mas é possivel usar só o price
        self.price = price
        if not genre or genre == ['']: # Com a amostra, percebi que alguns jogos não têm gênero definido
            self.genre = ["Undefined"]
        else:
            self.genre = genre
