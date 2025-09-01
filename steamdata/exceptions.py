class DataLoadError(Exception):
    """
    Exceção levantada em caso de erro ao carregar dados.
    """
    pass

class DataParseError(Exception):
    """
    Exceção levantada em caso de erro ao interpretar/converter dados do CSV.
    """
    pass

class QueryError(Exception):
    """
    Exceção levantada em caso de erro ao executar uma consulta.
    """
    pass