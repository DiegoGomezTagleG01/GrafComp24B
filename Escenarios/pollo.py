from manim import *

# Definición de la clase ShowChicken que hereda de Scene
class ShowChicken(Scene):
    def construct(self):
        # Crear un texto en la parte superior
        title_text = Text("¡Bienvenido a la presentación!", font_size=36).to_edge(UP)
        self.play(Write(title_text))  # Animar la aparición del texto

        self.play(FadeOut(title_text))

        title_text = Text("Diego Gomez Tagle Gonzalez & Yair Uriel Flores Hidalgo", font_size=36).to_edge(UP)
        self.play(Write(title_text))  # Animar la aparición del texto

        
        # Creación de la cabeza del pollo (círculo amarillo)
        cabeza = Circle(radius=1, color=YELLOW, fill_opacity=1)
        cabeza.set_stroke(color=BLACK, width=2)  # Añadir un borde negro

        # Creación del ojo derecho (punto negro)
        ojo_derecho = Dot(point=cabeza.get_center() + RIGHT * 0.2 + UP * 0.1, color=BLACK, radius=0.1)

        # Creación del pico (triángulo naranja)
        pico = Triangle(color=ORANGE, fill_opacity=1).scale(0.5)
        pico.set_stroke(color=BLACK, width=2)  # Añadir borde negro

        # Posicionar el pico: su punta en la parte superior del círculo y la base en la parte inferior
        pico.set_points_as_corners([
            cabeza.get_center() + UP * 0.65,  # Punta superior
            cabeza.get_center() + LEFT * 0.25 + DOWN * 0.5,  # Extremo izquierdo de la base
            cabeza.get_center() + RIGHT * 1.45 + DOWN * 0.5,  # Extremo derecho de la base
            cabeza.get_center() + UP * 0.65   # Volver al punto superior
        ])

        # Creación del cuerpo del pollo (media elipse)
        punto_izquierdo = LEFT * 6.5 + DOWN * 0.25  # Extremo izquierdo
        punto_derecho = RIGHT * -1.55 + DOWN * 0.25  # Extremo derecho
        altura = 0.5  # Altura de la media elipse

        # Crear arco entre los puntos para el cuerpo
        cuerpo = ArcBetweenPoints(punto_izquierdo + UP * altura, punto_derecho + UP * altura, angle=PI, color=YELLOW, fill_opacity=1)
        cuerpo.set_stroke(color=BLACK, width=2)  # Añadir borde negro

        # Posicionar y rotar el cuerpo para alinear con la cabeza
        cuerpo.move_to(cabeza.get_center() + DOWN * 0.25 + LEFT * 2.25)  # Alinear el cuerpo con la cabeza
        cuerpo.rotate(-PI / 12)  # Rotar si es necesario

        # Creación de las alitas
        alita_1 = ArcBetweenPoints(punto_izquierdo + UP * 1.55, punto_derecho + UP * 1.55, angle=PI, color=YELLOW, fill_opacity=0.8)
        alita_1.set_stroke(color=BLACK, width=2)  # Añadir borde negro
        alita_1.move_to(cabeza.get_center() + DOWN * 0.25 + LEFT * 2.0 + RIGHT * -0.5)  # Alinear alita_1
        alita_1.rotate(-PI / 6)  # Rotar si es necesario
        
        alita_2 = ArcBetweenPoints(punto_izquierdo + UP * 1.75, punto_derecho + UP * 1.55, angle=PI, color=YELLOW, fill_opacity=0.7)
        alita_2.set_stroke(color=BLACK, width=2)  # Añadir borde negro
        alita_2.move_to(cabeza.get_center() + UP * 0.1 + LEFT * 2.0 + RIGHT * -0.5)  # Alinear alita_2
        alita_2.rotate(-PI / 4)  # Rotar si es necesario

        # Creación de las patas (triángulos amarillos)
        pata_izquierda = Triangle(color=ORANGE, fill_opacity=1).scale(0.5)
        pata_derecha = Triangle(color=ORANGE, fill_opacity=1).scale(0.5)
        pata_izquierda.set_stroke(color=BLACK, width=2)  # Añadir borde negro
        pata_derecha.set_stroke(color=BLACK, width=2)  # Añadir borde negro

        # Posicionar las patas
        pata_izquierda.move_to(-cuerpo.get_top() + LEFT * 4.5)  # Alinear con la izquierda del cuerpo
        pata_derecha.move_to(-cuerpo.get_top() + LEFT * 3.5)  # Alinear con la derecha del cuerpo

        # Animaciones para crear cada parte del pollo
        self.play(Create(pata_izquierda))
        self.play(Create(pata_derecha))
        self.play(Create(cuerpo))
        self.play(Create(alita_1))
        self.play(Create(alita_2))
        self.play(Create(pico))
        self.play(Create(cabeza))
        self.play(Create(ojo_derecho))

        # Esperar 2 segundos antes de continuar
        self.wait(2)

        # Mensaje final
        final_message = Text("¡Hola, soy Pollina Jolie!", font_size=36).to_edge(DOWN)
        final_message[9:21].set_color(RED)  # Cambiar el color de "Pollina Jolie" a rojo
        self.play(Write(final_message))
        
        # Desvanecer el primer mensaje
        self.play(FadeOut(final_message))

        final_message = Text("¡Change the World!", font_size=36).to_edge(DOWN)
        final_message[:].set_color(RED)  # Cambiar el color a rojo
        self.play(Write(final_message))
        self.play(FadeOut(final_message))

        # Desvanecer todas las formas del pollo
        self.play(FadeOut(cabeza),
                  FadeOut(ojo_derecho),
                  FadeOut(pico),
                  FadeOut(cuerpo),
                  FadeOut(alita_1),
                  FadeOut(alita_2),
                  FadeOut(pata_izquierda),
                  FadeOut(pata_derecha))

        # Desvanecer el texto en la parte superior
        self.play(FadeOut(title_text))

        self.play(FadeOut(title_text))


# Crear la escena
scene = ShowChicken()
scene.render()
