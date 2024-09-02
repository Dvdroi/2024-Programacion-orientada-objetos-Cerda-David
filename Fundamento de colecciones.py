import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_cantidad(self, id, cantidad):
        if id in self.productos:
            self.productos[id].establecer_cantidad(cantidad)

    def actualizar_precio(self, id, precio):
        if id in self.productos:
            self.productos[id].establecer_precio(precio)

    def buscar_producto_por_nombre(self, nombre):
        return [producto for producto in self.productos.values() if producto.obtener_nombre() == nombre]

    def mostrar_todos_los_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: producto.__dict__ for id, producto in self.productos.items()}, f)

    def cargar_desde_archivo(self, archivo):
        with open(archivo, 'r') as f:
            productos = json.load(f)
            self.productos = {id: Producto(**datos) for id, datos in productos.items()}

def menu():
    inventario = Inventario()
    while True:
        print("\nMenú de Gestión de Inventario")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad de producto")
        print("4. Actualizar precio de producto")
        print("5. Buscar producto por nombre")
        print("6. Mostrar todos los productos")
        print("7. Guardar inventario en archivo")
        print("8. Cargar inventario desde archivo")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = input("ID del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(id, cantidad)
        elif opcion == '4':
            id = input("ID del producto: ")
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_precio(id, precio)
        elif opcion == '5':
            nombre = input("Nombre del producto: ")
            productos = inventario.buscar_producto_por_nombre(nombre)
            for producto in productos:
                print(producto)
        elif opcion == '6':
            inventario.mostrar_todos_los_productos()
        elif opcion == '7':
            archivo = input("Nombre del archivo para guardar: ")
            inventario.guardar_en_archivo(archivo)
        elif opcion == '8':
            archivo = input("Nombre del archivo para cargar: ")
            inventario.cargar_desde_archivo(archivo)
        elif opcion == '9':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()
