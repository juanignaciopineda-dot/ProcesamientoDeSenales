"""Escena 09 — Con mediciones blancas las ecuaciones de m < 0 no molestan: el causal es el no causal cortado."""
from comun.escena import *


class ElCausalEsElCortado(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        t = tabla_blanca()
        todo = VGroup(*t.ms, *t.cs, *t.hs, *t.rots)
        causal = self.palabra("causal", AMBAR, 0.8).move_to([-5.3, 3.4, 0])
        c0 = t.col(0)
        marco_neg = Rectangle(width=1.1, height=3.7, color=INK, stroke_width=3).set_fill(INK, 0.06)
        marco_neg.move_to([COL_X[0], -2.05, 0])
        cero = formula(r"h[j]=0\ \text{si}\ j<0", escala=0.7, colores={0: ESTIMACION}).move_to([-5.1, -2.2, 0])
        til = tilde(VERDE, 1.0).move_to([5.4, 1.0, 0])
        marco_pos = Rectangle(width=5.4, height=3.8, color=VERDE, stroke_width=4).set_fill(VERDE, 0.05)
        marco_pos.move_to([(COL_X[1] + COL_X[3]) / 2, 1.0, 0])
        fpos = formula(r"m\geq 0", escala=1.0, colores={0: AMBAR}).move_to([1.2, 3.55, 0])
        barras = Tallos([1, 0.5, 0.25], centro=(1.2, -2.8), paso=1.8, unidad=1.0, color=ESTIMACION)
        vtxt = [Text(s, color=ESTIMACION, weight=BOLD).scale(0.5).move_to([barras.x(i), -2.8 - 0.3, 0])
                for i, s in enumerate(["1", "0,5", "0,25"])]
        nocl = etiqueta("solución no causal", INK, 0.5).move_to([1.2, -3.8, 0])
        tj = tijeras().scale(0.9).move_to([-2.4, -1.2, 0])
        tj.permitir_encima = True
        with self.narrar("b1"):
            # «Y el causal»
            self.en("causal")
            self.play(FadeIn(todo), run_time=self.dur(0.6))
            self.pop(causal)

            # «las ecuaciones de eme negativo»
            self.en("neg")
            self.play(c0.animate.shift(DOWN * 3.0), run_time=self.dur(0.7))

            # «otras ecuaciones»
            self.en("otras")
            self.play(Create(marco_neg), run_time=self.dur(0.5))

            # «coeficientes que ahora valen cero»
            self.en("cero")
            self.play(FadeIn(cero), run_time=self.dur(0.5))

            # «no molestan a las demás»
            self.en("nomolestan")
            self.play(FadeIn(til, scale=0.6), run_time=self.dur(0.4))
            self.sfx("exito", gain=-18)

            # «Los coeficientes de eme mayor o igual que cero»
            self.en("mpos")
            self.play(Create(marco_pos), run_time=self.dur(0.5))
            self.pop(fpos)

            # «salen igual»
            self.en("igual")
            self.play(*[t.hs[i].animate(rate_func=there_and_back).scale(1.4).set_color(VERDE) for i in (1, 2, 3)],
                      run_time=self.dur(0.7))

            # «uno, cero coma cinco y cero coma dos cinco»
            self.en("vals")
            self.play(FadeIn(barras.base), *[FadeIn(v) for v in vtxt], run_time=self.dur(0.4))
            self.play(*[GrowFromEdge(barras.tallos[i], DOWN) for i in range(3)],
                      *[FadeIn(barras.puntos[i]) for i in range(3)], run_time=self.dur(0.7))

            # «Basta»
            self.en("basta")
            self.pop(self.palabra("basta", AMBAR, 0.7).move_to([5.2, -2.0, 0]))

            # «calcular la solución no causal»
            self.en("calc")
            self.play(FadeIn(nocl), run_time=self.dur(0.5))

            # «cortarle la parte no causal»
            self.en("corta")
            self.play(FadeIn(tj, scale=0.7), run_time=self.dur(0.4))
            self.play(FadeOut(c0), FadeOut(marco_neg), FadeOut(cero), run_time=self.dur(0.7))

        self.wait(1.0)
        self.limpiar()
