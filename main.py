import rickAndMorty

# RESPOSITORIO DE GITHUB: https://github.com/CodeByChriss/RickAndMortyPython

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
    rickMorty = rickAndMorty.rickAndMorty()
    rickMorty.iniciar()

    print("¡Hasta la próxima!")
    # api = getApiData.getApiData()
    # opcionElegida = api.mostrarOpciones()

    # if opcionElegida: # Si no es None
    #     api.obtenerDatos(opcionElegida)

if __name__ == '__main__':
    main()