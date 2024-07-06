# Clase base
class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.__id_empleado = id_empleado  # Atributo encapsulado
        self.salario_base = 1000

    def trabajar(self):
        print(f"{self.nombre} está trabajando.")

    def get_id_empleado(self):
        return self.__id_empleado

    def calcular_salario(self):
        return self.salario_base

# Clase derivada
class Desarrollador(Empleado):
    def __init__(self, nombre, id_empleado, lenguaje):
        super().__init__(nombre, id_empleado)
        self.lenguaje = lenguaje

    # Método sobrescrito (polimorfismo)
    def trabajar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}.")

    def calcular_salario(self):
        return self.salario_base * 1.5

# Clase derivada con polimorfismo de argumentos múltiples
class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, departamento="IT"):
        super().__init__(nombre, id_empleado)
        self.departamento = departamento

    def asignar_tarea(self, tarea, *empleados):
        print(f"{self.nombre} asigna la tarea '{tarea}' a:")
        for empleado in empleados:
            print(f"- {empleado.nombre}")

    def calcular_salario(self):
        return self.salario_base * 2

# Programa principal
if __name__ == "__main__":
    # Creando instancias
    dev1 = Desarrollador("Ana", "DEV001", "Python")
    dev2 = Desarrollador("Carlos", "DEV002", "Java")
    gerente = Gerente("Laura", "GER001", "Desarrollo")

    # Usando métodos de las clases
    dev1.trabajar()
    print(f"Salario de {dev1.nombre}: ${dev1.calcular_salario()}")

    dev2.trabajar()
    print(f"Salario de {dev2.nombre}: ${dev2.calcular_salario()}")

    gerente.trabajar()
    gerente.asignar_tarea("Desarrollar nueva feature", dev1, dev2)
    print(f"Salario de {gerente.nombre}: ${gerente.calcular_salario()}")

    # Demostrando encapsulación
    print(f"ID de {dev1.nombre}: {dev1.get_id_empleado()}")
    # Esto generaría un error: print(dev1.__id_empleado)