from manim import *
from portada import *
from textFormats import *


class escenasCombinadas(Scene):
    def construct(self):
        # Lista de escenas
        escenas = [
            WriteText,
            AddText,
            TipesOfText,
            TipesOfText2,
            DisplayFormula,
            TextInCenter,
            TextOnTopEdge,
            TextOnBottomEdge,
            TextOnRightEdge,
            TextOnLeftEdge,
            TextInUpperRightCorner,
            TextInLowerLeftCorner,
            CustomPosition1,
            CustomPosition2,
            RelativePosition1,
            RelativePosition2,
            RotateObject,
            MirrorObject,
            SizeTextOnLaTeX,
            TextFonts
        ]
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
        # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        
        # Fondo blanco inicial
        self.camera.background_color = BLACK

        # Final
        self.wait(2)

        text = Text("This is a regular text")
        self.play(Write(text))
        self.wait(3)

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        text = Text("This is a regular text")
        self.add(text)
        self.wait(3)


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        typesOfText = Tex("""
            This is a regular text,
            $this is a formula$,
            $$this is a formula$$
            """)
        self.play(Write(typesOfText))
        self.wait(3)

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        typesOfText = Tex("""
            This is a regular text,
            $\\frac{x}{y}$,
            $$x^2+y^2=a^2$$
            """)
        self.play(Write(typesOfText))
        self.wait(3)


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        typesOfText =Tex("""
            This is a regular text,
            $\\displaystyle\\frac{x}{y}$,
            $$x^2+y^2=a^2$$
            """)
        self.play(Write(typesOfText))
        self.wait(3)


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
        text = Text("Text")
        self.play(Write(text))
        self.wait(3)


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        text = Text("Text")
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(3)

        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
        text = Text("Text")
        text.to_edge(DOWN)
        self.play(Write(text))
        self.wait(3)


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
        text = Text("Text")
        text.to_edge(RIGHT)
        self.play(Write(text))
        self.wait(3)


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
        text = Text("Text")
        text.to_edge(LEFT)
        self.play(Write(text))
        self.wait(3)


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
        text = Text("Text")
        text.to_edge(UP+RIGHT)
        self.play(Write(text))
        self.wait(3)


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)
        text = Text("Text") 
        text.to_edge(LEFT+DOWN)
        self.play(Write(text))
        self.wait(3)


        # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        textM = Text("Text")
        textC = Text("Central text")
        textM.move_to(0.25*UP) 
        self.play(Write(textM),Write(textC))
        self.wait(3)


         # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        textM = Text("Text")
        textC = Text("Central text")
        textM.move_to(1*UP+1*RIGHT)
        self.play(Write(textM),Write(textC))
        self.wait(1)
        textM.move_to(1*UP+1*RIGHT) 
        self.play(Write(textM))
        self.wait(3)


         # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        textM = Text("Text")
        textC = Text("Reference text")
        textM.next_to(textC,LEFT,buff=1) 
        self.play(Write(textM),Write(textC))
        self.wait(3)

         # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        textM = Text("Text")
        textC = Text("Reference text")
        textM.shift(UP*0.1)
        self.play(Write(textM),Write(textC))
        self.wait(3)

         # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        textM = Text("Text")
        textC = Text("Reference text")
        textM.shift(UP)
        textM.rotate(PI/4) 
        self.play(Write(textM),Write(textC))
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI)
        self.wait(2)
         # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        textM = Text("Text")
        textM.flip(UP)
        self.play(Write(textM))
        self.wait(2)
         # Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        textHuge = Tex("{\\Huge Huge Text 012.\\#!?} Text")
        texthuge = Tex("{\\huge huge Text 012.\\#!?} Text")
        textLARGE = Tex("{\\LARGE LARGE Text 012.\\#!?} Text")
        textLarge = Tex("{\\Large Large Text 012.\\#!?} Text")
        textlarge = Tex("{\\large large Text 012.\\#!?} Text")
        textNormal = Tex("{\\normalsize normal Text 012.\\#!?} Text")
        textsmall = Tex("{\\small small Text 012.\\#!?} Texto normal")
        textfootnotesize = Tex("{\\footnotesize footnotesize Text 012.\\#!?} Text")
        textscriptsize = Tex("{\\scriptsize scriptsize Text 012.\\#!?} Text")
        texttiny = Tex("{\\tiny tiny Texto 012.\\#!?} Text normal")
        textHuge.to_edge(UP)
        texthuge.next_to(textHuge,DOWN,buff=0.1)
        textLARGE.next_to(texthuge,DOWN,buff=0.1)
        textLarge.next_to(textLARGE,DOWN,buff=0.1)
        textlarge.next_to(textLarge,DOWN,buff=0.1)
        textNormal.next_to(textlarge,DOWN,buff=0.1)
        textsmall.next_to(textNormal,DOWN,buff=0.1)
        textfootnotesize.next_to(textsmall,DOWN,buff=0.1)
        textscriptsize.next_to(textfootnotesize,DOWN,buff=0.1)
        texttiny.next_to(textscriptsize,DOWN,buff=0.1)
        self.add(textHuge,texthuge,textLARGE,textLarge,textlarge,textNormal,textsmall,textfootnotesize,textscriptsize,texttiny)
        self.wait(3)
# Limpiar los objetos para la próxima escena
        self.remove(*self.mobjects)

        textNormal = Tex("{Roman serif text 012.\\#!?} Text")
        textItalic = Tex("\\textit{Italic text 012.\\#!?} Text")
        textTypewriter = Tex("\\texttt{Typewritter text 012.\\#!?} Text")
        textBold = Tex("\\textbf{Bold text 012.\\#!?} Text")
        textSL = Tex("\\textsl{Slanted text 012.\\#!?} Text")
        textSC = Tex("\\textsc{Small caps text 012.\\#!?} Text")
        textNormal.to_edge(UP)
        textItalic.next_to(textNormal,DOWN,buff=.5)
        textTypewriter.next_to(textItalic,DOWN,buff=.5)
        textBold.next_to(textTypewriter,DOWN,buff=.5)
        textSL.next_to(textBold,DOWN,buff=.5)
        textSC.next_to(textSL,DOWN,buff=.5)
        self.add(textNormal,textItalic,textTypewriter,textBold,textSL,textSC)
        self.wait(3)







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
