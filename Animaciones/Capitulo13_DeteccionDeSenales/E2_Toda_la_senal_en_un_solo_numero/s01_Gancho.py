"""Escena 01 — Gancho: cientos de muestras, un sí o no, y todo cabe en un número."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        rng = np.random.default_rng(13)
        n = 220
        t = np.arange(n)
        pulso = np.zeros(n)
        pulso[96:112] = [1.0, 1.4, 1.8, 2.2, 2.4, 2.4, 2.2, 1.8, 1.8, 2.2, 2.4, 2.2, 1.8, 1.4, 1.0, 0.6]
        r = pulso + rng.normal(0, 1.5, n)
        L = Lienzo(ancho=7.6, alto=2.8, t_rango=(0, n - 1), v_max=7, centro=(0.3, 1.0))
        traza_r = L.curva(t, r, MEDIDA, 2.6)
        base = L.base()
        ant = antena(TXT).scale(1.3).move_to([-5.7, 1.0, 0])
        si = caja("sí", VERDE, ancho=1.6, alto=0.8, scale=0.6).move_to([5.9, 2.0, 0])
        no = caja("no", ROJO, ancho=1.6, alto=0.8, scale=0.6).move_to([5.9, 0.0, 0])
        barra = Rectangle(width=1.0, height=2.2, stroke_width=3, color=ESTIMACION).set_fill(ESTIMACION, 0.5)
        barra.move_to([0.3, 0.8, 0])
        g = MathTex("g", color=ESTIMACION).scale(1.3).next_to(barra, UP, buff=0.2)
        buscada = Barras((2, 2, 1), centro=(-2.0, -2.8), paso=1.3, unidad=0.55, color=SENAL, ancho=0.8)
        recibida = Barras((3, 1, 2), centro=(2.2, -2.8), paso=1.3, unidad=0.55, color=MEDIDA, ancho=0.8)

        rot = Text("la que buscamos", color=SENAL).scale(0.65).next_to(buscada, DOWN, buff=0.25)

        with self.narrar("b1"):
            # «Un radar oye»
            self.en("radar")
            self.play(FadeIn(ant), run_time=self.dur(0.5))
            self.play(Create(ant.ondas.set_color(TXT)), run_time=self.dur(0.3))

            # «cientos de muestras»
            self.en("muestras")
            self.play(Create(base), Create(traza_r), run_time=self.dur(1.2))

            # «decir sí o no»
            self.en("sino")
            self.pop(si, no)

            # «un solo número»
            self.en("numero")
            self.play(FadeOut(traza_r), FadeOut(base), FadeOut(si), FadeOut(no), run_time=self.dur(0.5))
            self.play(GrowFromEdge(barra, DOWN), run_time=self.dur(0.5))
            self.pop(g)

            # «lo parecida que es la señal recibida»
            self.en("parecida")
            self.play(FadeIn(recibida), FadeIn(buscada), run_time=self.dur(0.6))

            # «a la que buscamos»
            self.en("buscamos")
            self.play(FadeIn(rot), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
