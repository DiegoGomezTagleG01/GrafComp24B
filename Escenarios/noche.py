from manim import *

class NocheScene(Scene):
    def construct(self):
        # Crear el cielo oscuro como fondo
        cielo = Rectangle(width=config.frame_width, height=config.frame_height, color=DARK_BLUE, fill_opacity=1)
        self.add(cielo)  # Añadir el cielo oscuro al fondo

        # Crear el pasto en la parte inferior de la escena
        pasto = Rectangle(width=config.frame_width, height=2, color=GREEN, fill_opacity=1)
        pasto.shift(DOWN * 2.5)  # Colocar el pasto en la parte inferior de la pantalla
        self.add(pasto)

        # Crear la luna en la esquina superior derecha
        luna = Circle(radius=0.5, color=WHITE, fill_opacity=1)
        luna.set_stroke(color=WHITE, width=2)
        luna.to_corner(UP + RIGHT)  # Posicionar la luna en la esquina superior derecha
        self.add(luna)
        
        

        # Función para crear un árbol
        def crear_arbol(posicion_x):
            # Tronco del árbol
            tronco = Rectangle(width=0.3, height=1, color=DARK_BROWN, fill_opacity=1)
            tronco.set_stroke(color=BLACK, width=2)
            tronco.shift(DOWN * 1 + posicion_x)  # Colocar el tronco en la posición indicada

            # Copa del árbol (tres óvalos verdes oscuros)
            copa_1 = Ellipse(width=1, height=0.6, color=GREEN, fill_opacity=1).next_to(tronco, UP, buff=0)
            copa_2 = Ellipse(width=1.2, height=0.7, color=GREEN, fill_opacity=1).next_to(copa_1, UP * 0.3)
            copa_3 = Ellipse(width=0.8, height=0.5, color=GREEN, fill_opacity=1).next_to(copa_2, UP * 0.2)

            # Añadir cada parte del árbol a la escena
            self.add(tronco, copa_1, copa_2, copa_3)

        # Crear múltiples árboles en diferentes posiciones
        posiciones_arboles = [LEFT * 3, LEFT * 1, RIGHT * 1.5, RIGHT * 3.5]
        for pos in posiciones_arboles:
            crear_arbol(pos)

        # Mostrar mensaje de bienvenida en el centro
        mensaje = Text("¡Bienvenidos a una noche en Culichis Sinaloa!", font_size=36).to_edge(UP)
        self.play(Write(mensaje))
        self.play(FadeOut(mensaje))

        # Pausar para mostrar la escena
        self.wait(2)

        # Desvanecer el mensaje
        self.play(FadeOut(mensaje))

# Crear la escena
scene = NocheScene()
scene.render()