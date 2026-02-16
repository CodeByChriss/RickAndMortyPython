import getApiData

def main():
    api = getApiData.getApiData()
    opcionElegida = api.mostrarOpciones()

    if opcionElegida: # Si no es None
        api.obtenerDatos(opcionElegida)

if __name__ == '__main__':
    main()