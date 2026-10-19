"""Escena 07 — La apuesta del medio: 3,5 da 2,92 y gana a todas las anteriores."""
from comun.escena import *


class ApostarEnMedio(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        M = Mesa8(y_regla=0.4)
        caras = M.caras.caras
        marco = VGroup(SurroundingRectangle(caras[2], buff=0.1, color=ESTIMACION, stroke_width=4),
                       SurroundingRectangle(caras[3], buff=0.1, color=ESTIMACION, stroke_width=4))
        igual = Text("=", color=ESTIMACION, weight=BOLD).scale(1.2).move_to(M.p(3.5) + UP * 1.0)
        v317 = VGroup(*[M.cuadrado(k, "3,17", ESTIMACION, 0.7) for k in (3, 4)])
        medio = Text("?", color=ESTIMACION, weight=BOLD).scale(1.5).move_to(M.p(3.5) + DOWN * 1.15)
        reloj = reloj_arena(TXT).scale(0.9).move_to([-1.5, 3.1, 0])
        piensa = Text("Piénsalo", color=ESTIMACION, weight=BOLD).scale(0.9).next_to(reloj, RIGHT, buff=0.3)
        marca = M.marca(3.5)
        c625 = VGroup(*[M.cuadrado(k, "6,25", TXT, 0.7) for k in (1, 6)])
        c225 = VGroup(*[M.cuadrado(k, "2,25", TXT, 0.7) for k in (2, 5)])
        c025 = VGroup(*[M.cuadrado(k, "0,25", VERDE, 0.7) for k in (3, 4)])
        suman = MathTex(r"2\,(6{,}25+2{,}25+0{,}25)=17{,}5", color=TXT).scale(1.1).move_to([0, -2.3, 0])
        entre6 = MathTex(r"\frac{17{,}5}{6}", color=TXT).scale(1.3).move_to([-1.0, -3.3, 0])
        res = MathTex(r"\approx 2{,}92", color=VERDE).scale(1.4).move_to([1.3, -3.3, 0])

        filas = [("Apuesta 1", "9,17", ERROR), ("Apuesta 3 y 4", "3,17", TXT), ("Apuesta 3,5", "2,92", VERDE)]
        tabla = VGroup(*[VGroup(Text(a, color=TXT, weight=BOLD).scale(0.95), Text("→", color=INK).scale(0.95),
                                Text(b, color=c, weight=BOLD).scale(0.95)).arrange(RIGHT, buff=0.5)
                         for a, b, c in filas]).arrange(DOWN, buff=0.55, aligned_edge=LEFT).move_to([0, 0, 0])

        with self.narrar("b1"):
            # «tres y cuatro empatan»
            self.en("empatan")
            self.play(FadeIn(M), run_time=self.dur(0.5))
            self.play(FadeIn(marco), FadeIn(igual), FadeIn(v317), run_time=self.dur(0.6))

            # «quizá lo mejor esté en medio»
            self.en("medio")
            self.pop(medio)

            # «Piénsalo un momento»
            self.en("piensa")
            self.play(FadeIn(reloj, scale=0.6), FadeIn(piensa), run_time=self.dur(0.5))

            # «Apostemos tres coma cinco»
            self.en("apuesta35")
            self.play(*[FadeOut(m) for m in (marco, igual, v317, medio, reloj, piensa)], run_time=0.25)
            self.play(FadeIn(marca), run_time=self.dur(0.4))

            # «seis coma veinticinco»
            self.en("c625")
            self.play(FadeIn(c625, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «dos coma veinticinco»
            self.en("c225")
            self.play(FadeIn(c225, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «cero coma veinticinco»
            self.en("c025")
            self.play(FadeIn(c025, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «cada uno sale dos veces»
            self.en("dosveces")
            self.resaltar(c625, c225, c025, color=ESTIMACION, escala=1.2, run_time=0.6)

            # «Suman diecisiete coma cinco»
            self.en("suman")
            self.play(FadeIn(suman, shift=UP * 0.1), run_time=self.dur(0.6))

            # «entre seis»
            self.en("entre6")
            self.play(FadeIn(entre6, shift=UP * 0.1), run_time=self.dur(0.4))

            # «dos coma nueve dos»
            self.en("res")
            self.play(FadeIn(res, scale=1.3), run_time=self.dur(0.4))

            # «Más bajo que todos los anteriores»
            self.en("bajo")
            self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=0.3)
            self.play(FadeIn(tabla, lag_ratio=0.35), run_time=self.dur(1.0))
            self.resaltar(tabla[2], color=VERDE, escala=1.1, run_time=0.5)
        self.wait(1.0)
        self.limpiar()
