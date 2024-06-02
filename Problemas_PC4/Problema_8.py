import requests
import sqlite3
from datetime import datetime

def obtener_precios_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()

    precio_usd = data["bpi"]["USD"]["rate_float"]
    precio_gbp = data["bpi"]["GBP"]["rate_float"]
    precio_eur = data["bpi"]["EUR"]["rate_float"]

    return precio_usd, precio_gbp, precio_eur

def obtener_tipo_cambio_sunat():
    tipo_cambio_usd_pen = 3.8
    return tipo_cambio_usd_pen

def crear_base_datos():
    conn = sqlite3.connect("bitcoin.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bitcoin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            precio_usd REAL,
            precio_gbp REAL,
            precio_eur REAL,
            precio_pen REAL
        )
    """)
    conn.commit()
    conn.close()

def insertar_datos(fecha, precio_usd, precio_gbp, precio_eur, precio_pen):
    conn = sqlite3.connect("bitcoin.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
        VALUES (?, ?, ?, ?, ?)
    """, (fecha, precio_usd, precio_gbp, precio_eur, precio_pen))
    conn.commit()
    conn.close()

def consultar_precio(bitcoins, moneda):
    conn = sqlite3.connect("bitcoin.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT precio_{moneda.lower()} FROM bitcoin ORDER BY id DESC LIMIT 1")
    precio = cursor.fetchone()[0]
    conn.close()
    return precio * bitcoins

def main():
    # Obtener precios del Bitcoin en USD, GBP y EUR
    precio_usd, precio_gbp, precio_eur = obtener_precios_bitcoin()
    
    # Obtener tipo de cambio 
    tipo_cambio_usd_pen = obtener_tipo_cambio_sunat()
    precio_pen = precio_usd * tipo_cambio_usd_pen

    # Crear la base de datos y la tabla `bitcoin`
    crear_base_datos()

    # Insertar los datos 
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insertar_datos(fecha_actual, precio_usd, precio_gbp, precio_eur, precio_pen)

    # Consultar la base de datos 
    precio_10_bitcoins_pen = consultar_precio(10, 'PEN')
    precio_10_bitcoins_eur = consultar_precio(10, 'EUR')

    print(f"El precio de 10 bitcoins en PEN es: {precio_10_bitcoins_pen:.2f}")
    print(f"El precio de 10 bitcoins en EUR es: {precio_10_bitcoins_eur:.2f}")

if __name__ == "__main__":
    main()