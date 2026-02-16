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
    # created = String

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