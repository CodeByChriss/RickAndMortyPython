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
    
    # Lo convertimos a un diccionario para guardarlo en un fichero JSON
    def obtenerFormatoDiccionario(self):
        return {
            "id": self.id,
            "name": self.name,
            "air_date": self.air_date,
            "episode": self.episode,
            "characters": self.characters,
            "url": self.url,
            "created": self.obtenerFechaRegistro()
        }
    
    # Lo mostramos por pantalla al usuario de una forma más estética
    def mostrarDatos(self):
        separadorPrincipal = "=" * 50
        separadorSecundario = "-" * 50
        print(separadorPrincipal)
        print(f"DETALLES DEL EPISODIO: {self.name.upper()}")
        print(separadorSecundario)
        print(f"ID:             {self.id}")
        print(f"Código:         {self.episode}")
        print(f"Fecha Aire:     {self.air_date}")
        print(separadorSecundario)
        print(f"Personajes:     {self.obtenerCantidadCharacters()} en pantalla")
        print(f"URL Info:       {self.url}")
        print(f"Registrado:     {self.obtenerFechaRegistro()}")
        print(separadorPrincipal)