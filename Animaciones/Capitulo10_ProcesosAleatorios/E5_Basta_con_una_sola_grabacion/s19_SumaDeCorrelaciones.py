"""Escena 19 — Registro largo: la varianza es σ²/N por la suma de los coeficientes de correlación."""
from comun.escena import *


class SumaDeCorrelaciones(EscenaCurso):
    ESCENA = "19"

    def construct(self):
        Ls = Lienzo(ancho=11.0, alto=1.3, t_rango=(0, 1), v_max=3.0, centro=(0, 3.2))
        t = np.linspace(0, 1, 300)
        s = 1.2 * serie(21, 300, 0.6)
        Lt = Lienzo(ancho=10.0, alto=1.8, t_rango=(-1, 1), v_max=1.0, centro=(0, 1.3))
        tri = Polygon(Lt.p(-1, 0), Lt.p(-0.25, 0.97), Lt.p(0.25, 0.97), Lt.p(1, 0), color=AMBAR,
                      stroke_width=4).set_fill(AMBAR, 0.0)

        f = MathTex(r"\mathrm{Var}\approx", r"\frac{\sigma^2}{N}", r"\sum_k", r"\rho[k]", color=TXT).scale(1.2)
        f.move_to([0, -0.9, 0])
        f[1].set_color(AMBAR)
        f[3].set_color(CIAN)
        for p in f:
            p.set_opacity(0)
        self.add(f)

        with self.narrar("b1"):
            # «Para un registro largo»
            self.en("registro")
            self.play(Create(Ls.base()), Create(Ls.curva(t, s, SENAL, 2.5)), run_time=self.dur(1.2))

            # «casi plano»
            self.en("plano")
            self.play(Create(Lt.base()), Create(tri), run_time=self.dur(1.0))

            # «donde la autocovarianza importa»
            self.en("zona")
            tau = np.linspace(-1, 1, 160)
            cur = Lt.curva(tau, np.exp(-9 * np.abs(tau)), SENAL, 4)
            zona = Rectangle(width=1.4, height=1.75, color=SENAL, stroke_width=0).set_fill(SENAL, 0.25)
            zona.move_to(Lt.p(0, 0)).align_to(Lt.p(0, 0), DOWN)
            self.play(Create(cur), FadeIn(zona), run_time=self.dur(1.0))

            # «la varianza entre ene»
            self.en("sigman")
            self.play(f[0].animate.set_opacity(1), f[1].animate.set_opacity(1), run_time=0.5)

            # «multiplicada por la suma»
            self.en("suma")
            self.play(f[2].animate.set_opacity(1), run_time=0.4)

            # «coeficientes de correlación»
            self.en("rho")
            self.play(f[3].animate.set_opacity(1), run_time=0.4)
            self.resaltar(f[3], color=CIAN)

            # «en todas las separaciones»
            self.en("todas")
            llave = BraceBetweenPoints([-4.5, -2.0, 0], [4.5, -2.0, 0], direction=DOWN, color=INK)
            self.play(Create(llave), run_time=self.dur(0.8))

            # «la de cero, las de un lado y las del otro»
            self.en("lados")
            k0 = MathTex("k=0", color=AMBAR).scale(0.8).move_to([0, -2.9, 0])
            kp = MathTex("k>0", color=CIAN).scale(0.8).move_to([3.0, -2.9, 0])
            km = MathTex("k<0", color=CIAN).scale(0.8).move_to([-3.0, -2.9, 0])
            self.play(FadeIn(k0), FadeIn(kp), FadeIn(km), run_time=0.6)

            # «Esa suma dice»
            self.en("dice")
            self.resaltar(f[2], f[3], color=AMBAR)

            # «cuántas veces se repite»
            self.en("repite")
            self.play(FadeOut(llave), FadeOut(k0), FadeOut(kp), FadeOut(km), run_time=0.3)
            base = fila_puntos(6, 4.0, (-2.0, -3.2), SENAL, 0.12)
            copias = VGroup(*[Dot(base[i].get_center() + RIGHT * 0.22 * (j + 1), radius=0.12, color=AMBAR)
                              for i, n in enumerate((3, 1, 2, 3, 1, 2)) for j in range(n - 1)])
            self.play(FadeIn(base), run_time=0.3)
            self.play(LaggedStart(*[FadeIn(c, scale=0.4) for c in copias], lag_ratio=0.12), run_time=self.dur(1.2))

            # «cada dato»
            self.en("dato")
            self.resaltar(base[0], color=AMBAR, escala=1.8)
        self.wait(1.0)
        self.limpiar()
