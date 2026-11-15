"""Escena 16 — Cuando se alcanza el máximo la parábola toca el cero; y la autocorrelación cae desde su pico."""
from comun.escena import *


def g_c(x, c):
    return 4 * (x - 0.6) ** 2 + c


class MaximoYOlvido(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        pa = ejes([-0.3, 1.3, 0.5], [0, 6, 2], ancho=5.4, alto=3.0, x_label=r"\lambda", y_label="g")
        ax = pa[0]
        gp = VGroup(ax, pa[1]).move_to([-3.3, 1.3, 0])
        c = ValueTracker(2.56)
        parabola = always_redraw(lambda: ax.plot(lambda x: g_c(x, c.get_value()), x_range=[-0.3, 1.3, 0.02],
                                                 color=ESTIMACION, stroke_width=5))
        Lo = Lienzo(ancho=5.4, alto=1.5, t_rango=(0, 2), v_max=1.25, centro=(-3.3, -2.6))
        Lr = Lienzo(ancho=4.6, alto=2.6, t_rango=(-2, 2), v_max=1.0, centro=(3.6, 0.3))
        tau = np.linspace(-2, 2, 200)

        with self.narrar("b1"):
            # «se alcanza el máximo»
            self.en("alcanza")
            self.play(FadeIn(gp), run_time=0.3)
            self.add(parabola)
            self.play(c.animate.set_value(0.0), run_time=self.dur(1.6), rate_func=smooth)

            # «La parábola toca el cero»
            self.en("toca")
            vertice = always_redraw(lambda: Dot(ax.c2p(0.6, c.get_value()), radius=0.11, color=AMBAR))
            self.add(vertice)
            self.play(FadeIn(vertice, scale=0.5), run_time=0.3)
            self.resaltar(vertice, escala=2.0)

            # «un múltiplo de la otra»
            self.en("multiplo")
            mult = MathTex(r"\tilde x[n{+}1] = \lambda\,\tilde x[n]", color=TXT).scale(1.0).move_to([3.6, 2.9, 0])
            self.play(FadeIn(mult), run_time=0.5)

            # «sin nada de azar»
            self.en("sin_azar")
            pxy = ejes([-1.5, 1.5, 1], [-1.5, 1.5, 1], ancho=3.2, alto=2.2, tip=False)
            grupo_xy = VGroup(pxy[0]).move_to([3.6, 0.9, 0])
            rng = np.random.default_rng(5)
            xs = rng.uniform(-1.2, 1.2, 9)
            dots = VGroup(*[Dot(pxy[0].c2p(x, 0.6 * x), radius=0.08, color=AMBAR) for x in xs])
            rec = Line(pxy[0].c2p(-1.4, -0.84), pxy[0].c2p(1.4, 0.84), color=INK, stroke_width=2)
            self.play(Create(grupo_xy[0]), Create(rec), LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.08),
                      run_time=self.dur(1.0))

            # «los osciladores al cabo de un período»
            self.en("osc")
            base_o = Lo.base()
            curvas = [coseno(Lo, f, 1.0, SENAL, 2.2) for f in (0, 70, 140, 210, 280)]
            v1, v2 = Lo.vertical(0.25, AMBAR, 3.0, mitad=0.75), Lo.vertical(1.25, AMBAR, 3.0, mitad=0.75)
            rho = MathTex(r"\rho = 1", color=AMBAR).scale(1.1).move_to([3.6, -2.4, 0])
            self.play(Create(base_o), *[Create(k) for k in curvas], Create(v1), Create(v2), run_time=self.dur(1.0))
            self.pop(rho)

            # «Guarda también el punto más bajo»
            self.en("guarda")
            self.play(FadeOut(mult), FadeOut(grupo_xy), FadeOut(dots), FadeOut(rec), FadeOut(rho), run_time=0.3)
            self.play(c.animate.set_value(2.56), run_time=self.dur(1.0))
            pin = Dot(ax.c2p(0.6, 2.56), radius=0.13, color=AMBAR)
            self.add(pin)

            # «dos coma cinco seis»
            self.en("min")
            mn = MathTex(r"2{,}56", color=AMBAR).scale(1.0).next_to(pin, DOWN, buff=0.25)
            lm = MathTex(r"\lambda = 0{,}6", color=AMBAR).scale(0.75).next_to(ax.c2p(0.6, 0), DOWN, buff=0.3)
            self.play(FadeIn(mn), FadeIn(lm), run_time=0.5)

            # «porque volverá»
            self.en("volvera")
            vv = self.palabra("volverá", AMBAR, 0.7).move_to([-0.1, 3.3, 0])
            self.pop(vv)

            # «cae desde su pico»
            self.en("cae")
            base_r = Lr.base()
            rc = Lr.curva(tau, np.exp(-1.3 * np.abs(tau)), SENAL, 5)
            eje_r = Line(Lr.p(0, -0.2), Lr.p(0, 1.1), color=INK, stroke_width=2)
            ol = etiqueta("olvido", AMBAR, 0.6, BOLD).move_to([5.3, 1.9, 0])
            self.play(Create(base_r), Create(eje_r), Create(rc), FadeIn(ol), run_time=self.dur(1.2))

            # «un proceso»
            self.en("proceso")
            tt = np.linspace(0, 1, 7)
            nivel = [1, 1, -1, -1, 1, -1, -1]
            xs_ = []
            ys_ = []
            for a, b, n in zip(tt[:-1], tt[1:], nivel):
                xs_ += [a, b]
                ys_ += [n, n]
            Lt = Lienzo(ancho=4.6, alto=1.3, t_rango=(0, 1), v_max=1.3, centro=(3.6, -2.4))
            tel = Lt.curva(np.array(xs_), np.array(ys_), AMBAR, 4)
            self.play(Create(Lt.base()), Create(tel), run_time=self.dur(0.9), rate_func=linear)

            # «se ve muy bien»
            self.en("bien")
            self.resaltar(rc, color=AMBAR, escala=1.05)
        self.wait(1.0)
        parabola.clear_updaters()
        vertice.clear_updaters()
        self.limpiar()
