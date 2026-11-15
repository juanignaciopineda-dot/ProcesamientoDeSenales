"""Escena 13 — Ergodico: el promedio temporal sobre [−T, T] se acerca a la media del ensemble."""
from comun.escena import *


class Ergodico(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        L = Lienzo(ancho=8.4, alto=2.4, t_rango=(-4, 4), v_max=1.6, centro=(-2.5, 0.6))
        x = np.linspace(-4, 4, 320)
        y = 0.6 * serie(33, 320, 0.97)
        y = y - float(np.mean(y)) * 0.0
        senal = L.curva(x, y, SENAL, 3.5)
        base = L.base()
        ventana = Rectangle(width=float(L.x(1) - L.x(-1)), height=2.3, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.12)
        ventana.move_to([float(L.x(0)), 0.6, 0])
        t_p = MathTex(r"-T", color=AMBAR).scale(0.8).next_to(ventana, UP, buff=0.08).align_to(ventana, LEFT)
        t_q = MathTex(r"T", color=AMBAR).scale(0.8).next_to(ventana, UP, buff=0.08).align_to(ventana, RIGHT)
        # promedio temporal acumulado contra T (panel de la derecha)
        Ts = np.linspace(0.3, 4.0, 90)
        prom = np.array([np.mean(y[(x >= -T) & (x <= T)]) for T in Ts])
        P = Lienzo(ancho=3.6, alto=2.0, t_rango=(0.3, 4.0), v_max=1.0, centro=(4.6, 0.6))
        curva_p = P.curva(Ts, prom * (0.8 / max(abs(prom).max(), 1e-6)), AMBAR, 4)
        base_p = P.base()
        mu = DashedLine(P.p(0.3, 0), P.p(4.0, 0), color=VERDE, stroke_width=3)
        t_mu = MathTex(r"\mu_X", color=VERDE).scale(0.9).next_to(P.p(4.0, 0), RIGHT, buff=0.1)
        t_panel = etiqueta("promedio temporal", AMBAR, 0.5).move_to([4.6, 2.0, 0])
        f = MathTex(r"\lim_{T\to\infty}", r"\frac{1}{2T}", r"\int_{-T}^{T}", r"x(t)\,dt", r"=\mu_X", color=TXT)
        f.scale(1.5).move_to([0, -2.4, 0])
        f[0].set_color(AMBAR), f[1].set_color(RUIDO), f[4].set_color(VERDE)
        cuadro = SurroundingRectangle(f, color=AMBAR, buff=0.2, stroke_width=3)
        w1 = self.palabra("ergódico", AMBAR, 1.3).move_to([0, 3.3, 0])
        w2 = etiqueta("ergódico en media", AMBAR, 0.8, BOLD).move_to([0, 3.3, 0])

        with self.narrar("b1"):
            # «se llama ergódico»
            self.en("ergodico")
            self.pop(w1)

            # «Ergódico en media»
            self.en("enmedia")
            self.play(ReplacementTransform(w1, w2), run_time=self.dur(0.7))

            # «el promedio temporal»
            self.en("temporal")
            self.play(Create(base), Create(senal), run_time=self.dur(1.6))
            self.play(FadeIn(ventana), FadeIn(t_p), FadeIn(t_q), run_time=0.4)
            self.play(Create(base_p), FadeIn(t_panel), run_time=0.4)

            # «ventana cada vez más larga»
            self.en("ventana")
            self.play(ventana.animate.stretch_to_fit_width(float(L.x(4) - L.x(-4))).move_to([float(L.x(0)), 0.6, 0]),
                      t_p.animate.move_to([float(L.x(-4)) + 0.25, 2.0, 0]),
                      t_q.animate.move_to([float(L.x(4)) - 0.2, 2.0, 0]),
                      Create(curva_p), run_time=self.dur(2.4))

            # «la media del ensemble»
            self.en("ensemble")
            self.play(Create(mu), FadeIn(t_mu), run_time=self.dur(0.7))

            # «un límite»
            self.en("limite")
            self.play(Write(f[0]), run_time=self.dur(0.8))

            # «uno entre dos te»
            self.en("uno_dos_t")
            self.play(Write(f[1]), run_time=self.dur(0.7))

            # «la integral de la señal»
            self.en("integral")
            self.play(Write(f[2]), Write(f[3]), run_time=self.dur(1.0))

            # «entre menos te y te»
            self.en("limites")
            self.play(Indicate(f[2], color=AMBAR, scale_factor=1.25), run_time=self.dur(0.9))

            # «crece sin fin»
            self.en("fin")
            self.play(Write(f[4]), run_time=self.dur(0.8))
            self.play(Create(cuadro), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
