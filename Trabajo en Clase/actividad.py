from manim import *

class SquareAndCircle(Scene):
    def construct(self):
        square_izq_sup = Square()  
        square_izq_sup.set_fill(BLUE, opacity=0.5)

        square_drch_inf = Square()  
        square_drch_inf.set_fill(GREEN, opacity=0.5)

        circle_izq_inf = Circle()  
        circle_izq_inf.set_fill(RED, opacity=0.5)

        circle_drch_sup = Circle()  
        circle_drch_sup.set_fill(YELLOW, opacity=0.5)

        square_izq_sup.shift(LEFT * 5 + UP * 3)
        circle_drch_sup.shift(RIGHT * 5 + UP * 3)
        circle_izq_inf.shift(LEFT * 5 + DOWN * 3)
        square_drch_inf.shift(RIGHT * 5 + DOWN * 3)


        # Display the shapes on screen
        self.play(Create(square_izq_sup), Create(square_drch_inf),
                  Create(circle_izq_inf), Create(circle_drch_sup))
