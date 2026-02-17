import requests
import main
import character
import location
import episode

class getApiData:

    def __init__(self):
        # Documentación de la API: https://rickandmortyapi.com/documentation
        response = requests.get("https://rickandmortyapi.com/api")
        self.response = response

    # Mostramos las opciones que nos da la API
    def mostrarOpciones(self):
        if self.response.status_code == 200:
            opciones = self.response.json()
            if not opciones:
                print("Ha ocurrido un error, las opciones están vacias.")
                return
            
            i = 1
            print("╔═══════════════ Opciones disponibles ═══════════════╗")
            for clave in opciones:
                print(f"╠ {i}. {clave}.")
                i += 1
            print("╚════════════════════════════════════════════════════╝")
            
            return main.obtenerOpcion(1,i-1)
        else:
            print(f"Ha ocurrido un error al obtener la información de la API. Código de error: {self.response.status_code}")
            return None

    # Obtenemos los datos de la opción elegida por el usuario (1 -> characters, 2 -> locations, 3 -> episodes)
    def obtenerDatos(self,opcion):
        opcion = self.obtenerValorOpcion(opcion)
        if opcion: # Si no es None
            try:
                clave = opcion[0]
                url = opcion[1]
                page = 1
                opcionResponse = requests.get(f"{url}?page={page}") # Obtenemos la primera página
                if opcionResponse.status_code == 200:
                    # Obtenemos la cantidad de characters, location o episodes que hay
                    # (lo ofrece el propio diccionario que devuelve la api)
                    datos = opcionResponse.json()
                    info = datos['info']
                    cntPages = info['pages']
                    listaDatos = [] # lista donde se van a almacenar todos los objetos
                    
                    # Preguntamos la cantidad de páginas que quiere guardar
                    print(f"Hay un total de {cntPages} páginas y cada página contiene 20 registros de {clave}. ¿Cuántas quieres obtener?")
                    obtener = main.obtenerOpcion(1,cntPages)

                    # Pasamos los datos actuales a clases y a la lista correspondiente
                    listaDatos = self.guardarDatos(clave,datos['results'],listaDatos)
                    print(f"Página {page}/{obtener} cargada correctamente.")

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
                                    listaDatos = self.guardarDatos(clave, paginaDatos['results'],listaDatos)

                                    print(f"Página {i}/{obtener} cargada correctamente.")
                                else:
                                    print(f"Error al obtener la información de la página {i}. Código de error: {opcionResponse.status_code}")
                            else:
                                print("No hay página siguiente")
                    print("Datos obtenidos correctamente.")
                    return listaDatos
                else:
                    print(f"Error al obtener la información de la opción {clave}. Código de error: {opcionResponse.status_code}")
                    return []
            except requests.exceptions.RequestException as e:
                print("Error en la conexión:", e)
                return []
        else:
            return []

    # Como es un diccionario no podemos acceder diciendo que queremos la posición 2 por lo que devolvemos la que este en esa posición
    def obtenerValorOpcion(self,opcionIndex):
        opciones = self.response.json()
        for index, opcion in enumerate(opciones):
            if index == opcionIndex-1: # Hay que restar 1 porque al usuairo se le muestra como 1,2... Pero nosotros empezamos por 0.
                return (opcion,opciones[opcion]) # Tupla clave valor
        return None # si no se encuentra
    
    # Convertimos los datos a instancias de clases (objetos) y los guardamos en una lista que devolvemos
    def guardarDatos(self, nombreLista, datos, listaDatos):
        match nombreLista:
            case "characters":
                for entrada in datos:
                    newCharacter = character.character(
                        entrada['id'], entrada['name'], entrada['status'], entrada['species'], 
                        entrada['type'], entrada['gender'], entrada['origin'], entrada['location'], 
                        entrada['image'], entrada['episode'], entrada['url'], entrada['created']
                    )
                    listaDatos.append(newCharacter)
            case "locations":
                for entrada in datos:
                    newLocation = location.location(
                        entrada['id'], 
                        entrada['name'], 
                        entrada['type'], 
                        entrada['dimension'], 
                        entrada['residents'], 
                        entrada['url'], 
                        entrada['created']
                    )
                    listaDatos.append(newLocation)
            case "episodes":
                for entrada in datos:
                    newEpisode = episode.episode(
                        entrada['id'], 
                        entrada['name'], 
                        entrada['air_date'], 
                        entrada['episode'], 
                        entrada['characters'], 
                        entrada['url'], 
                        entrada['created']
                    )
                    listaDatos.append(newEpisode)
            case _: print(f"Error, la lista {nombreLista} no existe.")
        return listaDatos