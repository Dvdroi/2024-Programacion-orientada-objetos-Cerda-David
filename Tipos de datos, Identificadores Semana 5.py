# Programa para calcular el área de figuras geométricas
# Este programa permite al usuario seleccionar una figura (círculo, cuadrado o triángulo)
# y calcula su área basándose en los datos proporcionados por el usuario.

import math

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio ** 2

def calcular_area_cuadrado(lado):
    """Calcula el área de un cuadrado dado el largo de su lado."""
    return lado ** 2

def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dada su base y altura."""
    return 0.5 * base * altura

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nSeleccione la figura para calcular su área:")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Triángulo")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción (1-4): ")

        if opcion == '1':
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es: {area:.2f}")
        elif opcion == '2':
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            print(f"El área del cuadrado es: {area:.2f}")
        elif opcion == '3':
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print(f"El área del triángulo es: {area:.2f}")
        elif opcion == '4':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

        continuar = input("¿Desea calcular otra área? (s/n): ").lower()
        if continuar != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()