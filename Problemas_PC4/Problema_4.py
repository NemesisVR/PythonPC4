import requests

def obtener_precio_bitcoin():
    try:
        respuesta = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        respuesta.raise_for_status()  # Si hay un error, emitir una excepción
        datos = respuesta.json()

        precio_usd = datos['bpi']['USD']['rate']
        return precio_usd

    except requests.RequestException as e:
        print(f"Error al obtener los datos: {e}")
        return None

def guardar_precio_en_archivo(precio):
    nombre_archivo = 'precio_bitcoin.txt'
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"Precio actual de Bitcoin en USD: ${precio}")

    print(f"Datos guardados en {nombre_archivo}")

def main():
    precio = obtener_precio_bitcoin()
    if precio:
        guardar_precio_en_archivo(precio)

if __name__ == "__main__":
    main()
