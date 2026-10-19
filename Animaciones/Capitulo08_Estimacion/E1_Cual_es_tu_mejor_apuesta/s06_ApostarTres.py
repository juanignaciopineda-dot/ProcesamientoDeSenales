"""Escena 06 — Probar apuestas: el error cuadrático medio de apostar 3, 4 y 1 con el dado, a mano."""
from comun.escena import *


class ApostarTres(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.M = Mesa8(y_regla=0.4)
        self.cuad = []
        self.apuesta_tres()
        self.apuesta_cuatro_y_uno()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def apuesta_tres(self):
        M = self.M
        caras = M.caras.caras
        marca3 = M.marca(3)
        self.marca = marca3
        textos = ["4", "1", "0", "1", "4", "9"]
        cs = [M.cuadrado(k + 1, t, VERDE if t == "0" else TXT) for k, t in enumerate(textos)]
        self.cuad = cs
        foco = SurroundingRectangle(caras[0], buff=0.1, color=ESTIMACION, stroke_width=4)
        sextos = VGroup(*[MathTex(r"\tfrac16", color=INK).scale(1.1).move_to(M.p(k + 1) + UP * 2.1) for k in range(6)])
        suma = formula("4+1+0+1+4+9", "=", "19", escala=1.2, colores={2: ESTIMACION}).move_to([0, -2.1, 0])
        div = formula(r"\frac{19}{6}", r"\approx", r"3{,}17", escala=1.3, colores={2: ESTIMACION}).move_to([0, -3.3, 0])
        self.filas = VGroup(suma, div)

        with self.narrar("b1"):
            # «Probemos a apostar tres»
            self.en("apuesta3")
            self.play(FadeIn(M), FadeIn(marca3), run_time=self.dur(0.8))

            # «Si sale uno»
            self.en("sale1")
            self.play(FadeIn(foco), run_time=self.dur(0.3))

            # «su cuadrado, cuatro»
            self.en("c4")
            self.play(FadeIn(cs[0], shift=DOWN * 0.2), run_time=self.dur(0.35))

            # «Si sale dos»
            self.en("sale2")
            self.play(foco.animate.move_to(caras[1]), run_time=self.dur(0.3))

            # «el cuadrado es uno»
            self.en("c1")
            self.play(FadeIn(cs[1], shift=DOWN * 0.2), run_time=self.dur(0.35))

            # «Si sale tres, cero»
            self.en("c0")
            self.play(foco.animate.move_to(caras[2]), FadeIn(cs[2], shift=DOWN * 0.2), run_time=self.dur(0.35))

            # «Con cuatro, uno»
            self.en("c1b")
            self.play(foco.animate.move_to(caras[3]), FadeIn(cs[3], shift=DOWN * 0.2), run_time=self.dur(0.35))

            # «con cinco, cuatro»
            self.en("c4b")
            self.play(foco.animate.move_to(caras[4]), FadeIn(cs[4], shift=DOWN * 0.2), run_time=self.dur(0.35))

            # «con seis, nueve»
            self.en("c9")
            self.play(foco.animate.move_to(caras[5]), FadeIn(cs[5], shift=DOWN * 0.2), run_time=self.dur(0.35))

            # «probabilidad un sexto»
            self.en("sexto")
            self.play(FadeOut(foco), FadeIn(sextos, lag_ratio=0.1), run_time=self.dur(0.8))

            # «la suma, diecinueve»
            self.en("suma")
            self.play(FadeIn(suma[0], shift=UP * 0.1), run_time=self.dur(0.5))
            self.play(FadeIn(suma[1]), FadeIn(suma[2], scale=1.3), run_time=self.dur(0.4))

            # «dividida entre seis»
            self.en("div")
            self.play(FadeIn(div[0], shift=UP * 0.1), run_time=self.dur(0.5))

            # «tres coma uno siete»
            self.en("res")
            self.play(FadeIn(div[1]), FadeIn(div[2], scale=1.3), run_time=self.dur(0.5))
        self.wait(0.3)
        self.sextos = sextos

    # ------------------------------------------------------------ b2
    def apuesta_cuatro_y_uno(self):
        M = self.M
        cs = self.cuad
        marca3 = self.marca
        marca4, marca1 = M.marca(4), M.marca(1)
        v4 = ["9", "4", "1", "0", "1", "4"]
        v1 = ["0", "1", "4", "9", "16", "25"]
        n4 = [M.cuadrado(k + 1, t, VERDE if t == "0" else TXT) for k, t in enumerate(v4)]
        n1 = [M.cuadrado(k + 1, t, VERDE if t == "0" else (ERROR if t == "25" else TXT)) for k, t in enumerate(v1)]
        f6 = Arrow(M.p(4) + DOWN * 1.75, M.p(6) + DOWN * 1.75, buff=0, color=ERROR, stroke_width=5)
        f1 = Arrow(M.p(4) + DOWN * 1.75, M.p(1) + DOWN * 1.75, buff=0, color=ERROR, stroke_width=5)
        e6 = Text("2", color=ERROR, weight=BOLD).scale(0.7).next_to(f6, DOWN, buff=0.1)
        e1 = Text("3", color=ERROR, weight=BOLD).scale(0.7).next_to(f1, DOWN, buff=0.1)
        d196 = MathTex(r"\frac{19}{6}", color=TXT).scale(1.3).move_to([-1.3, -3.2, 0])
        r4 = MathTex(r"\approx 3{,}17", color=ESTIMACION).scale(1.3).move_to([1.1, -3.2, 0])
        empate = self.palabra("Empate", ESTIMACION, 1.3).move_to([0, 3.3, 0])
        r1 = formula(r"\frac{55}{6}", r"\approx", r"9{,}17", escala=1.3, colores={0: TXT, 2: ERROR}).move_to([0, -3.15, 0])
        x1 = cruz(ROJO, 1.1)

        with self.narrar("b2"):
            # «Ahora apostemos cuatro»
            self.en("apuesta4")
            self.play(FadeOut(self.filas), FadeOut(self.sextos), run_time=0.3)
            self.play(ReplacementTransform(marca3, marca4),
                      *[ReplacementTransform(cs[i], n4[i]) for i in range(6)], run_time=self.dur(0.7))

            # «Las cuentas son las mismas»
            self.en("mismas")
            self.resaltar(*n4, color=ESTIMACION, escala=1.3, run_time=0.6)

            # «el seis queda a dos»
            self.en("seis")
            self.play(GrowArrow(f6), FadeIn(e6), run_time=self.dur(0.5))

            # «el uno queda a tres»
            self.en("uno")
            self.play(GrowArrow(f1), FadeIn(e1), run_time=self.dur(0.5))

            # «diecinueve sextos»
            self.en("d196")
            self.play(FadeIn(d196, shift=UP * 0.1), run_time=self.dur(0.4))

            # «tres coma uno siete»
            self.en("res4")
            self.play(FadeIn(r4, shift=UP * 0.1), run_time=self.dur(0.4))

            # «Empate»
            self.en("empate")
            self.pop(empate)

            # «si apostamos uno»
            self.en("apuesta1")
            self.play(*[FadeOut(m) for m in (f6, f1, e6, e1, d196, r4, empate)], run_time=0.25)
            self.play(ReplacementTransform(marca4, marca1),
                      *[ReplacementTransform(n4[i], n1[i]) for i in range(6)], run_time=self.dur(0.6))

            # «el uno sale gratis»
            self.en("gratis")
            self.resaltar(n1[0], color=VERDE, escala=1.6, run_time=0.5)

            # «el seis cuesta veinticinco»
            self.en("cuesta")
            self.resaltar(n1[5], color=ERROR, escala=1.4, run_time=0.5)

            # «nueve coma uno siete»
            self.en("res1")
            self.play(FadeIn(r1, shift=UP * 0.1), run_time=self.dur(0.6))

            # «mala idea»
            self.en("mala")
            x1.move_to(marca1.tri)
            self.sfx("error")
            self.play(FadeIn(x1, scale=1.6), run_time=self.dur(0.4))
