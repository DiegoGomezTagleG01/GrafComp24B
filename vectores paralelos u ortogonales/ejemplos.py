from manim import *

class VectorScene(Scene):
    def construct(self):
        # Definición de los vectores para el primer caso
        a1 = np.array([4, -1, 0])/4  # 4i - j
        b1 = np.array([2, 8, 0])/4   # 2i + 8j

        # Crear los vectores en la escena con escala para hacerlos más grandes
        vector_a1 = Vector(a1, color=RED)
        vector_b1 = Vector(b1, color=BLUE)

        # Colocar las etiquetas de los componentes de los vectores
        text_a1_i = MathTex("4\\hat{i}", color=RED).next_to(vector_a1.get_end(), RIGHT)
        text_a1_j = MathTex("-\\hat{j}", color=RED).next_to(vector_a1.get_end(), DOWN)
        text_b1_i = MathTex("2\\hat{i}", color=BLUE).next_to(vector_b1.get_end(), RIGHT)
        text_b1_j = MathTex("8\\hat{j}", color=BLUE).next_to(vector_b1.get_end(), UP)

        # Calcular el producto punto
        producto_punto_ab1 = int(np.dot(a1, b1))

        # Crear el texto para el producto punto y la pregunta
        text_producto_punto1 = MathTex(f"\\mathbf{{(6,-18)}} \\cdot \\mathbf{{(-4,12)}} = {producto_punto_ab1}", color=WHITE)
        texto_ortogonal1 = MathTex("\\text{¿Son ortogonales?Sí, porque el producto punto es 0}").set_color(WHITE)
        

        # Colocar los textos en la escena
        text_producto_punto1.to_edge(DOWN*2.6)
        texto_ortogonal1.next_to(text_producto_punto1, DOWN*1.6)
        

        # Mostrar los vectores con las etiquetas
        self.play(Create(vector_a1), Write(text_a1_i), Write(text_a1_j))
        self.play(Create(vector_b1), Write(text_b1_i), Write(text_b1_j))

        # Mostrar el producto punto
        self.play(Write(text_producto_punto1))

        # Mostrar si son ortogonales
        self.play(Write(texto_ortogonal1))

        # Esperar un momento antes de desvanecer
        self.wait(2)

        # Desvanecer todo lo mostrado antes de pasar al siguiente conjunto de vectores
        self.play(FadeOut(vector_a1), FadeOut(vector_b1), FadeOut(text_a1_i), FadeOut(text_a1_j), 
                  FadeOut(text_b1_i), FadeOut(text_b1_j), FadeOut(text_producto_punto1), FadeOut(texto_ortogonal1))

        # Definición de los vectores para el segundo caso
        a2 = np.array([6, -18, 0])/6  # 6i - 18j
        b2 = np.array([-4, 12, 0])/6  # -4i + 12j

        # Crear los vectores en la escena con escala para hacerlos más grandes
        vector_a2 = Vector(a2, color=RED)
        vector_b2 = Vector(b2, color=BLUE)

        # Colocar las etiquetas de los componentes de los vectores
        text_a2_i = MathTex("6\\hat{i}", color=RED).next_to(vector_a2.get_end(), RIGHT)
        text_a2_j = MathTex("-18\\hat{j}", color=RED).next_to(vector_a2.get_end(), DOWN)
        text_b2_i = MathTex("-4\\hat{i}", color=BLUE).next_to(vector_b2.get_end(), RIGHT)
        text_b2_j = MathTex("12\\hat{j}", color=BLUE).next_to(vector_b2.get_end(), UP)

        # Calcular las fracciones X1/X2 y Y1/Y2
        X1_X2 = a2[0] / b2[0]  # X componente
        Y1_Y2 = a2[1] / b2[1]  # Y componente

        # Crear el texto para las fracciones X1/X2 y Y1/Y2 con los valores reales
        fracciones_texto = MathTex(f"\\frac{{6}}{{-4}} = {X1_X2}", color=WHITE).to_edge(LEFT)
        fracciones_texto_2 = MathTex(f"\\frac{{-18}}{{12}} = {Y1_Y2}", color=WHITE).next_to(fracciones_texto, DOWN)

        # Crear el texto para el producto punto y la pregunta
        producto_punto_ab2 = int(np.dot(a2, b2))
        text_producto_punto2 = MathTex(f"\\mathbf{{(6,-18)}} \\cdot \\mathbf{{(-4,12)}} = {producto_punto_ab2}", color=WHITE)
        
        # Crear los textos en dos líneas para el caso de paralelo/no ortogonal
        texto_pregunta = MathTex("\\text{¿Son paralelos u ortogonales?}", color=WHITE).to_edge(RIGHT)
        texto_respuesta = MathTex("\\text{Sí, es paralelo pero no ortogonal}", color=RED)

        # Colocar los textos en la escena
        text_producto_punto2.to_edge(UP, buff=0.5)
        texto_respuesta.next_to(texto_pregunta, DOWN*1.5)

        # Mostrar los vectores con las etiquetas
        self.play(Create(vector_a2), Write(text_a2_i), Write(text_a2_j))
        self.play(Create(vector_b2), Write(text_b2_i), Write(text_b2_j))

        # Mostrar las fracciones
        self.play(Write(fracciones_texto), Write(fracciones_texto_2))

        # Mostrar el producto punto
        self.play(Write(text_producto_punto2))

        # Mostrar si son paralelos o ortogonales
        self.play(Write(texto_pregunta), Write(texto_respuesta))
                
                # Desvanecer todos los elementos
        self.play(
            FadeOut(vector_a2), FadeOut(vector_b2),
            FadeOut(text_a2_i), FadeOut(text_a2_j),
            FadeOut(text_b2_i), FadeOut(text_b2_j),
            FadeOut(fracciones_texto), FadeOut(fracciones_texto_2),
            FadeOut(text_producto_punto2), FadeOut(texto_pregunta), FadeOut(texto_respuesta)
        )

        # Esperar al final para ver la escena
        self.wait(2)
