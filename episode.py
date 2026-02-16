class episode:

    # El tipo de las variables de esta clase son:
    # id = int
    # name = String
    # air_date = String
    # episode = String (ej: "S01E01")
    # characters = List (of URLs)
    # url = String (url)
    # created = String (tiempo en el que fue creado en la base de datos)

    def __init__(self, id, name, air_date, episode, characters, url, created):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created

    def obtenerCantidadCharacters(self):
        return len(self.characters)

    def obtenerFechaRegistro(self):
        # tiene este formato: 2017-12-29T18:51:29.693Z
        fecha = self.created.split("T") # divido la fecha de la hora
        return fecha[0]