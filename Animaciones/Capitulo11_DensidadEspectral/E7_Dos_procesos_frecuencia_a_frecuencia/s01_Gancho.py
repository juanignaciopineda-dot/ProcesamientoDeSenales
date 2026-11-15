"""Escena 01 — Gancho: dos grabaciones sin relación dan coherencia uno, y es mentira."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        L1 = Lienzo(ancho=4.6, alto=1.4, t_rango=(0, 4), v_max=1.0, centro=(-4.2, 1.9))
        L2 = Lienzo(ancho=4.6, alto=1.4, t_rango=(0, 4), v_max=1.0, centro=(-4.2, -0.3))
        r1 = ruido_t(L1, semilla=7, amp=0.3, color=CIAN)
        r2 = ruido_t(L2, semilla=12, amp=0.3, color=MAGENTA)
        ne = MathTex(r"\neq", color=INK).scale(0.9).move_to([-4.2, 0.8, 0])
        sin = etiqueta("sin relación", INK, 0.55).move_to([-4.2, -1.5, 0])
        cb = caja("coherencia", AMBAR, ancho=2.8, alto=1.0).move_to([1.4, 0.8, 0])
        a1 = flecha([-1.8, 1.9, 0], [0.0, 1.2, 0])
        a2 = flecha([-1.8, -0.3, 0], [0.0, 0.4, 0])
        a3 = flecha([2.9, 0.8, 0], [4.0, 0.8, 0])
        uno = MathTex("1", color=ERROR).scale(3.2).move_to([5.3, 0.8, 0])
        aura = Circle(radius=1.0, color=AMBAR, stroke_width=5).move_to(uno)
        with self.narrar("b1"):
            # «Dos grabaciones»
            self.en("dos")
            self.play(Create(L1.base()), Create(r1), Create(L2.base()), Create(r2),
                      run_time=self.dur(1.0), rate_func=linear)

            # «ninguna relación»
            self.en("sinrel")
            self.play(FadeIn(ne), FadeIn(sin), run_time=self.dur(0.5))

            # «Mides cuánto se parecen»
            self.en("mides")
            self.play(FadeIn(cb), GrowArrow(a1), GrowArrow(a2), run_time=self.dur(0.7))

            # «sale uno»
            self.en("uno")
            self.play(GrowArrow(a3), run_time=0.3)
            self.pop(uno, sonido="impacto")

            # «parecido perfecto»
            self.en("perfecto")
            self.play(Create(aura), run_time=self.dur(0.6))
            self.sfx("exito")

            # «Es mentira»
            self.en("mentira")
            x = cruz(ROJO, 2.0).move_to(uno)
            self.play(Create(x), run_time=0.3)
            self.sfx("error")

            # «hoy vemos por qué»
            self.en("porque")
            lp = lupa(TXT).scale(1.8).move_to([6.1, -0.9, 0])
            self.play(FadeIn(lp, scale=0.6), run_time=self.dur(0.5))
            self.play(lp.animate.shift(UL * 0.5), run_time=self.dur(0.8))

        self.wait(1.0)
        self.limpiar()
