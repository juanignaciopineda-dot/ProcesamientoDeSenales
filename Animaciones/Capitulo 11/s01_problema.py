"""Escena 1 - Por que no alcanza con transformar una realizacion.

Motiva todo el capitulo: una realizacion WSS tiene energia infinita y,
peor, cada realizacion da un espectro distinto. De ahi las dos salidas:
mirar potencia en vez de energia, y promediar sobre el ensemble.

    manim -pql s01_problema.py Problema
"""
from manim import *
import numpy as np
from comun import *

N = 512
FS = 1.0
T = np.arange(N)


def realizacion(semilla):
    """Ruido levemente coloreado: blanco por un promediador movil corto.

    Se usa un filtro corto a proposito: con uno largo el espectro se
    apila todo cerca de cero y no se ve la variabilidad, que es el punto.
    """
    rng = np.random.default_rng(semilla)
    w = rng.normal(0, 1, N + 5)
    h = np.exp(-np.arange(5) / 2.2)
    x = np.convolve(w, h, mode="valid")[:N]
    return x / np.std(x)


def periodograma(x):
    """Periodograma sobre toda la banda, normalizado a media 1."""
    X = np.fft.rfft(x * np.hanning(len(x)))
    P = (np.abs(X) ** 2) / len(x)
    f = np.fft.rfftfreq(len(x), d=1 / FS)
    P = P / np.mean(P[1:])                      # nivel medio ~ 1
    return f[1:] / 0.5 * 6.0, P[1:]             # f mapeada al ancho del cuadro


class Problema(Scene):
    def construct(self):
        configurar()

        tit = titulo("¿Por qué no alcanza con transformar?")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ panel tiempo
        ax_t, lab_t = ejes([0, N, N], [-3.6, 3.6], ancho=5.4, alto=2.5,
                           x_label="t", tip=True)
        ax_t.to_edge(LEFT, buff=0.75).shift(DOWN * 0.35)
        lab_t.next_to(ax_t.x_axis.get_end(), DR, buff=0.1)
        t_tit = subtitulo("una realización  x(t)", scale=0.5, color=AZUL)
        t_tit.next_to(ax_t, UP, buff=0.25)

        x1 = realizacion(1)
        onda = linea_datos(ax_t, T, x1, color=AZUL, ancho=2.2)

        self.play(Create(ax_t), FadeIn(lab_t), FadeIn(t_tit))
        self.play(Create(onda, run_time=2.0, rate_func=linear))
        self.wait(0.4)

        # ------------------------------------------------ energia infinita
        flechas = VGroup(
            MathTex(r"\cdots", color=INK).scale(0.8).next_to(ax_t, LEFT, buff=0.08),
            MathTex(r"\cdots", color=INK).scale(0.8).next_to(ax_t, RIGHT, buff=0.08),
        )
        aviso = nota("no empieza ni termina  →  energía infinita", scale=0.42)
        aviso.next_to(ax_t, DOWN, buff=0.3)
        self.play(FadeIn(flechas), FadeIn(aviso))
        self.wait(1.3)
        self.play(FadeOut(aviso), FadeOut(flechas))

        # ------------------------------------------------ panel frecuencia
        ax_f, lab_f = ejes([0, 6, 6], [0, 4.2], ancho=5.0, alto=2.5,
                           x_label=r"\omega")
        ax_f.to_edge(RIGHT, buff=0.75).shift(DOWN * 0.35)
        lab_f.next_to(ax_f.x_axis.get_end(), DR, buff=0.1)
        f_tit = subtitulo("su transformada (ventana finita)", scale=0.5,
                          color=AMBAR)
        f_tit.next_to(ax_f, UP, buff=0.25)

        fx, px = periodograma(x1)
        esp = linea_datos(ax_f, fx, px, color=AMBAR, ancho=2.0)

        self.play(Create(ax_f), FadeIn(lab_f), FadeIn(f_tit))
        self.play(Create(esp, run_time=1.5, rate_func=linear))
        self.wait(0.8)

        # ------------------------------------------------ cambio de realizacion
        pregunta = Text("¿Y si me hubiera tocado otra realización?",
                        color=TXT).scale(0.55)
        pregunta.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(pregunta, shift=UP * 0.15))
        self.wait(1.0)
        self.play(FadeOut(pregunta))

        contador = VGroup()
        for k, semilla in enumerate([7, 23, 99], start=2):
            xk = realizacion(semilla)
            fk, pk = periodograma(xk)
            onda_k = linea_datos(ax_t, T, xk, color=AZUL, ancho=2.2)
            esp_k = linea_datos(ax_f, fk, pk, color=AMBAR, ancho=2.0)
            self.play(Transform(onda, onda_k),
                      Transform(esp, esp_k), run_time=1.1)
            self.wait(0.55)

        alerta = Text("cada realización da un espectro completamente distinto",
                      color=ROJO).scale(0.52)
        alerta.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(alerta, shift=UP * 0.15))
        self.wait(1.8)
        self.play(FadeOut(alerta))

        # ------------------------------------------------ las dos salidas
        self.play(FadeOut(VGroup(ax_t, lab_t, t_tit, onda,
                                 ax_f, lab_f, f_tit, esp)))

        p1 = VGroup(
            Text("1.", color=VERDE, weight=BOLD).scale(0.7),
            Text("Mirar POTENCIA, no energía", color=TXT).scale(0.62),
        ).arrange(RIGHT, buff=0.28)
        p1n = nota("la potencia es energía por unidad de tiempo: es finita",
                   scale=0.44)
        p2 = VGroup(
            Text("2.", color=VERDE, weight=BOLD).scale(0.7),
            Text("Promediar sobre el ENSEMBLE", color=TXT).scale(0.62),
        ).arrange(RIGHT, buff=0.28)
        p2n = nota("así deja de depender de qué realización te tocó", scale=0.44)

        bloque_txt = VGroup(p1, p1n, p2, p2n).arrange(DOWN, buff=0.22,
                                                      aligned_edge=LEFT)
        bloque_txt.move_to(ORIGIN).shift(DOWN * 0.25)

        self.play(FadeIn(p1, shift=RIGHT * 0.2))
        self.play(FadeIn(p1n))
        self.wait(0.5)
        self.play(FadeIn(p2, shift=RIGHT * 0.2))
        self.play(FadeIn(p2n))
        self.wait(1.2)

        final = MathTex(r"S_{xx}(j\omega) \;=\; \mathcal{F}\{R_{xx}(\tau)\}",
                        color=AZUL).scale(0.85)
        final.next_to(bloque_txt, DOWN, buff=0.6)
        self.play(Write(final))
        self.wait(2.0)
        self.play(FadeOut(VGroup(tit, bloque_txt, final)))
        self.wait(0.3)
