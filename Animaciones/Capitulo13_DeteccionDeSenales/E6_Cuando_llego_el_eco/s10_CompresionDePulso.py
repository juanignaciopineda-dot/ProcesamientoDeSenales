"""Escena 10 — Compresión de pulso: pulso largo, autocorrelación estrecha."""
from comun.escena import *


class CompresionDePulso(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        largo = Tallos([1] * 13, centro=(-3.5, 1.2), paso=0.4, unidad=0.5, color=SENAL)
        ener = formula("E", "=", r"\text{largo}", r"\times", r"\text{amplitud}", escala=0.85,
                       colores={0: AMBAR}).move_to([-3.5, 3.0, 0])
        area = Rectangle(width=13 * 0.4, height=0.5, color=AMBAR, stroke_width=0).set_fill(AMBAR, 0.3).move_to([-3.5, 1.45, 0])
        tx = antena().scale(0.8).move_to([-6.2, -0.3, 0])
        tope = DashedLine([-6.0, 1.9, 0], [-1.0, 1.9, 0], color=ERROR, stroke_width=3)
        lim = Text("tope", color=ERROR).scale(0.45).move_to([-0.5, 1.9, 0])
        # autocorrelación estrecha
        ac = Tallos([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 3.6, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], centro=(3.5, -0.6), paso=0.4,
                    unidad=0.5, color=AMBAR)
        g = Text("grande", color=AMBAR).scale(0.5).move_to([3.5, 1.7, 0])
        peq = Text("pequeña", color=INK).scale(0.5).move_to([5.6, -1.4, 0])
        pl = Tallos([1] * 13, centro=(-4.2, -2.3), paso=0.2, unidad=0.4, color=SENAL)
        filt = caja("filtro", AMBAR, ancho=1.8, alto=0.7, scale=0.5).move_to([-1.6, -2.3, 0])
        f1 = flecha([-2.9, -2.3, 0], [-2.5, -2.3, 0], INK)
        pico = Tallos([0, 0, 0, 0, 0, 0, 3.0, 0, 0, 0, 0, 0, 0], centro=(1.4, -2.7), paso=0.2, unidad=0.4, color=AMBAR)
        f2 = flecha([-0.7, -2.3, 0], [0.0, -2.3, 0], INK)
        cp = Text("compresión de pulso", color=AMBAR, weight=BOLD).scale(0.75).move_to([-3.5, 3.0, 0])
        with self.narrar("b1"):
            # «Queremos un pulso largo»
            self.en("largo")
            self.play(FadeIn(largo), run_time=self.dur(0.6))
            # «la energía es el largo por la amplitud»
            self.en("energia")
            self.play(FadeIn(ener), FadeIn(area), run_time=self.dur(0.9))
            # «la amplitud del transmisor»
            self.en("transmisor")
            self.play(FadeIn(tx), run_time=self.dur(0.5))
            # «está limitada»
            self.en("limitada")
            self.play(Create(tope), FadeIn(lim), run_time=self.dur(0.6))
            # «Pero también queremos»
            self.en("tambien")
            self.play(FadeOut(ener), FadeOut(area), FadeOut(tx), FadeOut(tope), FadeOut(lim), run_time=0.3)
            # «una autocorrelación estrecha»
            self.en("estrecha")
            self.play(FadeIn(ac), run_time=self.dur(0.8))
            # «grande en el origen»
            self.en("origen")
            self.pop(g)
            # «pequeña en todos los demás desplazamientos»
            self.en("demas")
            self.pop(peq)
            # «Un pulso largo»
            self.en("pl")
            self.play(FadeIn(pl), run_time=0.4)
            # «se comprime en un pico estrecho»
            self.en("comprime")
            self.play(FadeIn(filt), GrowArrow(f1), GrowArrow(f2), run_time=0.4)
            self.play(FadeIn(pico), run_time=self.dur(0.6))
            # «compresión de pulso»
            self.en("compresion")
            self.pop(cp)
        self.wait(1.0)
        self.limpiar()
