"""Escena 01 — Gancho: una muestra se equivoca el 16 %, con la vecina baja al 10 %."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        # izquierda: las muestras recibidas y el error
        T = Tallos([2, 0], centro=(-4.0, 0.2), paso=1.8, unidad=1.0, color=MEDIDA, indices=True)
        r0 = MathTex("r_0", color=MEDIDA).scale(1.0).next_to(T.pos(0), UP, buff=0.12)
        r1 = MathTex("r_1", color=MEDIDA).scale(1.0).next_to(T.pos(1), UP, buff=0.15)
        e16 = MathTex(r"P_e = 15{,}9\,\%", color=ERROR).scale(1.2).move_to([-4.0, -1.4, 0])
        e10 = MathTex(r"P_e = 10{,}6\,\%", color=ERROR).scale(1.2).move_to([-4.0, -1.4, 0])
        cuadros = VGroup(*[Square(0.38, stroke_width=2).set_stroke(INK).set_fill(INK, 0.15) for _ in range(20)])
        cuadros.arrange_in_grid(rows=2, cols=10, buff=0.08).move_to([-4.0, -2.9, 0])
        rojos = [3, 9, 15]
        # derecha: dos muestras de ruido unidas por la memoria
        v0 = Dot([2.6, 0.6, 0], radius=0.2, color=RUIDO)
        v1 = Dot([5.6, 0.6, 0], radius=0.2, color=RUIDO)
        l0 = MathTex("v_0", color=RUIDO).scale(1.0).next_to(v0, DOWN, buff=0.15)
        l1 = MathTex("v_1", color=RUIDO).scale(1.0).next_to(v1, DOWN, buff=0.15)
        hilo = Line(v0.get_center(), v1.get_center(), color=RUIDO, stroke_width=4)
        copia = CurvedArrow(v1.get_top() + UP * 0.05, v0.get_top() + UP * 0.05, angle=PI / 2.2,
                            color=RUIDO, stroke_width=7)
        porque = Text("¿por qué?", color=AMBAR, weight=BOLD).scale(1.0).move_to([4.1, 3.0, 0])

        with self.narrar("b1"):
            # «una sola muestra»
            self.en("una")
            self.play(Create(T.base), Create(T.palito(0)), FadeIn(r0), run_time=self.dur(0.7))

            # «casi el dieciséis por ciento»
            self.en("err16")
            self.pop(e16)

            # «de las veces»
            self.en("veces")
            self.play(FadeIn(cuadros), run_time=self.dur(0.4))
            self.play(*[cuadros[i].animate.set_fill(ERROR, 0.8).set_stroke(ERROR) for i in rojos],
                      run_time=self.dur(0.5))

            # «la de al lado»
            self.en("lado")
            self.play(Create(T.palito(1)), FadeIn(r1), run_time=self.dur(0.6))

            # «poco más del diez»
            self.en("err10")
            self.play(ReplacementTransform(e16, e10), cuadros[15].animate.set_fill(INK, 0.15).set_stroke(INK),
                      run_time=self.dur(0.7))

            # «¿Por qué?»
            self.en("porque")
            self.pop(porque)

            # «el ruido tiene memoria»
            self.en("memoria")
            self.play(FadeIn(v0), FadeIn(v1), FadeIn(l0), FadeIn(l1), run_time=self.dur(0.4))
            self.play(Create(hilo), run_time=self.dur(0.5))

            # «el vecino delata al ruido»
            self.en("delata")
            self.play(Create(copia), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
