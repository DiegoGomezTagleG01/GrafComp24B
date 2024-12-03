from manim import *
from A_plots2D import Range 

class escenasCombinadas(ThreeDScene):

    def cambiar_fondo(self, color, duracion=2):
        self.camera.background_color = color
        
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

        circle = Circle()
        self.play(Create(circle))
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=0 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(GOLD, duracion=2)

        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6)
        self.play(Create(circle), Create(axes))
        self.wait()

   

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)# Configuración de los ejes

        # Cambiar a fondo blanco
        self.cambiar_fondo(DARK_BLUE, duracion=2)

        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(
            phi=80 * DEGREES, theta=45 * DEGREES, distance=6, gamma=30 * DEGREES
        )
        self.play(Create(circle), Create(axes))
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(DARK_GRAY, duracion=2)

        axes = ThreeDAxes()
        circle = Circle()
        self.play(Create(circle), Create(axes))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(GREEN_A, duracion=2)

        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.begin_ambient_camera_rotation(rate=0.1)  # Start moving camera
        self.wait(5)
        self.stop_ambient_camera_rotation()  # Stop camera rotation
        self.move_camera(phi=80 * DEGREES, theta=-PI / 2)  # Reset camera position
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        curve1 = ParametricFunction(
            lambda u: np.array(
                [1.2 * np.cos(u), 1.2 * np.sin(u), u / 2]
            ),
            color=RED,
            t_range=np.array([-TAU, TAU]),
        )
        curve2 = ParametricFunction(
            lambda u: np.array(
                [1.2 * np.cos(u), 1.2 * np.sin(u), u]
            ),
            color=RED,
            t_range=np.array([-TAU, TAU]),
        )
        axes = ThreeDAxes()

        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(Create(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)# Configuración de los ejes
        # Cambiar a fondo blanco
        self.cambiar_fondo(RED_B, duracion=2)

        curve1 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u / 2
            ]),
            color=RED, t_range=np.array([-TAU, TAU]),
        )

        curve2 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u
            ]),
            color=RED, t_range=np.array([-TAU, TAU]),
        )

        # Habilitar sombras para ambas curvas
        curve1.set_shade_in_3d(True)
        curve2.set_shade_in_3d(True)

        # Crear ejes 3D
        axes = ThreeDAxes()

        # Agregar ejes a la escena
        self.add(axes)

        # Configurar la cámara
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Animaciones
        self.play(Create(curve1))  # Crear la primera curva
        self.wait()
        self.play(
            Transform(curve1, curve2),  # Transformar la curva
            rate_func=there_and_back, 
            run_time=3
        )
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)# Configuración de los ejes

        # Cambiar a fondo blanco
        self.cambiar_fondo(BLACK, duracion=2)
 # Definir superficies paramétricas
        cylinder = Surface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)  # Resolución de la superficie
        ).fade(0.5)

        paraboloid = Surface(
            lambda u, v: np.array([
                np.cos(v) * u,
                np.sin(v) * u,
                u**2
            ]),
            u_range=[0, 2], v_range=[0, TAU],  # Uso de u_range y v_range
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)
        ).scale(2)

        para_hyp = Surface(
            lambda u, v: np.array([
                u,
                v,
                u**2 - v**2
            ]),
            u_range=[-2, 2], v_range=[-2, 2],  # Uso de u_range y v_range
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)
        ).scale(1)

        cone = Surface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                u
            ]),
            u_range=[0, 2], v_range=[0, TAU],  # Uso de u_range y v_range
            checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)
        ).scale(1)

        hip_one_side = Surface(
            lambda u, v: np.array([
                np.cosh(u) * np.cos(v),
                np.cosh(u) * np.sin(v),
                np.sinh(u)
            ]),
            u_range=[-2, 2], v_range=[0, TAU],  # Uso de u_range y v_range
            checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32)
        )

        ellipsoid = Surface(
            lambda u, v: np.array([
                1 * np.cos(u) * np.cos(v),
                2 * np.cos(u) * np.sin(v),
                0.5 * np.sin(u)
            ]),
            u_range=[-PI/2, PI/2], v_range=[0, TAU],  # Uso de u_range y v_range
            checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)
        ).scale(2)

        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            u_range=[-PI/2, PI/2], v_range=[0, TAU],  # Uso de u_range y v_range
            checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)
        ).scale(2)

        # Configurar la cámara
        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        # Animaciones
        self.add(axes)
        self.play(Write(sphere))  # Crear la esfera
        self.wait()
        self.play(ReplacementTransform(sphere, ellipsoid))  # Transformar a elipsoide
        self.wait()
        self.play(ReplacementTransform(ellipsoid, cone))  # Transformar a cono
        self.wait()
        self.play(ReplacementTransform(cone, hip_one_side))  # Transformar a hipérbola
        self.wait()
        self.play(ReplacementTransform(hip_one_side, para_hyp))  # Transformar a parábola hiperbólica
        self.wait()
        self.play(ReplacementTransform(para_hyp, paraboloid))  # Transformar a paraboloide
        self.wait()
        self.play(ReplacementTransform(paraboloid, cylinder))  # Transformar a cilindro
        self.wait()
        self.play(FadeOut(cylinder))  # Desaparecer el cilindro
        # Configuración de los ejes y la orientación de la cámara
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Primer texto 3D
        text3d = Text("This is a 3D text").scale(2)
        self.add(axes, text3d)
        self.wait(1)  # Espera para mostrar el primer texto

        # Limpiar la escena antes de la siguiente animación
        self.remove(text3d)  # Eliminar solo el texto, no los ejes


        # Cambiar a fondo blanco
        self.cambiar_fondo(DARK_BROWN, duracion=2)

        # Segundo texto 3D con rotación sobre el eje X
        text3d_rotated = Text("This is a 3D text").scale(2)
        text3d_rotated.rotate(PI / 2, axis=RIGHT)
        self.add(axes, text3d_rotated)
        self.wait(1)  # Espera para mostrar el texto rotado

        # Limpiar la escena antes de la siguiente animación
        self.remove(text3d_rotated)

        # Cambiar a fondo blanco
        self.cambiar_fondo(ORANGE, duracion=2)

        # Tercer texto 3D fijo en la esquina superior izquierda
        text3d_fixed = Text("This is a 3D text")
        self.add_fixed_in_frame_mobjects(text3d_fixed)
        text3d_fixed.to_corner(UL)
        self.add(axes)

        # Iniciar rotación de la cámara
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(Write(text3d_fixed))
        self.wait(1)  # Espera para mostrar el texto fijo

        # Crear la esfera como superficie 3D
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            u_range=[0, 2*PI],
            v_range=[0, TAU],
            checkerboard_colors=[RED, RED_E],
            resolution=(15, 32)
        )

        # Animar la creación de la esfera
        self.play(Create(sphere))
        self.wait(2)  # Espera para mostrar la esfera

        # Limpiar los objetos para la próxima escena si es necesario
        self.remove(*self.mobjects)

        # Cambiar a fondo blanco
        self.cambiar_fondo(BLUE_B, duracion=2)




        texto_gracias = Text(
            "Gracias por su atención!! ",
            font_size=32,
            color=WHITE
        )
        self.add_fixed_in_frame_mobjects(texto_gracias)
        self.play(FadeIn(texto_gracias))

        self.wait(5)
        self.play(FadeOut(texto_gracias))
        self.wait(2)
