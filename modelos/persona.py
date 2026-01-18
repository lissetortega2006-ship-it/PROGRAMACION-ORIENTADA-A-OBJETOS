
# CLASE BASE: Persona

# Esta clase representa una entidad general.
# Aquí se aplican los conceptos de:
# - Programación Orientada a Objetos
# - Encapsulación
# - Definición de atributos y métodos

class Persona:
    def __init__(self, nombre, edad):
        # ENCAPSULACIÓN:
        # Los atributos se definen como privados usando doble guion bajo (__)
        # Esto evita que se acceda directamente a ellos desde fuera de la clase
        self.__nombre = nombre
        self.__edad = edad

    # MÉTODOS GETTERS:
    # Permiten acceder a los atributos privados de forma controlada
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # MÉTODO COMÚN:
    # Este método puede ser utilizado por esta clase
    # o sobrescrito por las clases hijas (polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.__nombre} y tengo {self.__edad} años."

