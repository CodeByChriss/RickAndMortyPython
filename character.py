class character:
    
    # El tipo de las variables de esta clase son:
    # id = int
    # name = String
    # status = String
    # species = String
    # type = String
    # gender = String
    # origin = {"name":String,"url":String}
    # location = {"name":String,"url":String}
    # image = String (es una url)
    # episode = [] (de urls)
    # url = String (url de la información de este character)
    # created = String (tiempo en el que fue creado en la base de datos)

    def __init__(self, id, name, status, species, type, gender, origin, location, image, episode, url, created):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode = episode
        self.url = url
        self.created = created

    def obtenerCantidadEpisodios(self):
        return len(self.episode)
    
    def obtenerFechaRegistro(self):
        # tiene este formato: 2017-12-29T18:51:29.693Z
        fecha = self.created.split("T") # divido la fecha de la hora
        return fecha[0]
    
    # Lo convertimos a un diccionario para guardarlo en un fichero JSON
    def obtenerFormatoDiccionario(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "type": self.type,
            "gender": self.gender,
            "origin": self.origin,
            "location": self.location,
            "image": self.image,
            "episode": self.episode,
            "url": self.url,
            "created": self.created
        }
    
    # Lo mostramos por pantalla al usuario de una forma más estética
    def mostrarDatos(self):
        separadorPrincipal = "=" * 50
        separadorSecundario = "-" * 50
        print(separadorPrincipal)
        print(f"FICHA DE PERSONAJE: {self.name.upper()}")
        print(separadorSecundario)
        print(f"ID:        {self.id}")
        print(f"Imagen:    {self.image}")
        print(f"Estado:    {self.status}")
        print(f"Especie:   {self.species}")
        print(f"Tipo:      {self.type if self.type else 'N/A'}")
        print(f"Género:    {self.gender}")
        print(separadorSecundario)
        print(f"Origen:    {self.origin['name']}")
        print(f"Ubicación: {self.location['name']}")
        print(separadorSecundario)
        print(f"Apariciones: {self.obtenerCantidadEpisodios()} episodios")
        print(f"Registrado:  {self.obtenerFechaRegistro()}")
        print(separadorSecundario)
        print(f"Toda la información:  {self.url}")
        print(separadorPrincipal)