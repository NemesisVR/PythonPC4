from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()

    # Enlistado de fuentes admitidas 
    fuentes = figlet.getFonts()
    print("Fuentes admitidas por FIGlet:")
    for fuente in fuentes:
        print(fuente)

    # Solicitar una de las fuentes disponibles
    fuente_seleccionada = input("Ingrese el nombre de la fuente que desea utilizar (o presione Enter para seleccionar una al azar): ")
    if not fuente_seleccionada:
        fuente_seleccionada = random.choice(fuentes)  

    # Solicitar texto a imprimir
    texto_imprimir = input("Ingrese el texto que desea imprimir: ")

    # Establecer la fuente seleccionada
    figlet.setFont(font=fuente_seleccionada)

    # Imprimir el texto con la fuente elegida
    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()
