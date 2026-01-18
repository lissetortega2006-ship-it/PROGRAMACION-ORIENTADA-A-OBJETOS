# Importamos la clase Persona desde la carpeta modelos
from modelos.persona import Persona

# CLASE DERIVADA: Estudiante

# Esta clase aplica:
# - HERENCIA (hereda de Persona)
# - POLIMORFISMO (sobrescribe un método)

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # HERENCIA:
        # super() llama al constructor de la clase base Persona
        # para reutilizar sus atributos
        super().__init__(nombre, edad)

        # Atributo propio de la clase Estudiante
        self.carrera = carrera

    # POLIMORFISMO:
    # Se sobrescribe el método presentarse()
    # Aunque el nombre del método es el mismo,
    # el comportamiento es diferente al de la clase Persona
    def presentarse(self):
        return (
            f"Hola, soy {self.get_nombre()}, "
            f"estudio {self.carrera} y tengo {self.get_edad()} años."
        )
