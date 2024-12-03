from manim import *

# Clase para la cabeza del pollo
class Cabeza:
    def __init__(self, escala=1, posicion=ORIGIN):
        self.cabeza = None
        self.ojo_derecho = None
        self.pico = None
        self.escala = escala  # Nuevo parámetro para el tamaño
        self.posicion = posicion  # Nueva posición inicial

    def crear(self):
        # Creación de la cabeza del pollo (círculo amarillo)
        self.cabeza = Circle(radius=1 * self.escala, color=YELLOW, fill_opacity=1)
        self.cabeza.set_stroke(color=BLACK, width=2)  # Añadir un borde negro

        # Creación del ojo derecho (punto negro)
        self.ojo_derecho = Dot(point=self.cabeza.get_center() + RIGHT * 0.2 * self.escala + UP * 0.1 * self.escala, color=BLACK, radius=0.1 * self.escala)

        self.pico = Triangle(color=ORANGE, fill_opacity=1).scale(0.75 * self.escala)

        
        # Posicionar la cabeza y el ojo en la posición deseada
        self.cabeza.move_to(self.posicion)
        # Posicionar el triángulo en el centro de la cabeza
        self.pico.move_to(self.cabeza.get_center() + UP * 0.1+ RIGHT*0.5 * self.escala)  # Ajustado para mayor precisión

        self.ojo_derecho.move_to(self.cabeza.get_center() + RIGHT * 0.2 * self.escala + UP * 0.1 * self.escala)


    def dibujar(self, escena):
        # Dibujar la cabeza, el ojo y el pico en la escena
        escena.add(self.pico,self.cabeza, self.ojo_derecho)
   
    def animar_cabeza(self):
        # Dibujar la cabeza, el ojo y el pico en la escena
        return self.cabeza.animate.shift(RIGHT * 2), self.ojo_derecho.animate.shift(RIGHT * 2),self.pico.animate.shift(RIGHT * 2)


# Clase para el cuerpo del pollo
class Cuerpo:
    def __init__(self, cabeza, escala=1, posicion=ORIGIN):
        self.cuerpo = None
        self.escala = escala  # Nuevo parámetro para el tamaño
        self.posicion = posicion  # Nueva posición inicial

    def crear(self, cabeza):
        # Crear el cuerpo del pollo (media elipse)
        punto_izquierdo = LEFT * 6.5 * self.escala + DOWN * 0.25 * self.escala
        punto_derecho = RIGHT * -1.55 * self.escala + DOWN * 0.25 * self.escala
        altura = 0.5 * self.escala

        # Crear arco entre los puntos para el cuerpo
        self.cuerpo = ArcBetweenPoints(punto_izquierdo + UP * altura, punto_derecho + UP * altura, angle=PI, color=YELLOW, fill_opacity=1)
        self.cuerpo.set_stroke(color=BLACK, width=2)  # Añadir borde negro

        # Posicionar y rotar el cuerpo para alinear con la cabeza
        self.cuerpo.move_to(self.posicion + DOWN * 0.25 * self.escala + LEFT * 2.25 * self.escala)
        self.cuerpo.rotate(-PI / 12)  # Rotar si es necesario

    def dibujar(self, escena):
        # Dibujar el cuerpo en la escena
        escena.add(self.cuerpo)
    
    def animar_cuerpo(self):
        # Dibujar la cabeza, el ojo y el pico en la escena
        return self.cuerpo.animate.shift(RIGHT * 2) 

# Clase para las alas del pollo
class Alas:
    def __init__(self, cabeza, escala=1, posicion=ORIGIN):
        self.alita_1 = None
        self.alita_2 = None
        self.escala = escala  # Nuevo parámetro para el tamaño
        self.posicion = posicion  # Nueva posición inicial

    def crear(self, cabeza):
        # Crear las alitas
        punto_izquierdo = LEFT * 6.5 * self.escala + DOWN * 0.25 * self.escala
        punto_derecho = RIGHT * -1.55 * self.escala + DOWN * 0.25 * self.escala

        self.alita_1 = ArcBetweenPoints(punto_izquierdo + UP * 1.55 * self.escala, punto_derecho + UP * 1.55 * self.escala, angle=PI, color=YELLOW, fill_opacity=0.8)
        self.alita_1.set_stroke(color=BLACK, width=2)
        self.alita_1.move_to(self.posicion + DOWN * 0.25 * self.escala + LEFT * 2.0 * self.escala + RIGHT * -0.5 * self.escala)
        self.alita_1.rotate(-PI / 6)

        self.alita_2 = ArcBetweenPoints(punto_izquierdo + UP * 1.75 * self.escala, punto_derecho + UP * 1.55 * self.escala, angle=PI, color=YELLOW, fill_opacity=0.7)
        self.alita_2.set_stroke(color=BLACK, width=2)
        self.alita_2.move_to(self.posicion + UP * 0.1 * self.escala + LEFT * 2.0 * self.escala + RIGHT * -0.5 * self.escala)
        self.alita_2.rotate(-PI / 4)

    def dibujar(self, escena):
        # Dibujar las alas en la escena
        escena.add(self.alita_1, self.alita_2)

    def animar_alita(self):
        # Animar el movimiento del sol
        return self.alita_1.animate.shift(RIGHT * 2), self.alita_2.animate.shift(RIGHT * 2) 

# Clase para las patas del pollo
class Patas:
    def __init__(self, escala=1, posicion=ORIGIN):
        self.pata_izquierda = None
        self.pata_derecha = None
        self.escala = escala  # Nuevo parámetro para el tamaño
        self.posicion = posicion  # Nueva posición inicial

    def crear(self, cuerpo):
        # Crear las patas (triángulos naranjas)
        self.pata_izquierda = Triangle(color=ORANGE, fill_opacity=1).scale(0.5 * self.escala)
        self.pata_derecha = Triangle(color=ORANGE, fill_opacity=1).scale(0.5 * self.escala)
        self.pata_izquierda.set_stroke(color=BLACK, width=2)
        self.pata_derecha.set_stroke(color=BLACK, width=2)

        # Posicionar las patas más cerca del cuerpo
        # Ajustar las posiciones de las patas de acuerdo con el cuerpo
        # El cuerpo está centrado en su posición, entonces las patas estarán ligeramente abajo
        self.pata_izquierda.move_to(cuerpo.cuerpo.get_center() + LEFT * 1.15 * self.escala + DOWN * 1.4 * self.escala)
        self.pata_derecha.move_to(cuerpo.cuerpo.get_center() + RIGHT * 1.15 * self.escala + DOWN * 1.4 * self.escala)

    def dibujar(self, escena):
        # Dibujar las patas en la escena
        escena.add(self.pata_izquierda, self.pata_derecha)

    
    def animar_patita(self):
        # Animar el movimiento del sol
        return self.pata_izquierda.animate.shift(RIGHT * 2), self.pata_derecha.animate.shift(RIGHT * 2) 
