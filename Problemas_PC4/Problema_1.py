import requests

def obtener_precio_bitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response.raise_for_status()  
    data = response.json()
    return data['bpi']['USD']['rate_float']

def main():
    n = float(input("Ingrese la cantidad de bitcoins que posee: "))
    precio_bitcoin = obtener_precio_bitcoin()
    costo_total = n * precio_bitcoin
    print(f"El costo actual de {n} bitcoins es: ${costo_total:,.4f}")

if __name__ == "__main__":
    main()