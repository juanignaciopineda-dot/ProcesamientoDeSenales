"""Escena 4 - Que puede y que no puede ser una autocorrelacion.

Teorema de Bochner (Herglotz en discreto): una funcion es autocorrelacion
de un proceso WSS si y solo si su transformada es real, par y NO NEGATIVA.
La rectangular falla; la triangular pasa.

    manim -pql s04_bochner.py Bochner
"""
from manim import *
import numpy as np
from comun import *

TAU0 = 1.0
W_MAX = 11.0


def S_rect(w):
    """FT de un pulso rectangular de ancho 2*TAU0: se hace negativa."""
    if abs(w) < 1e-7:
        return 2 * TAU0
    return 2 * np.sin(w * TAU0) / w


def S_tri(w):
    """FT de un pulso triangular de base 2*TAU0: sinc^2, nunca negativa."""
    if abs(w) < 1e-7:
        return TAU0
    u = w * TAU0 / 2
    return TAU0 * (np.sin(u) / u) ** 2


def R_rect(t):
    return 1.0 if abs(t) < TAU0 else 0.0


def R_tri(t):
    return max(0.0, 1.0 - abs(t) / TAU0)


class Bochner(Scene):
    def construct(self):
        configurar()

        tit = titulo("¿Cualquier función puede ser una autocorrelación?")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.4)

        criterio = VGroup(
            Text("Criterio:", color=TXT).scale(0.55),
            MathTex(r"S_{xx}(j\omega)\;\geq\;0", color=AMBAR).scale(0.72),
            Text("en toda frecuencia", color=INK).scale(0.5),
        ).arrange(RIGHT, buff=0.25)
        criterio.next_to(tit, DOWN, buff=0.4)
        self.play(FadeIn(criterio))
        self.wait(1.2)
        self.play(criterio.animate.scale(0.75).to_edge(UP, buff=1.15))

        # ============================================ CASO 1: rectangular
        ax_r, lab_r = ejes([-2.6, 2.6, 2.6], [0, 1.3], ancho=4.4, alto=2.0,
                           x_label=r"\tau")
        ax_r.shift(LEFT * 3.5 + DOWN * 0.7)
        lab_r.next_to(ax_r.x_axis.get_end(), DR, buff=0.1)

        rect = VMobject(color=MAGENTA, stroke_width=4).set_points_as_corners([
            ax_r.c2p(-2.6, 0), ax_r.c2p(-TAU0, 0), ax_r.c2p(-TAU0, 1),
            ax_r.c2p(TAU0, 1), ax_r.c2p(TAU0, 0), ax_r.c2p(2.6, 0)])
        r_lbl = MathTex(r"R(\tau)\ \text{rectangular}", color=MAGENTA).scale(0.55)
        r_lbl.next_to(ax_r, UP, buff=0.25)

        ax_s, lab_s = ejes([-W_MAX, W_MAX, W_MAX], [-0.8, 2.4], ancho=5.0,
                           alto=2.4, x_label=r"\omega")
        ax_s.shift(RIGHT * 3.3 + DOWN * 0.7)
        lab_s.next_to(ax_s.x_axis.get_end(), DR, buff=0.1)

        self.play(Create(ax_r), FadeIn(lab_r), Create(rect), FadeIn(r_lbl))
        self.play(Create(ax_s), FadeIn(lab_s))

        sinc = ax_s.plot(S_rect, x_range=[-W_MAX, W_MAX, 0.02],
                         color=MAGENTA, stroke_width=4)
        s_lbl = MathTex(r"\mathcal{F}\{R\} = \frac{2\sin(\omega\tau_0)}{\omega}",
                        color=MAGENTA).scale(0.55)
        s_lbl.next_to(ax_s, UP, buff=0.18)
        self.play(Create(sinc, run_time=1.8), FadeIn(s_lbl))
        self.wait(0.6)

        # la parte negativa, resaltada
        linea0 = DashedLine(ax_s.c2p(-W_MAX, 0), ax_s.c2p(W_MAX, 0),
                           color=INK, stroke_width=1.6, dash_length=0.08)
        neg = ax_s.get_area(sinc, x_range=(-W_MAX, W_MAX), color=ROJO,
                            opacity=0.0, stroke_width=0)
        # areas negativas explicitas (los lobulos bajo cero)
        lobulos = VGroup()
        for a, b in [(np.pi / TAU0, 2 * np.pi / TAU0),
                     (-2 * np.pi / TAU0, -np.pi / TAU0),
                     (3 * np.pi / TAU0, 4 * np.pi / TAU0),
                     (-4 * np.pi / TAU0, -3 * np.pi / TAU0)]:
            if abs(b) <= W_MAX:
                lobulos.add(ax_s.get_area(sinc, x_range=(a, b), color=ROJO,
                                          opacity=0.7, stroke_width=0))
        self.play(Create(linea0))
        self.play(FadeIn(lobulos), run_time=0.8)

        marca_mal = veredicto(False, "se hace negativa")
        marca_mal.next_to(ax_s, DOWN, buff=0.35)
        self.play(FadeIn(marca_mal, scale=1.2))
        self.wait(0.6)
        veredicto1 = Text("una rectangular NO puede ser autocorrelación",
                          color=ROJO).scale(0.55)
        veredicto1.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(veredicto1))
        self.wait(1.8)

        # ============================================ CASO 2: triangular
        self.play(FadeOut(VGroup(lobulos, marca_mal, veredicto1)))

        tri = VMobject(color=VERDE, stroke_width=4).set_points_as_corners([
            ax_r.c2p(-2.6, 0), ax_r.c2p(-TAU0, 0), ax_r.c2p(0, 1),
            ax_r.c2p(TAU0, 0), ax_r.c2p(2.6, 0)])
        r_lbl2 = MathTex(r"R(\tau)\ \text{triangular}", color=VERDE).scale(0.55)
        r_lbl2.move_to(r_lbl)

        sinc2 = ax_s.plot(S_tri, x_range=[-W_MAX, W_MAX, 0.02],
                          color=VERDE, stroke_width=4)
        s_lbl2 = MathTex(r"\mathcal{F}\{R\} = \tau_0\,\mathrm{sinc}^2"
                         r"\!\left(\tfrac{\omega\tau_0}{2}\right)",
                         color=VERDE).scale(0.55)
        s_lbl2.move_to(s_lbl)

        self.play(Transform(rect, tri), Transform(r_lbl, r_lbl2), run_time=1.2)
        self.play(Transform(sinc, sinc2), Transform(s_lbl, s_lbl2), run_time=1.4)
        self.wait(0.4)

        area_ok = ax_s.get_area(sinc2, x_range=(-W_MAX, W_MAX), color=VERDE,
                                opacity=0.35, stroke_width=0)
        self.play(FadeIn(area_ok))

        marca_ok = veredicto(True, "nunca baja de cero")
        marca_ok.next_to(ax_s, DOWN, buff=0.35)
        self.play(FadeIn(marca_ok, scale=1.2))
        veredicto2 = Text("una triangular SÍ puede ser autocorrelación",
                          color=VERDE).scale(0.55)
        veredicto2.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(veredicto2))
        self.wait(2.0)

        # ============================================ cierre
        self.play(FadeOut(VGroup(ax_r, lab_r, rect, r_lbl, ax_s, lab_s, sinc,
                                 s_lbl, area_ok, linea0, marca_ok, veredicto2,
                                 criterio, neg)))
        cierre = VGroup(
            Text("Teorema de Bochner", color=AMBAR, weight=BOLD).scale(0.7),
            Text("(Herglotz, en tiempo discreto)", color=INK).scale(0.48),
            MathTex(r"R(\tau)\ \text{es autocorrelación válida}"
                    r"\iff \mathcal{F}\{R\}\ \text{real, par y}\ \geq 0",
                    color=TXT).scale(0.62),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.15), FadeIn(cierre[1]))
        self.wait(0.4)
        self.play(Write(cierre[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
