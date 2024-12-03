from manim import *
from portada import *
from textLikeArray import *


class escenasCombinadas(Scene):
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
        
        # Fondo blanco inicial
        self.camera.background_color = BLACK
        # Final
        self.wait(2)

        text = Tex("A","B","C","D","E","F")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2") #Hexadecimal color
        text[5].set_color(COLOR_P)
        self.play(Write(text))
        self.wait(2)

        # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
        
        text = MathTex("x", "=", "\\frac{a}{b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2][0].set_color(GREEN)  # Colorea el numerador "a"
        text[2][1].set_color(ORANGE)  # Colorea el denominador "-"
        text[2][2].set_color(PURPLE)  # Colorea el denominador "b"

        self.play(Write(text))
        self.wait(2)

         # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
        
        text = MathTex("x","=","\\frac{a}{b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        self.play(Write(text))
        self.wait(2)

         # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
        
        text = MathTex("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(2)

         # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
        

        text = MathTex("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx.}")
        text[0][0].set_color(RED)
        text[0][1].set_color(BLUE)
        
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(3)

 # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
        
        text = MathTex("\\sqrt{", "\\int_", "{a}^", "{b}", "{\\left(", "{x", "\\over", "y}", "\\right)}", "d", "x", ".}")
        colors = [RED, BLUE, GREEN, YELLOW, PINK, ORANGE, PURPLE, MAROON, TEAL, GOLD, GRAY]
        for i, color in enumerate(colors):
            text[i].set_color(color)
        self.play(Write(text))
        self.wait(3)

         # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
        

        text = MathTex("\\sqrt{","\\int_","{a","+","c}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        text[10].set_color(GRAY)
        text[11].set_color(RED)
        self.play(Write(text))
        self.wait(3)

        text = MathTex("\\sqrt{","\\int_","{a","+","c}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        for i,color in zip(text,[PURPLE,BLUE,GREEN,YELLOW,PINK]):
            i.set_color(color)
        self.play(Write(text))
        self.wait(3)

         # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
        
        text = MathTex("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
        text.set_color_by_tex("x", RED)
        self.play(Write(text))
        self.wait(2)
       
         # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
        
        text = MathTex("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
        text.set_color_by_tex("x", RED)
        text[6].set_color(RED)
        text[8].set_color(WHITE)
        self.play(Write(text))
        self.wait(2)

          # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
        
         # Crear un grupo de textos
        text = VGroup(
            *[Text(f"[{i}]") for i in range(8)]
        )
        
        # Posicionar los textos
        text.arrange(RIGHT)
        
        # Cambiar el color de algunos índices
        for i in [0, 1, 3, 4]:
            text[i].set_color(RED)
        
        # Animaciones
        self.play(Write(text))
        self.wait(3)


  # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
        
        # Crear un grupo de textos
        text = VGroup(
            *[Text(f"[{i}]") for i in range(8)]
        )
        
        # Posicionar los textos
        text.arrange(RIGHT)
        
        # Cambiar el color de los primeros tres índices
        for i in range(3):
            text[i].set_color(RED)
        
        # Animaciones
        self.play(Write(text))
        self.wait(3)
          
  # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
       
        # Crear un grupo de textos
        text = VGroup(
            *[Text(f"[{i}]") for i in range(8)]
        )
        
        # Posicionar los textos
        text.arrange(RIGHT)
        
        # Cambiar el color de los índices entre 2 y 5
        for i in range(2, 6):
            text[i].set_color(RED)
        
        # Animaciones
        self.play(Write(text))
        self.wait(3)

        text = VGroup(*[Text(f"[{i}]") for i in range(8)])
        text.arrange(RIGHT)
        for i, color in [(2, RED), (4, PINK)]:
            text[i].set_color(color)
        self.play(Write(text))
        self.wait(3)

        
  # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
       
       # Crear texto matemático
        text = MathTex("\\sum_{i=0}^n i=\\frac{n(n+1)}{2}")
        self.add(text)
        self.wait()
        
        # Escalar el texto
        self.play(text.animate.scale(2))  # Escala por un factor de 2
        self.wait(2)

          # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
       
        
        text = Text("Text or object")
        self.wait()
        self.add(text)
        self.wait(1)
        self.remove()
        self.wait(1)


          # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
        
        text = Text("Text or object")
        self.play(FadeIn(text))
        self.wait()
        self.play(FadeOut(text), run_time=1)
        self.wait()
        
        
          # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)

        # Crear texto
        text = Text("Text or object")
        
        # Aplicar FadeIn con dirección desde abajo
        self.play(FadeIn(text, shift=DOWN), run_time=3)
        
        self.wait()

          # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
       
        text = Text("Text or object")
        self.play(GrowFromCenter(text),run_time=3)
        self.wait()
        
  # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
       
        # Crear un objeto de texto
        text = Text("Text or object")
        
        # Usar la animación Write para mostrar el texto
        self.play(Write(text), run_time=1)
        self.wait()


  # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
           # Crear el texto
        text = Text("Text or object")
        self.add(text)
        self.wait(0.5)

        # Animar el cambio de color letra por letra
        self.play(
            LaggedStart(
                *[ApplyMethod(letter.set_color, YELLOW) for letter in text.submobjects],
                lag_ratio=0.1,  # Controla el retraso entre cada animación
                run_time=5     # Controla la duración total de la animación
            )
        )

        self.wait(0.5)



  # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
       
        # Crear texto con fórmulas matemáticas
        text = MathTex("\\sum_{i=1}^{\\infty}i", "=", "-\\frac{1}{2}")
        
        # Crear la cruz sobre el último elemento del texto
        cross = Cross(text[2])
        cross.set_stroke(RED, 6)
        
        # Animaciones
        self.play(Write(text))
        self.wait(0.5)
        self.play(Create(cross))  # Usar Create para elementos geométricos como Cross
        self.wait(2)


  # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
       
        # Crear texto con fórmulas matemáticas
        text = MathTex("\\sum_{i=1}^{\\infty}i", "=", "-\\frac{1}{2}")
        
        # Seleccionar un grupo que incluye el "=" y "-1/2"
        eq = VGroup(text[1], text[2])
        
        # Crear la cruz sobre el grupo seleccionado
        cross = Cross(eq)
        cross.set_stroke(RED, 6)
        
        # Animaciones
        self.play(Write(text))
        self.wait(0.5)
        self.play(Create(cross))  # Usar Create para Cross
        self.wait(2)

  # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
       

        # Crear texto con una fórmula matemática
        text = MathTex(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        
        # Crear un rectángulo alrededor de un elemento específico
        frameBox = SurroundingRectangle(text[4], buff=0.5 * SMALL_BUFF)
        
        # Animaciones
        self.play(Write(text))
        self.wait(0.5)
        self.play(Create(frameBox))  # Usar Create para el rectángulo
        self.wait(2)

          # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)


        # Crear texto con una fórmula matemática
        text = MathTex(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        
        # Seleccionar un grupo de elementos relacionados
        seleccion = VGroup(text[4], text[5], text[6])
        
        # Crear un rectángulo alrededor del grupo seleccionado
        frameBox = SurroundingRectangle(seleccion, buff=0.5 * SMALL_BUFF)
        frameBox.set_stroke(GREEN, 9)
        
        # Animaciones
        self.play(Write(text))
        self.wait(0.5)
        self.play(Create(frameBox))  # Usar Create para el rectángulo
        self.wait(2)

          # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)
       
        
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace_top = Brace(text[1], UP, buff = SMALL_BUFF)
        brace_bottom = Brace(text[3], DOWN, buff = SMALL_BUFF)
        text_top = brace_top.get_text("$g'f$")
        text_bottom = brace_bottom.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace_top),
            GrowFromCenter(brace_bottom),
            FadeIn(text_top),
            FadeIn(text_bottom)
            )
        self.wait()


  # Añadir el rectángulo negro y animar su opacidad
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
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
