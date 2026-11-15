"""Escena 17 — Cierre: resumen del episodio y anuncio del E1 del Cap. 11."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        f1 = formula(r"\mu_y", "=", "H(0)", r"\mu_x", escala=1.5, colores={2: AMBAR}).move_to([-1.6, 2.4, 0])
        f2 = formula(r"R_{yy}", "=", r"R_{hh}", "*", r"R_{xx}", escala=1.5).move_to([-1.6, 0.9, 0])
        f3 = formula(r"S_{yy}", "=", r"|H|^2", r"S_{xx}", escala=1.5).move_to([-1.6, -0.6, 0])
        det = self.palabra("determinista", VERDE, 0.9).move_to([4.6, 0.9, 0])
        preg = Text("?", color=ROJO, weight=BOLD).scale(1.6).move_to([2.2, -0.6, 0])

        with self.narrar("b1"):
            # «la media sale multiplicada»
            self.en("media")
            self.play(FadeIn(f1), run_time=self.dur(0.8))

            # «la autocorrelación»
            self.en("autocorr")
            self.play(FadeIn(f2), run_time=self.dur(0.8))

            # «una cuenta determinista»
            self.en("determ")
            self.pop(det)

            # «en frecuencia»
            self.en("frec")
            self.play(FadeIn(f3), run_time=self.dur(0.8))

            # «por el módulo al cuadrado»
            self.en("modulo")
            self.resaltar(f3[2], color=AMBAR, escala=1.15)

            # «Pero ¿qué dice»
            self.en("que_dice")
            self.pop(preg)

            # «esa densidad espectral de potencia»
            self.en("psd")
            self.play(f3[3].animate.set_color(AMBAR), run_time=self.dur(0.5))

            # «En el próximo capítulo»
            self.en("proximo")
            self.limpiar(0.25)
            prox = etiqueta("Próximo capítulo · 11", INK, 0.6).move_to([0, 1.7, 0])
            self.play(FadeIn(prox), run_time=0.3)

            # «¿en qué frecuencias vive el azar?»
            self.en("titulo_c11")
            a = self.palabra("¿En qué frecuencias", TXT, 1.5).move_to([0, 0.5, 0])
            b = self.palabra("vive el azar?", AMBAR, 1.5).move_to([0, -1.0, 0])
            self.pop(a, b)
        self.wait(1.0)
        self.limpiar()
