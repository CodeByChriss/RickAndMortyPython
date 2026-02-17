import main
import getApiData
import json

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
        nombreFichero = input("Dime el nombre del fichero que quieres cargar: ")
        try:
            with open(nombreFichero, "r", encoding="utf-8") as f:
                datos = json.load(nombreFichero)
        except FileNotFoundError:
            print("ERROR: Fichero no encontrado.")
        except json.JSONDecodeError:
            print("ERROR: El fichero JSON contiene errores.")

    def guardarFichero(self):
        nombreFichero = input("Dime el nombre del fichero en el que lo quieres guardar: ")
        datos = []
        # No hace falta usar try-except ya que Python por defecto crea el fichero si no existe
        with open(nombreFichero, "w", encoding="utf-8") as f:
            json.dump(datos,nombreFichero,indent=4,ensure_ascii=False)

    def visualizarDatos(self):
        pass

    def buscarPorID(self):
        pass

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