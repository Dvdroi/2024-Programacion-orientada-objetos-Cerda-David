def ingresar_temperaturas_diarias():
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Programa principal
def main():
    temperaturas_semana = ingresar_temperaturas_diarias()
    promedio_semanal = calcular_promedio_semanal(temperaturas_semana)
    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}")

if __name__ == "__main__":
    main()

class RegistroClima:
    def __init__(self):
        self.temperaturas_diarias = []

    def ingresar_temperatura_diaria(self, temperatura):
        self.temperaturas_diarias.append(temperatura)

    def ingresar_temperaturas_diarias(self):
        for i in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.ingresar_temperatura_diaria(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas_diarias) != 7:
            raise ValueError("Debe ingresar exactamente 7 temperaturas para calcular el promedio semanal.")
        promedio = sum(self.temperaturas_diarias) / len(self.temperaturas_diarias)
        return promedio

Programacion orientada a objetos
class RegistroClima:
    def __init__(self):
        self.temperaturas_diarias = []

    def ingresar_temperatura_diaria(self, temperatura):
        self.temperaturas_diarias.append(temperatura)

    def ingresar_temperaturas_diarias(self):
        for i in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.ingresar_temperatura_diaria(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas_diarias) != 7:
            raise ValueError("Debe ingresar exactamente 7 temperaturas para calcular el promedio semanal.")
        promedio = sum(self.temperaturas_diarias) / len(self.temperaturas_diarias)
        return promedio

# Programa principal
def main():
    registro_clima = RegistroClima()
    registro_clima.ingresar_temperaturas_diarias()
    promedio_semanal = registro_clima.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}")

if __name__ == "__main__":
    main()
