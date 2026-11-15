"""Escena 01 — Gancho: una temperatura tapada por el ruido y la pregunta del mejor filtro."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        t, y, v, x = sensor12(40)
        L = Lienzo(ancho=5.6, alto=2.8, t_rango=(0, 39), v_max=7, centro=(-4.0, 0.2))
        L2 = Lienzo(ancho=4.4, alto=2.8, t_rango=(0, 39), v_max=7, centro=(5.0, 0.2))
        base, base2 = L.base(), L2.base()
        cy = L.curva(t, y, SENAL, 4)
        cv = L.curva(t, v, RUIDO, 2.6)
        cx = L.curva(t, x, MEDIDA, 3.5)
        f1 = caja("filtro", AMBAR, ancho=2.0, alto=0.9).move_to([0.5, 0.2, 0])
        f2 = f1.copy().shift(UP * 1.9)
        f3 = f1.copy().shift(DOWN * 1.9)
        ent = flecha([-1.1, 0.2, 0], [-0.55, 0.2, 0], INK)
        sal = flecha([1.55, 0.2, 0], [2.4, 0.2, 0], INK)
        out = L2.curva(t, suavizada(x), ESTIMACION, 4)
        pregunta = Text("¿cuál es el mejor?", color=AMBAR, weight=BOLD).scale(0.7).move_to([0, 3.4, 0])
        grande = Text("?", color=AMBAR, weight=BOLD).scale(2.4).move_to([0, 0.2, 0])

        with self.narrar("b1"):
            # «Una temperatura»
            self.en("temp")
            self.play(Create(base), Create(cy), run_time=self.dur(0.8))

            # «tapada por el ruido»
            self.en("ruido")
            self.play(Create(cv), run_time=self.dur(0.6))
            self.play(cy.animate.set_stroke(opacity=0.3), cv.animate.set_stroke(opacity=0.3),
                      Create(cx), run_time=self.dur(0.7))

            # «un filtro»
            self.en("filtro")
            self.play(FadeIn(f1), Create(ent), run_time=self.dur(0.5))

            # «para recuperarla»
            self.en("recuperar")
            self.play(Create(sal), Create(base2), Create(out), run_time=self.dur(1.0))

            # «De todos los filtros posibles»
            self.en("todos")
            self.play(FadeIn(f2, shift=DOWN * 0.3), FadeIn(f3, shift=UP * 0.3), run_time=self.dur(0.6))

            # «¿cuál es el mejor?»
            self.en("cual")
            self.pop(pregunta)

            # «La respuesta»
            self.en("respuesta")
            self.play(*[FadeOut(m) for m in [f1, f2, f3, ent, sal, out, base2, cx, cy, cv, base]],
                      run_time=self.dur(0.4))
            self.pop(grande)

            # «un ángulo recto»
            self.en("recto")
            self.corte()
            F, r = flechas_xy(origen=(-2.8, -1.6), largo=4.6, angulo=50)
            self.play(Create(F.presente), Create(F.futuro), FadeIn(r["x"]), FadeIn(r["y"]), run_time=self.dur(0.5))
            self.play(Create(F.sombra), FadeIn(r["yh"]), Create(F.error), FadeIn(r["e"]), run_time=self.dur(0.5))
            self.play(Create(F.recto), run_time=self.dur(0.3))
        self.wait(1.0)
        self.limpiar()
