import main
import getApiData
import json
import character
import location
import episode

class rickAndMorty:
    
    def __init__(self):
        # Declaramos las variables de la clase vacias para evitar errores
        self.characters = []
        self.episodes = []
        self.locations = []

    def mostrarMenuPrincipal(self):
        print("╔═════════════════════════ Menú principal ═════════════════════════╗")
        print("╠ 1. Obtener datos de la API.")
        print("╠ 2. Cargar datos de un fichero JSON.")
        print("╠ 3. Exportar datos a un fichero JSON.")
        print("╠ 4. Interactuar con los datos.")
        print("╠ 5. Salir.")
        print("╚══════════════════════════════════════════════════════════════════╝")

    def mostrarMenuInteractuarDatos(self):
        print("╔═══════════════════ Opciones Interactuar con los datos ═══════════════════╗")
        print("╠ 1. Visualizar los datos.")
        print("╠ 2. Buscar por ID.")
        print("╠ 3. Ver cantidad de datos que tenemos.")
        print("╠ 4. Volver atrás.")
        print("╚══════════════════════════════════════════════════════════════════════════╝")

    def obtenerDatosAPI(self):
        apiData = getApiData.getApiData()
        opt = apiData.mostrarOpciones()
        datos = apiData.obtenerDatos(opt)
        match opt:
            case 1:
                self.characters = datos
            case 2:
                self.locations = datos
            case 3:
                self.episodes = datos
            case _:
                print("Error, datos no guardados.")

    def cargarFichero(self):
        print("Selecciona el tipo de dato que quieres cargar (este proceso no sobreescribe los datos actuales):")
        apiData = getApiData.getApiData()
        opt = apiData.mostrarOpciones()

        nombreFichero = input("Dime el nombre del fichero que quieres cargar: ")
        try:
            with open(nombreFichero, "r", encoding="utf-8") as f:
                datos = json.load(f)

            for dato in datos:
                try:
                    match opt:
                        case 1: # si es un character
                            newCharacter = character.character(
                                dato['id'], dato['name'], dato['status'], dato['species'], 
                                dato['type'], dato['gender'], dato['origin'], dato['location'], 
                                dato['image'], dato['episode'], dato['url'], dato['created']
                            )
                            self.characters.append(newCharacter)
                        case 2:
                            newLocation = location.location(
                                dato['id'], 
                                dato['name'], 
                                dato['type'], 
                                dato['dimension'], 
                                dato['residents'], 
                                dato['url'], 
                                dato['created']
                            )
                            self.locations.append(newLocation)
                        case 3:
                            newEpisode = episode.episode(
                                dato['id'], 
                                dato['name'], 
                                dato['air_date'], 
                                dato['episode'], 
                                dato['characters'], 
                                dato['url'], 
                                dato['created']
                            )
                            self.episode.append(newEpisode)
                except KeyError:
                    continue

            print("Fichero cargado correctamente.")
        except FileNotFoundError:
            print("ERROR: Fichero no encontrado.")
        except json.JSONDecodeError:
            print("ERROR: El fichero JSON contiene errores.")

    def guardarFichero(self):
        print("Selecciona el tipo de dato que quieres guardar:")
        apiData = getApiData.getApiData()
        opt = apiData.mostrarOpciones()
        
        nombreFichero = input("Dime el nombre del fichero en el que lo quieres guardar: ")

        datos = []
        match opt:
            case 1:
                datos = self.characters
            case 2:
                datos = self.locations
            case 3:
                datos = self.episodes

        datosDict = [d.obtenerFormatoDiccionario() for d in datos]

        # No hace falta usar try-except ya que Python por defecto crea el fichero si no existe
        with open(nombreFichero, "w", encoding="utf-8") as f:
            json.dump(datosDict,f,indent=4,ensure_ascii=False)

        print("Datos guardados con éxito.")

    def visualizarDatos(self):
        print("Selecciona el tipo de datos que quieres visualizar:")
        apiData = getApiData.getApiData()
        opt = apiData.mostrarOpciones()

        match opt:
            case 1:
                if self.characters:
                    for character in self.characters:
                        character.mostrarDatos()
                else:
                    print("No hay contenido de ese tipo.")
            case 2:
                if self.locations:
                    for location in self.locations:
                        location.mostrarDatos()
                else:
                    print("No hay contenido de ese tipo.")
            case 3:
                if self.episodes:
                    for episode in self.episodes:
                        episode.mostrarDatos()
                else:
                    print("No hay contenido de ese tipo.")

    def buscarPorID(self):
        print("Selecciona el tipo de dato por el que quieres buscar:")
        apiData = getApiData.getApiData()
        opt = apiData.mostrarOpciones()

        match opt:
            case 1:
                if self.characters:
                    lon = len(self.characters)
                    print(f"Introduce el ID que quieres buscar. El ID mínimo es 1 y el máximo es {lon}.")
                    idBuscar = main.obtenerOpcion(1,lon) # el primer ID es 1
                    for character in self.characters:
                        if character.id == idBuscar:
                            character.mostrarDatos()
                            return
                    print("Character no encontrado.")
                else:
                    print("No hay contenido de ese tipo.")
            case 2:
                if self.locations:
                    lon = len(self.locations)
                    print(f"Introduce el ID que quieres buscar. El ID mínimo es 1 y el máximo es {lon}.")
                    idBuscar = main.obtenerOpcion(1,lon) # el primer ID es 1
                    for location in self.locations:
                        if location.id == idBuscar:
                            location.mostrarDatos()
                            return
                    print("Location no encontrada.")
                else:
                    print("No hay contenido de ese tipo.")
            case 3:
                if self.episodes:
                    lon = len(self.episodes)
                    print(f"Introduce el ID que quieres buscar. El ID mínimo es 1 y el máximo es {lon}.")
                    idBuscar = main.obtenerOpcion(1,lon) # el primer ID es 1
                    for episode in self.episodes:
                        if episode.id == idBuscar:
                            episode.mostrarDatos()
                            return
                    print("Episode no encontrado.")
                else:
                    print("No hay contenido de ese tipo.")

    def obtenerCantidadCharacters(self):
        return len(self.characters)
    
    def obtenerCantidadLocations(self):
        return len(self.locations)
    
    def obtenerCantidadEpisodes(self):
        return len(self.episodes)
    
    def mostrarCantidades(self):
        print("╔═══════════════════ Cantidades de datos ═══════════════════╗")
        print(f"╠ Characters: {self.obtenerCantidadCharacters()}")
        print(f"╠ Locations: {self.obtenerCantidadLocations()}")
        print(f"╠ Episodes: {self.obtenerCantidadEpisodes()}")
        print("╚═══════════════════════════════════════════════════════════╝")

    def iniciar(self):
        opt = -1
        while opt != 5:
            self.mostrarMenuPrincipal()
            opt = main.obtenerOpcion(1,5)
            match opt:
                case 1:
                    self.obtenerDatosAPI()
                case 2:
                    self.cargarFichero()
                case 3:
                    self.guardarFichero()
                case 4:
                    self.mostrarMenuInteractuarDatos()
                    interactuarOpt = main.obtenerOpcion(1,4)
                    match interactuarOpt:
                        case 1:
                            self.visualizarDatos()
                        case 2:
                            self.buscarPorID()
                        case 3:
                            self.mostrarCantidades()
                        case 4:
                            continue
                case 5:
                    continue
        print("Aplicación cerrada correctamente.")