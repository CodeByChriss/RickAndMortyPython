import getApiData

# RESPOSITORIO DE GITHUB: https://github.com/CodeByChriss/RickAndMortyPython

# Variables Globales
characters = []
episodes = []
locations = []

def mostrarMenuPrincipal():
    print("╔═════════════════════════ Menú principal ═════════════════════════╗")
    print("╠ 1. Obtener datos de la API.")
    print("╠ 2. Cargar datos de un fichero JSON.")
    print("╠ 3. Exportar datos a un fichero JSON.")
    print("╠ 4. Interactuar con los datos.")
    print("╚══════════════════════════════════════════════════════════════════╝")

def mostrarMenuInteractuarDatos():
    print("╔═══════════════════ Opciones Interactuar con los datos ═══════════════════╗")
    print("╠ 1. Visualizar los datos.")
    print("╠ 2. Cargar datos de un fichero JSON.")
    print("╠ 3. Exportar datos a un fichero JSON.")
    print("╠ 4. Interactuar con los datos.")
    print("╚══════════════════════════════════════════════════════════════════════════╝")

def obtenerOpcion(min,max):
    while(True):
        try:
            num = int(input("Selecciona una opción: "))
            if num < min or num > max:
                print("La opción introducida no existe.")
            else:
                return num
        except ValueError:
            print("Debe ser un número.")

def main():
    api = getApiData.getApiData()
    opcionElegida = api.mostrarOpciones()

    if opcionElegida: # Si no es None
        api.obtenerDatos(opcionElegida)

if __name__ == '__main__':
    main()