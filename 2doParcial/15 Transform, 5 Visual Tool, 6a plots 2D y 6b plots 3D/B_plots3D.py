from manim import *

class CameraPosition1(ThreeDScene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait()


class CameraPosition2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=0 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()


class CameraPosition3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()


class CameraPosition4(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6)
        self.play(Create(circle), Create(axes))
        self.wait()


class CameraPosition5(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(
            phi=80 * DEGREES, theta=45 * DEGREES, distance=6, gamma=30 * DEGREES
        )
        self.play(Create(circle), Create(axes))
        self.wait()


class MoveCamera1(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.play(Create(circle), Create(axes))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait()


class MoveCamera2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.begin_ambient_camera_rotation(rate=0.1)  # Start moving camera
        self.wait(5)
        self.stop_ambient_camera_rotation()  # Stop camera rotation
        self.move_camera(phi=80 * DEGREES, theta=-PI / 2)  # Reset camera position
        self.wait()


class ParametricCurve1(ThreeDScene):
    def construct(self):
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

# Add this in the object: .set_shade_in_3d(True)
class ParametricCurve(ThreeDScene):
    def construct(self):
        # Definir curvas paramétricas
        curve1 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u / 2
            ]),
            color=RED, t_min=-TAU, t_max=TAU,
        )

        curve2 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u
            ]),
            color=RED, t_min=-TAU, t_max=TAU,
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

class SurfacesAnimation(ThreeDScene):
    def construct(self):
        # Crear los ejes 3D
        axes = ThreeDAxes()

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
            v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)
        ).scale(2)

        para_hyp = Surface(
            lambda u, v: np.array([
                u,
                v,
                u**2 - v**2
            ]),
            v_min=-2, v_max=2, u_min=-2, u_max=2,
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)
        ).scale(1)

        cone = Surface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                u
            ]),
            v_min=0, v_max=TAU, u_min=-2, u_max=2,
            checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)
        ).scale(1)

        hip_one_side = Surface(
            lambda u, v: np.array([
                np.cosh(u) * np.cos(v),
                np.cosh(u) * np.sin(v),
                np.sinh(u)
            ]),
            v_min=0, v_max=TAU, u_min=-2, u_max=2,
            checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32)
        )

        ellipsoid = Surface(
            lambda u, v: np.array([
                1 * np.cos(u) * np.cos(v),
                2 * np.cos(u) * np.sin(v),
                0.5 * np.sin(u)
            ]),
            v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2,
            checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)
        ).scale(2)

        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2,
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

from manim import *

# Clase para texto en 3D en el plano XY
class Text3D1(ThreeDScene):
    def construct(self):
        # Crear ejes 3D
        axes = ThreeDAxes()
        # Configurar la orientación de la cámara
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        # Crear texto en el plano XY
        text3d = Text("This is a 3D text").scale(2)
        # Agregar ejes y texto a la escena
        self.add(axes, text3d)


# Clase para texto en 3D rotado sobre el eje X
class Text3D2(ThreeDScene):
    def construct(self):
        # Crear ejes 3D
        axes = ThreeDAxes()
        # Configurar la orientación de la cámara
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        # Crear texto en 3D y rotarlo sobre el eje X
        text3d = Text("This is a 3D text").scale(2)
        text3d.rotate(PI / 2, axis=RIGHT)
        # Agregar ejes y texto a la escena
        self.add(axes, text3d)


# Clase para texto tradicional fijo en la cámara con animación
class Text3D3(ThreeDScene):
    def construct(self):
        # Crear ejes 3D
        axes = ThreeDAxes()
        # Configurar la orientación de la cámara
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        # Crear texto tradicional
        text3d = Text("This is a 3D text")
        # Fijar el texto en el marco de la cámara
        self.add_fixed_in_frame_mobjects(text3d)
        # Posicionar el texto en la esquina superior izquierda
        text3d.to_corner(UL)

        # Agregar ejes a la escena
        self.add(axes)
        # Iniciar rotación de la cámara
        self.begin_ambient_camera_rotation(rate=0.2)
        # Animar la aparición del texto
        self.play(Write(text3d))

        # Crear una esfera como superficie 3D
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            u_range=[0, PI],
            v_range=[0, TAU],
            checkerboard_colors=[RED, RED_E],
            resolution=(15, 32)
        )

        # Animar la creación de la esfera
        self.play(Create(sphere))
        self.wait(2)
