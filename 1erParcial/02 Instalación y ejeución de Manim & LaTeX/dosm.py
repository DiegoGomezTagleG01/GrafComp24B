from manim import *  # Importa todas las clases y funciones de Manim

class expresion(Scene):  # Define una escena de animación
    def construct(self):  # Método principal donde se construye la animación
        text = MathTex("x^2")  # Crea una fórmula matemática "x^2"
        self.add(text)  # Añade la fórmula a la escena

#Para ejecutar, poner en consola
#manim DosM.py expresion -pg