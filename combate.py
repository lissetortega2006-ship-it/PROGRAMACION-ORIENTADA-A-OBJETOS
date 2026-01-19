
# PROYECTO: Simulación de Combate con POO
# Explicación:
#   En este programa estoy aplicando Programación Orientada a Objetos
#   para simular un combate entre dos personajes: un Guerrero y un Mago.
#   Cada personaje tiene atributos, ataques y una forma distinta de hacer daño.



# CLASE PRINCIPAL: Personaje
# Esta es la clase base de donde salen los demás personajes.
# Aquí defino los atributos que cualquier personaje debe tener.


class Personaje:

    # Constructor donde le doy valores iniciales al personaje
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # Método para mostrar todos los atributos del personaje
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    # Método para subir de nivel (aumenta los atributos)
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    # Devuelve True si el personaje todavía no ha muerto
    def esta_vivo(self):
        return self.vida > 0

    # Cambia la vida a 0 y muestra que el personaje murió
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # Calcula el daño base usando la fuerza del personaje
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    # Método que ejecuta un ataque y muestra qué pasó
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)

        # Verifica si el enemigo sigue vivo
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()




# CLASE GUERRERO
# Hereda todo de Personaje, pero aquí le agrego el arma (espada)
# y cambio la forma en la que calcula el daño.

class Guerrero(Personaje):

    # Constructor del Guerrero con el atributo extra "espada"
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada   # esta es la potencia del arma

    # Método opcional para cambiar de espada durante el juego
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio=8, (2) Matadragones=10: "))

        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    # Muestra atributos del Guerrero incluyendo su arma
    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    # El Guerrero hace daño multiplicando fuerza por su espada
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa



# CLASE MAGO
# También hereda de Personaje, pero usa su libro para aumentar el daño.


class Mago(Personaje):

    # El constructor del mago incluye el atributo "libro"
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro  # poder del libro, sirve como multiplicador

    # Muestra los atributos del mago incluyendo el libro
    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

    # El mago hace daño basado en su inteligencia
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa




# FUNCIÓN DE COMBATE
# Aquí es donde los personajes se atacan por turnos.
# El combate sigue hasta que uno de los dos muera.

def combate(jugador_1, jugador_2):
    turno = 1

    # Mientras ambos estén vivos el combate continúa
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\n========================= Turno", turno, "=========================")

        # Turno del jugador 1
        print(">>> Acción de", jugador_1.nombre)
        jugador_1.atacar(jugador_2)

        # Turno del jugador 2
        print(">>> Acción de", jugador_2.nombre)
        jugador_2.atacar(jugador_1)

        turno += 1

    # Resultado final cuando alguien muere
    print("\n=========================== Fin ===========================")
    if jugador_1.esta_vivo():
        print("Ha ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("Ha ganado", jugador_2.nombre)
    else:
        print("Empate")




# CREACIÓN DE LOS PERSONAJES Y EJECUCIÓN DEL COMBATE
# Aquí instancio (creo) los dos personajes con sus atributos iniciales.

personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

# Muestro los atributos de cada personaje antes del combate
personaje_1.atributos()
personaje_2.atributos()

# Llamo a la función que inicia el combate
combate(personaje_1, personaje_2)
