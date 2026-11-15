"""Escena 21 — Tamaño de muestra efectivo: N_ef = N / Σ ρ[k]."""
from comun.escena import *


class NEfectiva(EscenaCurso):
    ESCENA = "21"

    def construct(self):
        fila = fila_puntos(40, 10.0, (0, 1.3), SENAL, 0.08)
        grupos = VGroup(*[RoundedRectangle(corner_radius=0.1, width=0.95, height=0.4, color=VERDE, stroke_width=3)
                          .move_to(VGroup(*fila[4 * i:4 * i + 4])) for i in range(10)])

        f = MathTex(r"N_{\mathrm{ef}}", "=", "N", "/", r"\sum_k \rho[k]", color=TXT).scale(1.2).move_to([0, -0.4, 0])
        f[0].set_color(VERDE)
        f[4].set_color(CIAN)
        for p in f:
            p.set_opacity(0)
        self.add(f)

        base, dx, y0, esc = ejes_k(7, ancho=8.0, alto=1.3, v_max=1.0, centro=(-1.0, -3.4))
        dx = 0.5
        bars = VGroup(*[barra_k(k, 0.9 ** abs(k), dx, y0, esc, -1.0, CIAN) for k in range(-7, 8)])

        with self.narrar("b1"):
            # «cuatro veces»
            self.en("cuatro")
            v = MathTex(r"\mathrm{Var}=4\times\frac{\sigma^2}{N}", color=TXT).scale(1.2).move_to([0, 3.2, 0])
            self.play(Write(v), run_time=self.dur(1.2))

            # «con datos independientes»
            self.en("indep")
            ti = etiqueta("independientes", INK, 0.55).move_to([0.8, 2.3, 0])
            self.play(FadeIn(ti), run_time=0.4)

            # «mil muestras del sensor»
            self.en("mil")
            self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in fila], lag_ratio=0.02), run_time=self.dur(1.0))

            # «mil entre cuatro»
            self.en("entre4")
            e4 = MathTex(r"1000\,/\,4", color=AMBAR).scale(1.0).move_to([-4.5, 2.2, 0])
            self.play(FadeIn(e4), run_time=0.4)

            # «doscientas cincuenta independientes»
            self.en("n250")
            self.play(Create(grupos), run_time=self.dur(0.9))
            n250 = self.palabra("250", VERDE, 1.3).move_to([5.0, 2.2, 0])
            self.pop(n250)

            # «A eso se le llama»
            self.en("llama")
            ll = BraceBetweenPoints([-5.0, 0.85, 0], [5.0, 0.85, 0], direction=DOWN, color=VERDE)
            self.play(Create(ll), run_time=0.5)

            # «tamaño de muestra efectivo»
            self.en("neff")
            self.play(f[0].animate.set_opacity(1), f[1].animate.set_opacity(1), run_time=0.5)

            # «el número de muestras»
            self.en("numero")
            self.play(f[2].animate.set_opacity(1), run_time=0.4)

            # «dividido entre la suma»
            self.en("dividido")
            self.play(f[3].animate.set_opacity(1), run_time=0.4)

            # «de los coeficientes de correlación»
            self.en("rho")
            self.play(f[4].animate.set_opacity(1), run_time=0.5)

            # «Con una memoria más larga»
            self.en("larga")
            self.play(Create(base), Create(bars), run_time=self.dur(1.0))

            # «cero coma nueve por paso»
            self.en("r09")
            tr = MathTex(r"\rho=0{,}9\ \text{por paso}", color=CIAN).scale(0.85).move_to([4.6, -2.3, 0])
            self.play(FadeIn(tr), run_time=0.4)

            # «diecinueve»
            self.en("v19")
            s19 = MathTex(r"\sum=19", color=AMBAR).scale(1.4).move_to([4.6, -3.3, 0])
            e53 = MathTex(r"1000/19\approx53", color=AMBAR).scale(1.0).move_to([-4.3, -0.4, 0])
            self.pop(s19)
            self.play(FadeIn(e53), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
