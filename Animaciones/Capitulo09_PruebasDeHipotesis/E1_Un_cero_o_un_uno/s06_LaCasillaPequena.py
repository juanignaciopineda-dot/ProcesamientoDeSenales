"""Escena 06 — En cada columna, lo que menos falla: la tabla del canal."""
from comun.escena import *
from comun.figuras_c9e1 import *


class LaCasillaPequena(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.columna_uno()
        self.columna_cero()
        self.wait(1.0)
        self.limpiar()

    def columna_uno(self):
        with self.narrar("b1"):
            # «¿Por qué gana?»
            self.en("porque")
            preg = Text("¿Por qué?", color=ESTIMACION, weight=BOLD).scale(0.75).move_to([0, 3.35, 0])
            self.pop(preg)

            # «la tabla del canal»
            self.en("tabla")
            T = TablaCanal(centro=(-0.6, -0.1), lado=1.6, esc=0.6)
            self.T = T
            self.play(FadeIn(T.armazon()), FadeIn(T.probs()), run_time=self.dur(0.6))

            # «columna por columna»
            self.en("columnas")
            col1 = VGroup(T.cel[0][1], T.cel[1][1], T.prob[0][1], T.prob[1][1], T.enc_c[1])
            self.play(col1.animate.shift(RIGHT * 0.35), run_time=self.dur(0.5))
            self.col1 = col1

            # «la columna de»
            self.en("col1")
            mc = SurroundingRectangle(VGroup(T.cel[0][1], T.cel[1][1]), color=MEDIDA, buff=0.08, stroke_width=5)
            self.mc = mc
            self.play(Create(mc), run_time=self.dur(0.4))

            # «cero coma veintisiete»
            self.en("c27")
            s1 = Text("Se envió 1", color=C1).scale(0.36).move_to(T.cel[1][1].get_center() + UP * 0.42)
            self.play(T.cel[1][1].animate.set_stroke(C1, 5), FadeIn(s1), run_time=self.dur(0.4))

            # «cero coma cero siete»
            self.en("c07")
            s0 = Text("Se envió 0", color=C0).scale(0.36).move_to(T.cel[0][1].get_center() + UP * 0.42)
            self.play(T.cel[0][1].animate.set_stroke(C0, 5), FadeIn(s0), run_time=self.dur(0.4))

            # «Si dices uno»
            self.en("di1")
            dec = Text("Decir 1", color=ESTIMACION, weight=BOLD).scale(0.55)
            dec.move_to([T.cel[0][1].get_x(), 2.55, 0])
            self.dec = dec
            self.pop(dec)

            # «aciertas la grande»
            self.en("grande")
            ok = tilde(VERDE, 0.5).next_to(T.cel[1][1], RIGHT, buff=0.3)
            self.play(T.prob[1][1].animate.set_color(VERDE), Create(ok), run_time=self.dur(0.4))

            # «fallas la pequeña»
            self.en("falla")
            mal = cruz(ERROR, 0.5).next_to(T.cel[0][1], RIGHT, buff=0.35)
            self.play(T.prob[0][1].animate.set_color(ERROR), Create(mal), run_time=self.dur(0.4))
            self.marcas = VGroup(ok, mal)

            # «Si dices cero, al revés»
            self.en("di0")
            dec0 = Text("Decir 0", color=ESTIMACION, weight=BOLD).scale(0.55).move_to(dec)
            self.play(Transform(dec, dec0), T.prob[1][1].animate.set_color(ERROR),
                      T.prob[0][1].animate.set_color(VERDE), FadeOut(self.marcas), run_time=self.dur(0.5))
            dec1 = Text("Decir 1", color=ESTIMACION, weight=BOLD).scale(0.55).move_to(dec)
            self.wait(0.5)
            otra = self.marcas.copy()
            self.play(Transform(dec, dec1), T.prob[1][1].animate.set_color(VERDE),
                      T.prob[0][1].animate.set_color(ERROR), FadeIn(otra), run_time=self.dur(0.5))

            # «Elegir lo más probable»
            self.en("elegir")
            el = Text("Elegir lo más probable", color=TXT).scale(0.55).move_to([0, -2.45, 0])
            self.el = el
            self.play(FadeIn(el, shift=UP * 0.2), run_time=self.dur(0.4))

            # «fallar la casilla»
            self.en("pequena")
            pq = Text("= Fallar la pequeña", color=ESTIMACION, weight=BOLD).scale(0.55).next_to(el, DOWN, buff=0.25)
            self.pq = pq
            self.pop(pq)

    def columna_cero(self):
        T = self.T
        with self.narrar("b2"):
            # «En la otra columna»
            self.en("col0")
            mc0 = SurroundingRectangle(VGroup(T.cel[0][0], T.cel[1][0]), color=MEDIDA, buff=0.08, stroke_width=5)
            self.play(Transform(self.mc, mc0), FadeOut(self.el), FadeOut(self.pq), FadeOut(self.dec),
                      run_time=self.dur(0.5))

            # «dices cero»
            self.en("verde")
            self.play(T.prob[0][0].animate.set_color(VERDE), run_time=self.dur(0.4))

            # «cero coma cero tres»
            self.en("c03")
            self.play(T.prob[1][0].animate.set_color(ERROR), run_time=self.dur(0.4))

            # «en cada columna»
            self.en("cada")
            rojos = [T.prob[0][1], T.prob[1][0]]
            self.play(*[r.animate(rate_func=there_and_back).scale(1.35) for r in rojos], run_time=self.dur(0.6))

            # «el menor»
            self.en("menor")
            c07 = T.prob[0][1].copy()
            c03 = T.prob[1][0].copy()
            self.add(c07, c03)
            dest = MathTex(r"0{,}07", "+", r"0{,}03", "=", r"0{,}10", color=TXT).scale(0.95).move_to([-0.6, -2.75, 0])
            dest[0].set_color(ERROR)
            dest[2].set_color(ERROR)
            self.play(c07.animate.move_to(dest[0]), c03.animate.move_to(dest[2]), run_time=self.dur(0.7))

            # «cero coma cero siete más»
            self.en("mas")
            self.play(ReplacementTransform(c07, dest[0]), FadeIn(dest[1]), run_time=self.dur(0.4))

            # «un diez por ciento»
            self.en("suma")
            self.play(ReplacementTransform(c03, dest[2]), FadeIn(dest[3]), FadeIn(dest[4]), run_time=self.dur(0.5))

            # «Ninguna regla puede bajar de ahí»
            self.en("suelo")
            suelo = Line(dest.get_corner(DL) + DOWN * 0.18 + LEFT * 0.3, dest.get_corner(DR) + DOWN * 0.18 + RIGHT * 0.3,
                         color=VERDE, stroke_width=5)
            minimo = Text("Mínimo", color=VERDE, weight=BOLD).scale(0.5).next_to(suelo, RIGHT, buff=0.25)
            self.play(Create(suelo), FadeIn(minimo), run_time=self.dur(0.5))
