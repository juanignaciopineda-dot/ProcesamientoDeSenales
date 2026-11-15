"""Escena 11 — Ejemplo continuo: onda telegráfica (λ = 1) por el pasabajos h(t) = 3e^{-3t}; R_hh(τ) = (3/2)e^{-3|τ|}."""
from comun.escena import *


class TelegraficaYFiltro(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.planteo()
        self.autocorrelacion_del_filtro()

    # ------------------------------------------------------------------ b1
    def planteo(self):
        L = Lienzo(ancho=3.2, alto=1.3, t_rango=(0, 6), v_max=1.4, centro=(-4.4, 2.9))
        onda = onda_tel(L, nivel0=1, color=AMBAR, ancho=4.0)
        lam = formula(r"\lambda", "=", "1", escala=1.0, colores={0: AMBAR}).move_to([-4.4, 1.6, 0])
        bl = BloqueLTI(r"h", centro=(0.9, 2.9), ancho=1.6, alto=1.0, largo=1.3, escala=0.8)
        Ls = Lienzo(ancho=2.6, alto=1.3, t_rango=(0, 1), v_max=1.4, centro=(5.4, 2.9))
        suave = Ls.curva(np.linspace(0, 1, 120), 0.5 * serie(9, 120, 0.97), MEDIDA, 3.5)
        # R_xx
        ax1, lab1 = ejes((-2, 2), (0, 1.2), ancho=4.6, alto=2.0, x_label=r"\tau")
        g1 = VGroup(ax1, lab1).move_to([-4.0, -0.6, 0])
        c1 = ax1.plot(lambda x: np.exp(-2 * abs(x)), x_range=[-2, 2], color=SENAL, stroke_width=5)
        f_r = formula(r"R_{xx}(\tau)", "=", r"e^{-2|\tau|}", escala=1.0).move_to([-4.0, -2.45, 0])
        d1 = Dot(ax1.c2p(0, 1), radius=0.12, color=AMBAR)
        v1 = formula(r"1", escala=0.9, colores={0: AMBAR}).next_to(d1, UP, buff=0.2)
        # h(t)
        ax2, lab2 = ejes((0, 2), (0, 3.4), ancho=4.4, alto=2.0, x_label="t")
        g2 = VGroup(ax2, lab2).move_to([3.6, -0.6, 0])
        c2 = ax2.plot(lambda x: 3 * np.exp(-3 * x), x_range=[0, 2], color=ESTIMACION, stroke_width=5)
        f_h = formula(r"h(t)", "=", r"3e^{-3t}", escala=1.0).move_to([3.6, -2.45, 0])
        f_u = formula(r"t \geq 0", escala=0.85, colores={0: INK}).move_to([2.0, 0.9, 0])
        area = ax2.get_area(c2, x_range=(0, 2), color=AMBAR, opacity=0.3)
        f_a = formula(r"\text{área} = 1", escala=0.9, colores={0: AMBAR}).move_to([5.4, 0.9, 0])
        g1_f = formula("H(0)", "=", "1", escala=1.1).move_to([3.6, -3.4, 0])
        cont = etiqueta("tiempo continuo", INK, 0.55).move_to([0, 3.6, 0])

        with self.narrar("b1"):
            # «un ejemplo continuo»
            self.en("continuo")
            self.play(FadeIn(cont), run_time=self.dur(0.4))

            # «la onda telegráfica»
            self.en("onda")
            self.play(Create(L.base()), Create(onda), run_time=self.dur(1.0), rate_func=linear)

            # «lambda igual a uno»
            self.en("lambda")
            self.play(FadeIn(lam), run_time=self.dur(0.4))

            # «e elevado a menos dos»
            self.en("r_xx")
            self.play(FadeIn(g1), Create(c1), FadeIn(f_r), run_time=self.dur(1.0))

            # «valor absoluto de tau»
            self.en("abs")
            self.resaltar(c1, color=AMBAR, escala=1.05)

            # «su varianza, uno»
            self.en("var1")
            self.play(FadeIn(d1), FadeIn(v1), run_time=self.dur(0.5))

            # «un pasabajos sencillo»
            self.en("pasabajos")
            self.play(FadeIn(bl), Create(suave), FadeIn(g2), run_time=self.dur(0.9))

            # «tres por e elevado a menos tres te»
            self.en("h_t")
            self.play(Create(c2), FadeIn(f_h), run_time=self.dur(1.0))

            # «a partir de te igual a cero»
            self.en("u_t")
            self.play(FadeIn(f_u), run_time=self.dur(0.4))

            # «Su área vale uno»
            self.en("area")
            self.play(FadeIn(area), FadeIn(f_a), run_time=self.dur(0.7))

            # «ganancia uno en continua»
            self.en("g1")
            self.play(FadeIn(g1_f), run_time=self.dur(0.5))
        self.wait(1.0)

    # ------------------------------------------------------------------ b2
    def autocorrelacion_del_filtro(self):
        ax, lab = ejes((-0.5, 2.5), (0, 3.4), ancho=6.4, alto=2.6, x_label="t")
        g = VGroup(ax, lab).move_to([0, 1.7, 0])
        tau = 0.6
        h = ax.plot(lambda x: 3 * np.exp(-3 * x), x_range=[0, 2.5], color=ESTIMACION, stroke_width=5)
        copia = ax.plot(lambda x: 3 * np.exp(-3 * (x - tau)), x_range=[tau, 2.5], color=AMBAR, stroke_width=5)
        prod = ax.plot(lambda x: 9 * np.exp(-3 * x) * np.exp(-3 * (x - tau)) / 3.0, x_range=[tau, 2.5], color=VERDE, stroke_width=4)
        area = ax.get_area(prod, x_range=(tau, 2.5), color=VERDE, opacity=0.3)
        f0 = formula(r"R_{hh}(\tau)", "=", "?", escala=1.3).move_to([0, -0.9, 0])
        f1 = formula(r"R_{hh}(\tau)", "=", r"9\,e^{-3\tau}", r"\int_0^{\infty} e^{-6t}\,dt", escala=1.3).move_to([0, -0.9, 0])
        f2 = formula("=", r"9\,e^{-3\tau}", r"\cdot", r"\tfrac16", escala=1.3).move_to([0, -0.9, 0])
        f3 = formula("=", r"\tfrac32\,e^{-3\tau}", escala=1.3).move_to([0, -2.0, 0])
        res = formula(r"R_{hh}(\tau)", "=", r"\tfrac32\,e^{-3|\tau|}", escala=1.5, colores={2: ESTIMACION}).move_to([0, -3.1, 0])
        caja_res = SurroundingRectangle(res, color=AMBAR, buff=0.18, stroke_width=3)
        tau_txt = MathTex(r"\tau", color=AMBAR).scale(0.9).move_to(ax.c2p(tau / 2, -0.4))

        with self.narrar("b2"):
            # «la autocorrelación determinista»
            self.en("r_hh")
            self.corte()
            self.play(FadeIn(g), Create(h), FadeIn(f0), run_time=self.dur(1.0))

            # «Deslizamos hache sobre sí misma»
            self.en("desliza")
            self.play(Create(copia), FadeIn(tau_txt), run_time=self.dur(1.0))

            # «multiplicamos»
            self.en("multiplica")
            self.play(Create(prod), run_time=self.dur(0.8))

            # «el área donde se solapan»
            self.en("solape")
            self.play(FadeIn(area), run_time=self.dur(0.6))

            # «nueve por e elevado a menos tres tau»
            self.en("nueve")
            self.play(FadeOut(f0), FadeIn(f1[:3]), run_time=self.dur(0.6))

            # «e elevado a menos seis te»
            self.en("seis")
            self.play(FadeIn(f1[3]), run_time=self.dur(0.6))

            # «un sexto»
            self.en("sexto")
            self.play(FadeOut(f1), FadeIn(f2), run_time=self.dur(0.6))

            # «tres medios»
            self.en("tres_medios")
            self.play(FadeIn(f3), run_time=self.dur(0.7))

            # «valor absoluto de tau»
            self.en("r_abs")
            self.play(FadeIn(res), Create(caja_res), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
