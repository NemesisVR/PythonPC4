def guardar_tabla(numero):
    with open(f'tabla-{numero}.txt', 'w') as archivo:
        for i in range(1, 11):
            archivo.write(f'{numero} x {i} = {numero * i}\n')

def leer_tabla(numero):
    try:
        with open(f'tabla-{numero}.txt', 'r') as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print(f'El archivo tabla-{numero}.txt no existe.')

def leer_linea_tabla(numero, linea):
    try:
        with open(f'tabla-{numero}.txt', 'r') as archivo:
            lineas = archivo.readlines()
            if 1 <= linea <= len(lineas):
                print(lineas[linea - 1].strip())
            else:
                print(f'La línea {linea} no existe en la tabla-{numero}.txt.')
    except FileNotFoundError:
        print(f'El archivo tabla-{numero}.txt no existe.')

def menu():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Leer una línea de la tabla de multiplicar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla(numero)
                print(f'Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt.')
            else:
                print("Número fuera de rango. Por favor, ingrese un número entre 1 y 10.")
        
        elif opcion == '2':
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                leer_tabla(numero)
            else:
                print("Número fuera de rango. Por favor, ingrese un número entre 1 y 10.")
        
        elif opcion == '3':
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                linea = int(input(f"Ingrese la línea de la tabla del {numero} que desea leer (1-10): "))
                if 1 <= linea <= 10:
                    leer_linea_tabla(numero, linea)
                else:
                    print("Número de línea fuera de rango. Por favor, ingrese un número entre 1 y 10.")
            else:
                print("Número fuera de rango. Por favor, ingrese un número entre 1 y 10.")
        
        elif opcion == '4':
            break
        
        else:
            print("La opción no es válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    menu()