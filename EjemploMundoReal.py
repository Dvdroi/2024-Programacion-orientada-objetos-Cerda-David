class Mascota:
    def __init__(self, nombre, especie, edad, precio):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.precio = precio
        self.adoptado = False

    def __str__(self):
        return f"{self.nombre} - {self.especie}, {self.edad} años"

class Cliente:
    def __init__(self, nombre, id_cliente):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.mascotas_adoptadas = []

    def adoptar(self, mascota):
        if not mascota.adoptado:
            self.mascotas_adoptadas.append(mascota)
            mascota.adoptado = True
            return True
        return False

    def devolver(self, mascota):
        if mascota in self.mascotas_adoptadas:
            self.mascotas_adoptadas.remove(mascota)
            mascota.adoptado = False
            return True
        return False

class TiendaMascotas:
    def __init__(self):
        self.mascotas = []
        self.clientes = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def realizar_adopcion(self, cliente, nombre_mascota):
        for mascota in self.mascotas:
            if mascota.nombre == nombre_mascota:
                if cliente.adoptar(mascota):
                    return True
        return False

    def procesar_devolucion(self, cliente, nombre_mascota):
        for mascota in self.mascotas:
            if mascota.nombre == nombre_mascota:
                return cliente.devolver(mascota)
        return False

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una tienda de mascotas
    mi_tienda = TiendaMascotas()

    # Crear algunas mascotas
    mascota1 = Mascota("Luna", "Gato", 2, 100)
    mascota2 = Mascota("Rocky", "Perro", 3, 150)

    # Agregar mascotas a la tienda
    mi_tienda.agregar_mascota(mascota1)
    mi_tienda.agregar_mascota(mascota2)

    # Crear un cliente
    cliente1 = Cliente("Carlos Pérez", "C001")

    # Registrar cliente en la tienda
    mi_tienda.registrar_cliente(cliente1)

    # Realizar una adopción
    if mi_tienda.realizar_adopcion(cliente1, "Luna"):
        print(f"{cliente1.nombre} ha adoptado a {mascota1}")
    else:
        print("No se pudo realizar la adopción")

    # Intentar adoptar la misma mascota de nuevo
    if mi_tienda.realizar_adopcion(cliente1, "Luna"):
        print(f"{cliente1.nombre} ha adoptado a {mascota1}")
    else:
        print("No se pudo realizar la adopción porque la mascota ya está adoptada")

    # Devolver la mascota
    if mi_tienda.procesar_devolucion(cliente1, "Luna"):
        print(f"{cliente1.nombre} ha devuelto a {mascota1}")
    else:
        print("No se pudo procesar la devolución")