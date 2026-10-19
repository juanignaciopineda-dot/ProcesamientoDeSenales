"""Escena 10 — Bayes con campanas: tachar el denominador y escalar por el a priori."""
from comun.escena import *
from comun.figuras_c9e1 import *


def fila_bayes(h: int, color, centro):
    """«P(Hh | r) = ph · f(r | Hh) / f(r)», con piezas sueltas:
    `.izq` (P(…) =), `.r` (la r), `.num` (p · f), `.p`, `.f`, `.barra`, `.den`."""
    izq = MathTex(rf"P(H_{h} \mid", "r", ")", "=", color=color).scale(1.0)
    izq[1].set_color(MEDIDA)
    num_ = MathTex(rf"p_{h}", r"\cdot", rf"f(r \mid H_{h})", color=color).scale(1.0)
    den = MathTex(r"f(r)", color=TXT).scale(1.0)
    barra = Line(LEFT, RIGHT, color=TXT, stroke_width=3).set_width(num_.width + 0.1)
    frac = VGroup(num_, barra, den).arrange(DOWN, buff=0.12)
    g = VGroup(izq, frac).arrange(RIGHT, buff=0.2).move_to([centro[0], centro[1], 0])
    g.izq, g.r, g.num, g.p, g.f, g.barra, g.den = izq, izq[1], num_, num_[0:2], num_[2], barra, den
    return g


class CampanasEscaladas(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.bayes()
        self.tachar_den()
        self.escalar()
        self.wait(1.0)
        self.limpiar()

    def bayes(self):
        with self.narrar("b1"):
            # «la regla de Bayes»
            self.en("bayes")
            tit = Text("Bayes", color=ESTIMACION, weight=BOLD).scale(0.75).move_to([0, 3.3, 0])
            raiz = Dot([-5.6, 2.6, 0], radius=0.08, color=INK)
            hojas = [Dot([-4.6, 3.1, 0], radius=0.08, color=C1), Dot([-4.6, 2.1, 0], radius=0.08, color=C0)]
            ramas = VGroup(*[Line(raiz.get_center(), h.get_center(), color=INK, stroke_width=3) for h in hojas])
            mini = VGroup(ramas, raiz, *hojas)
            self.pop(tit)
            self.play(FadeIn(mini), run_time=self.dur(0.4))

            # «con alturas»
            self.en("alturas")
            cm = VGroup(campana_mini((-5.3, 2.5), 1.1, 0.7, C0), campana_mini((-4.2, 2.5), 1.1, 0.7, C1))
            self.play(ReplacementTransform(mini, cm), run_time=self.dur(0.6))

            # «La probabilidad a posteriori de hache uno»
            self.en("post")
            F1 = fila_bayes(1, C1, (-3.5, 0.3))
            self.F1 = F1
            self.play(FadeIn(F1.izq, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «habiendo medido erre»
            self.en("r")
            self.play(F1.r.animate(rate_func=there_and_back).scale(1.5), run_time=self.dur(0.6))

            # «pe uno»
            self.en("p1")
            self.play(FadeIn(F1.p), run_time=self.dur(0.3))

            # «la altura de la campana del uno»
            self.en("f1")
            self.play(FadeIn(F1.f, shift=UP * 0.15), run_time=self.dur(0.4))

            # «la densidad total de erre»
            self.en("den")
            self.play(Create(F1.barra), FadeIn(F1.den, shift=UP * 0.15), run_time=self.dur(0.5))

    def tachar_den(self):
        F1 = self.F1
        with self.narrar("b2"):
            # «Para hache cero es igual»
            self.en("h0")
            F0 = fila_bayes(0, C0, (3.5, 0.3))
            self.play(FadeIn(F0, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «el mismo denominador»
            self.en("mismo")
            self.play(F1.den.animate.set_color(ESTIMACION), F0.den.animate.set_color(ESTIMACION),
                      run_time=self.dur(0.4))

            # «cuál de las dos es mayor»
            self.en("comparar")
            cmp = MathTex(r"\gtrless", color=ESTIMACION).scale(1.4).move_to([0, 0.3, 0])
            self.pop(cmp)

            # «ese denominador sobra»
            self.en("tacha")
            t1, t0 = tachar(F1.den), tachar(F0.den)
            self.play(Create(t1), Create(t0), run_time=self.dur(0.4))
            self.play(FadeOut(VGroup(F1.den, F0.den, F1.barra, F0.barra, t1, t0)), run_time=self.dur(0.4))

            # «es positivo»
            self.en("positivo")
            pos = MathTex(r"f(r) > 0", color=ESTIMACION).scale(0.85).move_to([0, -1.5, 0])
            self.play(FadeIn(pos), run_time=self.dur(0.4))

            # «Basta comparar»
            self.en("regla")
            R = formula(r"p_1", r"\cdot", r"f(r \mid H_1)", r"\gtrless", r"p_0", r"\cdot", r"f(r \mid H_0)",
                        colores={0: C1, 1: C1, 2: C1, 3: ESTIMACION, 4: C0, 5: C0, 6: C0}).scale(1.25)
            R.move_to([0, -2.6, 0])
            self.play(FadeOut(F1.izq), FadeOut(F0.izq), FadeOut(pos), run_time=self.dur(0.3))
            self.play(ReplacementTransform(F1.num[0], R[0]), ReplacementTransform(F1.num[1], R[1]),
                      ReplacementTransform(F1.num[2], R[2]), ReplacementTransform(cmp, R[3]),
                      run_time=self.dur(0.7))

            # «con pe cero por la suya»
            self.en("suya")
            self.play(ReplacementTransform(F0.num[0], R[4]), ReplacementTransform(F0.num[1], R[5]),
                      ReplacementTransform(F0.num[2], R[6]), run_time=self.dur(0.7))

    def escalar(self):
        C = Campanas9()
        with self.narrar("b3"):
            # «En el dibujo»
            self.en("dibujo")
            self.corte()
            eje = C.eje((0, 1, 2))
            c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
            self.play(FadeIn(eje), FadeIn(c0), FadeIn(c1), run_time=self.dur(0.5))

            # «se multiplica por su probabilidad a priori»
            self.en("factores")
            k0 = MathTex(r"\times\, 0{,}7", color=C0).scale(0.8).move_to(C.p(0, 0.4) + UP * 0.5)
            k1 = MathTex(r"\times\, 0{,}3", color=C1).scale(0.8).move_to(C.p(2, 0.4) + UP * 0.5)
            self.pop(k0, k1)

            # «La del cero»
            self.en("del0")
            self.play(c0.animate(rate_func=there_and_back).set_stroke(width=8), run_time=self.dur(0.6))

            # «el setenta por ciento»
            self.en("esc0")
            self.play(Transform(c0, C.campana(0, 0.7, C0)), k0.animate.move_to(C.p(0, 0.7 * 0.4) + UP * 0.5),
                      run_time=self.dur(0.9))

            # «se encoge al»
            self.en("esc1")
            self.play(Transform(c1, C.campana(2, 0.3, C1)), k1.animate.move_to(C.p(2, 0.3 * 0.4) + UP * 0.5),
                      run_time=self.dur(0.9))

            # «la curva que quede más alta»
            self.en("alta")
            t = np.linspace(C.r0, C.r1, 220)
            env = C.L.curva(t, np.maximum(C.f(0, t, P0), C.f(2, t, P1)), ESTIMACION, 7, opacidad=0.85)
            cur = Line(C.p(C.r0), C.p(C.r0) + UP * 3.0, color=MEDIDA, stroke_width=3)
            tiempo = self.margen() - 0.2
            self.play(Create(env), cur.animate.move_to(C.p(C.r1) + UP * 1.5), run_time=max(0.6, tiempo),
                      rate_func=linear)
            self.play(FadeOut(cur), run_time=0.2)
