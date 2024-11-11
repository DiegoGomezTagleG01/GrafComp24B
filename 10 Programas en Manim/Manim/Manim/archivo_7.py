from manim import *
import numpy as np

class Shapes(Scene):
  def construct(self):
    circulo = Circle() # Creación de circulo
    createCircle = Create(circulo) # Animación de creación
    self.play(createCircle) # Mostrar la animación
    fadeOutCircle = FadeOut(circulo) # Animación de desaparición
    self.play(fadeOutCircle) # Mostrar la animación

    rect = Rectangle(color="red", height=3, width=1)
    self.play(Create(rect))
    self.play(FadeOut(rect))
    cuadrado = Square(color="red") # Cuadrado
    cuadrado2 = Square(color="blue")
    cuadrado3 = Square(color="green") # Cuadrado
    cuadrado4 = Square(color="white")
    cuadrado5 = Square(color="yellow")
    cuadrado.move_to(np.array([5, -2, 0])) # Llevas al cuadrado a la coordenada
    #                         ( x, y, z)
    cuadrado2.to_edge(UP) # LLeva una figura al borde
    cuadrado3.to_edge(DOWN) # LLeva una figura al borde
    cuadrado4.to_edge(LEFT) # LLeva una figura al borde
    cuadrado5.to_edge(RIGHT) # LLeva una figura al borde
    # Hay cuatro direcciónes UP, LEFT, RIGHT, DOWN
    self.play(Create(cuadrado), Create(cuadrado2),Create(cuadrado3),Create(cuadrado4),Create(cuadrado5))
    self.play(FadeOut(cuadrado), FadeOut(cuadrado2),FadeOut(cuadrado3),FadeOut(cuadrado4),FadeOut(cuadrado5))

    linea = Line(np.array([2,0,0]),np.array([-2,1,0]))
#                               posición final
    self.play(Create(linea))
    self.play(FadeOut(linea))