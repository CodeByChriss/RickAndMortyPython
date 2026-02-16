class location:

    # El tipo de las variables de esta clase son:
    # id = int
    # name = String
    # type = String
    # dimension = String
    # residents = List (of URLs)
    # url = String (url)
    # created = String

    def __init__(self, id, name, type, dimension, residents, url, created):
        self.id = id
        self.name = name
        self.type = type
        self.dimension = dimension
        self.residents = residents
        self.url = url
        self.created = created