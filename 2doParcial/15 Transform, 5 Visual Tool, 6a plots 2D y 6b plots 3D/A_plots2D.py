from  manim import *


class PlotGraph(Scene):
    def construct(self):
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


def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))


class Plot1(Scene):
    def construct(self):
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
        x_label = axes.get_x_axis_label("x", direction=UP)
        y_label = axes.get_y_axis_label("y", direction=RIGHT)

        # Animaciones
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph), run_time=2)
        self.wait()
class Plot1v2(Scene):
    def construct(self):
        # Configuración de los ejes
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

        # Etiquetas para los ejes
        x_label = axes.get_x_axis_label("$x$")
        y_label = axes.get_y_axis_label("$y$")

        # Animaciones
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph), run_time=2)
        self.wait()

class Plot2(Scene):
    def construct(self):
        # Configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 1],  # [min, max, step]
            y_range=[0, 50, 5],  # [min, max, step]
            x_length=7,
            y_length=6,
            axis_config={"color": BLUE},
            tips=False
        )

        # Etiquetas para los ejes
        axes.add_coordinates(
            x_values=range(2, 8, 1),  # Etiquetas para el eje x
            y_values=range(20, 55, 5),  # Etiquetas para el eje y
        )
        x_label = axes.get_x_axis_label("$t$", direction=DOWN)
        y_label = axes.get_y_axis_label("$f(t)$", direction=LEFT)

        # Gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            color=GREEN,
        )

        # Animaciones
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph), run_time=2)
        self.wait()

class Plot3(Scene):
    def construct(self):
        # Configuración de los ejes
        axes = Axes(
            x_range=[0, 7, 1],  # [min, max, step]
            y_range=[0, 50, 10],  # [min, max, step]
            axis_config={"color": BLUE},
            tips=False
        )

        # Añadir etiquetas personalizadas
        axes.add_coordinates(
            x_values=[0, 2, 5, 4],  # Etiquetas específicas en el eje x
            y_values=range(0, 55, 5)  # Etiquetas en el eje y
        )

        # Gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            color=GREEN
        )

        # Animaciones
        self.play(Create(axes))
        self.play(Create(graph), run_time=2)
        self.wait()
class Plot4(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 7, 1],  # [min, max, step]
            y_range=[0, 50, 10],  # [min, max, step]
            axis_config={"color": BLUE},
            tips=False
        )

        # Añadir etiquetas personalizadas
        axes.add_coordinates(
            x_values=[3.5, 5, 4],  # Etiquetas específicas en el eje x
            y_values=range(0, 55, 5)  # Etiquetas en el eje y
        )

        # Gráfico de la función
        graph = axes.plot(
            lambda x: x**2,
            color=GREEN
        )

        # Animaciones
        self.play(Create(axes))
        self.play(Create(graph), run_time=2)
        self.wait()

        
class Plot5(Scene):
    def construct(self):
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

class Plot6(Scene):
    def construct(self):
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

class Plot7(Scene):
    def construct(self):
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

class PlotSinCos(Scene):
    def construct(self):
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