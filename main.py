#Descripción del Programa:
#El programa fue desarrollado en Python utilizando Programación Orientada a Objetos.
#Se implementó una clase base llamada Persona y una clase derivada llamada Estudiante,
#aplicando el concepto de herencia. Se utilizó encapsulación mediante el uso de atributos
#privados y métodos getters. Además, se aplicó polimorfismo sobrescribiendo el método
#presentarse(), permitiendo comportamientos distintos según el tipo de objeto.
#El proyecto se organizó en carpetas para separar responsabilidades y el funcionamiento
#se demuestra desde el archivo main.py.

# Archivo principal del programa
# Desde aquí se ejecuta la aplicación

# Importamos las clases desde la carpeta modelos
from modelos.persona import Persona
from modelos.estudiante import Estudiante

# CREACIÓN DE INSTANCIAS (OBJETOS):
# Se crean objetos reales a partir de las clases
persona1 = Persona("Carlos", 40)
estudiante1 = Estudiante("Lili", 20, "Ingeniería en Tecnología")

# DEMOSTRACIÓN DEL FUNCIONAMIENTO:
# Se llama al mismo método presentarse()
# pero cada objeto responde de forma distinta
# demostrando el POLIMORFISMO
print(persona1.presentarse())
print(estudiante1.presentarse())
