from manim import *

class ShowArc(Scene):
    def construct(self):
        mi_nombre = Text("Diego Gomez Tagle Gonzalez", font_size=24)
        mi_nombre.to_corner(DOWN + RIGHT)

        # Añadir el nombre a la escena
        self.add(mi_nombre)
        arco = Arc(radius=1, color=BLUE)
        nombre = Text("Arc").scale(0.5)
        nombre.next_to(arco, DOWN)
        self.play(Create(arco))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer el arco y el nombre
        self.play(FadeOut(arco), FadeOut(nombre))
        arco = ArcBetweenPoints(start=LEFT, end=RIGHT, color=GREEN)
        nombre = Text("ArcBetweenPoints").scale(0.5)
        nombre.next_to(arco, DOWN)
        
        # Mostrar el arco y su nombre
        self.play(Create(arco))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer el arco y el nombre
        self.play(FadeOut(arco), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        # Crear una flecha curva entre dos puntos
        flecha_curva = CurvedArrow(start_point=LEFT, end_point=RIGHT, color=RED)
        
        # Posicionar el nombre debajo de la flecha
        nombre = Text("CurvedArrow").scale(0.5)
        nombre.next_to(flecha_curva, DOWN)
        
        # Mostrar la flecha curva y su nombre
        self.play(Create(flecha_curva))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer la flecha y el nombre
        self.play(FadeOut(flecha_curva), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
         # Crear una flecha curva doble entre dos puntos
        flecha_curva_doble = CurvedDoubleArrow(start_point=LEFT, end_point=RIGHT, color=YELLOW)
        
        # Posicionar el nombre debajo de la flecha curva doble
        nombre = Text("CurvedDoubleArrow").scale(0.5)
        nombre.next_to(flecha_curva_doble, DOWN)
        
        # Mostrar la flecha curva doble y su nombre
        self.play(Create(flecha_curva_doble))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer la flecha curva doble y el nombre
        self.play(FadeOut(flecha_curva_doble), FadeOut(nombre))

        #----------------------------------------------------------------------------------------------------------------------------------------#
        
         # Crear un círculo de color morado
        circulo = Circle(color=PURPLE, fill_opacity=0.5)
        
        # Posicionar el nombre debajo del círculo
        nombre = Text("Circle").scale(0.5)
        nombre.next_to(circulo, DOWN)
        
        # Mostrar el círculo y su nombre
        self.play(Create(circulo))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer el círculo y el nombre
        self.play(FadeOut(circulo), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear un punto de color rosa
        punto = Dot(color=PINK)
        
        # Posicionar el nombre debajo del punto
        nombre = Text("Dot").scale(0.5)
        nombre.next_to(punto, DOWN)
        
        # Mostrar el punto y su nombre
        self.play(Create(punto))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer el punto y el nombre
        self.play(FadeOut(punto), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
         # Crear un punto pequeño de color azul claro
        punto_pequeño = Dot(color="#ADD8E6").scale(0.5)  # Usamos un código hexadecimal para azul claro
        
        # Posicionar el nombre debajo del punto pequeño
        nombre = Text("SmallDot").scale(0.5)
        nombre.next_to(punto_pequeño, DOWN)
        
        # Mostrar el punto pequeño y su nombre
        self.play(Create(punto_pequeño))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer el punto pequeño y el nombre
        self.play(FadeOut(punto_pequeño), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
         # Crear una elipse con color naranja
        elipse = Ellipse(width=3, height=1.5, color=ORANGE, fill_opacity=0.5)
        
        # Posicionar el nombre debajo de la elipse
        nombre = Text("Ellipse").scale(0.5)
        nombre.next_to(elipse, DOWN)
        
        # Mostrar la elipse y su nombre
        self.play(Create(elipse))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer la elipse y el nombre
        self.play(FadeOut(elipse), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear un sector anular con radio interior y exterior
        sector_anular = AnnularSector(inner_radius=0.5, outer_radius=1, color=WHITE)
        
        # Posicionar el nombre debajo del sector anular
        nombre = Text("AnnularSector").scale(0.5)
        nombre.next_to(sector_anular, DOWN)
        
        # Mostrar el sector anular y su nombre
        self.play(Create(sector_anular))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer el sector anular y el nombre
        self.play(FadeOut(sector_anular), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
         # Crear un sector circular con color dorado
        sector = Sector(color=GOLD, fill_opacity=0.5)
        
        # Posicionar el nombre debajo del sector
        nombre = Text("Sector").scale(0.5)
        nombre.next_to(sector, DOWN)
        
        # Mostrar el sector y su nombre
        self.play(Create(sector))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer el sector y el nombre
        self.play(FadeOut(sector), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear un anillo con radio interior y exterior
        anillo = Annulus(inner_radius=0.5, outer_radius=1.5, color=TEAL, fill_opacity=0.5)
        
        # Posicionar el nombre debajo del anillo
        nombre = Text("Annulus").scale(0.5)
        nombre.next_to(anillo, DOWN)
        
        # Mostrar el anillo y su nombre
        self.play(Create(anillo))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer el anillo y el nombre
        self.play(FadeOut(anillo), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear una línea de color azul que va de izquierda a derecha
        linea = Line(start=LEFT, end=RIGHT, color=BLUE)
        
        # Posicionar el nombre debajo de la línea
        nombre = Text("Line").scale(0.5)
        nombre.next_to(linea, DOWN)
        
        # Mostrar la línea y su nombre
        self.play(Create(linea))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer la línea y el nombre
        self.play(FadeOut(linea), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear una línea discontinua de color rojo que va de izquierda a derecha
        linea_discontinua = DashedLine(start=LEFT, end=RIGHT, color=RED)
        
        # Posicionar el nombre debajo de la línea discontinua
        nombre = Text("DashedLine").scale(0.5)
        nombre.next_to(linea_discontinua, DOWN)
        
        # Mostrar la línea discontinua y su nombre
        self.play(Create(linea_discontinua))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer la línea discontinua y el nombre
        self.play(FadeOut(linea_discontinua), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear un círculo para la tangente
        circulo = Circle(color=BLUE)

        # Crear una línea tangente al círculo en un punto
        linea_tangente = TangentLine(circulo, alpha=0.5, length=3, color=GREEN)
        
        # Posicionar el nombre debajo de la línea tangente
        nombre = Text("TangentLine").scale(0.5)
        nombre.next_to(linea_tangente, DOWN)
        
        # Mostrar el círculo, la línea tangente y su nombre
        self.play(Create(circulo))
        self.play(Create(linea_tangente))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer el círculo, la línea tangente y el nombre
        self.play(FadeOut(circulo), FadeOut(linea_tangente), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear un "codo" o ángulo de color naranja
        codo = Elbow(color=ORANGE)
        
        # Posicionar el nombre debajo del codo
        nombre = Text("Elbow").scale(0.5)
        nombre.next_to(codo, DOWN)
        
        # Mostrar el codo y su nombre
        self.play(Create(codo))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer el codo y el nombre
        self.play(FadeOut(codo), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear una flecha de color amarillo que va de izquierda a derecha
        flecha = Arrow(start=LEFT, end=RIGHT, color=YELLOW)
        
        # Posicionar el nombre debajo de la flecha
        nombre = Text("Arrow").scale(0.5)
        nombre.next_to(flecha, DOWN)
        
        # Mostrar la flecha y su nombre
        self.play(Create(flecha))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer la flecha y el nombre
        self.play(FadeOut(flecha), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear un vector de color púrpura que va hacia la derecha
        vector = Vector(direction=RIGHT, color=PURPLE)
        
        # Posicionar el nombre debajo del vector
        nombre = Text("Vector").scale(0.5)
        nombre.next_to(vector, DOWN)
        
        # Mostrar el vector y su nombre
        self.play(Create(vector))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer el vector y el nombre
        self.play(FadeOut(vector), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear una flecha doble de color turquesa que va de izquierda a derecha
        flecha_doble = DoubleArrow(start=LEFT, end=RIGHT, color=TEAL)
        
        # Posicionar el nombre debajo de la flecha doble
        nombre = Text("DoubleArrow").scale(0.5)
        nombre.next_to(flecha_doble, DOWN)
        
        # Mostrar la flecha doble y su nombre
        self.play(Create(flecha_doble))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca
        
        # Desvanecer la flecha doble y el nombre
        self.play(FadeOut(flecha_doble), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear un polígono de 3 vértices (triángulo) de color verde, usando 3 dimensiones
        poligono = Polygon(
            np.array([-1, 0, 0]),  # Coordenada (x, y, z)
            np.array([1, 0, 0]),   # Coordenada (x, y, z)
            np.array([0, 1, 0]),   # Coordenada (x, y, z)
            color=GREEN
        )

        # Posicionar el nombre debajo del polígono
        nombre = Text("Polygon").scale(0.5)
        nombre.next_to(poligono, DOWN)

        # Mostrar el polígono y su nombre
        self.play(Create(poligono))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca

        # Desvanecer el polígono y el nombre
        self.play(FadeOut(poligono), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
         # Crear un polígono regular con 5 lados de color púrpura y relleno
        poligono_regular = RegularPolygon(n=5, color=PURPLE, fill_opacity=0.5)

        # Posicionar el nombre debajo del polígono regular
        nombre = Text("RegularPolygon").scale(0.5)
        nombre.next_to(poligono_regular, DOWN)

        # Mostrar el polígono regular y su nombre
        self.play(Create(poligono_regular))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca

        # Desvanecer el polígono regular y el nombre
        self.play(FadeOut(poligono_regular), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
         # Crear un triángulo de color amarillo y relleno
        triangulo = Triangle(color=YELLOW, fill_opacity=0.5)

        # Posicionar el nombre debajo del triángulo
        nombre = Text("Triangle").scale(0.5)
        nombre.next_to(triangulo, DOWN)

        # Mostrar el triángulo y su nombre
        self.play(Create(triangulo))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca

        # Desvanecer el triángulo y el nombre
        self.play(FadeOut(triangulo), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
          # Crear una punta de flecha triangular de color blanco
        arrow_tip = ArrowTriangleTip(color=WHITE)

        # Posicionar el nombre debajo de la punta de flecha
        nombre = Text("ArrowTriangleTip").scale(0.5)
        nombre.next_to(arrow_tip, DOWN)

        # Mostrar la punta de flecha y su nombre
        self.play(Create(arrow_tip))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca

        # Desvanecer la punta de flecha y el nombre
        self.play(FadeOut(arrow_tip), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
         # Crear un rectángulo de color azul con relleno
        rectangle = Rectangle(color=BLUE, fill_opacity=0.5)

        # Posicionar el nombre debajo del rectángulo
        nombre = Text("Rectangle").scale(0.5)
        nombre.next_to(rectangle, DOWN)

        # Mostrar el rectángulo y su nombre
        self.play(Create(rectangle))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca

        # Desvanecer el rectángulo y el nombre
        self.play(FadeOut(rectangle), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear un cuadrado de color rojo con relleno
        square = Square(color=RED, fill_opacity=0.5)

        # Posicionar el nombre debajo del cuadrado
        nombre = Text("Square").scale(0.5)
        nombre.next_to(square, DOWN)

        # Mostrar el cuadrado y su nombre
        self.play(Create(square))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca

        # Desvanecer el cuadrado y el nombre
        self.play(FadeOut(square), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        # Crear un rectángulo con esquinas redondeadas de color azul con relleno
        rounded_rectangle = RoundedRectangle(color=BLUE, fill_opacity=0.5)

        # Posicionar el nombre debajo del rectángulo con esquinas redondeadas
        nombre = Text("RoundedRectangle").scale(0.5)
        nombre.next_to(rounded_rectangle, DOWN)

        # Mostrar el rectángulo con esquinas redondeadas y su nombre
        self.play(Create(rounded_rectangle))
        self.play(Write(nombre))
        self.wait(2)  # Esperar 2 segundos antes de que desaparezca

        # Desvanecer el rectángulo y el nombre
        self.play(FadeOut(rounded_rectangle), FadeOut(nombre))
        
        #----------------------------------------------------------------------------------------------------------------------------------------#
        
        self.play(FadeOut(mi_nombre))