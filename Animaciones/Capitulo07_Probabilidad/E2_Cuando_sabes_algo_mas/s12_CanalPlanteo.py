"""Escena 12 — Canal planteo: un emisor, un cable con ruido y un receptor."""
from comun.escena import *


class CanalPlanteo(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        emi = caja("Emisor", SENAL, ancho=2.4, alto=1.3, scale=0.7).move_to([-5.0, 1.0, 0])
        rec = caja("Receptor", MEDIDA, ancho=2.6, alto=1.3, scale=0.7).move_to([5.0, 1.0, 0])
        cable = Line(emi[0].get_right(), rec[0].get_left(), color=INK, stroke_width=5)
        bits = VGroup(MathTex("0", color=TXT).scale(1.6), MathTex("1", color=TXT).scale(1.6)).arrange(RIGHT, buff=0.5)
        bits.next_to(emi, UP, buff=0.35)
        t0 = Text("0 → 70 %", color=SENAL, weight=BOLD).scale(0.8).move_to([-4.6, -1.0, 0])
        t1 = Text("1 → 30 %", color=SENAL, weight=BOLD).scale(0.8).move_to([-4.6, -2.0, 0])
        ray = rayo().scale_to_fit_height(1.5).move_to([0.0, 2.1, 0])
        diez = Text("10 %", color=RUIDO, weight=BOLD).scale(1.0).move_to([0.0, 0.2, 0])
        bit1 = MathTex("1", color=SENAL).scale(2.0).move_to(emi[0].get_right() + RIGHT * 0.5 + UP * 0.0)
        bit0 = MathTex("0", color=RUIDO).scale(2.0).move_to([0.0, 1.0, 0])
        lleg = MathTex("1", color=MEDIDA).scale(2.6).move_to([5.0, 2.7, 0])
        preg = MathTex(r"P(\text{enviado }1\mid \text{recibido }1)=\,?", color=AMBAR).scale(1.4).move_to([1.2, -3.1, 0])

        with self.narrar("b1"):
            # «un ejemplo de señales»
            self.en("ejemplo")
            self.play(FadeIn(emi), Create(cable), FadeIn(rec), run_time=self.dur(0.9))

            # «Un emisor envía ceros y unos»
            self.en("emisor")
            self.play(FadeIn(bits, shift=UP * 0.2), run_time=self.dur(0.5))

            # «un cero el setenta por ciento»
            self.en("cero70")
            self.play(FadeIn(t0), run_time=self.dur(0.4))

            # «un uno el treinta»
            self.en("uno30")
            self.play(FadeIn(t1), run_time=self.dur(0.4))

            # «El cable tiene ruido»
            self.en("ruido")
            self.pop(ray)

            # «cambia el bit un diez por ciento»
            self.en("diez")
            self.play(FadeIn(diez), FadeIn(bit1), run_time=self.dur(0.4))
            self.play(bit1.animate.move_to([0.0, 1.0, 0]), run_time=self.dur(1.0))
            self.play(ReplacementTransform(bit1, bit0), run_time=self.dur(0.3))

            # «Llega un uno»
            self.en("llega")
            self.play(bit0.animate.move_to(lleg), run_time=self.dur(0.5))
            self.play(ReplacementTransform(bit0, lleg), run_time=self.dur(0.3))

            # «¿Qué probabilidad hay de que se enviara un uno?»
            self.en("pregunta")
            self.play(FadeIn(preg), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
