"""
Programa: Cálculo del área de un rectángulo
Descripción:
Este programa solicita al usuario las dimensiones de un rectángulo,
calcula su área y muestra si el área es grande o pequeña.
"""

# Solicitar datos al usuario
user_name = input("Ingrese su nombre: ")  # string
width = float(input("Ingrese el ancho del rectángulo: "))  # float
height = float(input("Ingrese el alto del rectángulo: "))  # float

# Cálculo del área
area = width * height  # float

# Se define un valor entero que servirá como límite de comparación
area_limit = 100

# Se evalúa si el área es mayor o igual al límite
# El resultado se almacena en una variable de tipo boolean
is_large = area >= area_limit

# Se muestran los resultados al usuario
print("\nResultados:")
print(f"Hola {user_name}, el área del rectángulo es: {area:.2f}")

# Estructura condicional que muestra un mensaje según el valor booleano
if is_large:
    print("El área es grande.")
else:
    print("El área es pequeña.")
    
