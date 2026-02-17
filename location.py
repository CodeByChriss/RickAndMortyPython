class location:

    # El tipo de las variables de esta clase son:
    # id = int
    # name = String
    # type = String
    # dimension = String
    # residents = List (of URLs)
    # url = String (url)
    # created = String (tiempo en el que fue creado en la base de datos)

    def __init__(self, id, name, type, dimension, residents, url, created):
        self.id = id
        self.name = name
        self.type = type
        self.dimension = dimension
        self.residents = residents
        self.url = url
        self.created = created

    def obtenerCantidadCharacters(self):
        return len(self.residents)

    def obtenerFechaRegistro(self):
        # tiene este formato: 2017-12-29T18:51:29.693Z
        fecha = self.created.split("T") # divido la fecha de la hora
        return fecha[0]
    
    def obtenerFormatoDiccionario(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "dimension": self.dimension,
            "residents": self.residents,
            "url": self.url,
            "created": self.created
        }
    
    def mostrarDatos(self):
        separadorPrincipal = "=" * 50
        separadorSecundario = "-" * 50
        print(separadorPrincipal)
        print(f"DATOS DE LOCALIZACIÓN: {self.name.upper()}")
        print(separadorSecundario)
        print(f"ID:        {self.id}")
        print(f"Tipo:      {self.type if self.type else 'N/A'}")
        print(f"Dimensión: {self.dimension if self.dimension else 'Unknown'}")
        print(separadorSecundario)
        print(f"Residentes Totales: {self.obtenerCantidadCharacters()}")
        print(f"URL Info:           {self.url}")
        print(f"Registrado:         {self.obtenerFechaRegistro()}")
        print(separadorPrincipal)