import rickAndMorty

# RESPOSITORIO DE GITHUB: https://github.com/CodeByChriss/RickAndMortyPython

# lo dejo en el main porque lo usa más de una clase
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

if __name__ == '__main__':
    main()