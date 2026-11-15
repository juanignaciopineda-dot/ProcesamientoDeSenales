"""Escena 05 — Fourier: H(jω), convolución ↔ producto y la ganancia en continua H(0)."""
from comun.escena import *


def _gan(w):
    return 1.0 / np.sqrt(1 + (w / 3.5) ** 2)


class FourierYGanancia(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.en_frecuencia()
        self.ganancia()

    # ------------------------------------------------------------------ b1
    def en_frecuencia(self):
        ax, lab = ejes((0, 10), (0, 1.3), ancho=5.2, alto=2.6, x_label=r"\omega", y_label=r"|H|")
        ag = VGroup(ax, lab).move_to([3.6, 1.0, 0])
        t = np.linspace(0, 4, 240)
        s1, s2, s3 = np.sin(2 * PI * 0.5 * t), 0.7 * np.sin(2 * PI * 1.25 * t), 0.5 * np.sin(2 * PI * 2.5 * t)
        L = Lienzo(ancho=5.0, alto=1.6, t_rango=(0, 4), v_max=1.6, centro=(-3.6, 2.4))
        suma = L.curva(t, (s1 + s2 + s3) * 0.7, SENAL, 3.5)
        ys = [0.6, -0.2, -1.0]
        senos = VGroup(*[Lienzo(ancho=5.0, alto=0.8, t_rango=(0, 4), v_max=1.6, centro=(-3.6, y)).curva(t, s, SENAL, 2.5)
                         for y, s in zip(ys, (s1, s2, s3))])
        flecha_f = Arrow([-1.6, 3.6, 0], [1.2, 3.6, 0], color=INK, buff=0, stroke_width=4)
        txt_f = etiqueta("Fourier", AMBAR, 0.55, BOLD).next_to(flecha_f, DOWN, buff=0.1)
        h_pal = Tallos([0.3, 0.6, 0.9, 0.55, 0.3, 0.1], centro=(-3.6, -2.7), paso=0.35, unidad=0.9, color=ESTIMACION)
        lab_h = MathTex(r"h", color=ESTIMACION).scale(0.8).next_to(h_pal, LEFT, buff=0.5)
        flecha_hh = Arrow([-2.2, -2.2, 0], [0.4, -0.3, 0], color=ESTIMACION, buff=0, stroke_width=3)
        gan = ax.plot(_gan, x_range=[0, 10], color=ESTIMACION, stroke_width=5)
        lab_hj = MathTex(r"H(j\omega)", color=ESTIMACION).scale(0.9).move_to([6.1, 2.4, 0])
        amps = VGroup(*[Arrow(ax.c2p(w, 0.0), ax.c2p(w, _gan(w)), color=AMBAR, buff=0, stroke_width=4) for w in (1.2, 6.0)])
        f_t = formula("y", "=", "h", "*", "x", escala=1.0).move_to([3.2, -1.8, 0])
        f_w = formula("Y", "=", "H", r"\cdot", "X", escala=1.0).move_to([3.2, -3.0, 0])
        ventaja = Text("¡más fácil!", color=AMBAR, weight=BOLD).scale(0.6).move_to([6.0, -3.0, 0])

        with self.narrar("b1"):
            # «en frecuencia»
            self.en("frec")
            self.play(FadeIn(ag), run_time=self.dur(0.7))

            # «La transformada de Fourier»
            self.en("fourier")
            self.play(Create(flecha_f), FadeIn(txt_f), run_time=self.dur(0.6))

            # «descompone una señal»
            self.en("descompone")
            self.play(Create(suma), run_time=self.dur(1.0))

            # «senos de todas las frecuencias»
            self.en("senos")
            self.play(LaggedStart(*[Create(s) for s in senos], lag_ratio=0.3), run_time=self.dur(1.2))

            # «La de la respuesta al impulso»
            self.en("la_de")
            self.play(FadeIn(h_pal), FadeIn(lab_h), Create(flecha_hh), run_time=self.dur(0.7))

            # «hache de jota omega»
            self.en("h_jw")
            self.play(Create(gan), FadeIn(lab_hj), run_time=self.dur(1.0))

            # «cuánto amplifica»
            self.en("amplifica")
            self.play(*[GrowArrow(a) for a in amps], run_time=self.dur(0.7))

            # «la gran ventaja»
            self.en("ventaja")
            self.pop(ventaja)

            # «una convolución en el tiempo»
            self.en("conv_t")
            self.play(FadeIn(f_t), run_time=self.dur(0.6))

            # «una multiplicación en frecuencia»
            self.en("mult")
            self.play(FadeIn(f_w), run_time=self.dur(0.6))
        self.wait(1.0)

    # ------------------------------------------------------------------ b2
    def ganancia(self):
        ax, lab = ejes((0, 10), (0, 1.3), ancho=5.0, alto=2.4, x_label=r"\omega", y_label=r"|H|")
        ag = VGroup(ax, lab).move_to([-3.6, 1.6, 0])
        gan = ax.plot(_gan, x_range=[0, 10], color=ESTIMACION, stroke_width=5)
        d0 = Dot(ax.c2p(0, 1.0), radius=0.12, color=AMBAR)
        lab_h0 = MathTex(r"H(0)", color=AMBAR).scale(0.9).next_to(d0, RIGHT, buff=0.25).shift(UP * 0.45)
        continua = etiqueta("ganancia en continua", AMBAR, 0.5).move_to([-3.6, -0.2, 0])
        f1 = formula("H(0)", "=", r"\sum_k h[k]", escala=1.1).move_to([3.6, 2.7, 0])
        f2 = formula(r"=", r"\int h(v)\,dv", escala=1.1).move_to([3.9, 1.3, 0])
        bl = BloqueLTI(r"H(0)=1", centro=(0, -2.3), ancho=2.4, alto=1.2, largo=2.4, escala=0.8)
        medios = formula(r"\tfrac12", "+", r"\tfrac12", "=", "1", escala=1.0).move_to([4.8, -0.6, 0])
        h_pal = Tallos([0.5, 0.5], centro=(0.0, -0.4), paso=0.7, unidad=1.2, color=ESTIMACION)
        Li = Lienzo(ancho=1.9, alto=1.0, t_rango=(0, 1), v_max=1.0, centro=(-2.75, -2.3))
        Ls = Lienzo(ancho=1.9, alto=1.0, t_rango=(0, 1), v_max=1.0, centro=(2.75, -2.3))
        rec_e = Li.curva([0, 1], [0.0, 0.0], SENAL, 5)
        rec_s = Ls.curva([0, 1], [0.0, 0.0], MEDIDA, 5)
        d2e = MathTex("2", color=SENAL).scale(0.8).next_to(rec_e, UP, buff=0.2)
        d2s = MathTex("2", color=MEDIDA).scale(0.8).next_to(rec_s, UP, buff=0.2)

        with self.narrar("b2"):
            # «hache en cero»
            self.en("h0")
            self.corte()
            self.add(ag)
            self.play(Create(gan), FadeIn(d0), FadeIn(lab_h0), run_time=self.dur(0.8))

            # «la ganancia en continua»
            self.en("continua")
            self.play(FadeIn(continua), run_time=self.dur(0.4))

            # «la suma de todos los valores de hache»
            self.en("suma_h")
            self.play(FadeIn(f1), run_time=self.dur(0.8))

            # «o su integral»
            self.en("integral_h")
            self.play(FadeIn(f2), run_time=self.dur(0.6))

            # «una entrada constante»
            self.en("const")
            self.play(FadeIn(bl), Create(rec_e), FadeIn(d2e), run_time=self.dur(0.8))

            # «sale multiplicada por ella»
            self.en("mult")
            self.play(Create(rec_s), FadeIn(d2s), run_time=self.dur(0.6))

            # «En el promediador»
            self.en("en_prom")
            self.play(FadeIn(h_pal), run_time=self.dur(0.5))

            # «un medio más un medio»
            self.en("medios")
            self.play(FadeIn(medios[:3]), run_time=self.dur(0.6))

            # «uno»
            self.en("uno")
            self.play(FadeIn(medios[3:]), run_time=self.dur(0.4))

            # «Entra un dos constante»
            self.en("entra2")
            self.resaltar(rec_e, color=AMBAR, escala=1.1)

            # «sale un dos»
            self.en("sale2")
            self.resaltar(rec_s, color=AMBAR, escala=1.1)
        self.wait(1.0)
        self.limpiar()
