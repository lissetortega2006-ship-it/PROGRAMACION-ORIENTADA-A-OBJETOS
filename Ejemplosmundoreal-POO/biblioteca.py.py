# ---------------------------------------------------------
# Programa: Sistema de Biblioteca
# Descripción del mundo real:
# Este programa modela una biblioteca real utilizando
# Programación Orientada a Objetos (POO). La biblioteca
# contiene libros, y cada libro puede ser prestado.
# Se utilizan clases, atributos y métodos para representar
# el comportamiento real de una biblioteca.


# Clase Libro
# Representa un libro del mundo real
class Libro:
    def __init__(self, titulo, autor):
        # Atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # Indica si el libro está disponible o no

    # Método para mostrar la información del libro
    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Estado:", estado)

    # Método para prestar el libro
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("El libro ha sido prestado:", self.titulo)
        else:
            print("El libro ya está prestado")


# Clase Biblioteca
# Representa una biblioteca que contiene varios libros
class Biblioteca:
    def __init__(self, nombre):
        # Atributos de la biblioteca
        self.nombre = nombre
        self.libros = []  # Lista que almacena los libros

    # Método para agregar un libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Método para mostrar todos los libros de la biblioteca
    def mostrar_libros(self):
        print("Biblioteca:", self.nombre)
        for libro in self.libros:
            libro.mostrar_info()  # Interacción entre objetos
            print("-------------------------")



# Creación de objetos (uso del programa)


# Se crean objetos de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("El principito", "Antoine de Saint-Exupéry")

# Se crea un objeto de la clase Biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# Interacción entre objetos:
# La biblioteca recibe libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Se muestran los libros disponibles
biblioteca.mostrar_libros()

# Se presta un libro
libro1.prestar()
