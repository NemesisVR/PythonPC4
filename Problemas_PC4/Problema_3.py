import requests
import zipfile
import os

def descargar_y_comprimir(url, nombre_imagen, nombre_zip, carpeta_destino):
    # Descargar la imagen 
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        print(f"Error al descargar la imagen, código de estado: {respuesta.status_code}")
        return

    # Guardar la imagen descargada
    with open(nombre_imagen, 'wb') as archivo:
        archivo.write(respuesta.content)

    # Comprimir la imagen 
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        zipf.write(nombre_imagen)

    # Descomprimir la imagen 
    with zipfile.ZipFile(nombre_zip, 'r') as zipf:
        zipf.extractall(carpeta_destino)

def main():
    url = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    nombre_imagen = 'Perrito_lol.jpg'
    nombre_zip = 'Peluchin.zip'
    carpeta_destino = r'C:\Users\Franco\OneDrive\Escritorio\FRANCO 2024'

    descargar_y_comprimir(url, nombre_imagen, nombre_zip, carpeta_destino)

if __name__ == "__main__":
    main()
