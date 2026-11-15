"""Escena 20 — Sumar los coeficientes de correlación del sensor: 1 + 2 · 1,5 = 4."""
from comun.escena import *


class SumarElSensor(EscenaCurso):
    ESCENA = "20"

    def construct(self):
        base, dx, y0, esc = ejes_k(5, ancho=10.0, alto=2.8, v_max=1.0, centro=(0, 0.0))
        dx = 0.8
        ro = [0.6 ** k for k in range(6)]
        barras = {k: barra_k(k, ro[abs(k)], dx, y0, esc, 0.0, AMBAR if k == 0 else CIAN) for k in range(-5, 6)}
        ks = {k: Text(str(k), color=INK).scale(0.4).move_to([k * dx, -0.3, 0]) for k in range(-5, 6)}

        def rot(k):
            return Text(num(ro[abs(k)], 3), color=TXT, weight=BOLD).scale(0.42).next_to(barras[k], UP, buff=0.08)

        with self.narrar("b1"):
            # «Sumémosla para el sensor»
            self.en("sumemos")
            self.play(Create(base), FadeIn(VGroup(*ks.values())), run_time=self.dur(0.8))

            # «En separación cero, uno»
            self.en("cero")
            self.play(GrowFromEdge(barras[0], DOWN), run_time=0.5)
            r0 = Text("1", color=AMBAR, weight=BOLD).scale(0.5).next_to(barras[0], UP, buff=0.08)
            self.play(FadeIn(r0), run_time=0.2)

            # «cero coma seis a cada lado»
            self.en("b06")
            self.play(GrowFromEdge(barras[1], DOWN), GrowFromEdge(barras[-1], DOWN), run_time=0.5)
            self.play(FadeIn(rot(1)), FadeIn(rot(-1)), run_time=0.3)

            # «cero coma tres seis»
            self.en("b036")
            self.play(GrowFromEdge(barras[2], DOWN), GrowFromEdge(barras[-2], DOWN), run_time=0.5)
            self.play(FadeIn(rot(2)), FadeIn(rot(-2)), run_time=0.3)

            # «cero coma dos uno seis»
            self.en("b0216")
            self.play(GrowFromEdge(barras[3], DOWN), GrowFromEdge(barras[-3], DOWN), run_time=0.5)
            self.play(FadeIn(rot(3)), FadeIn(rot(-3)), run_time=0.3)
            self.play(*[GrowFromEdge(barras[k], DOWN) for k in (4, -4, 5, -5)], run_time=self.dur(0.8))

            # «El lado derecho va sumando»
            self.en("lado")
            cont = MathTex(r"\sum_{k>0}=0{,}6", color=AMBAR).scale(1.2).move_to([3.0, -1.5, 0])
            self.play(FadeIn(cont), run_time=0.4)

            # «cero coma nueve seis»
            self.en("s096")
            c2 = MathTex(r"\sum_{k>0}=0{,}96", color=AMBAR).scale(1.2).move_to(cont)
            self.play(Transform(cont, c2), run_time=0.3)

            # «uno coma uno ocho»
            self.en("s118")
            c3 = MathTex(r"\sum_{k>0}=1{,}18", color=AMBAR).scale(1.2).move_to(cont)
            self.play(Transform(cont, c3), run_time=0.3)

            # «uno coma tres»
            self.en("s13")
            c4 = MathTex(r"\sum_{k>0}=1{,}3", color=AMBAR).scale(1.2).move_to(cont)
            self.play(Transform(cont, c4), run_time=0.3)

            # «uno coma cinco»
            self.en("s15")
            c5 = MathTex(r"\sum_{k>0}\to1{,}5", color=AMBAR).scale(1.2).move_to(cont)
            self.play(Transform(cont, c5), run_time=0.4)

            # «Los dos lados dan tres»
            self.en("tres")
            d = MathTex(r"2\times1{,}5=3", color=CIAN).scale(1.2).move_to([-3.0, -2.6, 0])
            self.pop(d)

            # «el uno del centro, cuatro»
            self.en("cuatro")
            t4 = MathTex(r"1+3=4", color=AMBAR).scale(1.6).move_to([3.0, -2.9, 0])
            self.pop(t4)
        self.wait(1.0)
        self.limpiar()
