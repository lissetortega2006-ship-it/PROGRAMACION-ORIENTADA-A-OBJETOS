
# Programa: Promedio semanal del clima
# Paradigma: Programación Orientada a Objetos (POO)
# Objetivo: Calcular el promedio semanal de temperaturas


class ClimaSemanal:
    """
    Clase que representa el registro climático de una semana.
    Maneja las temperaturas diarias y calcula el promedio semanal.
    """

    def __init__(self):
        # Atributo privado (encapsulamiento)
        self.__temperaturas = []

        # Lista de días de la semana
        self.dias = [
            "Lunes", "Martes", "Miércoles",
            "Jueves", "Viernes", "Sábado", "Domingo"
        ]

    def ingresar_temperaturas(self):
        """
        Solicita al usuario ingresar la temperatura de cada día.
        Guarda los valores en el atributo privado __temperaturas.
        """
        print("INGRESO DE TEMPERATURAS DIARIAS (POO)")

        for dia in self.dias:
            temp = float(input(f"Ingresa la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Calcula y retorna el promedio de las temperaturas
        almacenadas en el atributo privado.
        """
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_resultado(self):
        """
        Muestra el resultado del promedio semanal.
        Este método puede considerarse polimórfico si fuera extendido.
        """
        promedio = self.calcular_promedio()

        print("\n==============================")
        print(f"Promedio semanal de temperatura: {promedio:.2f} °C")
        print("==============================")


# Función principal del programa
def main():
    """
    1. Crea un objeto de la clase ClimaSemanal.
    2. Solicita el ingreso de temperaturas.
    3. Muestra el resultado final.
    """
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_resultado()


# Llamada al programa principal
main()
