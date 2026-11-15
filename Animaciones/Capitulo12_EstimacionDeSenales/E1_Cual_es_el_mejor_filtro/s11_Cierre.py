"""Escena 11 — Cierre: resumen y anuncio del episodio 2, «Lo que sabe el pasado»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        t, y, v, x = sensor12(40)
        resumen = self.palabra("resumen", AMBAR, 0.9).move_to([0, 3.3, 0])
        F, r = flechas_xy(origen=(-5.6, -1.6), largo=3.0, angulo=50)
        L = Lienzo(ancho=4.6, alto=1.2, t_rango=(0, 39), v_max=7, centro=(3.6, 2.0))
        curva = L.curva(t, x, MEDIDA, 3.0)
        a, b = L.p(22, 0), L.p(26, 0)
        vent = Rectangle(width=abs(b[0] - a[0]), height=1.4, stroke_width=2, color=AMBAR).set_fill(AMBAR, 0.25)
        vent.move_to([(a[0] + b[0]) / 2, 2.0, 0])
        M = MatrizT([["5", "2,4", "1,44"], ["2,4", "5", "2,4"], ["1,44", "2,4", "5"]],
                    centro=(2.0, -0.4), lado=1.2, escala=0.6)
        for k, c in enumerate([AMBAR, CIAN, VERDE]):
            M.diag(k).set_color(c)
        circs = VGroup(*[Circle(radius=0.13, color=AMBAR, stroke_width=3).move_to(L.p(k, x[k])) for k in (24, 25, 26)])
        # las barras del error
        base_y, esc = -3.0, 0.7
        eje = Line([-4.6, base_y, 0], [4.6, base_y, 0], color=INK, stroke_width=2)

        def barra(valor, cx):
            rr = Rectangle(width=1.3, height=valor * esc, stroke_width=0).set_fill(ERROR, 0.85)
            return rr.move_to([cx, base_y + valor * esc / 2, 0])
        barras = [barra(4.0, -3.6), barra(0.8, -1.8), barra(0.74, 0.0)]
        puntos = Text("· · ·", color=INK, weight=BOLD).scale(1.0).move_to([5.6, base_y + 0.5, 0])
        interr = Text("?", color=AMBAR, weight=BOLD).scale(1.6).move_to([2.7, base_y + 1.6, 0])
        # el dato que no se parece
        o = np.array([-1.6, -1.8, 0.0])
        fy = flecha_c(o, 3.2, 90, SENAL, 6)
        fz = flecha_c(o, 3.2, 0, INK, 6)
        ly = MathTex("y", color=SENAL).scale(0.9).move_to(o + UP * 3.6)
        lz = MathTex("z", color=INK).scale(0.9).move_to(o + RIGHT * 3.6)
        recto = Square(0.3, color=AMBAR, stroke_width=3).move_to(o + UR * 0.15)
        pregunta = Text("¿sirve?", color=AMBAR, weight=BOLD).scale(0.8).move_to([3.8, 0.3, 0])
        tarjeta = caja("Episodio 2", AMBAR, ancho=3.4, alto=0.9, scale=0.6).move_to([0, 2.4, 0])
        titulo_p = self.palabra("Lo que sabe el pasado", TXT, 1.2).move_to([0, 0.2, 0])

        with self.narrar("b1"):
            # «Resumimos»
            self.en("resumen")
            self.pop(resumen)

            # «deja el error perpendicular»
            self.en("perp")
            self.play(Create(F.presente), Create(F.futuro), Create(F.sombra), Create(F.error), Create(F.recto),
                      FadeIn(r["x"]), FadeIn(r["y"]), FadeIn(r["yh"]), FadeIn(r["e"]), run_time=self.dur(1.2))

            # «todo lo que ve»
            self.en("ve")
            self.play(Create(curva), FadeIn(vent), run_time=self.dur(0.8))

            # «una matriz de Toeplitz»
            self.en("toep")
            self.play(FadeIn(M), run_time=self.dur(0.7))

            # «Con tres muestras»
            self.en("tres")
            self.play(Create(circs), run_time=self.dur(0.4))

            # «baja de cuatro a cero coma siete cuatro»
            self.en("baja")
            self.corte()
            self.play(Create(eje), *[GrowFromEdge(b, DOWN) for b in barras], run_time=self.dur(1.2))

            # «¿hasta dónde baja»
            self.en("hasta")
            self.play(FadeIn(puntos), FadeIn(interr), run_time=self.dur(0.5))

            # «seguimos añadiendo muestras»
            self.en("mas")
            extras = [barra(0.7386, 1.8), barra(0.7386, 3.6)]
            self.play(*[GrowFromEdge(b, DOWN) for b in extras], run_time=self.dur(0.8))

            # «un dato que no se parece a lo que buscamos»
            self.en("dato")
            self.corte()
            self.play(GrowArrow(fy), GrowArrow(fz), FadeIn(ly), FadeIn(lz), Create(recto), run_time=self.dur(0.8))
            self.pop(pregunta)

            # «el próximo episodio»
            self.en("proximo")
            self.corte()
            self.pop(tarjeta)

            # «lo que sabe el pasado»
            self.en("titulo")
            self.pop(titulo_p)
        self.wait(1.0)
        self.limpiar()
