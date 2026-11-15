"""Escena 03 — El radar: el retardo del eco es lo que queremos medir."""
from comun.escena import *


class ElRadar(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        rad = radar13().scale(1.7).move_to([-5.6, 0.3, 0])
        rel = reloj().scale(0.9).move_to([-5.6, 2.5, 0])
        av = avion(AZUL).scale(1.5).move_to([4.6, 0.3, 0])
        puls = Tallos([2, 2, 1], centro=(-4.0, 0.3), paso=0.45, unidad=0.4, color=SENAL)
        eco = Tallos([2, 2, 1], centro=(2.6, 0.3), paso=0.45, unidad=0.4, color=SENAL)
        eco.set_opacity(0.45)
        L = Line([-5.0, -2.1, 0], [5.0, -2.1, 0], color=INK, stroke_width=3)
        ida = Arrow([-4.8, -1.75, 0], [4.8, -1.75, 0], color=SENAL, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.05)
        vuelta = Arrow([4.8, -2.45, 0], [-4.8, -2.45, 0], color=AMBAR, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.05)
        luz = Text("300.000 km/s", color=TXT).scale(0.6).move_to([0, 3.3, 0])
        ms = Text("1 ms", color=AMBAR, weight=BOLD).scale(0.55).move_to([0, -3.05, 0])
        km = formula("300{.}000", r"\cdot", "0{,}001", "/", "2", "=", r"150\,\text{km}", escala=0.8,
                     colores={6: AMBAR}).move_to([0, 3.3, 0])
        dd = MathTex("D", color=AMBAR).scale(0.8).move_to([0, -3.05, 0])
        llave = BraceBetweenPoints([-4.8, -2.8, 0], [4.8, -2.8, 0], direction=DOWN, color=AMBAR)
        dd.next_to(llave, DOWN, buff=0.1)
        pr = formula("D", "=", "?", escala=1.3, colores={0: AMBAR, 2: AMBAR}).move_to([0, 1.7, 0])
        with self.narrar("b1"):
            # «Un radar mide distancias»
            self.en("radar")
            self.play(FadeIn(rad), FadeIn(av), run_time=self.dur(0.8))
            # «con el tiempo»
            self.en("tiempo")
            self.play(FadeIn(rel), run_time=self.dur(0.5))
            # «El pulso sale»
            self.en("sale")
            self.sfx("whoosh")
            self.play(FadeIn(puls), run_time=0.3)
            self.play(puls.animate.shift(RIGHT * 3.3), run_time=self.dur(0.8))
            # «choca con el avión»
            self.en("choca")
            self.play(puls.animate.shift(RIGHT * 3.0), run_time=self.dur(0.7))
            self.resaltar(av, color=AMBAR, run_time=0.4)
            # «y vuelve»
            self.en("vuelve")
            self.play(FadeOut(puls), FadeIn(eco), run_time=0.3)
            self.play(eco.animate.shift(LEFT * 6.6), run_time=self.dur(0.9))
            # «cuanto más tarde en volver»
            self.en("tarde")
            self.play(Create(L), GrowArrow(ida), GrowArrow(vuelta), rel.minutero.animate.rotate(-PI, about_point=rel.aro.get_center()),
                      run_time=self.dur(1.0))
            # «más lejos está»
            self.en("lejos")
            self.play(av.animate.shift(RIGHT * 0.9), run_time=self.dur(0.7))
            # «Con la velocidad de la luz»
            self.en("luz")
            self.play(FadeIn(luz), run_time=self.dur(0.5))
            # «un milisegundo de ida y vuelta»
            self.en("ms")
            self.pop(ms)
            # «ciento cincuenta kilómetros»
            self.en("km")
            self.play(FadeOut(luz), FadeIn(km), run_time=self.dur(1.2))
            # «el retardo del eco»
            self.en("retardo")
            self.play(FadeOut(ms), Create(llave), FadeIn(dd), run_time=self.dur(0.7))
            # «es lo que queremos medir»
            self.en("medir")
            self.pop(pr)
        self.wait(1.0)
        self.limpiar()
