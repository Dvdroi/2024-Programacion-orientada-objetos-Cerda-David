import os

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo {ruta_script} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def ejecutar_script(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        print(f"\n--- Ejecutando {os.path.basename(ruta_script)} ---\n")
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            exec(archivo.read())
    except FileNotFoundError:
        print(f"El archivo {ruta_script} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el archivo: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        '2': 'Unidad 1/1.3. Estructuras de Datos/1.3-1. Ejemplo Estructuras de Datos.py',
        '3': 'Unidad 2/2.1. Programacion Orientada a Objetos/2.1-1. Ejemplo POO.py',
        # Agrega más opciones aquí
    }
    
    while True:
        print("\nMenu Principal - Dashboard")
        for key, valor in opciones.items():
            print(f"{key} - {os.path.basename(valor)}")
        print("0 - Salir")
        
        eleccion = input("Elige un script (v para ver, e para ejecutar) o '0' para salir: ")
        
        if eleccion == '0':
            break
        elif eleccion.lower().startswith(('v', 'e')) and eleccion[1:] in opciones:
            accion, num_script = eleccion[0].lower(), eleccion[1:]
            ruta_script = os.path.join(ruta_base, opciones[num_script])
            
            if accion == 'v':
                mostrar_codigo(ruta_script)
            elif accion == 'e':
                ejecutar_script(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
