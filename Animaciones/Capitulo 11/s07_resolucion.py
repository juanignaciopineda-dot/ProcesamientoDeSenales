"""Escena 7 - El compromiso resolucion contra varianza.

El periodograma esperado es la PSD verdadera convolucionada con una
sinc^2 de ancho ~pi/T. Dos picos separados por menos de eso no se
distinguen. Pero con un registro fijo, mas T significa menos M.

    manim -pql s07_resolucion.py Resolucion
"""
from manim import *
import numpy as np
from comun import *

W1, W2 = 2.6, 3.4          # las dos frecuencias, en unidades de escena
X_MAX = 6.0
REGISTRO = 2048            # muestras totales disponibles


def espectro_borroneado(T, sep_media=(W1 + W2) / 2, sep=(W2 - W1)):
    """PSD de dos tonos vista a traves de una ventana de largo T.

    Cada delta se convierte en el modulo cuadrado de la ventana, cuyo
    lobulo principal tiene semiancho proporcional a 1/T.
    """
    ancho = 9.0 / T                      # semiancho del lobulo, escalado
    def f(w):
        y = 0.0
        for w0 in (sep_media - sep / 2, sep_media + sep / 2):
            u = (w - w0) / ancho
            y += 1.0 if abs(u) < 1e-9 else (np.sin(np.pi * u) / (np.pi * u)) ** 2
        return y
    return f


class Resolucion(Scene):
    def construct(self):
        configurar()

        tit = titulo("Resolución contra varianza: no se puede todo")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        planteo = Text("El proceso tiene DOS componentes cíclicas cercanas",
                       color=TXT).scale(0.58)
        planteo.next_to(tit, DOWN, buff=0.35)
        self.play(FadeIn(planteo))
        self.wait(1.0)

        # ------------------------------------------------ la verdad
        ax, lab = ejes([0, X_MAX, X_MAX], [0, 2.5], ancho=8.6, alto=2.9,
                       x_label=r"\Omega")
        ax.shift(DOWN * 0.85)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab), FadeOut(planteo))

        verdad = VGroup(
            *[Arrow(ax.c2p(w, 0), ax.c2p(w, 2.0), color=VERDE, buff=0,
                    stroke_width=5, max_tip_length_to_length_ratio=0.12)
              for w in (W1, W2)])
        v_lbl = Text("la PSD verdadera: dos líneas", color=VERDE).scale(0.5)
        v_lbl.next_to(ax, UP, buff=0.2)
        self.play(GrowArrow(verdad[0]), GrowArrow(verdad[1]), FadeIn(v_lbl))
        self.wait(1.2)
        self.play(verdad.animate.set_opacity(0.35), FadeOut(v_lbl))

        # ------------------------------------------------ T chico
        Tv = ValueTracker(16.0)
        estimado = always_redraw(lambda: ax.plot(
            espectro_borroneado(Tv.get_value()),
            x_range=[0.05, X_MAX, 0.01], color=AMBAR, stroke_width=4,
            use_smoothing=False))
        self.play(FadeIn(estimado))

        info = always_redraw(lambda: VGroup(
            MathTex("T =", color=INK).scale(0.62),
            Integer(int(Tv.get_value()), color=AMBAR).scale(0.68),
            MathTex(r"\;\Rightarrow\; M =", color=INK).scale(0.62),
            Integer(max(1, int(REGISTRO / Tv.get_value())), color=VERDE).scale(0.68),
        ).arrange(RIGHT, buff=0.14).to_edge(UP, buff=1.25).shift(RIGHT * 3.4))
        reg = nota(f"registro fijo de {REGISTRO} muestras", scale=0.42)
        reg.next_to(info, DOWN, buff=0.16)
        self.play(FadeIn(info), FadeIn(reg))
        self.wait(0.5)

        m1 = Text("ventana corta: los dos picos se funden en uno",
                  color=ROJO).scale(0.52)
        m1.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(m1))
        self.wait(1.6)
        self.play(FadeOut(m1))

        # ------------------------------------------------ T crece
        self.play(Tv.animate.set_value(64.0), run_time=3.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.4)
        m2 = Text("ventana larga: ahora sí se resuelven", color=VERDE).scale(0.52)
        m2.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(m2))
        self.wait(1.4)
        self.play(FadeOut(m2))

        # ------------------------------------------------ pero...
        pero = Text("…pero fijate qué le pasó a M", color=AMBAR).scale(0.55)
        pero.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(pero), Indicate(info, scale_factor=1.25, color=AMBAR))
        self.wait(1.6)
        self.play(FadeOut(pero))

        crit = MathTex(r"\Delta\Omega_{\min}\;\approx\;\frac{\pi}{T}",
                       color=AZUL).scale(0.8)
        crit.to_edge(DOWN, buff=0.42)
        crit_n = nota("dos picos separados por menos que esto no se distinguen",
                      scale=0.42)
        crit_n.next_to(crit, UP, buff=0.14)
        self.play(Write(crit), FadeIn(crit_n))
        self.wait(2.0)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, estimado, verdad, info, reg,
                                 crit, crit_n)))
        izq = VGroup(
            Text("T grande", color=AZUL, weight=BOLD).scale(0.62),
            Text("mejor resolución", color=INK).scale(0.5),
            Text("más varianza", color=ROJO).scale(0.5),
        ).arrange(DOWN, buff=0.16)
        der = VGroup(
            Text("M grande", color=VERDE, weight=BOLD).scale(0.62),
            Text("menos varianza", color=INK).scale(0.5),
            Text("peor resolución", color=ROJO).scale(0.5),
        ).arrange(DOWN, buff=0.16)
        vs = Text("vs", color=AMBAR).scale(0.6)
        fila = VGroup(izq, vs, der).arrange(RIGHT, buff=1.1)
        fila.move_to(ORIGIN).shift(UP * 0.25)
        final = nota("con un registro fijo, mejorar uno empeora el otro. "
                     "Para mejorar los dos hace falta más datos.", scale=0.5)
        final.next_to(fila, DOWN, buff=0.65)

        self.play(FadeIn(izq, shift=RIGHT * 0.2))
        self.play(FadeIn(vs))
        self.play(FadeIn(der, shift=LEFT * 0.2))
        self.wait(0.6)
        self.play(FadeIn(final))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, fila, final)))
        self.wait(0.3)
