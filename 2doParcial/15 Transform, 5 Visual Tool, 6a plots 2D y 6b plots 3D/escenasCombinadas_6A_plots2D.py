from manim import *
import random
from A_plots2D import Range 

class escenasCombinadas(Scene):

    def cambiar_fondo(self, color, duracion=2):
        """
        Método para cambiar el fondo de la escena con una animación.

        Args:
            color (str): Color al que se cambiará el fondo.
            duracion (float): Tiempo de duración de la animación.
        """
        # Crear un rectángulo que cubra toda la pantalla
        fondo = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=color,
            fill_opacity=0,
            stroke_width=0
        )
        fondo.to_edge(ORIGIN)

        # Añadir el rectángulo y animar su opacidad
        self.add(fondo)
        self.play(fondo.animate.set_fill(opacity=1), run_time=duracion)
        # Cambiar el color de fondo real de la cámara
        self.camera.background_color = color
        self.remove(fondo)

    def construct(self):
        # Fondo blanco inicial
        self.camera.background_color = WHITE

        # Cargar imágenes de los logos
        logo_uaem = ImageMobject("logo_uaem.png").scale(0.8).shift(LEFT * 5)
        logo_ico = ImageMobject("logo_ico.png").scale(0.8).shift(RIGHT * 5)

        # Textos principales
        titulo_universidad = Text(
            "Centro Universitario UAEM ZUMPANGO",
            font_size=36,
            color=BLACK
        )
        texto_ingenieria = Text(
            "Ingeniería en Computación",
            font_size=32,
            color=BLACK
        )
        texto_materia = Text(
            "Graficación Computacional",
            font_size=32,
            color=BLACK
        )
        texto_periodo = Text(
            "Periodo 2024B",
            font_size=32,
            color=BLACK
        )

        # Datos generales
        datos_generales = Text(
            "Nombre: Diego Gómez Tagle González",
            font_size=28,
            color=BLACK,
            line_spacing=0.8
        )

        # Posiciones
        titulo_universidad.shift(UP * 2.5)
        texto_ingenieria.next_to(titulo_universidad, DOWN, buff=0.5)
        texto_materia.next_to(texto_ingenieria, DOWN, buff=0.5)
        texto_periodo.next_to(texto_materia, DOWN, buff=0.5)
        datos_generales.next_to(texto_periodo, DOWN, buff=1)

        # Añadir y animar elementos
        self.add(logo_uaem, logo_ico)
        self.play(FadeIn(titulo_universidad))
        self.play(Write(texto_ingenieria))
        self.play(Write(texto_materia))
        self.play(Write(texto_periodo))
        self.play(FadeIn(datos_generales))

        # Espera antes del cambio de color
        self.wait(2)

        # Cambiar colores del título
        titulo_nuevo = Text(
            "Centro Universitario UAEM ZUMPANGO",
            font_size=36
        )
        titulo_nuevo[:19].set_color('#877d06')  # "Centro Universitario"
        titulo_nuevo[19:].set_color('#124713')  # "UAEM ZUMPANGO"
        titulo_nuevo.shift(UP * 2.5)
        
        self.play(Transform(titulo_universidad, titulo_nuevo))

        # Espera antes de eliminar todo
        self.wait(2)

        # Desaparición y cambio de fondo
        self.play(
            FadeOut(titulo_universidad),
            FadeOut(texto_ingenieria),
            FadeOut(texto_materia),
            FadeOut(texto_periodo),
            FadeOut(datos_generales),
            FadeOut(logo_uaem),
            FadeOut(logo_ico)
        )
        # Crear un rectángulo negro que cubra toda la pantalla
        fondo_negro = Rectangle(
            width=120, height=120, color=BLACK, fill_opacity=0
        ).set_z_index(-1)  # Asegúrate de que esté detrás de los elementos

        # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Fondo blanco inicial
        self.camera.background_color = BLACK


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Configuración de los ejes
        axes = Axes(
            x_range=[4, 7.5, 0.5],  # [min, max, step]
            y_range=[20, 50, 5],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE},
            x_axis_config={
                "numbers_to_include": [4, 5, 6, 7],
                "label_direction": DOWN,
                "include_numbers": True,
            },
            y_axis_config={
                "numbers_to_include": [20, 30, 40, 50],
                "label_direction": RIGHT,
                "include_numbers": True,
            },
        )

        # Etiquetas de los ejes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        # Gráfico de la función
        graph = axes.plot(lambda x: x**2, x_range=[5, 7], color=GREEN)

        # Punto en las coordenadas iniciales
        dot = Dot(axes.coords_to_point(4, 20), color=RED)

        # Animaciones
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph), FadeIn(dot))
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(RED_E, duracion=2)

        # Configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 0.5],  # [min, max, step]
            y_range=[0, 50, 5],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE},
            x_axis_config={
                "numbers_to_include": list(np.arange(2, 7.5, 0.5)),
                "include_numbers": True,
                "label_direction": UP,
            },
            y_axis_config={
                "numbers_to_include": range(0, 60, 10),
                "include_numbers": True,
                "label_direction": RIGHT,
            },
        )

        # Gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            color=GREEN,
            x_range=[2, 4],
        )

        # Etiquetas de los ejes
        x_label = axes.get_x_axis_label("x", direction=UP)  # Etiqueta sin LaTeX para el eje X
        y_label = axes.get_y_axis_label("y", direction=RIGHT)  # Etiqueta sin LaTeX para el eje Y




        # Animaciones
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph), run_time=2)
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(DARK_BLUE, duracion=2)        

        # Nueva configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 1],  # [min, max, step]
            y_range=[0, 50, 5],  # [min, max, step]
            x_length=7,
            y_length=6,
            axis_config={"color": BLUE},
            tips=False
        ).move_to(ORIGIN)

        # Gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            color=GREEN,
            x_range=[2, 4],
        )

        # Etiquetas de los ejes (con LaTeX)
        x_label = axes.get_x_axis_label("x", direction=UP)  # Etiqueta sin LaTeX para el eje X
        y_label = axes.get_y_axis_label("y", direction=RIGHT)  # Etiqueta sin LaTeX para el eje Y

        # Animaciones
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph), run_time=2)
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(DARK_BROWN, duracion=2)

        # Configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 1],  # [min, max, step]
            y_range=[0, 50, 5],  # [min, max, step]
            x_length=7,
            y_length=6,
            axis_config={"color": BLUE},
            tips=False
        )

        # Etiquetas para los ejes X y Y
        x_labels = [Text(str(i)).next_to(axes.c2p(i, 0), DOWN) for i in range(2, 8, 1)]
        y_labels = [Text(str(i)).next_to(axes.c2p(0, i), LEFT) for i in range(20, 55, 5)]

        # Etiquetas de los ejes
        x_label = axes.get_x_axis_label(MathTex("t"), direction=DOWN)
        y_label = axes.get_y_axis_label(MathTex("f(t)"), direction=LEFT)

        # Gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            color=GREEN,
        )

        # Animaciones
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(*[Write(label) for label in x_labels])  # Escribir etiquetas de X
        self.play(*[Write(label) for label in y_labels])  # Escribir etiquetas de Y
        self.play(Create(graph), run_time=2)
        self.wait()



        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)


        # Cambiar a fondo blanco
        self.cambiar_fondo(DARKER_GREY, duracion=2)

        

        # Configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 1],  # [min, max, step]
            y_range=[0, 50, 10],  # [min, max, step]
            axis_config={"color": BLUE},
            tips=False
        )

        # Añadir etiquetas personalizadas en el eje X y Y
        x_values = [0, 2, 5, 4]  # Etiquetas específicas en el eje X
        y_values = range(0, 55, 5)  # Etiquetas en el eje Y

        # Crear etiquetas para el eje X
        x_labels = [Text(str(i)).next_to(axes.c2p(i, 0), DOWN) for i in x_values]

        # Crear etiquetas para el eje Y
        y_labels = [Text(str(i)).next_to(axes.c2p(0, i), LEFT) for i in y_values]

        # Gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            color=GREEN
        )

        # Animaciones
        self.play(Create(axes))
        self.play(*[Write(label) for label in x_labels])  # Escribir etiquetas personalizadas de X
        self.play(*[Write(label) for label in y_labels])  # Escribir etiquetas de Y
        self.play(Create(graph), run_time=2)
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)# Configuración de los ejes

        # Cambiar a fondo blanco
        self.cambiar_fondo(GRAY, duracion=2)


        axes = Axes(
            x_range=[0, 7, 1],  # [min, max, step]
            y_range=[0, 50, 10],  # [min, max, step]
            axis_config={"color": BLUE},
            tips=False
        )

        # Etiquetas personalizadas para el eje X
        x_values = [3.5, 5, 4]  # Etiquetas específicas en el eje X
        x_labels = [Text(str(i)).next_to(axes.c2p(i, 0), DOWN) for i in x_values]

        # Etiquetas personalizadas para el eje Y
        y_values = range(0, 55, 5)  # Etiquetas en el eje Y
        y_labels = [Text(str(i)).next_to(axes.c2p(0, i), LEFT) for i in y_values]

        # Gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            color=GREEN
        )

        # Animaciones
        self.play(Create(axes))
        self.play(*[Write(label) for label in x_labels])  # Escribir etiquetas personalizadas de X
        self.play(*[Write(label) for label in y_labels])  # Escribir etiquetas personalizadas de Y
        self.play(Create(graph), run_time=2)
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(BLUE_A, duracion=2)

        # Configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 0.5],  # [min, max, step]
            y_range=[0, 50, 10],  # [min, max, step]
            axis_config={"color": BLUE},
            tips=False
        )

        # Etiquetas personalizadas en el eje X
        x_labels = VGroup(
            MathTex("3.5").scale(0.7).next_to(axes.c2p(3.5, 0), DOWN),
            MathTex(r"\frac{9}{2}").scale(0.7).next_to(axes.c2p(4.5, 0), DOWN)
        )

        # Gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            color=GREEN
        )

        # Animaciones
        self.play(Create(axes))
        self.play(Write(x_labels))
        self.play(Create(graph), run_time=2)
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(BLACK, duracion=2)

        # Configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 0.5],  # [min, max, step]
            y_range=[0, 50, 10],  # [min, max, step]
            axis_config={"color": BLUE},
            tips=False
        )

        # Etiquetas personalizadas en el eje X
        decimal_values = [0, 0.5, 1, 1.5, 3.35]  # Posiciones de las etiquetas
        x_labels = VGroup(*[
            MathTex(f"{val:.2f}" if val % 1 != 0 else f"{int(val)}")  # Formatear etiquetas
            .scale(0.7)
            .next_to(axes.c2p(val, 0), DOWN)
            for val in decimal_values
        ])

        # Gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            color=GREEN
        )

        # Animaciones
        self.play(Create(axes))
        self.play(Write(x_labels))
        self.play(Create(graph), run_time=2)
        self.wait()



        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(MAROON, duracion=2)


        # Configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 0.5],  # [min, max, step]
            y_range=[0, 50, 10],  # [min, max, step]
            axis_config={"color": BLUE},
            tips=False
        )

        # Generación de etiquetas para el eje X
        step_x = 0.5
        end_x = 7
        x_labels = VGroup(*[
            MathTex(f"{x:.1f}").scale(0.7).next_to(axes.c2p(x, 0), DOWN)
            for x in np.arange(0, end_x + step_x, step_x)
        ])

        # Gráfico de la función
        graph = axes.plot(lambda x: x**2, color=GREEN)

        # Animaciones
        self.play(Create(axes))
        self.play(Write(x_labels))
        self.play(Create(graph), run_time=2)
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(BLACK, duracion=2)


        # Configuración de los ejes
        axes = Axes(
            x_range=[-3 * PI / 2, 3 * PI / 2, PI / 2],  # [min, max, step]
            y_range=[-1.5, 1.5, 0.5],  # [min, max, step]
            axis_config={"color": WHITE},
            tips=False
        )
        axes.x_axis.set_color(RED).set_stroke(width=2)
        axes.y_axis.set_color(YELLOW).set_stroke(width=2)

        # Etiquetas para los ejes
        sin_label = MathTex(r"\sin\theta").set_color(BLUE).next_to(axes.y_axis, UP)
        theta_label = MathTex(r"\theta").set_color(PURPLE).next_to(axes.x_axis, RIGHT + UP)

        # Etiquetas del eje Y
        y_labels = VGroup(
            MathTex("-1").scale(0.7).next_to(axes.c2p(0, -1), LEFT),
            MathTex("1").scale(0.7).next_to(axes.c2p(0, 1), LEFT)
        )

        # Etiquetas del eje X
        x_positions = [-3 * PI / 2, -PI, -PI / 2, 0, PI / 2, PI, 3 * PI / 2]
        x_labels_tex = [
            r"-\frac{3\pi}{2}", r"-\pi", r"-\frac{\pi}{2}", r"0",
            r"\frac{\pi}{2}", r"\pi", r"\frac{3\pi}{2}"
        ]
        x_labels = VGroup(*[
            MathTex(label).scale(0.7).next_to(axes.c2p(pos, 0), DOWN if pos != -PI and pos != PI else 2 * DOWN)
            for pos, label in zip(x_positions, x_labels_tex)
        ])

        # Gráficos de las funciones
        plot_sin = axes.plot(lambda x: np.sin(x), color=GREEN, x_range=[-4, 4])
        plot_cos = axes.plot(lambda x: np.cos(x), color=GRAY, x_range=[-PI, 0])
        plot_sin.set_stroke(width=3)
        plot_cos.set_stroke(width=2)

        # Animaciones
        self.play(Create(axes))
        self.play(Write(sin_label), Write(theta_label), Write(y_labels), Write(x_labels))
        self.play(Create(plot_sin), run_time=2)
        self.play(Create(plot_cos), run_time=2)
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(DARK_GRAY, duracion=2)

        texto_gracias = Text(
            "Gracias por su atención!! ",
            font_size=32,
            color=WHITE
        )

        self.play(FadeIn(texto_gracias))

        self.wait(5)
        self.play(FadeOut(texto_gracias))
        self.wait(2)
