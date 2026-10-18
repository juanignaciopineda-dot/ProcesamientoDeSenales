"""Escena 11 — El contraejemplo: Y = X² es dependencia total y covarianza cero."""
from comun.escena import *


class ParabolaPerfecta(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        ax, et = ejes((-1.3, 1.3, 1), (-0.2, 1.3, 1), ancho=7.0, alto=4.6, x_label="x", y_label="y")
        g = VGroup(ax, et).move_to([-2.6, -0.7, 0])
        with self.narrar("b1"):
            # «equis uniforme entre menos uno y uno»
            self.en("uniforme")
            base = Line([1.6, 2.3, 0], [6.4, 2.3, 0], color=INK, stroke_width=2)
            rect = Rectangle(width=3.2, height=0.9, color=SENAL, fill_opacity=0.35, stroke_width=3).move_to([4.0, 2.75, 0])
            m1 = Text("−1", color=INK).scale(0.55).move_to([2.4, 1.95, 0])
            m2 = Text("1", color=INK).scale(0.55).move_to([5.6, 1.95, 0])
            self.play(Create(base), FadeIn(rect, scale=0.5), FadeIn(m1), FadeIn(m2), run_time=self.dur(0.9))

            # «define i griega como equis al cuadrado»
            self.en("def_y")
            y = formula("Y", "=", "X^2", colores={0: MEDIDA, 2: SENAL}, escala=1.9).move_to([4.0, 0.7, 0])
            self.play(Create(g), run_time=self.dur(0.6))
            self.pop(y)

            # «Estas dos variables»
            self.en("estas")
            self.resaltar(y, color=AMBAR, escala=1.1)

            # «todo lo dependientes que pueden ser»
            self.en("dep")
            s = sello("Totalmente dependientes", ROJO).scale(1.2).move_to([4.0, -1.3, 0])
            self.pop(s)

            # «equis vale cero coma siete»
            self.en("x07")
            lin = DashedLine(ax.c2p(0.7, 0), ax.c2p(0.7, 1.2), color=AMBAR, stroke_width=3)
            et07 = Text("x = 0,7", color=AMBAR).scale(0.6).next_to(ax.c2p(0.7, 1.2), UP, buff=0.1)
            self.play(Create(lin), FadeIn(et07), run_time=self.dur(0.7))

            # «sabes sin ninguna duda»
            self.en("sin_duda")
            punto = Dot(ax.c2p(0.7, 0), radius=0.13, color=AMBAR)
            self.add(punto)
            self.play(punto.animate.move_to(ax.c2p(0.7, 0.49)), run_time=self.dur(0.8))

            # «cero coma cuarenta y nueve»
            self.en("y049")
            t49 = Text("0,49", color=AMBAR).scale(0.65).next_to(punto, LEFT, buff=0.25)
            self.play(FadeIn(t49, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «La nube ni siquiera es una nube»
            self.en("no_nube")
            xs = np.linspace(-1, 1, 41)
            pts = VGroup(*[Dot(ax.c2p(x, x * x), radius=0.08, color=SENAL) for x in xs])
            self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in pts], lag_ratio=0.03), run_time=self.dur(1.2))

            # «una parábola perfecta»
            self.en("parabola")
            curva = ax.plot(lambda x: x * x, x_range=[-1, 1, 0.02], color=SENAL, stroke_width=4)
            self.play(Create(curva), run_time=self.dur(0.9))
        self.wait(1.0)
        self.limpiar()
