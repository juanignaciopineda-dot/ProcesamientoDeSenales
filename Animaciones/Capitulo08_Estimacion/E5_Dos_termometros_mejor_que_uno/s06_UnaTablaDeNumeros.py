"""Escena 06 — Una tabla de números: la matriz de covarianzas y cómo se multiplica por una columna."""
from comun.escena import *
from comun.figuras_c8e5 import *

MC = (-1.4, -0.9)          # centro de la matriz grande (la misma posición en la escena 07)


def ecuaciones_arriba():
    """Las dos ecuaciones del sistema, escritas como «lado izquierdo = 4»."""
    ea = formula(r"5h_A+4h_B", "=", "4", escala=0.95).move_to([-3.6, 3.15, 0])
    eb = formula(r"4h_A+8h_B", "=", "4", escala=0.95).move_to([-3.6, 2.35, 0])
    return ea, eb


def matriz_grande(vacia=True):
    return Matriz8([["5", "4"], ["4", "8"]], centro=MC, dx=1.5, dy=1.2, escala=1.4, vacia=vacia)


class UnaTablaDeNumeros(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.tabla()
        self.por_columna()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def tabla(self):
        ea, eb = ecuaciones_arriba()
        tenues = VGroup(*[MathTex(r"\cdots", "=", "4", color=INK).scale(0.8).move_to([-3.6, 1.6 - 0.62 * i, 0])
                          for i in range(8)])
        for t in tenues:
            t.set_opacity(0.5)
        tres = VGroup(*[Termo8(l, centro=(1.4 + 1.3 * i, 2.4), alto=1.0, escala_letra=0.6)
                        for i, l in enumerate("ABC")])
        diez = VGroup(*[termometro(alto=0.8).move_to([0.6 + 0.62 * i, 2.5, 0]) for i in range(10)])
        M = matriz_grande()
        rej = VGroup(Line(M.p(0, 0) + [M.dx / 2, M.dy / 2, 0], M.p(1, 0) + [M.dx / 2, -M.dy / 2, 0]),
                     Line(M.p(0, 0) + [-M.dx / 2, -M.dy / 2, 0], M.p(0, 1) + [M.dx / 2, -M.dy / 2, 0]))
        rej.set_stroke(INK, 2, opacity=0.6)
        top = M.cy + M.nf * M.dy / 2 + 0.5
        izq = M.cx - M.nc * M.dx / 2 - 0.55
        enc = VGroup(MathTex("x_A", color=MEDIDA).scale(0.85).move_to([M.p(0, 0)[0], top, 0]),
                     MathTex("x_B", color=MEDIDA).scale(0.85).move_to([M.p(0, 1)[0], top, 0]),
                     MathTex("x_A", color=MEDIDA).scale(0.85).move_to([izq, M.p(0, 0)[1], 0]),
                     MathTex("x_B", color=MEDIDA).scale(0.85).move_to([izq, M.p(1, 0)[1], 0]))
        diag = Line(M.p(0, 0), M.p(1, 1), color=AMBAR, stroke_width=34, stroke_opacity=0.22)
        fuera = VGroup(M.celda(0, 1, CIAN), M.celda(1, 0, CIAN))
        for i, j in ((0, 0), (1, 1)):
            M.c[i][j].set_color(AMBAR)
        for i, j in ((0, 1), (1, 0)):
            M.c[i][j].set_color(CIAN)

        with self.narrar("b1"):
            # «Con tres termómetros»
            self.en("tres")
            self.play(FadeIn(ea), FadeIn(eb), run_time=0.4)
            self.play(FadeIn(tres, shift=LEFT * 0.2), FadeIn(tenues[0]), run_time=self.dur(0.6))

            # «con diez, diez»
            self.en("diez")
            self.play(FadeOut(tres), FadeIn(diez, lag_ratio=0.1), LaggedStart(*[FadeIn(t) for t in tenues[1:]],
                                                                              lag_ratio=0.15), run_time=self.dur(1.2))

            # «se usa una matriz»
            self.en("matriz")
            self.play(FadeOut(tenues), FadeOut(diez), run_time=0.3)
            self.play(Create(M.corchetes), run_time=self.dur(0.6))

            # «una tabla de números»
            self.en("tabla")
            self.play(Create(rej), run_time=self.dur(0.6))

            # «la tabla de covarianzas entre las lecturas»
            self.en("cov")
            self.play(LaggedStart(*[FadeIn(e, shift=DOWN * 0.1) for e in enc], lag_ratio=0.2), run_time=self.dur(1.0))

            # «En la diagonal»
            self.en("diag")
            self.play(Create(diag), run_time=self.dur(0.7))

            # «cinco y ocho»
            self.en("c58")
            self.play(FadeIn(M.c[0][0], scale=1.3), FadeIn(M.c[1][1], scale=1.3), run_time=self.dur(0.5))

            # «Fuera de la diagonal»
            self.en("fuera")
            self.play(Create(fuera), run_time=self.dur(0.6))

            # «cuatro, y otra vez cuatro»
            self.en("c44")
            self.play(FadeIn(M.c[0][1], scale=1.3), run_time=0.3)
            self.play(FadeIn(M.c[1][0], scale=1.3), run_time=self.dur(0.3))
        self.M, self.ea, self.eb, self.enc = M, ea, eb, enc
        self.deco = VGroup(rej, diag, fuera)

    # ------------------------------------------------------------ b2
    def por_columna(self):
        M = self.M
        H = Matriz8([["h_A"], ["h_B"]], centro=(MC[0] + 2.55, MC[1]), dx=1.1, dy=1.2, escala=1.3, color=ESTIMACION)
        igual = MathTex("=", color=TXT).scale(1.3).move_to([MC[0] + 3.65, MC[1], 0])
        x_r = MC[0] + 4.3
        r1a = MathTex("5h_A", color=TXT).scale(1.1).move_to([x_r, M.p(0, 0)[1], 0], aligned_edge=LEFT)
        r1b = MathTex("+4h_B", color=TXT).scale(1.1).next_to(r1a, RIGHT, buff=0.12)
        r2 = MathTex("4h_A+8h_B", color=TXT).scale(1.1).move_to([x_r, M.p(1, 0)[1], 0], aligned_edge=LEFT)
        marco = M.fila(0)

        with self.narrar("b2"):
            # «por una columna de números»
            self.en("col")
            self.play(FadeOut(self.deco), Create(H.corchetes), FadeIn(H.todas()), run_time=self.dur(0.6))

            # «fila por fila»
            self.en("filas")
            self.play(Create(marco), run_time=self.dur(0.5))
            self.play(marco.animate.move_to([MC[0], M.p(1, 0)[1], 0]), run_time=0.4)
            self.play(marco.animate.move_to([MC[0], M.p(0, 0)[1], 0]), run_time=0.4)

            # «término a término»
            self.en("tat")
            self.resaltar(M.c[0][0], H.c[0][0], color=AMBAR, escala=1.3, run_time=0.6)
            self.resaltar(M.c[0][1], H.c[1][0], color=AMBAR, escala=1.3, run_time=0.6)

            # «y se suma»
            self.en("suma")
            self.play(FadeIn(igual), run_time=self.dur(0.4))

            # «La primera fila»
            self.en("f1")
            self.resaltar(marco, color=AMBAR, escala=1.04)

            # «por los dos pesos»
            self.en("pesos")
            self.resaltar(H.todas(), color=AMBAR, escala=1.15)

            # «da cinco veces el peso de A»
            self.en("r1a")
            self.play(FadeIn(r1a, shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «más cuatro veces el de B»
            self.en("r1b")
            self.play(FadeIn(r1b, shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «La segunda»
            self.en("f2")
            self.play(marco.animate.move_to([MC[0], M.p(1, 0)[1], 0]), run_time=self.dur(0.4))

            # «cuatro veces el de A más ocho veces el de B»
            self.en("r2")
            self.play(FadeIn(r2, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «Son justo»
            self.en("justo")
            res = SurroundingRectangle(VGroup(r1a, r1b, r2), color=VERDE, buff=0.15)
            self.play(FadeOut(marco), Create(res), run_time=self.dur(0.5))

            # «los lados izquierdos»
            self.en("izq")
            m_a = Underline(self.ea[0], color=VERDE, stroke_width=5, buff=0.08)
            m_b = Underline(self.eb[0], color=VERDE, stroke_width=5, buff=0.08)
            self.play(Create(m_a), Create(m_b), run_time=self.dur(0.6))
