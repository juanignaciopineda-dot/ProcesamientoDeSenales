"""Escena 3 - Media y varianza: qué miden y por qué alcanzan.

La media es el centro de masa de la distribucion; la varianza, cuanto se
desparrama. Se desarrolla paso a paso la identidad sigma^2 = E[X^2] - mu^2
y se cierra con por que para la normal y la uniforme estos dos numeros
determinan toda la densidad.

    manim -pql s03_media_varianza.py MediaYVarianza
"""
from manim import *
import numpy as np
from comun import *

X0, X1 = -5.2, 5.2


class MediaYVarianza(Scene):
    def construct(self):
        configurar()

        tit = titulo("Media y varianza: dos números que resumen todo")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ============================================ la media como centro de masa
        ax, lab = ejes([X0, X1, X1], [0, 0.52], ancho=9.0, alto=2.6,
                       x_label="x")
        ax.shift(DOWN * 0.35)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)

        mu = ValueTracker(0.0)
        sig = ValueTracker(1.0)

        dens = always_redraw(lambda: ax.plot(
            lambda x: gauss(x, mu.get_value(), sig.get_value()),
            x_range=[X0, X1, 0.02], color=AZUL, stroke_width=4,
            use_smoothing=False))
        area = always_redraw(lambda: ax.get_area(
            ax.plot(lambda x: gauss(x, mu.get_value(), sig.get_value()),
                    x_range=[X0, X1, 0.02], use_smoothing=False),
            x_range=(X0, X1), color=AZUL, opacity=0.16, stroke_width=0))
        f_lbl = MathTex(r"f_X(x)", color=AZUL).scale(0.62)
        f_lbl.next_to(ax, UP, buff=0.15).align_to(ax, LEFT).shift(RIGHT * 0.6)

        self.play(Create(ax), FadeIn(lab))
        self.play(Create(dens), FadeIn(area), FadeIn(f_lbl))
        self.wait(0.4)

        # el fulcro: la media es donde la distribucion se equilibra
        fulcro = always_redraw(lambda: Triangle(color=AMBAR, fill_color=AMBAR,
                                                fill_opacity=0.9)
                               .scale(0.13)
                               .next_to(ax.c2p(mu.get_value(), 0), DOWN, buff=0.02))
        mu_lin = always_redraw(lambda: DashedLine(
            ax.c2p(mu.get_value(), 0),
            ax.c2p(mu.get_value(), gauss(mu.get_value(), mu.get_value(),
                                         sig.get_value())),
            color=AMBAR, stroke_width=2, dash_length=0.08))
        mu_lbl = always_redraw(lambda: MathTex(r"\mu_X", color=AMBAR).scale(0.6)
                               .next_to(ax.c2p(mu.get_value(), 0), DOWN, buff=0.32))

        self.play(FadeIn(fulcro), Create(mu_lin), FadeIn(mu_lbl))
        cm = Text("la media es el punto de equilibrio", color=AMBAR).scale(0.52)
        cm.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(cm))
        self.wait(0.8)
        self.play(mu.animate.set_value(-2.1), run_time=1.6)
        self.play(mu.animate.set_value(1.8), run_time=2.0)
        self.play(mu.animate.set_value(0.0), run_time=1.3)
        self.wait(0.5)

        e_def = MathTex(r"E[X]=\int_{-\infty}^{\infty} x\,f_X(x)\,dx",
                        color=AMBAR).scale(0.7)
        e_def.to_edge(DOWN, buff=0.45)
        self.play(FadeOut(cm), Write(e_def))
        self.wait(1.6)

        # ============================================ la varianza
        self.play(FadeOut(e_def))
        anchos = always_redraw(lambda: VGroup(*[
            DashedLine(ax.c2p(mu.get_value() + s * sig.get_value(), 0),
                       ax.c2p(mu.get_value() + s * sig.get_value(),
                              gauss(mu.get_value() + s * sig.get_value(),
                                    mu.get_value(), sig.get_value())),
                       color=VERDE, stroke_width=2, dash_length=0.08)
            for s in (-1, 1)]))
        flecha_s = always_redraw(lambda: DoubleArrow(
            ax.c2p(mu.get_value() - sig.get_value(), 0.46),
            ax.c2p(mu.get_value() + sig.get_value(), 0.46),
            color=VERDE, stroke_width=2.5, buff=0,
            max_tip_length_to_length_ratio=0.06))
        s_lbl = always_redraw(lambda: MathTex(r"2\sigma_X", color=VERDE)
                              .scale(0.55)
                              .next_to(ax.c2p(mu.get_value(), 0.46), UP, buff=0.06))

        self.play(Create(anchos), GrowArrow(flecha_s), FadeIn(s_lbl))
        disp = Text("la varianza mide cuánto se desparrama", color=VERDE).scale(0.52)
        disp.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(disp))
        self.play(sig.animate.set_value(2.0), run_time=1.8)
        self.play(sig.animate.set_value(0.6), run_time=1.8)
        self.play(sig.animate.set_value(1.15), run_time=1.2)
        self.wait(0.8)
        self.play(FadeOut(disp))

        # ============================================ la identidad
        self.play(FadeOut(VGroup(ax, lab, dens, area, f_lbl, fulcro, mu_lin,
                                 mu_lbl, anchos, flecha_s, s_lbl)))

        pasos = VGroup(
            MathTex(r"\sigma_X^2 = E\big[(X-\mu_X)^2\big]"),
            MathTex(r"= E\big[X^2 - 2\mu_X X + \mu_X^2\big]"),
            MathTex(r"= E[X^2] - 2\mu_X\,E[X] + \mu_X^2"),
            MathTex(r"= E[X^2] - 2\mu_X^2 + \mu_X^2"),
            MathTex(r"\sigma_X^2 = E[X^2] - \mu_X^2"),
        )
        for p in pasos:
            p.set_color(TXT).scale(0.78)
        pasos.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        pasos.move_to(ORIGIN).shift(DOWN * 0.15)
        pasos[-1].set_color(AMBAR)

        comentarios = [
            "definición",
            "cuadrado del binomio",
            "linealidad de la esperanza",
            "la esperanza de una constante es la constante",
            "",
        ]
        self.play(Write(pasos[0]))
        self.wait(0.5)
        for i in range(1, len(pasos)):
            c = nota(comentarios[i - 1], scale=0.42)
            c.next_to(pasos[i - 1], RIGHT, buff=0.6)
            self.play(FadeIn(c, shift=LEFT * 0.1), run_time=0.5)
            self.play(Write(pasos[i]), run_time=0.9)
            self.play(FadeOut(c), run_time=0.35)
        self.play(Circumscribe(pasos[-1], color=AMBAR, buff=0.15))
        self.wait(1.8)

        # ============================================ cierre
        self.play(FadeOut(pasos))
        cierre = VGroup(
            Text("¿Por qué nos conformamos con dos números?", color=TXT).scale(0.6),
            nota("Porque trabajar con la densidad completa suele ser inviable…",
                 scale=0.5),
            Text("y porque para la normal y la uniforme,", color=INK).scale(0.55),
            Text("μ y σ² determinan TODA la densidad.", color=AMBAR).scale(0.6),
        ).arrange(DOWN, buff=0.3)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.wait(0.5)
        self.play(FadeIn(cierre[1]))
        self.wait(0.6)
        self.play(FadeIn(cierre[2]), FadeIn(cierre[3], shift=UP * 0.12))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
