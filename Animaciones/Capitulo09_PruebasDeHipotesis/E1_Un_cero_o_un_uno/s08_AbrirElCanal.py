"""Escena 08 — El canal por dentro: amplitud más ruido y una campana por hipótesis."""
from comun.escena import *
from comun.figuras_c9e1 import *


class AbrirElCanal(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.cable()
        self.campanas()
        self.wait(1.0)
        self.limpiar()

    def cable(self):
        y = 0.9
        with self.narrar("b1"):
            # «una caja que cambiaba bits»
            self.en("caja")
            K = canal9(centro=(0, y), ancho=9.0)
            self.play(FadeIn(K), run_time=self.dur(0.4))
            b = bit9(0, lado=0.45).move_to(K.p_ent() + RIGHT * 0.3)
            self.add(b)
            self.play(b.animate.move_to(K.caja.get_left() + LEFT * 0.3).set_opacity(0), run_time=self.dur(0.6))
            self.remove(b)
            b2 = bit9(1, color=ERROR, lado=0.45).move_to(K.caja.get_right() + RIGHT * 0.3)
            self.play(FadeIn(b2), run_time=self.dur(0.2))
            self.play(b2.animate.move_to(K.p_sal() + LEFT * 0.3), run_time=self.dur(0.5))

            # «Vamos a abrirla»
            self.en("abrir")
            cable = Line(K.p_ent(), K.p_sal(), color=INK, stroke_width=4)
            self.play(FadeOut(K.caja, shift=UP * 0.5), FadeOut(K.rot, shift=UP * 0.5), FadeOut(b2),
                      FadeOut(K.ent), FadeOut(K.sal), Create(cable), run_time=self.dur(0.7))
            self.cable_ = cable

            # «cero voltios»
            self.en("v0")
            nivel0 = Line([-6.4, y + 0.6, 0], [-5.2, y + 0.6, 0], color=C0, stroke_width=5)
            t0 = Text("0 V", color=C0).scale(0.45).next_to(nivel0, UP, buff=0.12)
            e0 = bit9(0, lado=0.42).next_to(nivel0, DOWN, buff=0.2)
            self.play(Create(nivel0), FadeIn(t0), FadeIn(e0), run_time=self.dur(0.5))

            # «dos voltios»
            self.en("v2")
            pulso = pulsos9([0, 1, 0], centro=(-3.9, y + 0.6), ancho_bit=0.5, alto=1.2, color=C1)
            t2 = Text("2 V", color=C1).scale(0.45).move_to([-3.9, y + 2.1, 0])
            e2 = bit9(1, lado=0.42).move_to([-3.9, e0.get_y(), 0])
            self.play(Create(pulso), FadeIn(t2), FadeIn(e2), run_time=self.dur(0.5))
            self.niveles = VGroup(nivel0, t0, e0, pulso, t2, e2)

            # «se le suma»
            self.en("ruido")
            g = garabato9(centro=(0.3, y), ancho=2.2, alto=0.7)
            mas = MathTex("+", color=RUIDO).scale(0.9).move_to([0.3, y - 0.75, 0])
            self.play(Create(g), FadeIn(mas), run_time=self.dur(0.6))

            # «Lo que llega, erre»
            self.en("r")
            pt = Dot([4.3, y, 0], radius=0.13, color=MEDIDA)
            rt = MathTex("r", color=MEDIDA).scale(0.9).next_to(pt, UP, buff=0.2)
            self.play(FadeIn(pt, scale=0.5), FadeIn(rt), run_time=self.dur(0.4))
            self.play(pt.animate(rate_func=wiggle).shift(UP * 0.12), run_time=self.dur(0.6))

            # «la amplitud enviada»
            self.en("a")
            F = formula("R", "=", "A", "+", "V", colores={0: MEDIDA, 2: SENAL, 4: RUIDO}).scale(1.5)
            F.move_to([0, -1.5, 0])
            self.play(FadeIn(F[0]), FadeIn(F[1]), FadeIn(F[2], shift=UP * 0.2), run_time=self.dur(0.5))

            # «más el ruido»
            self.en("v")
            self.play(FadeIn(F[3]), FadeIn(F[4], shift=UP * 0.2), run_time=self.dur(0.4))

            # «modulación por amplitud de pulsos»
            self.en("pam")
            pam = Text("PAM", color=ESTIMACION, weight=BOLD).scale(0.7).move_to([0, -2.7, 0])
            self.pop(pam)

            # «la forma más simple»
            self.en("tren")
            tren = pulsos9([0, 1, 1, 0, 1, 0], centro=(-2.6, y), ancho_bit=0.75, alto=1.0, color=C1)
            self.play(FadeOut(self.niveles), run_time=self.dur(0.3))
            self.play(Create(tren), run_time=self.dur(0.8))
            self.play(tren.animate.shift(RIGHT * 2.2), run_time=self.dur(1.0))

    def campanas(self):
        C = Campanas9()
        self.C = C
        with self.narrar("b2"):
            # «El ruido es gaussiano»
            self.en("ejes")
            self.corte()
            eje = C.eje((0, 1, 2))
            self.play(FadeIn(eje), run_time=self.dur(0.4))

            # «una campana centrada en cero»
            self.en("campana")
            c0 = C.campana(0, 1, TXT)
            self.play(Create(c0), run_time=self.dur(0.8))

            # «un desvío de un»
            self.en("desvio")
            v = C.f(0, 1.0)
            da = DoubleArrow(C.p(0, v), C.p(1, v), color=ESTIMACION, buff=0, stroke_width=4,
                             tip_length=0.18, max_tip_length_to_length_ratio=0.3)
            sg = MathTex(r"\sigma = 1", color=ESTIMACION).scale(0.7).next_to(da, UP, buff=0.12)
            self.play(GrowFromCenter(da), FadeIn(sg), run_time=self.dur(0.5))

            # «Si se envió un cero»
            self.en("h0")
            l0 = Text("Si se envió 0", color=C0).scale(0.5).move_to(C.p(-1.7, 0.43))
            self.play(c0.animate.set_color(C0), FadeIn(l0), FadeOut(da), FadeOut(sg), run_time=self.dur(0.5))

            # «solo ruido»
            self.en("solo")
            rng = np.random.default_rng(7)
            caidas = [Dot(C.p(float(x), 0) + UP * 3.0, radius=0.08, color=MEDIDA) for x in rng.normal(0, 1, 5)]
            self.play(LaggedStart(*[Succession(FadeIn(d, run_time=0.1), d.animate(run_time=0.45).shift(DOWN * 3.0))
                                    for d in caidas], lag_ratio=0.35), run_time=self.dur(1.6))
            self.play(*[FadeOut(d) for d in caidas], run_time=self.dur(0.3))

            # «Si se envió un uno»
            self.en("h1")
            c1 = c0.copy()
            self.add(c1)
            l1 = Text("Si se envió 1", color=C1).scale(0.5).move_to(C.p(3.7, 0.43))
            self.play(Transform(c1, C.campana(2, 1, C1)), run_time=self.dur(0.8))
            self.play(FadeIn(l1), run_time=self.dur(0.3))

            # «desplazada hasta el dos»
            self.en("dos")
            fl = Arrow(C.p(0, 0.47), C.p(2, 0.47), color=ESTIMACION, buff=0, stroke_width=4,
                       max_tip_length_to_length_ratio=0.12)
            self.play(GrowArrow(fl), run_time=self.dur(0.5))

            # «Dos campanas iguales»
            self.en("iguales")
            self.play(FadeOut(fl), c0.animate(rate_func=there_and_back).set_stroke(width=8),
                      c1.animate(rate_func=there_and_back).set_stroke(width=8), run_time=self.dur(0.7))

            # «que se solapan»
            self.en("solapan")
            sol = C.solape()
            self.play(FadeIn(sol), run_time=self.dur(0.6))
