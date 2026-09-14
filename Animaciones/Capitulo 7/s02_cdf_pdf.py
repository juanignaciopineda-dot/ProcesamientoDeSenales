"""Escena 2 - CDF, PDF y PMF: los tres casos.

La CDF se define igual siempre; lo que cambia es su forma. Continua ->
derivable, la derivada es la PDF. Discreta -> escalera, los saltos son la
PMF. Mixta -> curva suave con un salto, y ahi aparece el impulso de Dirac.

    manim -pql s02_cdf_pdf.py CDFyPDF
"""
from manim import *
import numpy as np
from comun import *

X0, X1 = -3.4, 3.4
MU, SIG = 0.0, 1.0


def F_cont(x):
    """CDF gaussiana, via una aproximacion suave de la funcion error."""
    z = (x - MU) / (SIG * np.sqrt(2))
    # aproximacion de erf con error < 1e-7, mas que suficiente para dibujar
    t = 1 / (1 + 0.3275911 * abs(z))
    y = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t
              - 0.284496736) * t + 0.254829592) * t * np.exp(-z * z)
    erf = y if z >= 0 else -y
    return 0.5 * (1 + erf)


def f_cont(x):
    return gauss(x, MU, SIG)


SALTOS = [(-1.6, 0.25), (0.0, 0.40), (1.7, 0.35)]       # (posicion, masa)


def F_disc(x):
    return sum(m for p, m in SALTOS if x >= p)


X_MIX, MASA_MIX = 0.8, 0.32


def F_mix(x):
    """Mitad continua, mitad atomo en X_MIX."""
    base = (1 - MASA_MIX) * F_cont(x)
    return base + (MASA_MIX if x >= X_MIX else 0.0)


class CDFyPDF(Scene):
    def construct(self):
        configurar()

        tit = titulo("La CDF y su derivada")
        self.play(FadeIn(tit, shift=DOWN * 0.2))

        defi = MathTex(r"F_X(x)\;=\;P(X\leq x)", color=TXT).scale(0.85)
        defi.next_to(tit, DOWN, buff=0.4)
        self.play(Write(defi))
        self.wait(0.8)
        univ = nota("la definición es la misma para los tres tipos de variable; "
                    "lo que cambia es la forma", scale=0.46)
        univ.next_to(defi, DOWN, buff=0.25)
        self.play(FadeIn(univ))
        self.wait(1.8)
        self.play(FadeOut(univ), defi.animate.scale(0.7).to_edge(UP, buff=1.15))

        # ------------------------------------------------ los dos paneles
        ax_F, lab_F = ejes([X0, X1, X1], [0, 1.18], ancho=5.2, alto=2.3,
                           x_label="x")
        ax_F.shift(LEFT * 3.4 + DOWN * 0.9)
        lab_F.next_to(ax_F.x_axis.get_end(), DR, buff=0.1)
        # OJO: subtitulo() devuelve un Text, que no interpreta LaTeX. Para
        # mezclar palabra y formula hay que combinar Text con MathTex.
        def rotulo(palabra, formula, color):
            return VGroup(Text(palabra, color=color).scale(0.5),
                          MathTex(formula, color=color).scale(0.62)
                          ).arrange(RIGHT, buff=0.22)

        t_F = rotulo("CDF", r"F_X(x)", AZUL)
        t_F.next_to(ax_F, UP, buff=0.22)
        uno = DashedLine(ax_F.c2p(X0, 1), ax_F.c2p(X1, 1), color=INK,
                         stroke_width=1.4, dash_length=0.08)
        uno_l = MathTex("1", color=INK).scale(0.5).next_to(ax_F.c2p(X0, 1),
                                                           LEFT, buff=0.12)

        ax_f, lab_f = ejes([X0, X1, X1], [0, 0.62], ancho=5.2, alto=2.3,
                           x_label="x")
        ax_f.shift(RIGHT * 3.4 + DOWN * 0.9)
        lab_f.next_to(ax_f.x_axis.get_end(), DR, buff=0.1)
        t_f = rotulo("PDF", r"f_X(x)", VERDE)
        t_f.next_to(ax_f, UP, buff=0.22)

        self.play(Create(ax_F), FadeIn(lab_F), FadeIn(t_F),
                  Create(uno), FadeIn(uno_l),
                  Create(ax_f), FadeIn(lab_f), FadeIn(t_f))

        # ============================================ 1. CONTINUA
        etiqueta = Text("VARIABLE CONTINUA", color=AZUL, weight=BOLD).scale(0.55)
        etiqueta.next_to(defi, DOWN, buff=0.3)
        F1 = ax_F.plot(F_cont, x_range=[X0, X1, 0.02], color=AZUL,
                       stroke_width=4, use_smoothing=False)
        f1 = ax_f.plot(f_cont, x_range=[X0, X1, 0.02], color=VERDE,
                       stroke_width=4, use_smoothing=False)
        a1 = ax_f.get_area(f1, x_range=(X0, X1), color=VERDE, opacity=0.15,
                           stroke_width=0)

        self.play(FadeIn(etiqueta))
        self.play(Create(F1, run_time=1.4))
        self.wait(0.4)

        deriv = MathTex(r"f_X(x)=\frac{d}{dx}F_X(x)", color=VERDE).scale(0.6)
        deriv.next_to(ax_f, DOWN, buff=0.35)
        self.play(Create(f1, run_time=1.2), FadeIn(a1), Write(deriv))
        self.wait(0.6)

        crece = nota("la CDF nunca decrece  ⇒  la PDF nunca es negativa",
                     scale=0.46)
        crece.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(crece))
        self.wait(1.8)
        self.play(FadeOut(crece))

        # ---- la banda [a, b]
        a, b = -0.7, 1.3
        banda_f = ax_f.get_area(f1, x_range=(a, b), color=AMBAR, opacity=0.7,
                                stroke_width=0)
        p_a, p_b = F_cont(a), F_cont(b)
        seg = Line(ax_F.c2p(b, p_a), ax_F.c2p(b, p_b), color=AMBAR,
                   stroke_width=5)
        guia_a = DashedLine(ax_F.c2p(a, 0), ax_F.c2p(a, p_a), color=INK,
                            stroke_width=1.4, dash_length=0.07)
        guia_b = DashedLine(ax_F.c2p(b, 0), ax_F.c2p(b, p_b), color=INK,
                            stroke_width=1.4, dash_length=0.07)
        h_a = DashedLine(ax_F.c2p(a, p_a), ax_F.c2p(b, p_a), color=INK,
                         stroke_width=1.4, dash_length=0.07)

        self.play(FadeIn(banda_f), Create(guia_a), Create(guia_b),
                  Create(h_a), Create(seg))
        rel = MathTex(r"P(a<X\leq b)=F_X(b)-F_X(a)=\int_a^b f_X(x)\,dx",
                      color=AMBAR).scale(0.62)
        rel.to_edge(DOWN, buff=0.42)
        # se oculta 'deriv' mientras dura 'rel': comparten la franja de abajo
        self.play(FadeOut(deriv), Write(rel))
        self.wait(2.2)
        self.play(FadeOut(VGroup(banda_f, guia_a, guia_b, h_a, seg, rel)),
                  FadeIn(deriv))

        # ============================================ 2. DISCRETA
        et2 = Text("VARIABLE DISCRETA", color=MAGENTA, weight=BOLD).scale(0.55)
        et2.move_to(etiqueta)

        F2 = VMobject(color=MAGENTA, stroke_width=4)
        pts, acum = [ax_F.c2p(X0, 0)], 0.0
        for p, m in SALTOS:
            pts += [ax_F.c2p(p, acum), ax_F.c2p(p, acum + m)]
            acum += m
        pts.append(ax_F.c2p(X1, acum))
        F2.set_points_as_corners(pts)

        f2 = stem(ax_f, [p for p, _ in SALTOS], [m for _, m in SALTOS],
                  color=MAGENTA, ancho=4.5, radio=0.06)
        t_f2 = rotulo("PMF", r"p_X(x_j)", MAGENTA)
        t_f2.move_to(t_f)
        deriv2 = MathTex(r"P(X=x_j)=p_X(x_j)", color=MAGENTA).scale(0.6)
        deriv2.move_to(deriv)

        self.play(Transform(etiqueta, et2), Transform(F1, F2),
                  FadeOut(VGroup(f1, a1)), Transform(t_f, t_f2),
                  Transform(deriv, deriv2), run_time=1.6)
        self.play(FadeIn(f2))
        self.wait(0.6)
        obs2 = nota("la CDF es una escalera: cada salto es la masa de ese valor",
                    scale=0.46)
        obs2.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(obs2))
        self.wait(2.0)
        self.play(FadeOut(obs2))

        # ============================================ 3. MIXTA
        et3 = Text("VARIABLE MIXTA", color=AMBAR, weight=BOLD).scale(0.55)
        et3.move_to(etiqueta)

        F3 = VMobject(color=AMBAR, stroke_width=4)
        izq = np.arange(X0, X_MIX, 0.02)
        der = np.arange(X_MIX, X1, 0.02)
        p3 = [ax_F.c2p(x, F_mix(x)) for x in izq]
        p3 += [ax_F.c2p(X_MIX, (1 - MASA_MIX) * F_cont(X_MIX))]
        p3 += [ax_F.c2p(x, F_mix(x)) for x in der]
        F3.set_points_as_corners(p3)

        f3 = ax_f.plot(lambda x: (1 - MASA_MIX) * f_cont(x),
                       x_range=[X0, X1, 0.02], color=AMBAR, stroke_width=4,
                       use_smoothing=False)
        a3 = ax_f.get_area(f3, x_range=(X0, X1), color=AMBAR, opacity=0.15,
                           stroke_width=0)
        impulso = Arrow(ax_f.c2p(X_MIX, 0), ax_f.c2p(X_MIX, 0.52),
                        color=ROJO, buff=0, stroke_width=6,
                        max_tip_length_to_length_ratio=0.16)
        imp_lbl = MathTex(r"k\,\delta(x-x_0)", color=ROJO).scale(0.5)
        imp_lbl.next_to(impulso, UR, buff=0.05).shift(LEFT * 0.35)

        t_f3 = rotulo("PDF", r"f_X(x)", AMBAR)
        t_f3.move_to(t_f)
        deriv3 = MathTex(r"\text{el salto de }F_X\ \Rightarrow\ \text{impulso}",
                         color=AMBAR).scale(0.6)
        deriv3.move_to(deriv)

        self.play(Transform(etiqueta, et3), Transform(F1, F3),
                  FadeOut(f2), Transform(t_f, t_f3),
                  Transform(deriv, deriv3), run_time=1.6)
        self.play(Create(f3), FadeIn(a3))
        self.wait(0.4)

        # marcar el salto en la CDF y el impulso correspondiente en la PDF
        salto = Line(ax_F.c2p(X_MIX, (1 - MASA_MIX) * F_cont(X_MIX)),
                     ax_F.c2p(X_MIX, F_mix(X_MIX)), color=ROJO, stroke_width=6)
        self.play(Create(salto), Flash(ax_F.c2p(X_MIX, F_mix(X_MIX)),
                                       color=ROJO, line_length=0.15))
        self.play(GrowArrow(impulso), FadeIn(imp_lbl))
        self.wait(0.8)

        obs3 = nota("es el caso más habitual en procesamiento de señales: "
                    "una curva suave con un átomo de probabilidad", scale=0.46)
        obs3.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(obs3))
        self.wait(2.4)

        # ============================================ cierre
        self.play(FadeOut(VGroup(ax_F, lab_F, t_F, uno, uno_l, F1, salto,
                                 ax_f, lab_f, t_f, f3, a3, impulso, imp_lbl,
                                 deriv, obs3, etiqueta, defi)))
        cierre = VGroup(
            Text("Una sola definición, tres formas:", color=INK).scale(0.55),
            Text("continua → derivada suave", color=AZUL).scale(0.58),
            Text("discreta → escalera y saltos", color=MAGENTA).scale(0.58),
            Text("mixta → las dos cosas a la vez", color=AMBAR).scale(0.58),
        ).arrange(DOWN, buff=0.26)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        for l in cierre[1:]:
            self.play(FadeIn(l, shift=UP * 0.12), run_time=0.55)
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
