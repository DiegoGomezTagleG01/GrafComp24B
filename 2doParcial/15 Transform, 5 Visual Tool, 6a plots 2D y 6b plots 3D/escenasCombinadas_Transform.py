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


        texto1 = Text("First text")
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1,texto2))
        self.wait()
        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(RED_E, duracion=2)


        texto1 = Text("First text")
        texto1.to_edge(UP)
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1,texto2))
        self.wait()
        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo( DARK_BLUE,duracion=2)


        text1 = Text("Function")
        text2 = Text("Derivative")
        text3 = Text("Integral")
        text4 = Text("Transformation")
        self.play(Write(text1))
        self.wait()
		#Trans text1 -> text2
        self.play(ReplacementTransform(text1,text2))
        self.wait()
		#Trans text2 -> text3
        self.play(ReplacementTransform(text2,text3))
        self.wait()
		#Trans text3 -> text4
        self.play(ReplacementTransform(text3,text4))
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(DARK_BROWN, duracion=2)

        formula = MathTex(
			"\\frac{d}{dx}", #0
			"(", #1
			"u", #2
			"+", #3
			"v", #4
			")", #5
			"=", #6
			"\\frac{d}{dx}", #7
			"u", #8
			"+", #9
			"\\frac{d}{dx}", #10
			"v" #11
			)
        formula.scale(2)
        self.play(Write(formula[0:7]))
        self.wait()
        self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9])
			)
        self.wait()
        self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10])
			)
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
         # Cambiar a fondo blanco
        self.cambiar_fondo(DARK_GREY, duracion=2)

        formula = MathTex("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
        formula.scale(2)
        self.play(Write(formula[0:7]))
        self.wait()
        self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
        self.wait()
        self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(GOLD_B, duracion=2)

        formula = MathTex("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
        formula.scale(2)
        formula[8].set_color(RED)
        formula[11].set_color(BLUE)
        self.play(Write(formula[0:7]))
        self.wait()
        self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
        self.wait()
        self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(RED_E, duracion=2)


        formula = MathTex("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
        formula.scale(2)
        for letter,color in [("u",RED),("v",BLUE)]:
            formula.set_color_by_tex(letter,color)
            self.play(Write(formula[0:7]))
        self.wait()
        self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
        self.wait()
        self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(ORANGE, duracion=2)

        formula1 = MathTex(
				"\\neg",		#0
				"\\forall",		#1
				"x",			#2
				":",			#3
				"P(x)"			#4
			)
        formula2 = MathTex(
				"\\exists",		#0
				"x",			#1
				":",			#2
				"\\neg",		#3
				"P(x)"			#4
			)
        for size,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
            formula.scale(size)
            formula.move_to(pos)
        self.play(Write(formula1))
        self.wait()
        changes = [
			[(0,1,2,3,4),
			# | | | | |
			# v v v v v
			 (3,0,1,2,4)],
		]
        for pre_ind,post_ind in changes:
            self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
            self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(BLACK, duracion=2)

        formula1 = MathTex(
				"\\neg","\\forall","x",":","P(x)"
			)
        formula2 = MathTex(
				"\\exists","x",":","\\neg","P(x)"
			)
        for tam,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
            formula.scale(tam)
            formula.move_to(pos)
        self.play(Write(formula1))
        self.wait()
        changes = [
			# First time
			[(2,3,4),
			# | | |
			# v v v
			 (1,2,4)],
			# Second time
			[(0,),
			# | 
			# v
			 (3,)],
			# Third time
			[(1,),
			# | 
			# v
			 (0,)]
		]
        for pre_ind,post_ind in changes:
            self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
            self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(GOLD_D, duracion=2)


        formula1 = MathTex(
				"\\neg","\\forall","x",":","P(x)"
			)
        formula2 = MathTex(
				"\\exists","x",":","\\neg","P(x)"
			)
        parametters = [(2,2*UP,formula1,GREEN,"\\forall"),
					  (2,2*DOWN,formula2,ORANGE,"\\exists")]
        for size,pos,formula,col,sim in parametters:
            formula.scale(size)
            formula.move_to(pos)
            formula.set_color_by_tex(sim,col)
            formula.set_color_by_tex("\\neg",PINK)
            self.play(Write(formula1))
        self.wait()
        changes = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
		]
        for pre_ind,post_ind in changes:
            self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
            self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(GREEN_E, duracion=2)


        formula1 = MathTex(
				"\\neg","\\forall","x",":","P(x)"
			)
        formula2 = MathTex(
				"\\exists","x",":","\\neg","P(x)"
			)
        parametters = [(2,2*UP,formula1,GREEN,"\\forall"),
					  (2,2*DOWN,formula2,ORANGE,"\\exists")]
        for size,pos,formula,col,sim in parametters:
            formula.scale(size)
            formula.move_to(pos)
            formula.set_color_by_tex(sim,col)
            formula.set_color_by_tex("\\neg",PINK)
        self.play(Write(formula1))
        self.wait()
        changes = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
		]
        for pre_ind,post_ind in changes:
            self.play(*[
				ReplacementTransform(
					formula1[i],formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
            self.wait()
               

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
         # Cambiar a fondo blanco
        self.cambiar_fondo(DARK_GREY, duracion=2)

        text = Text("Text")
        text.scale(3)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.set_color(YELLOW),  # Utiliza `text.animate` para aplicar un cambio de color
            run_time=2
        )
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
         # Cambiar a fondo blanco
        self.cambiar_fondo(BLACK, duracion=2)

        text = Text("Text")
        text.scale(2)  # Escala inicial
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.scale(3),  # Usa `animate` para animar el escalado
            run_time=2
        )
        self.wait()


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

         # Cambiar a fondo blanco
        self.cambiar_fondo(GREEN_D, duracion=2)

        text = Text("Text")
        text.scale(2)
        text.shift(LEFT * 2)  # Desplazamiento inicial
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.shift(RIGHT * 2),  # Usa `animate` para animar el desplazamiento
            run_time=2,
        )
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
         # Cambiar a fondo blanco
        self.cambiar_fondo(RED_E, duracion=2)

        text = Text("Text")
        text.scale(2)
        text.shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        
        # Animar múltiples transformaciones simultáneamente
        self.play(
            text.animate.shift(RIGHT * 2),  # Animar desplazamiento
            text.animate.scale(2),         # Animar escalado
            text.animate.set_color(RED),   # Animar cambio de color
            run_time=2
        )
        self.wait()

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
         # Cambiar a fondo blanco
        self.cambiar_fondo(ORANGE, duracion=2)







        texto_gracias = Text(
            "Gracias por su atención!! ",
            font_size=32,
            color=WHITE
        )

        self.play(FadeIn(texto_gracias))

        self.wait(5)
        self.play(FadeOut(texto_gracias))
        self.wait(2)
