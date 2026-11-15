"""Escena 08 — Correlación cruzada: R_yx(τ) = h(τ) * R_xx(τ); no aparece t."""
from comun.escena import *


class CorrelacionCruzada(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.cuenta()
        self.resultado()

    # ------------------------------------------------------------------ b1
    def cuenta(self):
        r1 = formula(r"E\big[", r"y(t+\tau)", r"x(t)", r"\big]", escala=1.0).move_to([0, 2.9, 0])
        r2 = formula("=", r"E\big[", r"\int h(v)\,x(t+\tau-v)\,dv", r"\cdot", r"x(t)", r"\big]", escala=1.0).move_to([0, 1.6, 0])
        r3 = formula("=", r"\int h(v)", r"E[x(t+\tau-v)\,x(t)]", r"dv", escala=1.0).move_to([0, 0.3, 0])
        r4 = formula("=", r"\int h(v)", r"R_{xx}(\tau-v)", r"dv", escala=1.0).move_to([0, -1.0, 0])
        for r in (r2, r3, r4):
            r.align_to(r2, LEFT).shift(LEFT * 0.0)
        r2.move_to([0, 1.6, 0])
        r3.align_to(r2[0], LEFT)
        r4.align_to(r2[0], LEFT)
        sub = Underline(r3[2], color=AMBAR, buff=0.1, stroke_width=5)
        L = Lienzo(ancho=4.6, alto=1.3, t_rango=(0, 1), v_max=1.5, centro=(-3.0, -3.0))
        t = np.linspace(0, 1, 120)
        curva = L.curva(t, 0.6 * serie(41, 120, 0.9), SENAL, 3)
        v1, v2 = L.vertical(0.25, AMBAR, 3.5, mitad=0.7), L.vertical(0.65, AMBAR, 3.5, mitad=0.7)
        sep = BraceBetweenPoints(L.p(0.65, -0.8), L.p(0.25, -0.8), color=AMBAR)
        sep_t = MathTex(r"\tau-v", color=AMBAR).scale(0.8).next_to(sep, DOWN, buff=0.1)

        with self.narrar("b1"):
            # «la correlación cruzada»
            self.en("cruzada")
            self.play(FadeIn(r1), run_time=self.dur(0.8))

            # «la salida en te más tau»
            self.en("y_tau")
            self.play(r1[1].animate(rate_func=there_and_back).scale(1.25).set_color(MEDIDA), run_time=0.5)

            # «la entrada en te»
            self.en("x_t")
            self.play(r1[2].animate(rate_func=there_and_back).scale(1.25).set_color(SENAL), run_time=0.5)

            # «una integral»
            self.en("integral")
            self.play(FadeIn(r2[:3]), run_time=self.dur(0.9))

            # «el producto también»
            self.en("producto")
            self.play(FadeIn(r2[3:]), run_time=self.dur(0.6))

            # «La esperanza vuelve a entrar»
            self.en("entra")
            self.play(FadeIn(r3), run_time=self.dur(1.0))

            # «dentro queda»
            self.en("dentro")
            self.play(Create(sub), run_time=self.dur(0.5))

            # «dos entradas separadas»
            self.en("separadas")
            self.play(Create(curva), Create(v1), Create(v2), run_time=self.dur(0.8))
            self.play(Create(sep), FadeIn(sep_t), run_time=self.dur(0.5))

            # «la autocorrelación de la entrada»
            self.en("autocorr")
            self.play(FadeIn(r4), run_time=self.dur(0.8))

            # «en tau menos uve»
            self.en("tau_v")
            self.play(r4[2].animate(rate_func=there_and_back).scale(1.2).set_color(AMBAR), run_time=0.6)
        self.wait(1.0)

    # ------------------------------------------------------------------ b2
    def resultado(self):
        f = formula(r"R_{yx}(\tau)", "=", r"\int", r"h(v)", r"R_{xx}(\tau-v)", r"dv", escala=1.1).move_to([0, 3.0, 0])
        res = formula(r"R_{yx}(\tau)", "=", r"h(\tau)", "*", r"R_{xx}(\tau)", escala=1.2).move_to([0, 1.7, 0])
        caja_res = SurroundingRectangle(res, color=AMBAR, buff=0.2, stroke_width=3)
        bl = BloqueLTI(r"h", centro=(0, 0.0), ancho=1.8, alto=1.1, largo=2.0)
        Le = Lienzo(ancho=2.6, alto=1.2, t_rango=(-1.5, 1.5), v_max=1.2, centro=(-4.5, 0.0))
        Ls = Lienzo(ancho=2.6, alto=1.2, t_rango=(-1.5, 1.5), v_max=1.2, centro=(4.5, 0.0))
        tau = np.linspace(-1.5, 1.5, 120)
        c_e = Le.curva(tau, np.exp(-2.5 * np.abs(tau)), SENAL, 4)
        c_s = Ls.curva(tau, 0.75 * np.exp(-1.6 * np.abs(tau - 0.3)), MEDIDA, 4)
        t_txt = MathTex("t", color=TXT).scale(1.0).move_to([-3.3, -1.9, 0])
        t_tach = tachar(t_txt)
        no_t = etiqueta("no aparece", INK, 0.68).next_to(t_txt, LEFT, buff=0.25)
        solo = formula(r"\text{solo }", r"\tau", escala=0.9, colores={1: AMBAR}).move_to([0, -1.9, 0])
        wss = sello("conjuntamente WSS", VERDE).scale(0.9).move_to([4.2, -2.0, 0])
        anun = caja("¿conjuntamente WSS? → ahora", AMBAR, ancho=6.6, alto=0.8, scale=0.6).move_to([-0.4, -3.4, 0])
        ok = tilde().scale(0.8).next_to(anun, RIGHT, buff=0.3)

        with self.narrar("b2"):
            # «hache de uve»
            self.en("h_v")
            self.corte()
            self.play(FadeIn(f), run_time=0.4)
            self.play(f[3].animate(rate_func=there_and_back).scale(1.25).set_color(ESTIMACION), run_time=0.5)

            # «erre sub equis equis de tau menos uve»
            self.en("r_xx")
            self.play(f[4].animate(rate_func=there_and_back).scale(1.25).set_color(SENAL), run_time=0.6)

            # «una convolución»
            self.en("conv")
            self.play(FadeIn(res), Create(caja_res), run_time=self.dur(0.8))

            # «hache convolucionada»
            self.en("h_conv")
            self.play(FadeIn(bl), Create(c_e), run_time=self.dur(0.8))
            self.play(Create(c_s), run_time=self.dur(0.7))

            # «la autocorrelación de la entrada»
            self.en("de_entrada")
            self.play(c_e.animate.set_stroke(width=7), run_time=self.dur(0.4))

            # «Y en el resultado»
            self.en("resultado")
            self.resaltar(caja_res, color=AMBAR, escala=1.05)

            # «no aparece te»
            self.en("sin_t")
            self.play(FadeIn(t_txt), FadeIn(no_t), run_time=0.3)
            self.play(Create(t_tach), run_time=0.4)

            # «solo tau»
            self.en("solo_tau")
            self.play(FadeIn(solo), run_time=self.dur(0.5))

            # «conjuntamente estacionarias»
            self.en("conj")
            self.pop(wss)

            # «como habíamos anunciado»
            self.en("anunciado")
            self.play(FadeIn(anun), FadeIn(ok, scale=0.6), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
