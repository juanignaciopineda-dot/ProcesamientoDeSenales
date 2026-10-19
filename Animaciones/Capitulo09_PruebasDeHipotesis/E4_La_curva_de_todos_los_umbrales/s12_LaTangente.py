"""Escena 12 — El punto de Bayes: la recta de igual error que toca la curva es tangente, y eta = p₀/p₁."""
from comun.escena import *
from comun.figuras_c9e4 import *

PLANO_11 = dict(origen=(-1.6, -3.2), lado=4.6)
M = P0 / P1                                    # pendiente de las rectas de igual error
FA_MAP, PD_MAP = roc9(CRUCE9)                  # (0,077; 0,72)
C_TAN = PD_MAP - M * FA_MAP                    # ordenada al origen de la tangente


def color_recta(c: float):
    """De rojo (mucho error, abajo a la derecha) a verde (poco, arriba a la izquierda)."""
    a = (c + 0.7) / 1.4
    return interpolate_color(ManimColor(ERROR), ManimColor(VERDE), float(np.clip(a, 0, 1)))


class LaTangente(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.P = PlanoRoc9(**PLANO_11)
        self.cur = self.P.curva()
        self.add(self.P, self.cur)
        self.deslizar()
        self.igualar()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def deslizar(self):
        P = self.P
        with self.narrar("b1"):
            # «Son rectas paralelas»
            self.en("familia")
            cs = [-0.7, -0.35, 0.0, 0.35, 0.7]
            fam = VGroup(*[P.recta(M, (0, c), color=TXT, ancho=3) for c in cs])
            self.play(LaggedStart(*[Create(r) for r in fam], lag_ratio=0.2), run_time=self.dur(1.0))

            # «menos error»
            self.en("verde")
            self.play(*[r.animate.set_stroke(color_recta(c)) for r, c in zip(fam, cs)], run_time=self.dur(0.5))
            fl = Arrow(P.p(0.75, 0.25), P.p(0.55, 0.45), color=DET, buff=0, stroke_width=5,
                       max_tip_length_to_length_ratio=0.3)
            self.play(GrowArrow(fl), run_time=self.dur(0.3))

            # «Desliza una»
            self.en("desliza")
            c = ValueTracker(-0.35)
            una = always_redraw(lambda: P.recta(M, (0, c.get_value()), color=color_recta(c.get_value()), ancho=4.5))
            self.play(FadeOut(fam), FadeOut(fl), FadeIn(una), run_time=self.dur(0.35))
            self.play(c.animate.set_value(C_TAN - 0.12), run_time=self.dur(2.6), rate_func=linear)

            # «por última vez»
            self.en("ultima")
            self.play(c.animate.set_value(C_TAN), run_time=self.dur(1.2))
            una.clear_updaters()
            self.una = una

            # «en un solo punto»
            self.en("toca")
            dot = P.punto(FA_MAP, PD_MAP, color=TXT, radio=0.11)
            self.sfx("tick")
            self.play(FadeIn(dot, scale=0.3), run_time=self.dur(0.3))
            self.dot = dot

            # «es tangente»
            self.en("tangente")
            tt = Text("Tangente", color=TXT, weight=BOLD).scale(0.5).move_to(P.p(0.46, 1.0) + UP * 0.32)
            self.pop(tt)
            self.tt = tt

    # ------------------------------------------------------------ b2
    def igualar(self):
        P = self.P
        with self.narrar("b2"):
            # «la misma pendiente»
            self.en("misma")
            self.play(FadeOut(self.tt), run_time=0.2)
            self.zoom(P.p(0.3, 0.62), 8.0, run_time=self.dur(0.8))

            # «La de la recta»
            self.en("recta")
            r = MathTex(r"\text{Recta: } \dfrac{p_0}{p_1}", color=TXT).scale(0.62).move_to(P.p(0.55, 0.5))
            self.play(FadeIn(r, shift=LEFT * 0.15), run_time=self.dur(0.4))

            # «La de la curva es eta»
            self.en("curva")
            cv = MathTex(r"\text{Curva: } \eta", color=ROC).scale(0.62).next_to(r, DOWN, buff=0.3)
            self.play(FadeIn(cv, shift=LEFT * 0.15), run_time=self.dur(0.4))

            # «Así que eta vale»
            self.en("igual")
            eq = MathTex(r"\eta = \dfrac{p_0}{p_1}", color=ROC).scale(0.8).move_to(VGroup(r, cv))
            marco = SurroundingRectangle(eq, color=ROC, buff=0.15, stroke_width=4)
            self.play(ReplacementTransform(VGroup(r, cv), eq), run_time=self.dur(0.6))
            self.play(Create(marco), run_time=self.dur(0.35))

            # «la regla del máximo a posteriori»
            self.en("map")
            mp = Text("MAP", color=ROC, weight=BOLD).scale(0.45).next_to(marco, DOWN, buff=0.18)
            self.pop(mp)

            # «con un dibujo»
            self.en("dibujo")
            self.zoom_reset(run_time=self.dur(0.8))

            # «cero coma cero setenta y siete»
            self.en("fa")
            par = rotulo_par9("0,077", "0,72", escala=0.5).move_to(P.p(0.3, 0.75))
            self.play(FadeIn(par[0:3]), run_time=self.dur(0.35))

            # «cero coma setenta y dos»
            self.en("pd")
            info = Text("Umbral 1,42 · Error 0,139", color=INK).scale(0.4).next_to(par, DOWN, buff=0.15)
            info.align_to(par, LEFT)
            self.play(FadeIn(par[3:]), FadeIn(info), run_time=self.dur(0.45))
