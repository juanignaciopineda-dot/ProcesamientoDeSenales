"""Escena 2 - La PSD y el argumento del filtro pasabanda ideal.

Por que S_xx(jw) merece el nombre de *densidad*: el area bajo cualquier
banda es exactamente la potencia esperada que el proceso tiene en esa banda.

    manim -pql s02_pasabanda.py PSDPasabanda
"""
from manim import *
import numpy as np
from comun import *

ALFA = 3.0
W_MAX = 8.0


def S(w):
    """PSD del proceso exponencialmente correlacionado."""
    return 2 * ALFA / (ALFA ** 2 + w ** 2)


POT_TOTAL = 2 * np.arctan(W_MAX / ALFA) / (2 * np.pi) * 2  # normalizador


def potencia_en_banda(w0, bw):
    """(1/2pi) * integral de S sobre las dos bandas simetricas."""
    a, b = w0 - bw / 2, w0 + bw / 2
    # primitiva de 2a/(a^2+w^2) es 2*arctan(w/a)
    F = lambda w: 2 * np.arctan(w / ALFA)
    una = F(b) - F(a)
    return 2 * una / (2 * np.pi)          # las dos bandas, +w0 y -w0


class PSDPasabanda(Scene):
    def construct(self):
        configurar()

        # ------------------------------------------------ titulo
        tit = titulo("¿Por qué “densidad” espectral de potencia?")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.4)

        # ------------------------------------------------ el experimento
        x_lbl = MathTex("x(t)", color=AZUL).scale(0.62)
        filtro = bloque(r"H(j\omega)", color=AMBAR, ancho=2.0)
        y_lbl = MathTex("y(t)", color=VERDE).scale(0.62)
        diag = VGroup(x_lbl, filtro, y_lbl).arrange(RIGHT, buff=0.85)
        diag.next_to(tit, DOWN, buff=0.45).shift(RIGHT * 0.3)
        f1 = flecha(x_lbl.get_right(), filtro.get_left())
        f2 = flecha(filtro.get_right(), y_lbl.get_left())
        pie = nota("pasabanda ideal: deja pasar una banda, corta todo lo demás")
        pie.next_to(diag, DOWN, buff=0.28)

        self.play(FadeIn(x_lbl), GrowArrow(f1), FadeIn(filtro))
        self.play(GrowArrow(f2), FadeIn(y_lbl))
        self.play(FadeIn(pie, shift=UP * 0.15))
        self.wait(1.2)
        # el diagrama ya cumplio su funcion: se va para liberar el cuadro
        self.play(FadeOut(pie), FadeOut(VGroup(diag, f1, f2)))

        # ------------------------------------------------ la PSD
        ax, lab = ejes([-W_MAX, W_MAX], [0, 0.78], ancho=8.6, alto=3.1,
                       x_label=r"\omega")
        grupo_ax = VGroup(ax, lab).shift(DOWN * 0.55)
        psd = curva(ax, S, [-W_MAX, W_MAX], color=AZUL, ancho=4)
        psd_lbl = MathTex(r"S_{xx}(j\omega)", color=AZUL).scale(0.7)
        psd_lbl.next_to(ax.c2p(-W_MAX + 1.1, S(1.4)), UP, buff=0.15)

        self.play(Create(ax), FadeIn(lab))
        self.play(Create(psd, run_time=1.4), FadeIn(psd_lbl))
        self.wait(0.6)

        # ------------------------------------------------ la banda movil
        w0 = ValueTracker(5.2)
        bw = ValueTracker(1.6)

        def banda(signo):
            return always_redraw(lambda: ax.get_area(
                psd,
                x_range=(signo * w0.get_value() - bw.get_value() / 2,
                         signo * w0.get_value() + bw.get_value() / 2),
                color=AMBAR, opacity=0.75, stroke_width=0))

        b_pos, b_neg = banda(+1), banda(-1)
        self.play(FadeIn(b_pos), FadeIn(b_neg))

        etiqueta_banda = always_redraw(lambda: MathTex(
            r"\omega_0", color=AMBAR).scale(0.6).next_to(
            ax.c2p(w0.get_value(), 0), DOWN, buff=0.18))
        self.play(FadeIn(etiqueta_banda))

        # ------------------------------------------------ el medidor
        H_MED = 2.6
        marco = Rectangle(width=0.52, height=H_MED, color=INK, stroke_width=2)
        marco.to_edge(LEFT, buff=0.7).shift(DOWN * 0.4)
        relleno = always_redraw(lambda: Rectangle(
            width=0.52,
            height=max(1e-3, H_MED * potencia_en_banda(w0.get_value(),
                                                       bw.get_value()) / 0.30),
            stroke_width=0, fill_color=VERDE, fill_opacity=0.85,
        ).align_to(marco, DOWN).align_to(marco, LEFT))
        med_lbl = MathTex(r"E[y^2(t)]", color=VERDE).scale(0.55)
        med_lbl.next_to(marco, UP, buff=0.2)

        self.play(FadeIn(marco), FadeIn(relleno), FadeIn(med_lbl))
        self.wait(0.5)

        rel = MathTex(
            r"E[y^2(t)] \;=\; \frac{1}{2\pi}\int_{\text{banda}} S_{xx}(j\omega)\, d\omega",
            color=TXT).scale(0.62)
        rel.next_to(ax, DOWN, buff=0.42)
        self.play(Write(rel))
        self.wait(0.8)

        # ------------------------------------------------ barrido
        self.play(w0.animate.set_value(1.2), run_time=3.2,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.4)
        self.play(w0.animate.set_value(6.4), run_time=3.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.3)
        self.play(w0.animate.set_value(2.4), run_time=2.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.5)

        obs = nota("el área de la franja ES la potencia esperada en esa banda,")
        obs2 = nota("no importa dónde esté ni qué tan angosta sea")
        VGroup(obs, obs2).arrange(DOWN, buff=0.12).next_to(rel, DOWN, buff=0.3)
        self.play(FadeIn(obs), FadeIn(obs2))
        self.wait(1.4)
        self.play(FadeOut(obs), FadeOut(obs2))

        # ------------------------------------------------ el limite
        self.play(bw.animate.set_value(0.28), run_time=2.4)
        limite = MathTex(
            r"E[y^2(t)] \;\longrightarrow\; S_{xx}(j\omega_0)\,\frac{\Delta\omega}{2\pi}",
            color=AMBAR).scale(0.68)
        limite.move_to(rel)
        self.play(FadeOut(rel), FadeIn(limite))
        self.wait(1.6)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(b_pos, b_neg, etiqueta_banda, marco, relleno,
                                 med_lbl, limite)))
        cierre = VGroup(
            Text("Potencia por unidad de frecuencia.", color=TXT).scale(0.62),
            Text("Por eso se llama densidad.", color=AMBAR).scale(0.62),
        ).arrange(DOWN, buff=0.18)
        cierre.next_to(ax, DOWN, buff=0.55)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.play(FadeIn(cierre[1], shift=UP * 0.15))
        self.wait(2.0)
        self.play(FadeOut(VGroup(tit, ax, lab, psd, psd_lbl, cierre)))
        self.wait(0.3)
