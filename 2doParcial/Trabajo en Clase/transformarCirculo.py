from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(circle))  # animate the creation of the square
        self.play(Transform(circle, square))  # interpolate the square into the circle
        self.play(FadeOut(circle))  # fade out animation