
# Programa: Promedio semanal del clima
# Paradigma: Programación Tradicional (Funciones)
# Objetivo: Calcular el promedio semanal de temperaturas

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    """
    Solicita al usuario ingresar la temperatura de cada día de la semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []
    print("INGRESO DE TEMPERATURAS DIARIAS")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Recorremos los días de la semana y pedimos la temperatura
    for dia in dias:
        temp = float(input(f"Ingresa la temperatura del día {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Retorna el valor promedio.
    """
    return sum(temperaturas) / len(temperaturas)


# Función principal del programa
def main():
    """
    Controla el flujo del programa:
    1. Solicita las temperaturas
    2. Calcula el promedio
    3. Muestra el resultado final
    """
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)

    print("\n==============================")
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")
    print("==============================")


# Llamada al programa principal
main()
