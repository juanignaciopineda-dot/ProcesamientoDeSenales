"""Escena 4 - El filtro de Wiener no restringido.

Al pedir ortogonalidad en TODO el eje, la relacion vale para todo m y se
puede transformar. En frecuencia el problema se desacopla: cada Omega es
un problema de dos variables, identico al del capitulo 8.

    manim -pql s04_no_causal.py NoCausal
"""
from manim import *
import numpy as np
from comun import *


class NoCausal(Scene):
    def construct(self):
        configurar()

        tit = titulo("Wiener no causal: el problema se desacopla en frecuencia")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ la cadena de pasos
        p1 = MathTex(r"E\big[(y[n]-\hat{y}[n])\,x[n-m]\big]=0",
                     r"\quad \text{para \textbf{todo} } m", color=TXT).scale(0.68)
        p1[1].set_color(AMBAR)
        p1.next_to(tit, DOWN, buff=0.45)
        self.play(Write(p1))
        self.wait(1.2)

        p2 = MathTex(r"h[m] * C_{xx}[m] \;=\; C_{yx}[m]",
                     color=TXT).scale(0.72)
        p2.next_to(p1, DOWN, buff=0.4)
        self.play(FadeIn(p2, shift=UP * 0.12))
        self.wait(0.9)

        n_clave = nota("como vale en todo el eje, se pueden transformar los "
                       "dos lados", scale=0.48)
        n_clave.next_to(p2, DOWN, buff=0.3)
        self.play(FadeIn(n_clave))
        self.wait(1.5)

        p3 = MathTex(r"H(e^{j\Omega})\,D_{xx}(e^{j\Omega}) = D_{yx}(e^{j\Omega})",
                     color=TXT).scale(0.72)
        p3.move_to(p2)
        self.play(FadeOut(n_clave), Transform(p2, p3))
        self.wait(1.0)

        sol = MathTex(r"H(e^{j\Omega}) \;=\; "
                      r"\frac{D_{yx}(e^{j\Omega})}{D_{xx}(e^{j\Omega})}",
                      color=AZUL).scale(0.95)
        sol.next_to(p2, DOWN, buff=0.5)
        self.play(Write(sol))
        self.play(Circumscribe(sol, color=AZUL, buff=0.2, run_time=1.4))
        self.wait(1.2)

        # ------------------------------------------------ el paralelo con el cap 8
        self.play(FadeOut(VGroup(p1, p2)), sol.animate.scale(0.72)
                  .next_to(tit, DOWN, buff=0.5))

        cap8 = MathTex(r"\mathbf{a} = C_{XX}^{-1}\,\mathbf{c}_{XY}",
                       color=VERDE).scale(0.8)
        cap12 = MathTex(r"H = D_{xx}^{-1}\,D_{yx}", color=AZUL).scale(0.8)
        et8 = subtitulo("capítulo 8: dos variables", scale=0.46, color=VERDE)
        et12 = subtitulo("capítulo 12: dos procesos", scale=0.46, color=AZUL)
        col8 = VGroup(et8, cap8).arrange(DOWN, buff=0.22)
        col12 = VGroup(et12, cap12).arrange(DOWN, buff=0.22)
        par = VGroup(col8, MathTex(r"\Longleftrightarrow", color=AMBAR).scale(0.9),
                     col12).arrange(RIGHT, buff=0.8)
        par.next_to(sol, DOWN, buff=0.55)

        self.play(FadeIn(col8, shift=RIGHT * 0.15))
        self.play(FadeIn(par[1]))
        self.play(FadeIn(col12, shift=LEFT * 0.15))
        self.wait(1.6)

        misma = Text("Es la misma fórmula", color=AMBAR).scale(0.6)
        misma.next_to(par, DOWN, buff=0.45)
        self.play(FadeIn(misma, scale=1.1))
        self.wait(1.6)
        self.play(FadeOut(VGroup(par, misma, sol)))

        # ------------------------------------------------ el desacople
        expl = Text("¿Por qué es tan simple?", color=TXT).scale(0.62)
        expl.next_to(tit, DOWN, buff=0.45)
        self.play(FadeIn(expl))

        ax, lab = ejes([0, PI, PI], [0, 2.2], ancho=8.2, alto=2.0,
                       x_label=r"\Omega")
        ax.shift(DOWN * 0.9)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        # bins independientes
        nb = 11
        bordes = np.linspace(0, PI, nb + 1)
        bins = VGroup()
        for i in range(nb):
            a, b = bordes[i], bordes[i + 1]
            alto = 0.55 + 1.2 * np.exp(-((a + b) / 2 - 0.8) ** 2 / 0.45)
            r = Rectangle(width=(ax.c2p(b, 0)[0] - ax.c2p(a, 0)[0]) * 0.86,
                          height=(ax.c2p(0, alto)[1] - ax.c2p(0, 0)[1]),
                          stroke_color=AZUL, stroke_width=2,
                          fill_color=AZUL, fill_opacity=0.22)
            r.move_to(ax.c2p((a + b) / 2, alto / 2))
            bins.add(r)
        self.play(LaggedStart(*[FadeIn(b, scale=0.85) for b in bins],
                              lag_ratio=0.09, run_time=1.8))
        self.wait(0.5)

        n_des = nota("el filtro actúa de forma independiente en cada frecuencia:",
                     scale=0.48)
        n_des2 = nota("lo que hace en una banda no afecta a las demás",
                      scale=0.48)
        VGroup(n_des, n_des2).arrange(DOWN, buff=0.12).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(n_des), FadeIn(n_des2))
        self.wait(1.6)
        self.play(Indicate(bins[4], color=AMBAR, scale_factor=1.25),
                  run_time=1.0)
        self.wait(0.8)
        self.play(FadeOut(VGroup(n_des, n_des2)))

        # ------------------------------------------------ coherencia y MMSE
        self.play(FadeOut(VGroup(ax, lab, bins, expl)))

        coh = MathTex(r"\gamma_{yx}(e^{j\Omega}) = "
                      r"\frac{D_{yx}(e^{j\Omega})}"
                      r"{\sqrt{D_{yy}(e^{j\Omega})\,D_{xx}(e^{j\Omega})}}",
                      color=AMBAR).scale(0.75)
        coh_n = nota("la función de coherencia: el coeficiente de correlación, "
                     "frecuencia por frecuencia", scale=0.46)
        mmse = MathTex(r"\text{MMSE}=\frac{1}{2\pi}\int_{-\pi}^{\pi}"
                       r"D_{yy}(e^{j\Omega})\Big(1-|\gamma_{yx}(e^{j\Omega})|^2"
                       r"\Big)\,d\Omega", color=TXT).scale(0.68)
        cap8mmse = MathTex(r"\text{compará con}\quad \sigma_Y^2\,(1-\rho^2)",
                           color=VERDE).scale(0.6)

        grupo = VGroup(coh, coh_n, mmse, cap8mmse).arrange(DOWN, buff=0.38)
        grupo.next_to(tit, DOWN, buff=0.65)

        self.play(Write(coh))
        self.play(FadeIn(coh_n))
        self.wait(1.2)
        self.play(Write(mmse))
        self.wait(0.8)
        self.play(FadeIn(cap8mmse))
        self.wait(2.0)

        # ------------------------------------------------ cierre
        self.play(FadeOut(grupo))
        cierre = VGroup(
            Text("Donde la coherencia se acerca a 1,", color=INK).scale(0.58),
            Text("la estimación en esa banda es buena.", color=VERDE).scale(0.62),
            Text("Donde se acerca a 0, el filtro no puede hacer nada.",
                 color=ROJO).scale(0.58),
        ).arrange(DOWN, buff=0.26)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]), FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.6)
        self.play(FadeIn(cierre[2], shift=UP * 0.12))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
