def contar_lineas_codigo(ruta_archivo):
    if not ruta_archivo.endswith('.py'):
        return
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas_codigo = sum(1 for linea in archivo if linea.strip() and not linea.strip().startswith('#'))
        
        print(f"El archivo {ruta_archivo} tiene {lineas_codigo} líneas de código.")
    except FileNotFoundError:
        print("Archivo no encontrado. Verifique la ruta e intente otra vez.")

# Solicitar la ruta del archivo 
ruta_archivo = input("Ingrese la ruta del archivo .py: ")
contar_lineas_codigo(ruta_archivo)