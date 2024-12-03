from manim import *  # Importa todas las clases y funciones de Manim

class cubito(Scene):  # Define una escena de animación
    def construct(self):  # Método principal donde se construye la animación
        sq = Square()  # Crea un cuadrado
        circ = Circle().set_fill(opacity=1)  # Crea un círculo y lo rellena completamente
        self.play(Transform(sq, circ))  # Anima la transformación del cuadrado al círculo
        self.wait()  # Pausa para mantener la animación visible

##Para ejecutar, poner en consola
#manim PrimerP.py cubito -p