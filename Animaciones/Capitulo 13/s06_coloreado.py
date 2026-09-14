"""Escena 6 - Deteccion en ruido coloreado: blanquear y despues adaptar.

Si el ruido no es blanco, se lo modela como blanco filtrado y se blanquea
primero con 1/M; el problema se reduce al caso conocido. El filtro total
resulta H = S(e^-jW) / (D_vv/sigma^2): grande donde el SNR de entrada es
alto. Y ahora la forma de s[n] SI importa.

    manim -pql s06_coloreado.py RuidoColoreado
"""
from manim import *
import numpy as np
from comun import *


def Dvv(w, a=0.6):
    """PSD de un AR(1): ruido coloreado, mas fuerte en baja frecuencia."""
    return 1.0 / (1 - 2 * a * np.cos(w) + a ** 2)


def Smag2(w, centro=1.4, ancho=0.35):
    return np.exp(-((w - centro) ** 2) / ancho) + np.exp(-((w + centro) ** 2) / ancho)


class RuidoColoreado(Scene):
    def construct(self):
        configurar()

        tit = titulo("Ruido coloreado: blanquear y después adaptar")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        idea = subtitulo("mismo truco del capítulo 11: pensar el ruido "
                         "coloreado como blanco filtrado", scale=0.48)
        idea.next_to(tit, DOWN, buff=0.35).set_x(0)
        self.play(FadeIn(idea))
        self.wait(1.2)
        self.play(FadeOut(idea))

        # ------------------------------------------------ diagrama
        r_lbl = MathTex("r[n]", color=INK).scale(0.5)
        blanq = bloque(r"1/M(z)", color=VERDE, ancho=2.0, alto=0.9, scale=0.42)
        p_lbl = MathTex("p[n]", color=INK).scale(0.5)
        adap = bloque(r"\text{adaptado a }p", color=AZUL, ancho=2.6, alto=0.9,
                     scale=0.4)
        g_lbl = MathTex("g[0]", color=INK).scale(0.5)
        cadena = VGroup(r_lbl, blanq, p_lbl, adap, g_lbl).arrange(RIGHT, buff=0.55)
        cadena.next_to(tit, DOWN, buff=0.6).set_x(0)
        flechas = VGroup(*[flecha(cadena[i].get_right(), cadena[i + 1].get_left())
                           for i in range(len(cadena) - 1)])
        self.play(FadeIn(r_lbl), FadeIn(blanq))
        self.play(GrowArrow(flechas[0]))
        self.play(FadeIn(p_lbl))
        self.play(GrowArrow(flechas[1]))
        self.play(FadeIn(adap))
        self.play(GrowArrow(flechas[2]))
        self.play(FadeIn(g_lbl))
        self.play(GrowArrow(flechas[3]))
        n_diag = nota("después del blanqueador: señal $p[n]$ (=$s$ pasada "
                      "por $1/M$) en ruido BLANCO", scale=0.44)
        n_diag.next_to(cadena, DOWN, buff=0.4)
        self.play(FadeIn(n_diag))
        self.wait(1.8)
        self.play(FadeOut(VGroup(cadena, flechas, n_diag)))

        # ------------------------------------------------ el filtro total
        Htot = MathTex(r"H(e^{j\Omega})=\frac{S(e^{-j\Omega})}"
                       r"{D_{vv}(e^{j\Omega})/\sigma^2}", color=AZUL).scale(0.85)
        Htot.next_to(tit, DOWN, buff=0.6).set_x(0)
        caja = SurroundingRectangle(Htot, color=AZUL, buff=0.28)
        self.play(Write(Htot), Create(caja))
        self.wait(1.4)
        self.play(VGroup(Htot, caja).animate.scale(0.8)
                  .next_to(tit, DOWN, buff=0.35).set_x(0))

        # ------------------------------------------------ los espectros
        w = np.linspace(-np.pi, np.pi, 400)
        ax, lab = ejes([-PI, PI, PI], [0, 3.4, 3.4], ancho=7.6, alto=2.4,
                       x_label=r"\Omega")
        ax.next_to(Htot, DOWN, buff=0.4)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        c_s = ax.plot(Smag2, x_range=[-PI, PI, 0.01], color=VERDE, stroke_width=3.5)
        c_v = ax.plot(lambda x: Dvv(x) * 0.55, x_range=[-PI, PI, 0.01],
                     color=ROJO, stroke_width=3.5)
        c_h = ax.plot(lambda x: 1.3 * Smag2(x) / (Dvv(x) * 0.55),
                     x_range=[-PI, PI, 0.01], color=AZUL, stroke_width=4)
        l_s = MathTex(r"|S|^2", color=VERDE).scale(0.5).next_to(
            ax.c2p(1.4, Smag2(1.4)), UP, buff=0.08)
        l_v = MathTex(r"D_{vv}", color=ROJO).scale(0.5).next_to(
            ax.c2p(0, Dvv(0) * 0.55), UP, buff=0.35)
        l_h = MathTex(r"|H|", color=AZUL).scale(0.5).next_to(
            ax.c2p(1.4, 1.3 * Smag2(1.4) / (Dvv(1.4) * 0.55)), UR, buff=0.08)
        self.play(Create(c_v), FadeIn(l_v))
        self.play(Create(c_s), FadeIn(l_s))
        self.play(Create(c_h), FadeIn(l_h))
        n_sens = nota("$H$ es grande donde la señal es fuerte Y el ruido "
                      "débil: donde el SNR de entrada es alto", scale=0.44)
        n_sens.next_to(ax, DOWN, buff=0.3)
        self.play(FadeIn(n_sens))
        self.wait(2.0)
        self.play(FadeOut(VGroup(Htot, caja, ax, lab, c_s, c_v, c_h, l_s, l_v,
                                 l_h, n_sens)))

        # ------------------------------------------------ desempeno depende de forma
        Ep = MathTex(r"\frac{E_p}{\sigma^2}=\frac{1}{2\pi}\int_{-\pi}^{\pi}"
                     r"\frac{|S(e^{j\Omega})|^2}{D_{vv}(e^{j\Omega})}\,d\Omega",
                     color=AMBAR).scale(0.72)
        Ep.next_to(tit, DOWN, buff=0.6).set_x(0)
        self.play(Write(Ep))
        n_Ep = nota("ahora SÍ depende de la FORMA de $s[n]$, no solo de "
                    "su energía:\nconviene poner la señal donde el ruido "
                    "es débil", scale=0.46)
        n_Ep.next_to(Ep, DOWN, buff=0.35)
        self.play(FadeIn(n_Ep))
        self.wait(2.2)
        self.play(FadeOut(VGroup(Ep, n_Ep)))

        # ------------------------------------------------ nyquist
        nyq_tit = Text("De paso: diseño de pulsos de Nyquist", color=TXT).scale(0.56)
        nyq_tit.next_to(tit, DOWN, buff=0.5).set_x(0)
        self.play(FadeIn(nyq_tit))

        pulso_total = MathTex(r"P(j\omega)H_c(j\omega)H_c(-j\omega)P(-j\omega)"
                              r"=|P(j\omega)|^2|H_c(j\omega)|^2", color=TXT).scale(0.58)
        pulso_total.next_to(nyq_tit, DOWN, buff=0.4)
        self.play(Write(pulso_total))
        n_nyq = nota("la condición de no-ISI va sobre $|P|^2$, no sobre $P$:\n"
                     "el conformado se reparte entre transmisor y receptor "
                     "→ raíz de coseno alzado", scale=0.44)
        n_nyq.next_to(pulso_total, DOWN, buff=0.35)
        self.play(FadeIn(n_nyq))
        self.wait(2.2)
        self.play(FadeOut(VGroup(nyq_tit, pulso_total, n_nyq)))

        # ------------------------------------------------ cierre
        cierre = VGroup(
            Text("Blanquear no es un caso especial:", color=INK).scale(0.56),
            Text("es la receta general del capítulo 11, otra vez.",
                 color=AZUL).scale(0.58),
            nota("y esta vez sí importa dónde pusiste la energía", scale=0.48),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.4)
        self.play(FadeIn(cierre[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
