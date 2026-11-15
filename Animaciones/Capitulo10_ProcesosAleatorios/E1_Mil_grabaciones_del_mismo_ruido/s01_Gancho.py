"""Escena 01 — Gancho: dos grabaciones del mismo ruido no coinciden; mil, menos aún."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        t = np.linspace(0, 1, 260)
        L1 = Lienzo(ancho=10.5, alto=2.3, t_rango=(0, 1), v_max=2.6, centro=(-0.6, 1.5))
        L2 = Lienzo(ancho=10.5, alto=2.3, t_rango=(0, 1), v_max=2.6, centro=(-0.6, -1.2))

        with self.narrar("b1"):
            # «Grabas el ruido»
            self.en("grab1")
            b1 = L1.base()
            c1 = L1.curva(t, serie(11, 260, 0.8), RUIDO, 3.5)
            self.play(Create(b1), run_time=0.3)
            self.play(Create(c1), run_time=self.dur(1.8), rate_func=linear)

            # «y otra vez»
            self.en("grab2")
            b2 = L2.base()
            c2 = L2.curva(t, serie(12, 260, 0.8), RUIDO, 3.5)
            self.play(Create(b2), run_time=0.3)
            self.play(Create(c2), run_time=self.dur(1.8), rate_func=linear)

            # «no se parecen en nada»
            self.en("distintas")
            distinto = Text("≠", color=ROJO, weight=BOLD).scale(2.4).move_to([6.1, 0.15, 0])
            self.pop(distinto)
            self.play(c1.animate.set_stroke(width=5.5), c2.animate.set_stroke(width=5.5),
                      run_time=self.dur(0.6))

            # «Mil grabaciones»
            self.en("mil")
            self.play(*[FadeOut(m) for m in (b1, c1, b2, c2, distinto)], run_time=0.35)
            Lp = Lienzo(ancho=11.5, alto=4.9, t_rango=(0, 1), v_max=2.2, centro=(0, 0.9))
            pila = pila_de_curvas(Lp, 46, semilla=5, a=0.85, color=RUIDO, opacidad=0.5, ancho=2.2, escala=0.55)
            self.play(LaggedStart(*[Create(c) for c in pila], lag_ratio=0.04),
                      run_time=self.dur(3.0))

            # «¿Cómo se describe el azar»
            self.en("pregunta")
            q = Text("¿Cómo se describe el azar de una señal entera?", color=TXT, weight=BOLD).scale(0.72)
            q.move_to([0, -3.35, 0])
            self.play(FadeIn(q, shift=UP * 0.2), run_time=0.5)

        self.wait(1.0)
        self.limpiar()
