"""Escena 5 - Senal en ruido aditivo: el filtro reparte segun el SNR.

El caso canonico. El filtro de Wiener no hace nada mas que darle ganancia
a las bandas donde la senal domina y cortarle a las bandas donde manda el
ruido. Se barre el nivel de ruido para verlo.

    manim -pql s05_senal_en_ruido.py SenalEnRuido
"""
from manim import *
import numpy as np
from comun import *

RHO = 0.5
ESC_Y = 2.0             # potencia de la senal


def Dyy(w):
    return ESC_Y * (1 + 2 * RHO * np.cos(w))


class SenalEnRuido(Scene):
    def construct(self):
        configurar()

        tit = titulo("Señal en ruido: el filtro reparte ganancia según el SNR")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        modelo = MathTex(r"x[n]=y[n]+v[n]", color=TXT).scale(0.72)
        modelo.next_to(tit, DOWN, buff=0.35)
        self.play(Write(modelo))
        self.wait(0.6)

        formula = MathTex(r"H(e^{j\Omega})=",
                          r"\frac{D_{yy}(e^{j\Omega})}"
                          r"{D_{yy}(e^{j\Omega})+D_{vv}(e^{j\Omega})}",
                          color=AZUL).scale(0.75)
        formula.next_to(modelo, DOWN, buff=0.3)
        self.play(Write(formula))
        self.wait(1.2)
        self.play(VGroup(modelo, formula).animate.scale(0.78)
                  .arrange(RIGHT, buff=0.7).next_to(tit, DOWN, buff=0.35))

        # ------------------------------------------------ los espectros
        sig_v = ValueTracker(1.0)

        ax, lab = ejes([-PI, PI, PI], [0, 6.4], ancho=7.6, alto=2.9,
                       x_label=r"\Omega")
        ax.shift(DOWN * 0.95 + LEFT * 0.55)
        lab.next_to(ax.x_axis.get_end(), DOWN, buff=0.22)
        self.play(Create(ax), FadeIn(lab))

        c_sig = ax.plot(Dyy, x_range=[-PI, PI, 0.01], color=VERDE,
                        stroke_width=4, use_smoothing=False)
        a_sig = ax.get_area(c_sig, x_range=(-PI, PI), color=VERDE,
                            opacity=0.14, stroke_width=0)
        c_ruido = always_redraw(lambda: ax.plot(
            lambda w: sig_v.get_value(), x_range=[-PI, PI],
            color=ROJO, stroke_width=4))

        l_sig = MathTex(r"D_{yy}", color=VERDE).scale(0.6)
        l_sig.next_to(ax.c2p(0, Dyy(0)), UP, buff=0.12)
        l_ruido = always_redraw(lambda: MathTex(r"D_{vv}", color=ROJO)
                                .scale(0.6)
                                .next_to(ax.c2p(-PI, sig_v.get_value()), UR,
                                         buff=0.08))

        self.play(Create(c_sig), FadeIn(a_sig), FadeIn(l_sig))
        self.play(Create(c_ruido), FadeIn(l_ruido))
        self.wait(0.6)

        # ------------------------------------------------ el filtro, en su eje
        ax_h, _ = ejes([-PI, PI, PI], [0, 1.15], ancho=7.6, alto=2.9, tip=False)
        ax_h.move_to(ax)
        c_H = always_redraw(lambda: ax_h.plot(
            lambda w: Dyy(w) / (Dyy(w) + sig_v.get_value()),
            x_range=[-PI, PI, 0.01], color=AZUL, stroke_width=5,
            use_smoothing=False))
        # la etiqueta va arriba a la izquierda del cuadro, lejos de la curva
        l_H = MathTex(r"H(e^{j\Omega})", color=AZUL).scale(0.62)
        l_H.next_to(ax.c2p(-PI, 5.9), RIGHT, buff=0.15)

        # escala de ganancia a la derecha, para que se lea que H va de 0 a 1.
        # se omite el 0 porque cae justo sobre la etiqueta del eje Omega
        esc = VGroup()
        for v, txt in [(0.5, "0.5"), (1.0, "1")]:
            p = ax_h.c2p(PI, v)
            esc.add(Line(p, p + RIGHT * 0.12, color=AZUL, stroke_width=2))
            esc.add(MathTex(txt, color=AZUL).scale(0.45)
                    .next_to(p + RIGHT * 0.12, RIGHT, buff=0.06))
        esc_lbl = subtitulo("ganancia", scale=0.4, color=AZUL)
        esc_lbl.next_to(ax_h.c2p(PI, 1.15), UR, buff=0.08)

        self.play(Create(c_H), FadeIn(l_H), FadeIn(esc), FadeIn(esc_lbl))
        self.wait(0.8)

        # ------------------------------------------------ barrido del ruido
        med = always_redraw(lambda: VGroup(
            MathTex(r"\sigma_v^2 =", color=ROJO).scale(0.6),
            DecimalNumber(sig_v.get_value(), num_decimal_places=2, color=ROJO)
            .scale(0.6),
        ).arrange(RIGHT, buff=0.14).to_corner(UR, buff=0.7).shift(DOWN * 1.35))
        self.play(FadeIn(med))

        m1 = nota("poco ruido: el filtro deja pasar casi todo", scale=0.48)
        m1.to_edge(DOWN, buff=0.45)
        self.play(sig_v.animate.set_value(0.16), run_time=2.2)
        self.play(FadeIn(m1))
        self.wait(1.5)
        self.play(FadeOut(m1))

        m2 = nota("mucho ruido: solo sobrevive la banda donde la señal domina",
                  scale=0.48)
        m2.to_edge(DOWN, buff=0.45)
        self.play(sig_v.animate.set_value(4.2), run_time=3.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.play(FadeIn(m2))
        self.wait(1.8)
        self.play(FadeOut(m2))
        self.play(sig_v.animate.set_value(1.1), run_time=1.8)

        # ------------------------------------------------ los dos extremos
        ext = VGroup(
            MathTex(r"D_{yy}\gg D_{vv}\ \Rightarrow\ H\to 1",
                    color=VERDE).scale(0.62),
            MathTex(r"D_{vv}\gg D_{yy}\ \Rightarrow\ H\to 0",
                    color=ROJO).scale(0.62),
        ).arrange(DOWN, buff=0.22)
        ext.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(ext[0], shift=UP * 0.12))
        self.play(FadeIn(ext[1], shift=UP * 0.12))
        self.wait(2.2)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, ax_h, c_sig, a_sig, c_ruido, c_H,
                                 l_sig, l_ruido, l_H, esc, esc_lbl, med, ext,
                                 modelo, formula)))
        cierre = VGroup(
            Text("El filtro de Wiener no hace magia:", color=INK).scale(0.58),
            Text("le da ganancia a cada banda según su relación señal-ruido.",
                 color=AZUL).scale(0.62),
            nota("nada más que eso, y es notablemente sensato", scale=0.5),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.5)
        self.play(FadeIn(cierre[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
