"""Escena 01 — Gancho: dependencia total y covarianza cero."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        ax, et = ejes((-1.3, 1.3, 1), (-0.2, 1.3, 1), ancho=6.8, alto=4.4, x_label="x", y_label="y")
        g = VGroup(ax, et).move_to([-2.6, -0.7, 0])
        xs = np.linspace(-1, 1, 36)
        pts = VGroup(*[Dot(ax.c2p(x, x * x), radius=0.1, color=SENAL) for x in xs])
        curva = ax.plot(lambda x: x * x, x_range=[-1, 1, 0.02], color=SENAL, stroke_width=4)
        with self.narrar("b1"):
            # «una es exactamente el cuadrado de la otra»
            self.en("cuadrado")
            y = formula("Y", "=", "X^2", colores={0: MEDIDA, 2: SENAL}, escala=1.8).move_to([-2.6, 3.0, 0])
            self.play(Create(g), FadeIn(y), run_time=self.dur(0.6))
            self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in pts], lag_ratio=0.04), run_time=self.dur(1.2))
            self.play(Create(curva), run_time=self.dur(0.6))

            # «Dependencia total»
            self.en("dep")
            s = sello("Dependencia total", ROJO).scale(1.5).move_to([4.4, 1.7, 0])
            self.pop(s)

            # «su covarianza vale cero»
            self.en("cero")
            c0 = formula(r"\sigma_{XY}", "=", "0", colores={0: AMBAR, 2: AMBAR}, escala=2.0).move_to([4.4, -0.4, 0])
            self.pop(c0)

            # «¿Cómo puede ser?»
            self.en("pregunta")
            q = Text("?", color=AMBAR, weight=BOLD).scale(3.2).move_to([4.4, -2.5, 0])
            self.pop(q)
        self.wait(0.5)
        self.limpiar()
