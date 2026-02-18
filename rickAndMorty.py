import main
import getApiData
import json
import character
import location
import episode


# Clase que lleva la lógica principal de la aplicación y que contiene las variables
# He creado esta clase para practicar más con clases y no dejar las variables como globales en el main.py
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
        print("╠ 3. Filtrar datos.")
        print("╠ 4. Ver cantidad de datos que tenemos.")
        print("╠ 5. Volver atrás.")
        print("╚══════════════════════════════════════════════════════════════════════════╝")

    # Obtenemos los datos haciendo uso de la clase getApiData
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
        # Se pregunta al usuario que tipo de dato es el que contiene el fichero
        print("Selecciona el tipo de dato que quieres cargar (este proceso no sobreescribe los datos actuales):")
        apiData = getApiData.getApiData()
        opt = apiData.mostrarOpciones()

        # Se pregunta por el nombre del fichero y se lee del mismo
        nombreFichero = input("Dime el nombre del fichero que quieres cargar: ")
        try:
            with open(nombreFichero, "r", encoding="utf-8") as f:
                datos = json.load(f)

            # Guardamos los datos creando nuevas instancias de las clases y agregandolas a las listas actuales
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
                            self.episodes.append(newEpisode)
                except KeyError:
                    continue

            print("Fichero cargado correctamente.")
        except FileNotFoundError:
            print("ERROR: Fichero no encontrado.")
        except json.JSONDecodeError:
            print("ERROR: El fichero JSON contiene errores.")

    def guardarFichero(self):
        # Preguntamos al usuario por el tipo de dato que quiere guardar (character, location o episode)
        print("Selecciona el tipo de dato que quieres guardar:")
        apiData = getApiData.getApiData()
        opt = apiData.mostrarOpciones()
        
        nombreFichero = input("Dime el nombre del fichero en el que lo quieres guardar: ")

        # Por defecto datos es una lista vacía y se llena según la opción elegida
        datos = []
        match opt:
            case 1:
                datos = self.characters
            case 2:
                datos = self.locations
            case 3:
                datos = self.episodes

        # Convertimos todos los objetos a diccionario para luego guardarlos
        datosDict = [d.obtenerFormatoDiccionario() for d in datos]

        # No hace falta usar try-except ya que Python por defecto crea el fichero si no existe
        with open(nombreFichero, "w", encoding="utf-8") as f:
            json.dump(datosDict,f,indent=4,ensure_ascii=False)

        print("Datos guardados con éxito.")

    def visualizarDatos(self):
        # Preguntamos al usuario por el tipo de dato que quiere visualizar
        print("Selecciona el tipo de datos que quieres visualizar:")
        apiData = getApiData.getApiData()
        opt = apiData.mostrarOpciones()

        # Según el tipo de datos seleccionado por el usuario se muestra una lista u otra.
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

    def obtenerID(self, texto):
        while(True):
            try:
                num = int(input(texto))
                return num
            except ValueError:
                print("Debe ser un número.")

    def buscarPorID(self):
        # Preguntamos al usuario por el tipo de dato que quiere buscar
        print("Selecciona el tipo de dato por el que quieres buscar:")
        apiData = getApiData.getApiData()
        opt = apiData.mostrarOpciones()

        # Según el tipo de dato se usa una lista u otra para buscar por su ID
        match opt:
            case 1:
                if self.characters:
                    idBuscar = self.obtenerID("Introduce el ID que quieres buscar: ")
                    for character in self.characters:
                        if character.id == idBuscar:
                            character.mostrarDatos()
                            return
                    print("Character no encontrado.")
                else:
                    print("No hay contenido de ese tipo.")
            case 2:
                if self.locations:
                    idBuscar = self.obtenerID("Introduce el ID que quieres buscar: ")
                    for location in self.locations:
                        if location.id == idBuscar:
                            location.mostrarDatos()
                            return
                    print("Location no encontrada.")
                else:
                    print("No hay contenido de ese tipo.")
            case 3:
                if self.episodes:
                    idBuscar = self.obtenerID("Introduce el ID que quieres buscar: ")
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

    def filtrar(self):
        # Preguntamos al usuario por el tipo de dato que quiere filtrar
        print("Selecciona el tipo de datos que quieres filtrar:")
        apiData = getApiData.getApiData()
        opt = apiData.mostrarOpciones()

        # Dependiendo del tipo de dato por el que quiera filtrar le permitimos filtrar por una opción u otra.
        match opt:
            case 1: # Characters
                if self.characters:
                    num = int(input("Introduce la opción por la que quieres filtrar ( 1 -> Status ('Alive','Dead','unkown'), 2 -> species ('Human',etc) ): "))
                    filtro = input(f"Introduce el valor por el que quieres filtrar en el campo {"status" if num == 1 else "species"}: ")
                    
                    # Comprobamos si el campo seleccionario es igual al valor introducido y nos quedamos con el caso de ser cierto
                    filtrados = []
                    for character in self.characters:
                        if num == 1: # si es status
                            if character.status == filtro:
                                filtrados.append(character)
                        else:
                            if character.species == filtro:
                                filtrados.append(character)
                    
                    # Mostramos los que hemos encontrado o mostramos que no hay coincidencias
                    if filtrados:
                        for f in filtrados:
                            f.mostrarDatos()
                        print(f"Se han encontrado un total de {len(filtrados)} characters.")
                    else:
                        print("No hay resultado con ese filtro.")
                else:
                    print("No hay contenido de ese tipo.")
            case 2: # Locations
                if self.locations:
                    num = int(input("Introduce la opción por la que quieres filtrar ( 1 -> Type ('Planet',etc), 2 -> Dimension ('Dimension C-137',etc) ): "))
                    filtro = input(f"Introduce el valor por el que quieres filtrar en el campo {"type" if num == 1 else "dimension"}: ")

                    # Comprobamos si el campo seleccionario es igual al valor introducido y nos quedamos con el caso de ser cierto
                    filtrados = []
                    for location in self.locations:
                        if num == 1: # si es type
                            if location.type == filtro:
                                filtrados.append(location)
                        else:
                            if location.dimension == filtro:
                                filtrados.append(location)

                    # Mostramos los que hemos encontrado o mostramos que no hay coincidencias
                    if filtrados:
                        for f in filtrados:
                            f.mostrarDatos()
                        print(f"Se han encontrado un total de {len(filtrados)} locations.")
                    else:
                        print("No hay resultado con ese filtro.")
                else:
                    print("No hay contenido de ese tipo.")
            case 3: # Episodes
                if self.episodes:
                    # No ofrezco opciones de filtrar porque unicamente permito filtrar por si X ID de character ha estado en ese episodio o no
                    filtro = input(f"Introduce el ID del character por el que quieres filtrar (buscará si ese personaje está en el episodio o no): ")

                    # Comprobamos si el campo seleccionario es igual al valor introducido y nos quedamos con el caso de ser cierto
                    filtrados = []
                    for episode in self.episodes:
                        for character in episode.characters:
                            # el formato de character es este: "https://rickandmortyapi.com/api/character/1"
                            # por lo que voy a hacer un split por "/" y me voy a quedar con el último elemento de la lista
                            contenido = character.split("/")
                            characterID = contenido[len(contenido)-1]

                            if characterID == filtro:
                                filtrados.append(episode)

                    # Mostramos los que hemos encontrado o mostramos que no hay coincidencias
                    if filtrados:
                        for f in filtrados:
                            f.mostrarDatos()
                        print(f"Se han encontrado un total de {len(filtrados)} episodes.")
                    else:
                        print("No hay resultado con ese filtro.")
                else:
                    print("No hay contenido de ese tipo.")
            case _:
                print("Opción no contemplada.")

    def filtrar(self):
        # Preguntamos al usuario por el tipo de dato que quiere filtrar
        print("Selecciona el tipo de datos que quieres filtrar:")
        apiData = getApiData.getApiData()
        opt = apiData.mostrarOpciones()

        # Dependiendo del tipo de dato por el que quiera filtrar le permitimos filtrar por una opción u otra.
        match opt:
            case 1: # Characters
                if self.characters:
                    num = int(input("Introduce la opción por la que quieres filtrar ( 1 -> Status ('Alive','Dead','unkown'), 2 -> species ('Human',etc) ): "))
                    filtro = input(f"Introduce el valor por el que quieres filtrar en el campo {"status" if num == 1 else "species"}: ")
                    
                    # Comprobamos si el campo seleccionario es igual al valor introducido y nos quedamos con el caso de ser cierto
                    filtrados = []
                    for character in self.characters:
                        if num == 1: # si es status
                            if character.status == filtro:
                                filtrados.append(character)
                        else:
                            if character.species == filtro:
                                filtrados.append(character)
                    
                    # Mostramos los que hemos encontrado o mostramos que no hay coincidencias
                    if filtrados:
                        for f in filtrados:
                            f.mostrarDatos()
                        print(f"Se han encontrado un total de {len(filtrados)} characters.")
                    else:
                        print("No hay resultado con ese filtro.")
                else:
                    print("No hay contenido de ese tipo.")
            case 2: # Locations
                if self.locations:
                    num = int(input("Introduce la opción por la que quieres filtrar ( 1 -> Type ('Planet',etc), 2 -> Dimension ('Dimension C-137',etc) ): "))
                    filtro = input(f"Introduce el valor por el que quieres filtrar en el campo {"type" if num == 1 else "dimension"}: ")

                    # Comprobamos si el campo seleccionario es igual al valor introducido y nos quedamos con el caso de ser cierto
                    filtrados = []
                    for location in self.locations:
                        if num == 1: # si es type
                            if location.type == filtro:
                                filtrados.append(location)
                        else:
                            if location.dimension == filtro:
                                filtrados.append(location)

                    # Mostramos los que hemos encontrado o mostramos que no hay coincidencias
                    if filtrados:
                        for f in filtrados:
                            f.mostrarDatos()
                        print(f"Se han encontrado un total de {len(filtrados)} locations.")
                    else:
                        print("No hay resultado con ese filtro.")
                else:
                    print("No hay contenido de ese tipo.")
            case 3: # Episodes
                if self.episodes:
                    # No ofrezco opciones de filtrar porque unicamente permito filtrar por si X ID de character ha estado en ese episodio o no
                    filtro = input(f"Introduce el ID del character por el que quieres filtrar (buscará si ese personaje está en el episodio o no): ")

                    # Comprobamos si el campo seleccionario es igual al valor introducido y nos quedamos con el caso de ser cierto
                    filtrados = []
                    for episode in self.episodes:
                        for character in episode.characters:
                            # el formato de character es este: "https://rickandmortyapi.com/api/character/1"
                            # por lo que voy a hacer un split por "/" y me voy a quedar con el último elemento de la lista
                            contenido = character.split("/")
                            characterID = contenido[len(contenido)-1]

                            if characterID == filtro:
                                filtrados.append(episode)

                    # Mostramos los que hemos encontrado o mostramos que no hay coincidencias
                    if filtrados:
                        for f in filtrados:
                            f.mostrarDatos()
                        print(f"Se han encontrado un total de {len(filtrados)} episodes.")
                    else:
                        print("No hay resultado con ese filtro.")
                else:
                    print("No hay contenido de ese tipo.")
            case _:
                print("Opción no contemplada.")

    # Función principal de la clase que maneja toda la lógica de la aplicació
    def iniciar(self):
        opt = -1
        while opt != 5:
            self.mostrarMenuPrincipal()
            opt = main.obtenerOpcion(1,5)
            match opt:
                case 1: # Obtener datos de la API
                    self.obtenerDatosAPI()
                case 2: # Cargar datos de un fichero JSON
                    self.cargarFichero()
                case 3: # Exportar los datos a un fichero JSON
                    self.guardarFichero()
                case 4: # Interactuar con los datos
                    self.mostrarMenuInteractuarDatos()
                    interactuarOpt = main.obtenerOpcion(1,4)
                    match interactuarOpt:
                        case 1: # Visualizar todos los datos
                            self.visualizarDatos()
                        case 2: # Buscar por ID
                            self.buscarPorID()
                        case 3: # Filtrar datos
                            self.filtrar()
                        case 4: # Ver la cantidad de datos que tenemos por tipo
                            self.mostrarCantidades()
                        case 5: # Volver atrás
                            continue
                case 5: # Salir de la aplicación
                    continue
        print("Aplicación cerrada correctamente.")