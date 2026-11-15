"""Escena 07 — La cadena completa del detector y la pregunta: ¿por qué funciona?"""
from comun.escena import *


class ElDetectorCompleto(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        grupo, cajas, flechas = cadena_cajas(
            ["señal recibida r[n]", "filtro adaptado", "muestrear en n = 2", "comparar con γ"],
            centro=(0, 1.0), colores=[MEDIDA, ESTIMACION, ESTIMACION, ESTIMACION],
            ancho=2.6, hueco=0.7, alto=1.0, escala=0.42)
        gam = MathTex(r"\gamma=4{,}5", color=AMBAR).scale(0.8).next_to(cajas[3], UP, buff=0.3)
        h1 = Text("hay señal", color=VERDE).scale(0.55)
        h0 = Text("solo ruido", color=INK).scale(0.55)
        xc = cajas[3].get_center()[0]
        h1.move_to([xc - 1.2, -1.0, 0])
        h0.move_to([xc + 1.2, -1.0, 0])
        a1 = flecha(cajas[3].get_bottom() + LEFT * 0.4, h1.get_top() + UP * 0.05, VERDE, 3)
        a0 = flecha(cajas[3].get_bottom() + RIGHT * 0.4, h0.get_top() + UP * 0.05, INK, 3)
        q = interrogante13(AMBAR, 2.0).move_to([-1.5, 3.0, 0])
        rl = reloj().scale(1.2).move_to([-3.4, -2.3, 0])
        esp = campana_mini(centro=(0.5, -2.3), ancho=1.8, alto=1.1, color=SENAL)
        base = Line([-0.5, -2.8, 0], [1.5, -2.8, 0], color=INK, stroke_width=2)
        with self.narrar("b1"):
            # «una cadena sencilla»
            self.en("cadena")
            self.play(FadeIn(grupo), run_time=self.dur(0.8))

            # «la señal recibida entra»
            self.en("entra")
            self.resaltar(cajas[0], color=MEDIDA, escala=1.08)

            # «en el filtro adaptado»
            self.en("filtro")
            self.resaltar(cajas[1], color=AMBAR, escala=1.08)

            # «se toma la salida»
            self.en("muestreo")
            self.resaltar(cajas[2], color=AMBAR, escala=1.08)

            # «se compara con el umbral»
            self.en("umbral")
            self.resaltar(cajas[3], color=AMBAR, escala=1.08)
            self.play(FadeIn(gam), run_time=0.3)

            # «Sí o no»
            self.en("sino")
            self.play(Create(a1), Create(a0), run_time=self.dur(0.4))
            self.play(FadeIn(h1), FadeIn(h0), run_time=self.dur(0.4))

            # «¿por qué funciona tan bien?»
            self.en("porque")
            self.pop(q)

            # «en el tiempo»
            self.en("tiempo")
            self.play(FadeIn(rl, scale=0.7), run_time=self.dur(0.5))

            # «y en la frecuencia»
            self.en("frec")
            self.play(FadeIn(base), Create(esp), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
