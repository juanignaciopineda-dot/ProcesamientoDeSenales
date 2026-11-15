"""Escena 07 — El azar está en cuál oscilador te toca: X(t) = A sen(Φt + Θ) con A, Φ y Θ aleatorias."""
from comun.escena import *


class AzarEnLosParametros(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        L = Lienzo(ancho=8.6, alto=3.0, t_rango=(0, 2), v_max=1.5, centro=(-0.6, -0.7))
        t = np.linspace(0, 2, 260)
        A, f, th = 1.0, 1.0, -0.9
        principal = L.curva(t, A * np.sin(2 * np.pi * f * t + th), SENAL, 4.5)
        base = L.base()
        t_pico = (np.pi / 2 - th) / (2 * np.pi * f)
        t_cero = -th / (2 * np.pi * f)

        with self.narrar("b1"):
            self.play(Create(base), Create(principal), run_time=self.dur(0.9), rate_func=linear)

            # «¿dónde está el azar?»
            self.en("donde")
            q = Text("?", color=AMBAR, weight=BOLD).scale(2.6).move_to([5.6, -0.7, 0])
            self.pop(q)

            # «un seno perfecto»
            self.en("perfecto")
            ok = tilde(VERDE, 1.0).move_to([5.6, -0.7, 0])
            self.play(FadeOut(q), run_time=0.15)
            self.pop(ok)

            # «cuál de todos los senos»
            self.en("cual")
            self.play(FadeOut(ok), run_time=0.15)
            fantasmas = VGroup(*[L.curva(t, a_ * np.sin(2 * np.pi * f_ * t + p_), INK, 2.4, 0.5)
                                 for a_, f_, p_ in ((0.5, 1.5, 2.0), (0.8, 0.7, 4.0), (1.2, 1.2, 1.0),
                                                    (0.6, 2.0, 5.0), (0.9, 0.5, 3.0))])
            self.play(LaggedStart(*[Create(g) for g in fantasmas], lag_ratio=0.2), run_time=self.dur(2.0))
            self.play(principal.animate.set_stroke(AMBAR, width=6), run_time=self.dur(0.5))

            # «equis de te es»
            self.en("xt")
            F = formula("X", "(", "t", ")", "=", "A", r"\operatorname{sen}", "(", r"\Phi", "t", "+", r"\Theta", ")",
                        escala=1.4).move_to([0, 2.75, 0])
            self.play(FadeIn(F[0:5], shift=DOWN * 0.15), run_time=self.dur(0.6))

            # «A por el seno»
            self.en("a_sin")
            self.play(FadeIn(F[5:8], shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «fi por te más theta»
            self.en("fi_theta")
            self.play(FadeIn(F[8:13], shift=DOWN * 0.15), run_time=self.dur(0.8))

            # «La amplitud A»
            self.en("amp")
            fl_a = DoubleArrow(L.p(t_pico, 0), L.p(t_pico, 1.0), color=AMBAR, stroke_width=4, buff=0)
            self.play(F[5].animate.set_color(AMBAR), GrowFromCenter(fl_a), run_time=self.dur(0.6))

            # «la frecuencia fi»
            self.en("frec")
            fl_f = DoubleArrow(L.p(t_pico, 1.3), L.p(t_pico + 1 / f, 1.3), color=AMBAR, stroke_width=4, buff=0)
            self.play(F[8].animate.set_color(AMBAR), GrowFromCenter(fl_f), run_time=self.dur(0.6))

            # «la fase theta»
            self.en("fase")
            fl_p = DoubleArrow(L.p(0, -0.3), L.p(t_cero, -0.3), color=AMBAR, stroke_width=4, buff=0)
            self.play(F[11].animate.set_color(AMBAR), GrowFromCenter(fl_p), run_time=self.dur(0.6))

            # «variables aleatorias»
            self.en("va")
            self.play(FadeOut(fl_a), FadeOut(fl_f), FadeOut(fl_p), run_time=0.2)
            signos = VGroup(*[Text("?", color=AMBAR, weight=BOLD).scale(0.8).next_to(F[i], UP, buff=0.12)
                              for i in (5, 8, 11)])
            self.play(LaggedStart(*[FadeIn(s, scale=0.5) for s in signos], lag_ratio=0.2), run_time=self.dur(0.9))

            # «fijada para siempre»
            self.en("fija")
            self.play(FadeOut(signos), FadeOut(fantasmas), run_time=0.2)
            abierto = candado(AMBAR, abierto=True).scale(1.5).move_to([5.6, -0.7, 0])
            cerrado = candado(AMBAR, abierto=False).scale(1.5).move_to([5.6, -0.7, 0])
            self.pop(abierto)
            self.play(Transform(abierto, cerrado), run_time=0.3)
        self.wait(1.0)
        self.limpiar()
