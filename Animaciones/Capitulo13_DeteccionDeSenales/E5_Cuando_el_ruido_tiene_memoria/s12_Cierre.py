"""Escena 12 — Cierre: blanquear y adaptar; falta saber cuándo llega el pulso (anuncia E6)."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        blq = caja("blanqueador", ESTIMACION, ancho=2.8, alto=0.9, scale=0.5).move_to([-4.3, 2.7, 0])
        bola = Circle(radius=0.5, color=RUIDO, stroke_width=4).set_fill(RUIDO, 0.15).move_to([-0.6, 2.7, 0])
        adp = caja("filtro adaptado", SENAL, ancho=3.2, alto=0.9, scale=0.5).move_to([3.8, 2.7, 0])
        a1 = flecha(blq.get_right(), bola.get_left() + LEFT * 0.03, INK)
        a2 = flecha(bola.get_right(), adp.get_left() + LEFT * 0.03, INK)
        Pl = Tallos([1, 1], centro=(-3.0, 0.5), paso=1.1, unidad=0.9, color=SENAL)
        Pr = Tallos([1, -1], centro=(2.4, 0.5), paso=1.1, unidad=0.9, color=SENAL)
        n125 = MathTex(num_tex(1.25), color=AMBAR).scale(1.0).move_to([-3.0, -1.0, 0])
        n5 = MathTex("5", color=AMBAR).scale(1.0).move_to([2.4, -1.0, 0])
        # el pulso en un lugar fijo
        linea = Line([-5.5, 0.4, 0], [5.5, 0.4, 0], color=INK, stroke_width=2)
        ticks = VGroup(*[Line([x, 0.3, 0], [x, 0.5, 0], color=INK, stroke_width=2) for x in np.arange(-5, 5.1, 1.0)])
        pul = Tallos([2, 2, 1], centro=(-2.0, 0.4), paso=0.7, unidad=0.6, color=SENAL)
        ok = tilde(VERDE, 0.9).move_to([-2.0, 2.3, 0])
        # el radar
        ant = antena(TXT).scale(1.1).move_to([-5.0, -0.8, 0])
        av = avion_arriba(AZUL).scale(1.3).move_to([4.5, 1.6, 0])
        enlace = DashedLine([-4.2, -0.4, 0], [3.6, 1.4, 0], color=INK, stroke_width=2.5)
        dq = MathTex("D = ?", color=AMBAR).scale(1.2).move_to([-0.2, 2.2, 0])
        prox = Text("próximo episodio", color=INK).scale(0.55).move_to([0, -1.9, 0])
        titulo_ = Text("¿Cuándo llegó el eco?", color=AMBAR, weight=BOLD).scale(0.95).move_to([0, -2.9, 0])
        eco = CurvedArrow([3.6, 1.0, 0], [-4.0, 0.1, 0], angle=-PI / 4, color=CIAN, stroke_width=4)

        with self.narrar("b1"):
            # «se blanquea primero»
            self.en("blanquea")
            self.play(FadeIn(blq), Create(a1), FadeIn(bola), run_time=self.dur(0.8))

            # «se adapta después»
            self.en("adapta")
            self.play(Create(a2), FadeIn(adp), run_time=self.dur(0.7))

            # «la forma de la señal sí importa»
            self.en("forma")
            self.play(Create(Pl.base), Create(Pl.palito(0)), Create(Pl.palito(1)),
                      Create(Pr.base), Create(Pr.palito(0)), Create(Pr.palito(1)), run_time=self.dur(0.8))
            self.play(FadeIn(n125), FadeIn(n5), run_time=self.dur(0.5))

            # «siempre hemos sabido»
            self.en("sabido")
            self.corte()
            self.play(Create(linea), Create(ticks), Create(pul.base), run_time=self.dur(0.6))
            self.play(Create(ok), run_time=self.dur(0.4))

            # «cuándo llegaba el pulso»
            self.en("cuando")
            self.play(*[Create(pul.palito(i)) for i in range(3)], run_time=self.dur(0.7))

            # «Un radar de verdad»
            self.en("radar")
            self.corte()
            self.play(FadeIn(ant), FadeIn(av), Create(enlace), run_time=self.dur(0.8))

            # «justo lo que quiere medir»
            self.en("medir")
            self.pop(dq)

            # «En el próximo episodio»
            self.en("proximo")
            self.play(FadeIn(prox), run_time=self.dur(0.4))

            # «¿cuándo llegó el eco?»
            self.en("eco")
            self.pop(titulo_)
            self.play(Create(eco), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
