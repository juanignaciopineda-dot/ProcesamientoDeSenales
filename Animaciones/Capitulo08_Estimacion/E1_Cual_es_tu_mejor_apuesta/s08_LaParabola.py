"""Escena 08 — La parábola de las apuestas: el fondo está en la media (3,5) y vale la varianza (2,92)."""
from comun.escena import *


class LaParabola(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.dibujo()
        self.sorpresa()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def dibujo(self):
        P = ParabolaApuestas8(centro=(-0.6, -0.1), ancho=8.6, alto=4.6)
        nums = VGroup(*[Text(str(k), color=INK).scale(0.45).move_to(P.xy(k, 0) + DOWN * 0.3) for k in range(1, 7)])
        x_et = Text("Apuesta", color=INK, weight=BOLD).scale(0.6).move_to(P.xy(P.A1, 0) + DOWN * 0.75 + LEFT * 1.0)
        y_et = Text("Error cuadrático medio", color=INK, weight=BOLD).scale(0.6).move_to(P.xy(P.A0, P.EMAX) + UP * 0.35 + RIGHT * 1.6)
        valores = [(1, "9,17"), (3, "3,17"), (4, "3,17"), (3.5, "2,92")]
        pts = {a: P.punto(a, AZUL) for a, _ in valores}
        etq = {}
        for a, t in valores:
            etq[a] = Text(t, color=TXT).scale(0.5)
            if a == 3.5:
                etq[a].move_to(pts[a].get_center() + DOWN * 0.95 + RIGHT * 0.5)
            elif a == 1:
                etq[a].next_to(pts[a], LEFT, buff=0.15)
            else:
                etq[a].move_to(pts[a].get_center() + DOWN * 0.4 + (LEFT if a == 3 else RIGHT) * 0.35)
        v = pts[3.5]
        guia = DashedLine(P.p(3.5), P.xy(3.5, 0), color=VERDE, stroke_width=3)
        t35 = Text("3,5", color=VERDE, weight=BOLD).scale(0.6).move_to(P.xy(3.5, 0) + DOWN * 0.3)
        media = Text("Media = 3,5", color=ESTIMACION, weight=BOLD).scale(0.9).move_to([5.0, 1.6, 0])
        cap7 = Text("Capítulo 7", color=INK, weight=BOLD).scale(0.6).move_to([5.0, 0.9, 0])

        with self.narrar("b1"):
            # «en un dibujo»
            self.en("dibujo")
            self.play(Create(P.eje_x), Create(P.eje_y), FadeIn(nums), run_time=self.dur(0.8))

            # «en horizontal, la apuesta»
            self.en("horiz")
            self.play(FadeIn(x_et), run_time=self.dur(0.4))

            # «en vertical»
            self.en("vert")
            self.play(FadeIn(y_et), run_time=self.dur(0.4))

            # «Los puntos»
            self.en("puntos")
            for a, _ in valores:
                self.play(FadeIn(pts[a], shift=DOWN * 0.4), FadeIn(etq[a]), run_time=self.dur(0.4))

            # «una curva en forma de U»
            self.en("u")
            self.play(Create(P.curva), run_time=self.dur(1.4))

            # «su punto más bajo»
            self.en("bajo")
            self.play(v.animate.set_color(VERDE).scale(1.4), run_time=self.dur(0.4))

            # «justo en tres coma cinco»
            self.en("tres5")
            self.play(Create(guia), FadeIn(t35), run_time=self.dur(0.5))

            # «es la media del dado»
            self.en("media")
            self.pop(media)

            # «capítulo siete»
            self.en("capsiete")
            self.play(FadeIn(cap7, shift=UP * 0.1), run_time=self.dur(0.5))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def sorpresa(self):
        M = Mesa8(y_regla=0.2)
        t35 = Text("3,5", color=ESTIMACION, weight=BOLD).scale(1.3).move_to(M.p(3.5) + DOWN * 1.3)
        f35 = Arrow(t35.get_top() + UP * 0.03, M.p(3.5) + DOWN * 0.08, buff=0, color=ESTIMACION, stroke_width=5)
        x35 = cruz(ROJO, 1.3).move_to(t35)
        acertar = Text("Acertar", color=INK, weight=BOLD).scale(1.0).move_to([-4.2, -2.9, 0])
        tach = Line(acertar.get_left() + LEFT * 0.1, acertar.get_right() + RIGHT * 0.1, color=ROJO, stroke_width=7)
        poco = Text("Equivocarse poco, en promedio", color=VERDE, weight=BOLD).scale(0.85).move_to([2.0, -2.9, 0])

        P = ParabolaApuestas8(centro=(-0.6, -0.1), ancho=8.6, alto=4.6)
        v = Dot(P.p(3.5), radius=0.15, color=VERDE)
        fondo = DashedLine(P.p(3.5), P.xy(P.A0, P.SUELO), color=ESTIMACION, stroke_width=4)
        n292 = Text("2,92", color=ESTIMACION, weight=BOLD).scale(0.7).next_to(P.xy(P.A0, P.SUELO), LEFT, buff=0.15)
        suena = Text("¿Te suena?", color=INK, weight=BOLD).scale(0.9).move_to([5.0, 2.0, 0])
        var = Text("Varianza del dado = 2,92", color=ESTIMACION, weight=BOLD).scale(0.8).move_to([3.4, 3.2, 0])
        casual = Text("¿Casualidad?", color=ESTIMACION, weight=BOLD).scale(1.0).move_to([4.4, -0.5, 0])
        tach2 = Line(casual.get_left() + LEFT * 0.1, casual.get_right() + RIGHT * 0.1, color=ROJO, stroke_width=7)
        demos = Text("Lo demostramos", color=VERDE, weight=BOLD).scale(0.8).move_to([4.4, -1.4, 0])

        with self.narrar("b2"):
            # «la sorpresa»
            self.en("sorpresa")
            self.corte()
            self.play(FadeIn(M), FadeIn(f35), run_time=self.dur(0.8))
            self.pop(t35)

            # «no saca nunca»
            self.en("nunca")
            self.sfx("error")
            self.play(FadeIn(x35, scale=1.6), run_time=self.dur(0.4))

            # «No buscamos acertar»
            self.en("acertar")
            self.play(FadeIn(acertar), run_time=self.dur(0.4))
            self.play(Create(tach), run_time=self.dur(0.3))

            # «equivocarnos lo menos posible en promedio»
            self.en("promedio")
            self.play(FadeIn(poco, shift=UP * 0.1), run_time=self.dur(0.6))

            # «el error que queda en el fondo»
            self.en("fondo")
            self.corte()
            self.add(P.eje_x, P.eje_y, P.curva, v)
            self.play(Create(fondo), FadeIn(n292), run_time=self.dur(0.8))

            # «también te sonará»
            self.en("sonara")
            self.pop(suena)

            # «es la varianza del dado»
            self.en("varianza")
            self.pop(var)

            # «¿Casualidad?»
            self.en("casualidad")
            self.pop(casual)

            # «demostrar que no»
            self.en("demostrar")
            self.play(Create(tach2), run_time=self.dur(0.3))
            self.play(FadeIn(demos, shift=UP * 0.1), run_time=self.dur(0.5))
