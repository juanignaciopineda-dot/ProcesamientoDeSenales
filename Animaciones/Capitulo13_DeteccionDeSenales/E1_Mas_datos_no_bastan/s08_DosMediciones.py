"""Escena 08 — Dos mediciones: la densidad conjunta es un cuadrado y la regla es la misma."""
from comun.escena import *


class DosMediciones(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.P = Plano2(centro=(-3.0, -0.3), u=1.7)
        self.conjunta()
        self.regla()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def conjunta(self):
        P = self.P
        # las densidades de antes, como bandas pegadas a cada eje
        b0x = Rectangle(width=2 * P.u, height=0.22, color=RUIDO, fill_color=RUIDO, fill_opacity=0.5,
                        stroke_width=2).move_to(P.p(0, 0) + DOWN * 0.11)
        b1x = Rectangle(width=P.u, height=0.4, color=SENAL, fill_color=SENAL, fill_opacity=0.5,
                        stroke_width=2).move_to(P.p(0, 0) + DOWN * 0.2)
        b0y = Rectangle(width=0.22, height=2 * P.u, color=RUIDO, fill_color=RUIDO, fill_opacity=0.5,
                        stroke_width=2).move_to(P.p(0, 0) + LEFT * 0.11)
        b1y = Rectangle(width=0.4, height=P.u, color=SENAL, fill_color=SENAL, fill_opacity=0.5,
                        stroke_width=2).move_to(P.p(0, 0) + LEFT * 0.2)
        bandas = VGroup(b0x, b1x, b0y, b1y)
        perp = MathTex(r"\perp", color=AMBAR).scale(1.9).move_to(P.p(1.25, 1.25))
        prod = formula(r"f(r_1,r_2)", "=", "f(r_1)", r"\cdot", "f(r_2)", escala=1.15).move_to([3.9, 3.1, 0])
        t_h0 = MathTex("H_0", color=RUIDO).scale(1.3).move_to(P.p(-1.4, 1.25))
        t_h1 = MathTex("H_1", color=SENAL).scale(1.2).move_to(P.p(-0.66, 0.66))
        n0a = MathTex(r"\text{lado }2\Rightarrow\text{área }4", color=RUIDO).scale(1.05).move_to([4.0, 1.8, 0])
        n0h = MathTex(r"\text{altura}=\tfrac14", color=RUIDO).scale(1.2).move_to([4.0, 0.9, 0])
        n1a = MathTex(r"\text{lado }1\Rightarrow\text{área }1", color=SENAL).scale(1.05).move_to([4.0, -0.3, 0])
        n1h = MathTex(r"\text{altura}=1", color=SENAL).scale(1.2).move_to([4.0, -1.2, 0])
        self.paneles = VGroup(prod, n0a, n0h, n1a, n1h, perp, t_h0, t_h1, bandas)

        with self.narrar("b1"):
            # «dos mediciones independientes»
            self.en("dos")
            self.corte()
            self.play(FadeIn(P.ejes), FadeIn(P.rot1), FadeIn(P.rot2), run_time=self.dur(0.5))
            self.play(FadeIn(bandas), run_time=self.dur(0.5))

            # «las mismas reglas de antes»
            self.en("reglas")
            self.play(bandas.animate(rate_func=there_and_back).set_stroke(AMBAR, 5), run_time=self.dur(0.7))

            # «Como son independientes»
            self.en("indep")
            self.pop(perp)

            # «la densidad conjunta es el producto»
            self.en("producto")
            self.play(*[FadeIn(prod[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(1.0))

            # «Bajo la hipótesis cero»
            self.en("bajoh0")
            self.play(FadeIn(P.grande, scale=0.6), FadeIn(t_h0), run_time=self.dur(0.7))

            # «de área cuatro»
            self.en("a4")
            self.play(FadeIn(n0a, shift=UP * 0.1), run_time=self.dur(0.5))

            # «su altura es un cuarto»
            self.en("alto14")
            self.play(FadeIn(n0h, shift=UP * 0.1), run_time=self.dur(0.5))

            # «Bajo la hipótesis uno»
            self.en("bajoh1")
            self.play(FadeIn(P.pequeno, scale=0.6), FadeIn(t_h1), run_time=self.dur(0.7))

            # «de área uno»
            self.en("a1")
            self.play(FadeIn(n1a, shift=UP * 0.1), run_time=self.dur(0.5))

            # «su altura es uno»
            self.en("alto1")
            self.play(FadeIn(n1h, shift=UP * 0.1), run_time=self.dur(0.5))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def regla(self):
        P = self.P
        base_y = -3.4
        esc = 13.0
        suelo = Line([2.2, base_y, 0], [6.8, base_y, 0], color=INK, stroke_width=2)
        bar0 = barra_v(3.4, base_y, 3 / 16 * esc, ancho=1.2, color=RUIDO)
        bar1 = barra_v(5.6, base_y, 4 / 16 * esc, ancho=1.2, color=SENAL)
        x_p0 = MathTex(r"\times\,p_0", color=RUIDO).scale(1.1).move_to(P.p(1.6, 0.8))
        x_p1 = MathTex(r"\times\,p_1", color=SENAL).scale(1.1).move_to(P.p(1.6, -0.6))
        c0 = MathTex(r"\tfrac34\cdot\tfrac14", color=RUIDO).scale(1.25).move_to([3.4, 3.0, 0])
        d3 = MathTex(r"=\tfrac{3}{16}", color=RUIDO).scale(1.25).move_to([3.4, 1.9, 0])
        c1 = MathTex(r"\tfrac14\cdot 1", color=SENAL).scale(1.25).move_to([5.6, 3.0, 0])
        d4 = MathTex(r"=\tfrac{4}{16}", color=SENAL).scale(1.25).move_to([5.6, 1.9, 0])
        mayor = MathTex(r"4>3", color=AMBAR).scale(1.5).move_to([4.5, 0.9, 0])
        lab1 = MathTex(r"\text{decido }H_1", color=SENAL).scale(1.0).move_to(P.p(-1.0, -1.75))
        lab0 = MathTex(r"\text{decido }H_0", color=INK).scale(1.0).move_to(P.p(1.0, -1.75))

        with self.narrar("b2"):
            # «escalar por el a priori»
            self.en("escalar")
            self.play(FadeOut(self.paneles), run_time=0.3)
            self.play(FadeIn(x_p0), FadeIn(x_p1), run_time=self.dur(0.5))

            # «y comparar»
            self.en("comparar")
            self.play(Create(suelo), run_time=self.dur(0.4))

            # «tres cuartos por un cuarto»
            self.en("c0")
            self.play(FadeIn(c0, shift=UP * 0.1), run_time=self.dur(0.6))

            # «tres dieciseisavos»
            self.en("d3")
            self.play(FadeIn(d3), GrowFromEdge(bar0, DOWN), run_time=self.dur(0.7))

            # «un cuarto por uno»
            self.en("c1")
            self.play(FadeIn(c1, shift=UP * 0.1), run_time=self.dur(0.6))

            # «cuatro dieciseisavos»
            self.en("d4")
            self.play(FadeIn(d4), GrowFromEdge(bar1, DOWN), run_time=self.dur(0.7))

            # «Cuatro es mayor que tres»
            self.en("mayor")
            self.pop(mayor)

            # «dentro del cuadrado pequeño»
            self.en("dentro")
            self.play(P.pequeno.animate.set_fill(SENAL, 0.8), FadeIn(lab1), run_time=self.dur(0.6))

            # «fuera de él»
            self.en("fuera")
            self.play(P.grande.animate.set_fill(INK, 0.3).set_stroke(INK, 3), FadeIn(lab0), run_time=self.dur(0.6))
        self.wait(0.3)
