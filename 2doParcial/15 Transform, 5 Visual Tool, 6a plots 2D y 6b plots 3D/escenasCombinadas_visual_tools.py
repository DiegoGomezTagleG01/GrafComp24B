from manim import *

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

        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=",       #0
            "f(x)\\frac{d}{dx}g(x)",        #1
            "+",                            #2
            "g(x)\\frac{d}{dx}f(x)"         #3
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff = SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff = SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
            )
        self.wait()
        self.play(
        	ReplacementTransform(brace1,brace2),
        	ReplacementTransform(t1,t2)
        	)
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
         # Cambiar a fondo blanco
        self.cambiar_fondo(RED_E, duracion=2)

        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff = SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff = SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
            )
        self.wait()
        self.play(
        	ReplacementTransform(brace1.copy(),brace2),
        	ReplacementTransform(t1.copy(),t2)
        	)
        self.wait()



        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
         # Cambiar a fondo blanco
        self.cambiar_fondo(GREEN_E, duracion=2)

        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        self.wait()

        # Crear los rectángulos rodeando las partes específicas del texto
        framebox1 = SurroundingRectangle(text[1], buff=0.1, color=YELLOW)
        framebox2 = SurroundingRectangle(text[3], buff=0.1, color=YELLOW)

        # Mostrar el primer rectángulo
        self.play(Create(framebox1))
        self.wait()

        # Reemplazar el primer rectángulo por el segundo
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait()


        # Crear el texto con MathTex
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        self.wait()

        # Crear rectángulos rodeando partes específicas del texto
        framebox1 = SurroundingRectangle(text[1], buff=0.1, color=YELLOW)
        framebox2 = SurroundingRectangle(text[3], buff=0.1, color=YELLOW)

        # Mostrar el primer rectángulo
        self.play(Create(framebox1))  # Usar Create en lugar de ShowCreation
        self.wait()

        # Reemplazar el primer rectángulo por el segundo
        self.play(
            ReplacementTransform(framebox1.copy(), framebox2, path_arc=-np.pi)
        )
        self.wait()



        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(BLUE_D, duracion=2)

        # Crear el texto principal
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        self.wait()

        # Crear los cuadros que rodean los términos
        framebox1 = SurroundingRectangle(text[1], buff=0.1, color=YELLOW)
        framebox2 = SurroundingRectangle(text[3], buff=0.1, color=YELLOW)

        # Crear los términos adicionales (g'f y f'g)
        t1 = MathTex("g'f")
        t2 = MathTex("f'g")

        # Posicionar los términos adicionales
        t1.next_to(framebox1, UP, buff=0.1)
        t2.next_to(framebox2, UP, buff=0.1)

        # Animar el primer cuadro y el término t1
        self.play(
            Create(framebox1),  # Usar Create en lugar de ShowCreation
            FadeIn(t1)
        )
        self.wait()
        # Reemplazar el cuadro y el término
        self.play(
            ReplacementTransform(framebox1.copy(), framebox2),
            ReplacementTransform(t1.copy(), t2),
        )
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(ORANGE, duracion=2)

        step1 = Text("Step 1")
        step2 = Text("Step 2")
        arrow = Arrow(LEFT,RIGHT)
        step1.move_to(LEFT*2)
        arrow.next_to(step1,RIGHT,buff = .1)
        step2.next_to(arrow,RIGHT,buff = .1)
        self.play(Write(step1))
        self.wait()
        self.play(GrowArrow(arrow))
        self.play(Write(step2))
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT*2+DOWN*2)
        step2.move_to(4*RIGHT+2*UP)
        arrow1 = Arrow(step1.get_right(),step2.get_left(),buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Arrow(step1.get_top(),step2.get_bottom(),buff=0.1)
        arrow2.set_color(BLUE)
        self.play(Write(step1),Write(step2))
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(BLUE_C, duracion=2)

        # Crear los textos
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        
        # Posicionar los textos
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(RIGHT * 4 + UP * 2)
        
        # Crear las líneas (flechas)
        arrow1 = Line(step1.get_right(), step2.get_left(), buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1)
        arrow2.set_color(BLUE)
        
        # Animar los textos y flechas
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))  # Usar Create en lugar de ShowCreation
        self.play(Create(arrow2))  # Usar Create en lugar de ShowCreation
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(GOLD_D, duracion=2)

        # Crear los textos
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        
        # Posicionar los textos
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(RIGHT * 4 + UP * 2)
        
        # Crear las líneas (flechas)
        arrow1 = DashedLine(step1.get_right(), step2.get_left(), buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1)
        arrow2.set_color(BLUE)
        
        # Animar los textos y flechas
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))  # Usar Create en lugar de ShowCreation
        self.play(Create(arrow2))  # Usar Create en lugar de ShowCreation
        self.wait()



        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(RED_E, duracion=2)

         # Crear textos
        step1 = Text("Step 1")
        step2 = Text("Step 2")

        # Posicionar textos
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(RIGHT * 4 + UP * 2)

        # Crear flecha en lugar de línea
        arrow = Arrow(step1.get_right(), step2.get_left(), buff=0.1)

        # Animaciones
        self.play(Write(step1), Write(step2))
        self.play(GrowArrow(arrow))  # Animación de crecimiento para la flecha

        # Mover step2 a la izquierda (animación correcta)
        self.play(step2.animate.next_to(step1, LEFT * 2))

        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(RED_E, duracion=2)

       # Crear los textos
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step3 = step2.copy()

        # Posicionar los textos
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(RIGHT * 4 + UP * 2)
        step3.next_to(step2, LEFT * 2)

        # Crear la flecha
        arrow = Arrow(step1.get_right(), step2.get_left(), buff=0.1)
        arrow_copy = Arrow(step1.get_right(), step3.get_bottom(), buff=0.1)

        # Animar los textos y la flecha
        self.play(Write(step1), Write(step2))
        self.play(GrowArrow(arrow))
        self.play(
            ReplacementTransform(step2, step3),
            ReplacementTransform(arrow, arrow_copy)
        )
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
         # Cambiar a fondo blanco
        self.cambiar_fondo(BLACK, duracion=2)



        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)



        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        
        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)







        texto_gracias = Text(
            "Gracias por su atención!! ",
            font_size=32,
            color=WHITE
        )

        self.play(FadeIn(texto_gracias))

        self.wait(5)
        self.play(FadeOut(texto_gracias))
        self.wait(2)
