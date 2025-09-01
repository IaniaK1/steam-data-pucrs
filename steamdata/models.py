class Game:
    """
    Representa um jogo da Steam.

    Atributos:
        id (int): ID do jogo.
        name (str): Nome do jogo.
        year (int): Ano de lançamento.
        is_free (bool): Indica se o jogo é gratuito.
        price (float): Preço do jogo.
        genre (list): Lista de gêneros do jogo.
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
