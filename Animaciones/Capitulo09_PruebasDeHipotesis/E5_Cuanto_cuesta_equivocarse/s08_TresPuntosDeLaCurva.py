"""Escena 08 — Riesgo no es error: cada regla gana con su vara, y los tres criterios son tres puntos de la curva."""
from comun.escena import *
from comun.figuras_c9e5 import *

PLANO_8 = dict(origen=(-5.6, -3.3), lado=5.6)
XD = 2.4
U_NP = 1.645


class TresPuntosDeLaCurva(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.varas()
        self.curva()
        self.moraleja()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def varas(self):
        T = TablaDosReglas9(y0=2.2, paso=0.9, escala=0.5)
        celdas = T.todas()
        self.add(T, celdas)
        with self.narrar("b1"):
            # «gana en error»
            self.en("verr")
            m1 = T.marco(0, 2)
            self.play(Create(m1), T.cel[0][2].animate.set_color(VERDE), run_time=self.dur(0.4))

            # «catorce por ciento contra veintiuno»
            self.en("cmp1")
            c1 = Text("14 % < 21 %", color=TXT).scale(0.5).move_to([T.xs[2], T.y(1) - 0.8, 0])
            self.play(FadeIn(c1, shift=UP * 0.15), run_time=self.dur(0.4))

            # «El riesgo mínimo»
            self.en("rmfila")
            self.play(T.filas[1].animate(rate_func=there_and_back).scale(1.15).set_color(ESTIMACION),
                      run_time=self.dur(0.5))

            # «gana en coste»
            self.en("vcoste")
            m2 = T.marco(1, 3)
            self.play(Create(m2), T.cel[1][3].animate.set_color(VERDE), run_time=self.dur(0.4))

            # «treinta y uno contra»
            self.en("cmp2")
            c2 = Text("0,31 < 0,48", color=TXT).scale(0.5).move_to([T.xs[3], T.y(1) - 0.8, 0])
            self.play(FadeIn(c2, shift=UP * 0.15), run_time=self.dur(0.4))

            # «No hay contradicción»
            self.en("nocontra")
            self.play(m1.animate(rate_func=there_and_back).set_stroke(width=8),
                      m2.animate(rate_func=there_and_back).set_stroke(width=8), run_time=self.dur(0.6))

            # «persiguen cosas distintas»
            self.en("distintas")
            od = Text("Objetivos distintos", color=AMBAR, weight=BOLD).scale(0.6).move_to([3.0, -1.6, 0])
            self.pop(od)

            # «El segundo acepta»
            self.en("segundo")
            fa0, fa1 = T.marco(0, 0, ERROR), T.marco(1, 0, ERROR)
            self.play(Create(fa0), Create(fa1), run_time=self.dur(0.4))

            # «más del triple de falsas alarmas»
            self.en("triple")
            tr = MathTex(r"0{,}077 \to 0{,}27 \quad \times 3{,}5", color=ERROR).scale(0.7).move_to([T.xs[0] - 0.6, -1.6, 0])
            self.play(FadeIn(tr, shift=UP * 0.15), run_time=self.dur(0.4))

            # «ocho enfermos de cada cien»
            self.en("ocho")
            self.corte()
            g8 = rejilla3(8, lado=0.3, centro=(3.2, 0.2))
            for p in g8.pts[8:]:
                p.set_color(C1)
            t8 = Text("8 se escapan", color=ERROR, weight=BOLD).scale(0.5).next_to(g8, DOWN, buff=0.3)
            r8 = Text("Riesgo mínimo", color=ESTIMACION).scale(0.48).next_to(g8, UP, buff=0.3)
            self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in g8], lag_ratio=0.008), FadeIn(r8),
                      run_time=self.dur(0.8))
            self.play(FadeIn(t8), run_time=self.dur(0.3))

            # «en lugar de veintiocho»
            self.en("veintiocho")
            g28 = rejilla3(28, lado=0.3, centro=(-3.2, 0.2))
            for p in g28.pts[28:]:
                p.set_color(C1)
            t28 = Text("28 se escapan", color=ERROR, weight=BOLD).scale(0.5).next_to(g28, DOWN, buff=0.3)
            r28 = Text("Máximo a posteriori", color=ESTIMACION).scale(0.48).next_to(g28, UP, buff=0.3)
            self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in g28], lag_ratio=0.008), FadeIn(r28),
                      run_time=self.dur(0.8))
            self.play(FadeIn(t28), run_time=self.dur(0.3))

    # ------------------------------------------------------------ b2
    def curva(self):
        with self.narrar("b2"):
            # «En la curva es un punto más»
            self.en("curva")
            self.corte()
            P = PlanoRoc9(**PLANO_8)
            cur = P.curva()
            ptos = {}
            for u in (U_NP, U_MAP):
                ptos[u] = P.punto(*roc9(u), color=TXT, radio=0.1)
            vac = Circle(radius=0.2, color=TXT, stroke_width=4).set_fill(FONDO, 1).move_to(P.p(*roc9(U_R)))
            q = Text("?", color=ROC, weight=BOLD).scale(0.45).move_to(vac)
            self.play(FadeIn(P), Create(cur), FadeIn(P.diagonal()), run_time=self.dur(0.7))
            self.play(FadeIn(ptos[U_NP]), FadeIn(ptos[U_MAP]), FadeIn(vac), FadeIn(q), run_time=self.dur(0.4))

            # «cero coma cuarenta y siete»
            self.en("pend")
            tg_r = P.tangente(U_R, largo=0.6, color=ROC, ancho=4)
            self.play(Create(tg_r), run_time=self.dur(0.5))

            # «más arriba y más a la derecha»
            self.en("punto")
            d_r = P.punto(*roc9(U_R), color=TXT, radio=0.1)
            par = rotulo_par9("0,27", "0,92", escala=0.5).move_to(P.p(0.5, 0.82))
            self.play(FadeOut(q), FadeOut(vac), FadeIn(d_r, scale=0.4), FadeIn(par), run_time=self.dur(0.4))

            # «Tres criterios»
            self.en("tres")
            tres = VGroup(ptos[U_NP], ptos[U_MAP], d_r)
            self.play(tres.animate(rate_func=there_and_back).scale(1.8).set_color(ROC), run_time=self.dur(0.6))

            # «Neyman-Pearson»
            self.en("np")
            tg_n = P.tangente(U_NP, largo=0.45, color=TXT, ancho=4)
            e_n = Text("Neyman-Pearson · 3,6", color=TXT).scale(0.58).move_to([XD + 2.0, -0.6, 0])
            f_n = Line(e_n.get_left() + LEFT * 0.1, ptos[U_NP].get_center(), color=INK, stroke_width=2,
                       buff=0.12)
            self.play(Create(tg_n), FadeIn(e_n), Create(f_n), run_time=self.dur(0.5))

            # «El máximo a posteriori»
            self.en("map")
            tg_m = P.tangente(U_MAP, largo=0.45, color=TXT, ancho=4)
            e_m = Text("Máximo a posteriori · 2,33", color=TXT).scale(0.58).move_to([XD + 2.0, 0.6, 0])
            f_m = Line(e_m.get_left() + LEFT * 0.1, ptos[U_MAP].get_center(), color=INK, stroke_width=2,
                       buff=0.12)
            self.play(Create(tg_m), FadeIn(e_m), Create(f_m), run_time=self.dur(0.5))

            # «El riesgo mínimo»
            self.en("rm")
            e_r = Text("Riesgo mínimo · 0,47", color=ROC).scale(0.58).move_to([XD + 2.0, 1.8, 0])
            f_r = Line(e_r.get_left() + LEFT * 0.1, d_r.get_center(), color=INK, stroke_width=2, buff=0.12)
            self.play(FadeIn(e_r), Create(f_r), run_time=self.dur(0.5))

            # «se tumba»
            self.en("tumba")
            self.play(tg_r.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.6))

    # ------------------------------------------------------------ b3
    def moraleja(self):
        with self.narrar("b3"):
            # «La moraleja»
            self.en("moraleja")
            self.corte()
            t = Text("Moraleja", color=INK).scale(0.5).move_to([0, 3.2, 0])
            self.play(FadeIn(t), run_time=self.dur(0.3))

            # «solo si todos los errores cuestan lo mismo»
            self.en("si")
            l1 = Text("Mínimo error  ⇔  Costes iguales", color=TXT).scale(0.6).move_to([0, 2.1, 0])
            self.play(FadeIn(l1, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «Cuando no es así»
            self.en("noasi")
            uno = Text("1", color=ESTIMACION, weight=BOLD).scale(0.8).move_to([-0.4, 1.0, 0])
            cin = Text("5", color=ERROR, weight=BOLD).scale(0.8).move_to([0.4, 1.0, 0])
            self.play(FadeIn(uno), FadeIn(cin), run_time=self.dur(0.3))
            self.play(uno.animate.shift(LEFT * 1.2), cin.animate.shift(RIGHT * 1.2).scale(1.5), run_time=self.dur(0.5))

            # «hay que minimizar el coste»
            self.en("coste")
            l2 = Text("Si no: Mínimo coste", color=VERDE, weight=BOLD).scale(0.6).move_to([0, -0.1, 0])
            self.pop(l2)

            # «cambia es el umbral»
            self.en("umbral")
            l3 = Text("Cambia el umbral,", color=AMBAR, weight=BOLD).scale(0.85).move_to([0, -1.35, 0])
            self.pop(l3)

            # «no el detector»
            self.en("detector")
            l4 = Text("no el detector", color=TXT, weight=BOLD).scale(0.85).move_to([0, -2.3, 0])
            P = PlanoRoc9(origen=(4.4, -3.6), lado=1.6, rotulos=False, escala=0.3)
            self.play(FadeIn(l4, shift=UP * 0.15), FadeIn(P), Create(P.curva(ancho=4)), run_time=self.dur(0.6))
