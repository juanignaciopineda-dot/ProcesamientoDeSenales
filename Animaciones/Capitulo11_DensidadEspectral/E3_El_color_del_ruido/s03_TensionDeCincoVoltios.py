"""Escena 03 — Una tensión de 5 V con 1 V de desviación: potencia = media² + varianza = 26."""
from comun.escena import *


class TensionDeCincoVoltios(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.fluctua()
        self.cuenta()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def fluctua(self):
        L = Lienzo(ancho=6.2, alto=5.6, t_rango=(0, 3), v_max=7, centro=(-3.3, -0.2))
        t = np.linspace(0, 3, 150)
        fl = serie(9, 150, 0.7)
        base = L.base()
        trazo = L.curva(t, fl, AZUL, 3.2)
        with self.narrar("b1"):
            # «no oscilan alrededor de cero»
            self.en("nocero")
            self.play(Create(base), Create(trazo), run_time=self.dur(0.7))
            self.play(trazo.animate.shift(UP * float(L.y(5) - L.y(0))), run_time=self.dur(0.9))

            # «una tensión»
            self.en("tension")
            v = Text("V", color=INK).scale(0.6).move_to(L.p(0, 6.4) + LEFT * 0.35)
            eje = Line(L.p(0, -0.4), L.p(0, 6.6), color=INK, stroke_width=2)
            self.play(Create(eje), FadeIn(v), run_time=self.dur(0.5))

            # «cinco voltios»
            self.en("cinco")
            l5 = DashedLine(L.p(0, 5), L.p(3, 5), color=AMBAR, stroke_width=3)
            t5 = Text("5 V", color=AMBAR, weight=BOLD).scale(0.55).move_to(L.p(3, 5) + RIGHT * 0.55)
            self.play(Create(l5), FadeIn(t5), run_time=self.dur(0.5))

            # «una desviación típica de un voltio»
            self.en("desv")
            banda = Rectangle(width=L.ancho, height=float(L.y(2) - L.y(0)), stroke_width=0)
            banda.set_fill(MAGENTA, 0.18).move_to(L.p(1.5, 5))
            t1 = Text("±1 V", color=MAGENTA, weight=BOLD).scale(0.5).move_to(L.p(3, 6.4) + RIGHT * 0.55)
            self.play(FadeIn(banda), FadeIn(t1), run_time=self.dur(0.6))

            # «Hay dos cosas mezcladas»
            self.en("dos")
            cajas = VGroup(caja("media", AZUL, ancho=2.6, alto=0.7, scale=0.5).move_to([4.2, 3.2, 0]),
                           caja("fluctuaciones", MAGENTA, ancho=3.2, alto=0.7, scale=0.5).move_to([4.2, 0.2, 0]))
            self.play(FadeIn(cajas), run_time=self.dur(0.5))

            # «un valor medio que no cambia nunca»
            self.en("media")
            lm = Line([2.5, 2.3, 0], [5.9, 2.3, 0], color=AZUL, stroke_width=6)
            self.play(Create(lm), l5.animate.set_stroke(AZUL, width=6), run_time=self.dur(0.6))

            # «unas fluctuaciones»
            self.en("fluct")
            Lm = Lienzo(ancho=3.4, alto=1.6, t_rango=(0, 3), v_max=3, centro=(4.2, -1.3))
            mf = Lm.curva(t, fl, MAGENTA, 3)
            bm = Lm.base()
            self.play(Create(bm), Create(mf), run_time=self.dur(0.6))

            # «¿Cuánta potencia tiene?»
            self.en("pregunta")
            q = Text("¿potencia?", color=AMBAR, weight=BOLD).scale(0.8).move_to([4.2, -3.3, 0])
            self.pop(q)
        self.fuera_b1 = Group(base, trazo, eje, v, l5, t5, banda, t1, q)

    # ------------------------------------------------------------ b2
    def cuenta(self):
        self.play(FadeOut(self.fuera_b1), run_time=0.3)
        f1 = oculta(formula(r"\sigma^2", "=", r"E[x^2]", "-", r"\mu^2").scale(1.15)).move_to([-3.4, 2.7, 0])
        f2 = formula(r"E[x^2]", "=", r"\mu^2", "+", r"\sigma^2").scale(1.15).move_to([-3.4, 2.7, 0])
        f3 = oculta(formula("=", "25", "+", "1", "=", "26").scale(1.15)).move_to([-3.4, 1.2, 0])
        self.add(f1, f3)
        with self.narrar("b2"):
            # «la varianza»
            self.en("var")
            self.play(*revelar(f1[0], f1[1]), run_time=self.dur(0.4))
            # «la esperanza del cuadrado»
            self.en("esp")
            self.play(*revelar(f1[2]), run_time=self.dur(0.4))
            # «menos la media al cuadrado»
            self.en("menos")
            self.play(*revelar(f1[3], f1[4]), run_time=self.dur(0.4))
            # «Despejando»
            self.en("despeja")
            self.play(ReplacementTransform(f1, f2), run_time=self.dur(0.8))
            # «la media al cuadrado más la varianza»
            self.en("sumaps")
            self.play(f2[2].animate.set_color(AZUL), f2[4].animate.set_color(MAGENTA), run_time=self.dur(0.5))
            # «veinticinco más uno»
            self.en("suma")
            f3[1].set_color(AZUL)
            f3[3].set_color(MAGENTA)
            self.play(*revelar(f3[0], f3[1], f3[2], f3[3]), run_time=self.dur(0.6))
            # «veintiséis»
            self.en("v26")
            f3[5].set_color(AMBAR)
            self.play(*revelar(f3[4], f3[5]), run_time=self.dur(0.5))
            # «la parte constante»
            self.en("const")
            b25 = Rectangle(width=1.1, height=2.5, stroke_width=2, color=AZUL).set_fill(AZUL, 0.5)
            b25.move_to([-5.6, -3.7 + 1.25, 0])
            self.play(GrowFromEdge(b25, DOWN), run_time=self.dur(0.7))
            # «la continua»
            self.en("continua")
            tc = Text("la continua", color=AZUL, weight=BOLD).scale(0.55).next_to(b25, RIGHT, buff=0.3)
            self.play(FadeIn(tc), run_time=self.dur(0.4))
            # «Solo uno»
            self.en("uno")
            b1_ = Rectangle(width=1.1, height=0.1, stroke_width=2, color=MAGENTA).set_fill(MAGENTA, 0.8)
            b1_.move_to([-2.0, -3.7 + 0.05, 0])
            tf = Text("fluctuaciones", color=MAGENTA, weight=BOLD).scale(0.55).next_to(b1_, RIGHT, buff=0.3)
            self.play(GrowFromEdge(b1_, DOWN), FadeIn(tf), run_time=self.dur(0.6))
