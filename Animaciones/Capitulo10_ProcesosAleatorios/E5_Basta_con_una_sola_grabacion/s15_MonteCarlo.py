"""Escena 15 — Simulación: los puntos caen sobre la fórmula; el sensor es ergódico, la pila no."""
from comun.escena import *


def var_promedio(N, a=0.6, sigma2=4.0):
    """Varianza exacta del promedio de N muestras con memoria a por paso."""
    k = np.arange(1, N)
    return sigma2 / N * (1 + 2 * np.sum((1 - k / N) * a ** k))


class MonteCarlo(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        # log-log: x = log10 N (1,3 a 3,5), y = log10 var (−2,5 a 0,9)
        ancho, alto, cx, cy = 5.6, 3.2, 3.6, -0.4

        def px(N):
            return cx - ancho / 2 + (np.log10(N) - 1.3) / 2.2 * ancho

        def py(v):
            return cy - alto / 2 + (np.log10(v) + 2.5) / 3.4 * alto

        Ns = np.array([20, 100, 500, 2000])
        exactas = [var_promedio(int(n)) for n in Ns]
        rng = np.random.default_rng(5)
        sim = [v * float(np.exp(rng.normal(0, 0.05))) for v in exactas]

        L = Lienzo(ancho=5.6, alto=2.6, t_rango=(0, 1), v_max=3.0, centro=(-3.6, 1.6))
        t = np.linspace(0, 1, 120)
        stack = VGroup(*[L.curva(t, 1.0 * serie(400 + i, 120, 0.6) + 0.3 * serie(900 + i, 120, 0.99), SENAL, 1.6, 0.45)
                         for i in range(9)])

        with self.narrar("b1"):
            # «No son solo cuentas»
            self.en("cuentas")
            tx = caja("cuentas", INK, ancho=2.4, alto=0.7).move_to([-5.3, 3.5, 0])
            self.play(FadeIn(tx), run_time=0.4)

            # «miles de sensores»
            self.en("miles")
            self.play(Create(L.base()), LaggedStart(*[Create(c) for c in stack], lag_ratio=0.12), run_time=self.dur(1.6))

            # «cuánto se dispersan sus promedios»
            self.en("dispersan")
            fin = VGroup(*[Dot(L.p(1.03, float(np.mean(1.0 * serie(400 + i, 120, 0.6) + 0.3 * serie(900 + i, 120, 0.99)))),
                               radius=0.07, color=AMBAR) for i in range(9)])
            self.play(FadeIn(fin), run_time=0.6)

            # «los puntos caen exactamente»
            self.en("puntos")
            eje = VGroup(Line([cx - ancho / 2, cy - alto / 2, 0], [cx + ancho / 2, cy - alto / 2, 0], color=INK, stroke_width=2),
                         Line([cx - ancho / 2, cy - alto / 2, 0], [cx - ancho / 2, cy + alto / 2, 0], color=INK, stroke_width=2))
            nx = etiqueta("N", INK, 0.55).move_to([cx + ancho / 2 + 0.2, cy - alto / 2 - 0.3, 0])
            vy = MathTex(r"\mathrm{Var}", color=INK).scale(0.7).move_to([cx - ancho / 2, cy + alto / 2 + 0.3, 0])
            pts = VGroup(*[Dot([px(n), py(v), 0], radius=0.11, color=AMBAR) for n, v in zip(Ns, sim)])
            self.play(Create(eje), FadeIn(nx), FadeIn(vy), run_time=0.5)
            self.play(FadeIn(pts, scale=0.5), run_time=0.6)

            # «sobre la fórmula»
            self.en("formula")
            NN = np.unique(np.round(np.logspace(1.35, 3.3, 40)).astype(int))
            curva = VMobject(stroke_color=SENAL, stroke_width=4).set_fill(opacity=0)
            curva.set_points_as_corners([[px(n), py(var_promedio(int(n))), 0] for n in NN])
            self.play(Create(curva), run_time=self.dur(1.2))

            # «una grabación larga»
            self.en("larga")
            self.corte()
            Ll = Lienzo(ancho=11.0, alto=2.6, t_rango=(0, 1), v_max=3.0, centro=(0, 0.6))
            tt = np.linspace(0, 1, 400)
            s = 1.0 * serie(77, 400, 0.6)
            acum = np.cumsum(s) / np.arange(1, 401)
            gr = Ll.curva(tt, s, SENAL, 2.5, 0.6)
            mu = DashedLine(Ll.p(0, 0), Ll.p(1, 0), color=INK, stroke_width=2)
            tmu = MathTex(r"\mu=20", color=INK).scale(0.7).next_to(Ll.p(1, 0), RIGHT, buff=0.1)
            self.play(Create(Ll.base()), Create(gr), Create(mu), FadeIn(tmu), run_time=self.dur(1.2))

            # «se pega a la media»
            self.en("pega")
            pr = Ll.curva(tt, acum * 1.0, AMBAR, 5)
            self.play(Create(pr), run_time=self.dur(1.6), rate_func=linear)

            # «El sensor es ergódico»
            self.en("ergo")
            e1 = caja("sensor", SENAL, ancho=2.8, alto=0.8).move_to([-3.6, -2.4, 0])
            tl = tilde(VERDE, 0.45).next_to(e1, RIGHT, buff=0.15)
            self.play(FadeIn(e1), FadeIn(tl), run_time=0.4)

            # «la pila, no»
            self.en("no")
            e2 = caja("pila", AMBAR, ancho=2.8, alto=0.8).move_to([3.0, -2.4, 0])
            x = cruz(ROJO, 0.45).next_to(e2, RIGHT, buff=0.15)
            self.sfx("error")
            self.play(FadeIn(e2), FadeIn(x), run_time=0.4)

            # «la memoria»
            self.en("memoria")
            mem = self.palabra("memoria", AMBAR, 0.8).move_to([0, -3.5, 0])
            self.pop(mem)

            # «se borra»
            self.en("borra")
            Lb = Lienzo(ancho=2.6, alto=0.8, t_rango=(0, 2), v_max=1.0, centro=(-3.6, -3.4))
            tau = np.linspace(0, 2, 80)
            self.play(Create(Lb.curva(tau, np.exp(-2.5 * tau), SENAL, 4)), run_time=self.dur(0.6))

            # «la otra no»
            self.en("dura")
            Ld = Lienzo(ancho=2.6, alto=0.8, t_rango=(0, 2), v_max=1.0, centro=(3.0, -3.4))
            self.play(Create(Line(Ld.p(0, 1.0), Ld.p(2, 1.0), color=ROJO, stroke_width=4)), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
