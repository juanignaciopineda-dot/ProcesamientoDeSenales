"""Escena 11 — Los tres tipos de memoria: la moneda no recuerda, el sensor olvida poco a poco, los osciladores no olvidan."""
from comun.escena import *


class TresMemorias(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        ks9 = range(0, 9)
        P1 = Palitos(ks9, [1] + [0] * 8, ancho=3.8, alto=2.4, v_max=1.0, centro=(-4.6, 0.6))
        P2 = Palitos(ks9, [0.6 ** k for k in ks9], ancho=3.8, alto=2.4, v_max=1.0, centro=(0.0, 0.6))
        ks17 = range(0, 17)
        P3 = Palitos(ks17, [0.5 * np.cos(2 * np.pi * k / 8) for k in ks17], ancho=3.8, alto=2.4, v_max=1.0,
                     centro=(4.6, 0.6), punto=0.05)
        with self.narrar("b1"):
            # «la memoria del proceso»
            self.en("memoria")
            c = formula("C", escala=1.0, colores={0: AMBAR}).move_to([-6.3, 2.45, 0])
            self.play(FadeIn(P1.base), FadeIn(P1.eje), FadeIn(c), run_time=self.dur(0.6))

            # «tres tipos»
            self.en("tres")
            self.play(FadeIn(P2.base), FadeIn(P2.eje), FadeIn(P3.base), FadeIn(P3.eje), run_time=self.dur(0.6))

            # «La moneda no recuerda nada»
            self.en("moneda")
            l1 = Text("no recuerda", color=TXT, weight=BOLD).scale(0.6).move_to([-4.6, -1.9, 0])
            self.play(Create(P1.tallos[0]), FadeIn(P1.puntos[0]), run_time=0.5)
            self.pop(l1)

            # «El sensor recuerda»
            self.en("sensor")
            self.play(LaggedStart(*[AnimationGroup(Create(a), FadeIn(b)) for a, b in zip(P2.tallos, P2.puntos)],
                                  lag_ratio=0.15), run_time=self.dur(1.6))

            # «poco a poco»
            self.en("poco")
            l2 = Text("olvida poco a poco", color=TXT, weight=BOLD).scale(0.6).move_to([0, -1.9, 0])
            x06 = formula(r"\times 0{,}6", escala=0.9, colores={0: AMBAR}).move_to([0.9, 2.2, 0])
            self.pop(l2)
            self.pop(x06)

            # «los osciladores no olvidan nunca»
            self.en("osc")
            l3 = Text("no olvida", color=TXT, weight=BOLD).scale(0.6).move_to([4.6, -1.9, 0])
            self.play(LaggedStart(*[AnimationGroup(Create(a), FadeIn(b)) for a, b in zip(P3.tallos, P3.puntos)],
                                  lag_ratio=0.06), run_time=self.dur(1.8))
            self.pop(l3)

            # «un período entero después»
            self.en("periodo")
            x8 = P3.pos(8, 0.0)[0]
            guia = DashedLine([x8, 0.6, 0], [x8, 2.2, 0], color=AMBAR, stroke_width=3)
            per = Text("1 período", color=AMBAR).scale(0.5).move_to([x8, 2.5, 0])
            self.play(Create(guia), FadeIn(per), run_time=self.dur(0.6))

            # «vuelve a valer un medio»
            self.en("medio")
            p8 = Dot(P3.pos(8), radius=0.12, color=AMBAR)
            mitad = formula(r"\tfrac12", escala=1.0, colores={0: AMBAR}).next_to(p8, RIGHT, buff=0.25)
            self.play(FadeIn(p8, scale=2), run_time=0.3)
            self.pop(mitad)

            # «Los tres van a volver»
            self.en("vuelven")
            rects = [Rectangle(width=4.2, height=5.5, color=AMBAR, stroke_width=3).move_to([x, 0.3, 0])
                     for x in (-4.6, 0.0, 4.6)]
            self.play(*[Create(r) for r in rects], run_time=0.6)
        self.wait(1.0)
        self.limpiar()
