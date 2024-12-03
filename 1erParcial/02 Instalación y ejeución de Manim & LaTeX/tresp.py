from manim import *  # Importa todas las clases y funciones de Manim

class formula_general(Scene):  # Define una escena de animación
    def construct(self):  # Método principal donde se construye la animación
        text = MathTex("x=-b \pm \\frac{\sqrt{b^2-4ac}}{2ac}")  # Crea una fórmula matemática "x^2"
        self.add(text)  # Añade la fórmula a la escena

#manim tresp.py formula_general -pg