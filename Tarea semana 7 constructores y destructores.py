import time


class Archivo:
    def __init__(self, nombre, modo='r'):
        """
        Constructor de la clase Archivo.
        Inicializa los atributos y abre el archivo.

        :param nombre: Nombre del archivo
        :param modo: Modo de apertura (por defecto 'r' - lectura)
        """
        self.nombre = nombre
        self.modo = modo
        self.archivo = None
        try:
            self.archivo = open(self.nombre, self.modo)
            print(f"Archivo '{self.nombre}' abierto en modo '{self.modo}'")
        except IOError:
            print(f"Error al abrir el archivo '{self.nombre}'")

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Cierra el archivo si está abierto.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' cerrado")


class Temporizador:
    def __init__(self):
        """
        Constructor de la clase Temporizador.
        Inicializa el tiempo de inicio.
        """
        self.tiempo_inicio = time.time()
        print("Temporizador iniciado")

    def __del__(self):
        """
        Destructor de la clase Temporizador.
        Calcula y muestra el tiempo transcurrido.
        """
        tiempo_transcurrido = time.time() - self.tiempo_inicio
        print(f"Temporizador finalizado. Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")


# Demostración de uso
def main():
    # Uso de la clase Archivo
    archivo = Archivo("ejemplo.txt", "w")
    # El archivo se cerrará automáticamente cuando el objeto sea destruido

    # Uso de la clase Temporizador
    temporizador = Temporizador()

    # Simulamos algún proceso
    print("Realizando alguna tarea...")
    time.sleep(2)

    # Los destructores se llamarán automáticamente al final del programa
    print("Fin del programa")


if __name__ == "__main__":
    main()