import os
from datetime import datetime

class Producto:
    def __init__(self, id, nombre, categoria, cantidad, precio, stock_minimo):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = cantidad
        self.precio = precio
        self.stock_minimo = stock_minimo

    def __str__(self):
        return f"{self.id},{self.nombre},{self.categoria},{self.cantidad},{self.precio},{self.stock_minimo}"

class Inventario:
    def __init__(self):
        self.productos = {}
        self.archivo = "inventario_mejorado.txt"
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    id, nombre, categoria, cantidad, precio, stock_minimo = linea.strip().split(',')
                    self.productos[int(id)] = Producto(int(id), nombre, categoria, int(cantidad), float(precio), int(stock_minimo))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(f"{producto}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto
        self.guardar_inventario()

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            self.guardar_inventario()
            return True
        return False

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            return True
        return False

    def obtener_producto(self, id):
        return self.productos.get(id)

    def listar_productos(self):
        return list(self.productos.values())

    def productos_por_categoria(self, categoria):
        return [p for p in self.productos.values() if p.categoria.lower() == categoria.lower()]

    def alertas_stock_bajo(self):
        return [p for p in self.productos.values() if p.cantidad <= p.stock_minimo]

def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Ver producto")
    print("5. Listar todos los productos")
    print("6. Listar productos por categoría")
    print("7. Ver alertas de stock bajo")
    print("8. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            stock_minimo = int(input("Stock mínimo: "))
            producto = Producto(id, nombre, categoria, cantidad, precio, stock_minimo)
            inventario.agregar_producto(producto)
            print("Producto agregado exitosamente.")

        elif opcion == "2":
            id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (presione Enter para no cambiar): ")
            precio = input("Nuevo precio (presione Enter para no cambiar): ")
            if inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None):
                print("Producto actualizado exitosamente.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            id = int(input("ID del producto a eliminar: "))
            if inventario.eliminar_producto(id):
                print("Producto eliminado exitosamente.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            id = int(input("ID del producto a ver: "))
            producto = inventario.obtener_producto(id)
            if producto:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Categoría: {producto.categoria}, "
                      f"Cantidad: {producto.cantidad}, Precio: {producto.precio}, Stock mínimo: {producto.stock_minimo}")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            productos = inventario.listar_productos()
            if productos:
                for producto in productos:
                    print(f"ID: {producto.id}, Nombre: {producto.nombre}, Categoría: {producto.categoria}, "
                          f"Cantidad: {producto.cantidad}, Precio: {producto.precio}, Stock mínimo: {producto.stock_minimo}")
            else:
                print("No hay productos en el inventario.")

        elif opcion == "6":
            categoria = input("Ingrese la categoría a buscar: ")
            productos = inventario.productos_por_categoria(categoria)
            if productos:
                for producto in productos:
                    print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
            else:
                print(f"No se encontraron productos en la categoría '{categoria}'.")

        elif opcion == "7":
            alertas = inventario.alertas_stock_bajo()
            if alertas:
                print("Productos con stock bajo:")
                for producto in alertas:
                    print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Stock mínimo: {producto.stock_minimo}")
            else:
                print("No hay productos con stock bajo.")

        elif opcion == "8":
            print("Gracias por usar el sistema de gestión de inventarios. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()