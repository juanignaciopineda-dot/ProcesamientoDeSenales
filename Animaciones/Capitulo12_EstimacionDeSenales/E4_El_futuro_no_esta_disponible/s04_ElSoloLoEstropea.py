"""Escena 04 — La ecuación es la misma, pero vale solo para m ≥ 0: ese «solo» lo estropea todo."""
from comun.escena import *


class ElSoloLoEstropea(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        f = oculta(formula("h", r"\ast", "C_{xx}", "=", "C_{yx}", r"\quad", r"\text{solo}", r"\quad m\geq 0",
                           escala=1.4, colores={0: ESTIMACION, 2: MEDIDA, 4: SENAL, 6: ROJO, 7: AMBAR}))
        f.move_to([0, 2.6, 0])
        self.add(f)
        rec = caja("episodio anterior: se transformaba", INK, ancho=5.6, alto=0.8, scale=0.5).move_to([0, 0.9, 0])
        izq = Line([-6, -0.8, 0], [0, -0.8, 0], color=AZUL, stroke_width=9)
        der = Line([0, -0.8, 0], [6, -0.8, 0], color=AZUL, stroke_width=9)
        lm = MathTex("m", color=INK).scale(0.7).move_to([6.5, -0.8, 0])
        cero = Text("0", color=INK).scale(0.45).move_to([0, -1.25, 0])
        celdas = []
        for y, r in ((-2.4, "p"), (-3.4, "q")):
            fila = VGroup(*[Square(side_length=0.6, color=INK, stroke_width=2.5) for _ in range(7)]).arrange(RIGHT, buff=0.0)
            fila.move_to([0.6, y, 0])
            rot = MathTex(r, color=SENAL if r == "p" else RUIDO).scale(0.9).next_to(fila, LEFT, buff=0.4)
            celdas.append(VGroup(fila, rot))
        with self.narrar("b1"):
            # «hache convolucionado con la autocorrelación»
            self.en("conv")
            self.play(*revelar(f[0], f[1], f[2]), run_time=self.dur(0.7))

            # «igual a la correlación cruzada»
            self.en("igual")
            self.play(*revelar(f[3], f[4]), run_time=self.dur(0.6))

            # «solo para eme mayor o igual que cero»
            self.en("solom")
            self.play(*revelar(f[5], f[6], f[7]), run_time=self.dur(0.7))

            # «ese solo lo estropea todo»
            self.en("estropea")
            self.sfx("error")
            self.play(f[6].animate(rate_func=there_and_back).scale(1.6), run_time=self.dur(0.7))

            # «Recuerda el episodio anterior»
            self.en("recuerda")
            self.play(FadeIn(rec, shift=UP * 0.2), run_time=self.dur(0.5))

            # «la igualdad valía en todo el eje»
            self.en("eje")
            self.play(Create(izq), Create(der), FadeIn(lm), FadeIn(cero), run_time=self.dur(0.9))

            # «Ahora no»
            self.en("ahorano")
            self.play(izq.animate.set_stroke(opacity=0.2), run_time=self.dur(0.5))
            self.sfx("tick")

            # «dos secuencias muy pequeñas»
            self.en("dos")
            self.play(FadeIn(celdas[0]), FadeIn(celdas[1]), run_time=self.dur(0.6))

        self.wait(1.0)
        self.limpiar()
