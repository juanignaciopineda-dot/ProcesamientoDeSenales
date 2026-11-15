"""Escena 14 — Segunda razón: en un sistema LTI, la media y la autocorrelación de la salida salen de las de la entrada."""
from comun.escena import *


class LosFiltros(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        L = Lienzo(ancho=2.6, alto=1.4, t_rango=(0, 1), v_max=2.4, centro=(-5.4, 0.0))
        caja_lti = caja("LTI", AZUL, ancho=2.6, alto=1.5, scale=0.9).move_to([0, 0, 0])
        with self.narrar("b1"):
            # «La segunda son los filtros»
            self.en("segunda")
            dos = caja_tex("2", AZUL, 0.9, 0.9, 0.9).move_to([-6.2, 3.3, 0])
            w = self.palabra("los filtros", AMBAR, 1.2).move_to([-3.9, 3.3, 0])
            self.play(FadeIn(dos), run_time=0.3)
            self.pop(w)

            # «pasar las señales»
            self.en("pasar")
            entra = L.curva(np.linspace(0, 1, 120), 1.0 * serie(61, 120, 0.8), SENAL, 3.2)
            self.play(Create(entra), run_time=self.dur(1.2), rate_func=linear)

            # «sistemas lineales e invariantes en el tiempo»
            self.en("lti")
            a1 = flecha([-3.9, 0, 0], [-1.45, 0, 0], INK, 4)
            a2 = flecha([1.45, 0, 0], [3.9, 0, 0], INK, 4)
            self.play(Create(caja_lti), GrowArrow(a1), GrowArrow(a2), run_time=self.dur(0.9))

            # «Señales y Sistemas»
            self.en("sys")
            sys_ = etiqueta("Señales y Sistemas", INK, 0.6).move_to([0, -1.3, 0])
            self.play(FadeIn(sys_, shift=UP * 0.15), run_time=0.5)

            # «LTI»
            self.en("lti_sigla")
            self.play(caja_lti[0].animate(rate_func=there_and_back).scale(1.15).set_stroke(AMBAR), run_time=0.6)

            # «la media y la autocorrelación de la salida»
            self.en("salida")
            ys = formula(r"\mu_{Y}", ",", "R_{YY}", escala=1.0, colores={0: AMBAR, 2: AMBAR}).move_to([5.3, 0.0, 0])
            self.play(FadeIn(ys, shift=LEFT * 0.2), run_time=self.dur(0.8))

            # «las de la entrada»
            self.en("entrada")
            self.play(FadeOut(entra), run_time=0.2)
            xs = formula(r"\mu_{X}", ",", "R_{XX}", escala=1.0, colores={0: SENAL, 2: SENAL}).move_to([-5.3, 0.0, 0])
            flujo = CurvedArrow([-5.3, 0.6, 0], [5.3, 0.6, 0], angle=-TAU / 6, color=AMBAR, stroke_width=3)
            self.play(FadeIn(xs, shift=RIGHT * 0.2), run_time=self.dur(0.6))
            self.play(Create(flujo), run_time=self.dur(0.8))

            # «sin ninguna densidad»
            self.en("sin_dens")
            dens = formula(r"f_{X(t_1)\cdots X(t_n)}", escala=1.0).move_to([0, -2.6, 0])
            self.play(FadeIn(dens), run_time=0.4)
            self.play(Create(tachar(dens)), run_time=0.4)

            # «resultado central del capítulo»
            self.en("central")
            halo = SurroundingRectangle(caja_lti, color=AMBAR, buff=0.25, stroke_width=5)
            self.play(Create(halo), run_time=self.dur(0.6))

            # «el último episodio»
            self.en("ultimo")
            ep = etiqueta("episodio 7", AMBAR, 0.7).move_to([3.4, 3.3, 0])
            self.pop(ep)
        self.wait(1.0)
        self.limpiar()
