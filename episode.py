class episode:

    # El tipo de las variables de esta clase son:
    # id = int
    # name = String
    # air_date = String
    # episode = String (ej: "S01E01")
    # characters = List (of URLs)
    # url = String (url)
    # created = String

    def __init__(self, id, name, air_date, episode, characters, url, created):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created