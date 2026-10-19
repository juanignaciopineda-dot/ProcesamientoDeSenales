"""Escena 01 — Gancho: mil pruebas sin una falsa alarma no prueban que el detector no falle."""
from comun.escena import *
from comun.figuras_c9e6 import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        with self.narrar("b1"):
            # «Pruebas un detector»
            self.en("detector")
            det = caja_detector6(ancho=3.8, alto=1.8, escala=0.8).move_to([-3.9, 1.3, 0])
            self.play(FadeIn(det, shift=UP * 0.2), run_time=self.dur(0.5))

            # «mil veces»
            self.en("mil")
            rej = rejilla6(centro=(3.1, 0.6), ancho=6.6, radio=0.045)
            cont = Text("1.000 pruebas", color=TXT).scale(0.65).next_to(rej, DOWN, buff=0.35)
            self.play(LaggedStart(*[FadeIn(d) for d in rej], lag_ratio=0.002), FadeIn(cont),
                      run_time=self.dur(1.0))

            # «ni una sola falsa alarma»
            self.en("cero")
            cero = VGroup(Text("Falsas alarmas: 0", color=VERDE, weight=BOLD).scale(0.75), tilde(VERDE, 0.5))
            cero.arrange(RIGHT, buff=0.25).next_to(det, DOWN, buff=0.7)
            self.pop(cero)

            # «¿Puedes decir»
            self.en("pregunta")
            q = Text("?", color=ESTIMACION, weight=BOLD).scale(1.4).next_to(cero, RIGHT, buff=0.3)
            self.pop(q)

            # «que nunca se equivoca?»
            self.en("nunca")
            err = MathTex(r"P_{FA} = 0\ ?", color=TXT).scale(1.2).next_to(cero, DOWN, buff=0.55)
            self.play(FadeIn(err, shift=UP * 0.15), run_time=self.dur(0.4))

            # «Uno que se equivoca»
            self.en("otro")
            self.corte()
            det2 = caja_detector6(ancho=3.8, alto=1.8, escala=0.8).move_to([-3.9, 2.0, 0])
            raro = Text("Falla 1 de cada 740", color=ERROR).scale(0.65).next_to(det2, DOWN, buff=0.3)
            self.add(det2)
            self.play(FadeIn(raro, shift=UP * 0.1), run_time=self.dur(0.4))

            # «una vez de cada mil»
            self.en("fa")
            fa = MathTex(r"P_{FA} \approx 0{,}00135", color=ERROR).scale(1.15).next_to(raro, DOWN, buff=0.45)
            self.play(Write(fa), run_time=self.dur(0.6))

            # «ese mismo resultado»
            self.en("mismo")
            cero2 = VGroup(Text("Falsas alarmas: 0", color=VERDE, weight=BOLD).scale(0.75), tilde(VERDE, 0.5))
            cero2.arrange(RIGHT, buff=0.2).next_to(fa, DOWN, buff=0.6)
            self.pop(cero2)

            # «una de cada cuatro veces»
            self.en("cuatro")
            rejs = VGroup(*[rejilla6(n=200, columnas=20, ancho=2.6, radio=0.04) for _ in range(4)])
            rejs.arrange_in_grid(2, 2, buff=0.5).move_to([3.3, 0.7, 0])
            self.play(LaggedStart(*[FadeIn(r) for r in rejs], lag_ratio=0.2), run_time=self.dur(0.7))
            marco = SurroundingRectangle(rejs[0], color=ESTIMACION, buff=0.12, stroke_width=4)
            pc = Text("26 %", color=ESTIMACION, weight=BOLD).scale(1.1).next_to(rejs, DOWN, buff=0.4)
            self.play(rejs[0].animate.set_color(ESTIMACION), Create(marco), run_time=self.dur(0.4))
            self.pop(pc)
        self.wait(0.8)
        self.limpiar()
