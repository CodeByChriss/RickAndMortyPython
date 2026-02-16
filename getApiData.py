import requests
import math # lo usaré para redondear a la alza
import character
import location
import episode

class getApiData:

    def __init__(self):
        # Documentación de la API: https://rickandmortyapi.com/documentation
        response = requests.get("https://rickandmortyapi.com/api")
        # Declaramos las variables de la clase vacias para evitar errores
        self.characters = []
        self.episodes = []
        self.locations = []
        self.response = response

    # Mostramos las opciones que nos da la API
    def mostrarOpciones(self):
        if self.response.status_code == 200:
            opciones = self.response.json()
            if not opciones:
                print("Ha ocurrido un error, las opciones están vacias.")
                return
            
            i = 1
            print("Las opciones disponibles son:")
            for clave in opciones:
                print(f"\t{i}. {clave}")
                i += 1
            
            return self.obtenerOpcion(1,i-1)
        else:
            print(f"Ha ocurrido un error al obtener la información de la API. Código de error: {self.response.status_code}")
            return None

    def obtenerOpcion(self,min,max):
        while(True):
            try:
                num = int(input("Selecciona una opción: "))
                if num < min or num > max:
                    print("La opción introducida no existe.")
                else:
                    return num
            except ValueError:
                print("Debe ser un número.")

    # Obtenemos los datos de la opción elegida por el usuario (1 -> characters, 2 -> locations, 3 -> episodes)
    def obtenerDatos(self,opcion):
        opcion = self.obtenerValorOpcion(opcion)
        if opcion: # Si no es None
            clave = opcion[0]
            url = opcion[1]
            page = 1
            opcionResponse = requests.get(f"{url}?page={page}") # Obtenemos la primera página
            if opcionResponse.status_code == 200:
                # Obtenemos la cantidad de characters, location o episodes que hay
                # (lo ofrece el propio diccionario que devuelve la api)
                datos = opcionResponse.json()
                info = datos['info']
                cnt = info['count']
                cntPages = math.ceil(cnt/20) # Cada página tiene 20 entradas por lo que la cantidad de páginas es cnt (total de entradas que hay en todas las páginas) / 20 (entradas por página)
                
                # Preguntamos la cantidad de páginas que quiere guardar
                print(f"Hay un total de {cntPages}. ¿Cuántas quieres obtener?: ")
                obtener = self.obtenerOpcion(1,cntPages)

                # Pasamos los datos actuales a clases y a la lista correspondiente
                self.guardarDatos(clave,datos['results'])

                # Repetimos el proceso para cada página que el usuario haya introducido
                if obtener > 1: # Ya que la primera página se obtiene si o si
                    paginaSiguiente = info['next']
                    for i in range(2, obtener+1):
                        if paginaSiguiente: # si hay página siguiente
                            paginaResponse = requests.get(paginaSiguiente)
                            if paginaResponse.status_code == 200:
                                paginaDatos = paginaResponse.json()
                                paginaInfo = paginaDatos['info']
                                paginaSiguiente = paginaInfo['next'] # guardamos la próxima siguiente

                                # igual que antes, guardamos los datos
                                self.guardarDatos(clave, paginaDatos['results'])
                            else:
                                print(f"Error al obtener la información de la página {i}. Código de error: {opcionResponse.status_code}")
                        else:
                            print("No hay página siguiente")
                print("Datos obtenimos correctamente.")
                print(f"Longitudes actuales: characters: {len(self.characters)}, locations: {len(self.locations)}, episodes: {len(self.episodes)}")
            else:
                print(f"Error al obtener la información de la opción {clave}. Código de error: {opcionResponse.status_code}")

    # Como es un diccionario no podemos acceder diciendo que queremos la posición 2 por lo que devolvemos la que este en esa posición
    def obtenerValorOpcion(self,opcionIndex):
        opciones = self.response.json()
        for index, opcion in enumerate(opciones):
            if index == opcionIndex-1: # Hay que restar 1 porque al usuairo se le muestra como 1,2... Pero nosotros empezamos por 0.
                return (opcion,opciones[opcion]) # Tupla clave valor
        return None # si no se encuentra
    
    # Convertimos los datos a instancias de clases (objetos) y los guardamos en su lista correspondiente.
    def guardarDatos(self, nombreLista, listaDatos):
        match nombreLista:
            case "characters":
                for entrada in listaDatos:
                    self.characters.append(character.characters("test"))
            case "locations":
                for entrada in listaDatos:
                    self.locations.append(location.locations("test"))
            case "episodes":
                for entrada in listaDatos:
                    self.episodes.append(episode.episodes("test"))
            case _: print(f"Error, la lista {nombreLista} no existe.")