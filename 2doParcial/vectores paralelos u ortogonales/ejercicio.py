from manim import *

class VectorScene3D(ThreeDScene):
    def construct(self):
        # Configuración inicial de la cámara en 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Vectores en 3D
        u = np.array([-2, 8, -12]) / 2
        v = np.array([1, -4, 6]) / 2
        vector_u = Arrow3D(start=[0, 0, 0], end=u, color=RED)
        vector_v = Arrow3D(start=[0, 0, 0], end=v, color=BLUE)

        # Etiquetas de los vectores
        text_u = MathTex("\\mathbf{u} = \\begin{bmatrix}-2 \\\\ 8 \\\\ -12\\end{bmatrix}", color=RED).to_corner(UL)
        text_v = MathTex("\\mathbf{v} = \\begin{bmatrix}1 \\\\ -4 \\\\ 6\\end{bmatrix}", color=BLUE).to_corner(UR)

        # Producto punto
        producto_punto = int(np.dot(u, v))
        text_producto_punto = MathTex(
            "\\mathbf{u} \\cdot \\mathbf{v} = ",
            f"{producto_punto}",
            color=WHITE
        ).to_edge(UP * 0.25)

        # Verificaciones de ortogonalidad y paralelismo
        text_ortogonalidad = MathTex("\\text{¿Son ortogonales? No, } \\mathbf{u} \\cdot \\mathbf{v} \\neq 0").next_to(text_producto_punto, DOWN)
        text_paralelismo = MathTex("\\text{¿Son paralelos? Sí, tienen la misma proporción.}").next_to(text_ortogonalidad, DOWN)

        # Cálculo de proporciones
        proporciones = [u[i] / v[i] for i in range(3)]
        text_proporcion = MathTex(
            "\\text{Proporción: }",
            f"\\frac{{{u[0]}}}{{{v[0]}}} = {proporciones[0]:.1f}, \\; "
            f"\\frac{{{u[1]}}}{{{v[1]}}} = {proporciones[1]:.1f}, \\; "
            f"\\frac{{{u[2]}}}{{{v[2]}}} = {proporciones[2]:.1f}",
            color=YELLOW
        ).next_to(text_paralelismo, DOWN)

        # Crear ejes
        axes = ThreeDAxes()

        # Animaciones
        self.play(Create(axes))
        self.play(Create(vector_u), Write(text_u))
        self.play(Create(vector_v), Write(text_v))
        self.wait(1)

        # Ajustar la cámara para que muestre ambos vectores claramente
        self.move_camera(phi=60 * DEGREES, theta=-30 * DEGREES, run_time=3)
        self.wait(1)

        # Mostrar el producto punto
        self.play(Write(text_producto_punto))
        self.wait(1)

        # Mostrar verificaciones de ortogonalidad y paralelismo
        self.play(Write(text_ortogonalidad))
        self.wait(1)
        self.play(Write(text_paralelismo))
        self.wait(1)

        # Mostrar las proporciones entre los vectores
        self.play(Write(text_proporcion))
        self.wait(2)
