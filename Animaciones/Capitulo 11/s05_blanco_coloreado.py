"""Escena 5 - Procesos blancos y coloreados.

Blanco = incorrelado en el tiempo = espectro plano. Al pasarlo por un
filtro modelador la senal se suaviza a la vista, la autocorrelacion se
ensancha y el espectro toma forma.

    manim -pql s05_blanco_coloreado.py BlancoColoreado
"""
from manim import *
import numpy as np
from comun import *

N = 90
RHO = 0.45


def _blanco(semilla=3):
    rng = np.random.default_rng(semilla)
    w = rng.choice([-1.0, 1.0], size=N + 1)
    return w


W = _blanco()
X_BLANCO = W[1:]
# modelador de dos taps: x[n] = a w[n] + b w[n-1], con a*b/(a^2+b^2)=rho
_a = np.sqrt((1 + np.sqrt(1 - 4 * RHO ** 2)) / 2)
_b = RHO / _a
X_COLOR = (_a * W[1:] + _b * W[:-1])
X_COLOR = X_COLOR / np.std(X_COLOR)


class BlancoColoreado(Scene):
    def construct(self):
        configurar()

        tit = titulo("Procesos blancos y coloreados")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ tres paneles
        ax_t, _ = ejes([0, N, N], [-2.6, 2.6], ancho=4.3, alto=1.9, tip=False)
        ax_t.shift(LEFT * 4.15 + DOWN * 0.4)
        t_tit = subtitulo("realización", scale=0.46)
        t_tit.next_to(ax_t, UP, buff=0.2)

        ax_c, lab_c = ejes([-6, 6, 6], [0, 1.25], ancho=3.6, alto=1.9,
                           x_label="m")
        ax_c.shift(DOWN * 0.4)
        lab_c.next_to(ax_c.x_axis.get_end(), DR, buff=0.08)
        c_tit = subtitulo("autocovarianza", scale=0.46)
        c_tit.next_to(ax_c, UP, buff=0.2)

        ax_s, lab_s = ejes([-PI, PI, PI], [0, 2.6], ancho=3.8, alto=1.9,
                           x_label=r"\Omega")
        ax_s.shift(RIGHT * 4.2 + DOWN * 0.4)
        lab_s.next_to(ax_s.x_axis.get_end(), DR, buff=0.08)
        s_tit = subtitulo("espectro", scale=0.46)
        s_tit.next_to(ax_s, UP, buff=0.2)

        self.play(Create(ax_t), FadeIn(t_tit),
                  Create(ax_c), FadeIn(lab_c), FadeIn(c_tit),
                  Create(ax_s), FadeIn(lab_s), FadeIn(s_tit))

        # ------------------------------------------------ el blanco
        etiqueta = Text("BLANCO", color=AZUL, weight=BOLD).scale(0.62)
        etiqueta.next_to(tit, DOWN, buff=0.35).to_edge(LEFT, buff=0.7)

        senal = linea_datos(ax_t, np.arange(N), X_BLANCO, color=AZUL, ancho=2.0)
        ms = np.arange(-6, 7)
        cov = stem(ax_c, ms, [1.0 if m == 0 else 0.0 for m in ms],
                   color=AZUL, ancho=3.0)
        esp = ax_s.plot(lambda w: 1.0, x_range=[-PI, PI], color=AZUL,
                        stroke_width=4)
        esp_area = ax_s.get_area(esp, x_range=(-PI, PI), color=AZUL,
                                 opacity=0.14, stroke_width=0)

        self.play(FadeIn(etiqueta))
        self.play(Create(senal, run_time=1.6, rate_func=linear))
        self.play(FadeIn(cov), FadeIn(esp), FadeIn(esp_area))
        self.wait(0.5)

        obs1 = nota("cada muestra es independiente de las demás", scale=0.44)
        obs1.to_edge(DOWN, buff=0.62)
        self.play(FadeIn(obs1))
        self.wait(1.0)
        obs2 = nota("una sola delta en el origen  →  espectro totalmente plano",
                    scale=0.44)
        obs2.to_edge(DOWN, buff=0.62)
        self.play(FadeOut(obs1), FadeIn(obs2))
        self.wait(1.6)
        self.play(FadeOut(obs2))

        # ------------------------------------------------ el filtro
        # se ubica por encima de los titulos de los paneles para no pisarlos
        filtro = bloque(r"H(e^{j\Omega})", color=AMBAR, ancho=2.2, alto=0.8,
                        scale=0.5)
        f_nota = nota("filtro modelador", scale=0.42)
        grupo_f = VGroup(filtro, f_nota).arrange(RIGHT, buff=0.3)
        grupo_f.move_to(UP * 2.32).shift(RIGHT * 0.6)
        self.play(FadeIn(grupo_f))
        self.wait(0.8)

        # ------------------------------------------------ el coloreado
        etiqueta2 = Text("COLOREADO", color=AMBAR, weight=BOLD).scale(0.62)
        etiqueta2.move_to(etiqueta, aligned_edge=LEFT)

        senal2 = linea_datos(ax_t, np.arange(N), X_COLOR, color=AMBAR, ancho=2.0)
        cov2 = stem(ax_c, ms,
                    [1.0 if m == 0 else (RHO if abs(m) == 1 else 0.0) for m in ms],
                    color=AMBAR, ancho=3.0)
        esp2 = ax_s.plot(lambda w: 1 + 2 * RHO * np.cos(w), x_range=[-PI, PI],
                         color=AMBAR, stroke_width=4)
        esp2_area = ax_s.get_area(esp2, x_range=(-PI, PI), color=AMBAR,
                                  opacity=0.14, stroke_width=0)

        self.play(Transform(etiqueta, etiqueta2),
                  Transform(senal, senal2),
                  Transform(cov, cov2),
                  Transform(esp, esp2),
                  Transform(esp_area, esp2_area),
                  run_time=2.0)
        self.wait(0.8)

        obs3 = nota("la señal ahora es más lenta: arrastra memoria de un paso",
                    scale=0.44)
        obs3.to_edge(DOWN, buff=0.62)
        self.play(FadeIn(obs3))
        self.wait(1.5)
        obs4 = nota("la covarianza se ensanchó y el espectro dejó de ser plano",
                    scale=0.44)
        obs4.to_edge(DOWN, buff=0.62)
        self.play(FadeOut(obs3), FadeIn(obs4))
        self.wait(1.8)
        self.play(FadeOut(obs4))

        # ------------------------------------------------ ida y vuelta
        equiv = MathTex(
            r"C_{xx}[m]=K\delta[m] \iff D_{xx}(e^{j\Omega})=K",
            color=TXT).scale(0.66)
        equiv.to_edge(DOWN, buff=0.62)
        self.play(Write(equiv))
        self.wait(0.6)
        doble = nota("y vale en los dos sentidos: espectro plano ⇒ media nula "
                     "e incorrelado", scale=0.42)
        doble.next_to(equiv, UP, buff=0.18)
        self.play(FadeIn(doble))
        self.wait(2.2)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax_t, t_tit, senal, ax_c, lab_c, c_tit, cov,
                                 ax_s, lab_s, s_tit, esp, esp_area, grupo_f,
                                 etiqueta, equiv, doble)))
        cierre = VGroup(
            Text("Blanco  =  sin memoria  =  espectro plano", color=AZUL).scale(0.62),
            Text("Coloreado  =  con memoria  =  espectro con forma",
                 color=AMBAR).scale(0.62),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.play(FadeIn(cierre[1], shift=UP * 0.15))
        self.wait(2.0)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
