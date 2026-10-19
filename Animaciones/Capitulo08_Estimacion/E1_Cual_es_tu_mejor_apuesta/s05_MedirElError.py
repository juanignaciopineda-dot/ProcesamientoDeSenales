"""Escena 05 — Medir el error: el error con signo se cancela; el cuadrado no. Error cuadrático medio y el sombrero."""
from comun.escena import *


class MedirElError(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.con_signo()
        self.al_cuadrado()
        self.sombrero()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def con_signo(self):
        medir = Text("¿Cuánto nos equivocamos?", color=TXT, weight=BOLD).scale(0.9).move_to([0, 3.4, 0])
        f = VGroup(Text("Error =", color=TXT, weight=BOLD), Text("Sale", color=SENAL, weight=BOLD),
                   Text("−", color=TXT, weight=BOLD), Text("Dijimos", color=ESTIMACION, weight=BOLD)
                   ).arrange(RIGHT, buff=0.3).scale(0.9).move_to([0, 2.4, 0])
        R = RectaNum(1, 6, centro=(0, 0.2), ancho=9.0, marcas=[1, 2, 3, 4, 5, 6])
        dijimos = Dot(R.p(3), radius=0.17, color=ESTIMACION)
        l_dij = Text("Dijimos", color=ESTIMACION, weight=BOLD).scale(0.5).move_to(R.p(3) + UP * 1.0)
        d5 = Dot(R.p(5), radius=0.17, color=SENAL)
        l5 = Text("Sale", color=SENAL, weight=BOLD).scale(0.5).move_to(R.p(5) + UP * 1.0)
        a5 = Arrow(R.p(3) + UP * 0.38, R.p(5) + UP * 0.38, buff=0.08, color=ERROR, stroke_width=5)
        e5 = Text("+2", color=ERROR, weight=BOLD).scale(0.7).move_to(R.p(4) + UP * 0.8)
        d1 = Dot(R.p(1), radius=0.17, color=SENAL)
        l1 = Text("Sale", color=SENAL, weight=BOLD).scale(0.5).move_to(R.p(1) + UP * 1.0)
        a1 = Arrow(R.p(3) + UP * 0.38, R.p(1) + UP * 0.38, buff=0.08, color=ERROR, stroke_width=5)
        e1 = Text("−2", color=ERROR, weight=BOLD).scale(0.7).move_to(R.p(2) + UP * 0.8)
        suma = formula("(+2)", "+", "(-2)", "=", "0", escala=1.3, colores={4: ERROR}).move_to([0, -1.7, 0])
        enorme = VGroup(Text("−100", color=ERROR, weight=BOLD), Text("+100", color=ERROR, weight=BOLD),
                        Text("= 0", color=ERROR, weight=BOLD)).arrange(RIGHT, buff=0.6).move_to([0, -3.0, 0])

        with self.narrar("b1"):
            # «medir cuánto nos equivocamos»
            self.en("medir")
            self.pop(medir)

            # «lo que sale menos lo que dijimos»
            self.en("formula")
            self.play(FadeIn(f, lag_ratio=0.3), run_time=self.dur(1.0))

            # «Si apuestas tres»
            self.en("apuestas3")
            self.play(FadeIn(R), FadeIn(dijimos, scale=0.5), FadeIn(l_dij), run_time=self.dur(0.7))

            # «sale cinco»
            self.en("sale5")
            self.play(FadeIn(d5, scale=0.5), FadeIn(l5), GrowArrow(a5), run_time=self.dur(0.7))

            # «el error es dos»
            self.en("mas2")
            self.pop(e5)

            # «si sale uno»
            self.en("sale1")
            self.play(FadeIn(d1, scale=0.5), FadeIn(l1), GrowArrow(a1), run_time=self.dur(0.7))

            # «menos dos»
            self.en("menos2")
            self.pop(e1)

            # «Podríamos promediar los errores»
            self.en("promediar")
            self.play(*[FadeIn(suma[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.7))

            # «los positivos y los negativos»
            self.en("positivos")
            self.resaltar(e5, e1, color=ERROR, escala=1.3, run_time=0.6)

            # «se cancelarían»
            self.en("cancelan")
            self.play(FadeIn(suma[3]), FadeIn(suma[4], scale=1.4), run_time=self.dur(0.5))

            # «un error enorme hacia arriba»
            self.en("enorme")
            self.play(FadeIn(enorme[0]), FadeIn(enorme[1]), run_time=self.dur(0.6))

            # «taparía otro enorme hacia abajo»
            self.en("tapa")
            self.pop(enorme[2])
        self.wait(0.4)

    # ------------------------------------------------------------ b2
    def al_cuadrado(self):
        c1 = MathTex(r"(+2)^2", color=TXT).scale(1.7).move_to([-2.6, 1.3, 0])
        c2 = MathTex(r"(-2)^2", color=TXT).scale(1.7).move_to([2.6, 1.3, 0])
        v1 = Text("4", color=VERDE, weight=BOLD).scale(1.8).move_to(c1)
        v2 = Text("4", color=VERDE, weight=BOLD).scale(1.8).move_to(c2)
        s = formula("4", "+", "4", "=", "8", escala=1.5).move_to([-0.7, -0.5, 0])
        ok = tilde(VERDE, 1.0).next_to(s, RIGHT, buff=0.6)

        cab = VGroup(Text("Error", color=INK, weight=BOLD), Text("→", color=INK), Text("Coste", color=ERROR, weight=BOLD)
                     ).arrange(RIGHT, buff=0.4).scale(0.8).move_to([0, 2.6, 0])

        def fila(e, c, y):
            g = VGroup(Text(str(e), color=TXT, weight=BOLD), Text("→", color=INK), Text(str(c), color=ERROR, weight=BOLD))
            g.arrange(RIGHT, buff=0.55).scale(1.1).move_to([0, y, 0])
            return g
        f1, f2, f3 = fila(1, 1, 1.4), fila(2, 4, 0.2), fila(3, 9, -1.0)

        E = formula("E[", "(", "Y", "-", r"\hat{y}", ")^2", "]", escala=2.0, colores={2: SENAL, 4: ESTIMACION}).move_to([0, 0.8, 0])
        etq = Text("Error cuadrático medio", color=ESTIMACION, weight=BOLD).scale(0.9).move_to([0, -0.7, 0])
        media_c = Text("Media del cuadrado", color=INK, weight=BOLD).scale(0.8).move_to([0, 2.9, 0])
        baja = Arrow([4.3, 1.7, 0], [4.3, 0.2, 0], buff=0, color=VERDE, stroke_width=6)
        minimo = Text("Mínimo", color=VERDE, weight=BOLD).scale(0.7).next_to(baja, DOWN, buff=0.15)

        with self.narrar("b2"):
            # «elevar el error al cuadrado»
            self.en("cuadrado")
            self.corte()
            self.play(FadeIn(c1, shift=DOWN * 0.2), FadeIn(c2, shift=DOWN * 0.2), run_time=self.dur(0.6))

            # «Un cuadrado»
            self.en("uncuad")
            self.resaltar(c1, c2, color=ESTIMACION, escala=1.15, run_time=0.6)

            # «nunca es negativo»
            self.en("positivo")
            self.play(ReplacementTransform(c1, v1), ReplacementTransform(c2, v2), run_time=self.dur(0.6))

            # «nada se cancela»
            self.en("sumacuatro")
            self.play(FadeIn(s, shift=UP * 0.1), run_time=self.dur(0.5))
            self.play(FadeIn(ok, scale=0.5), run_time=self.dur(0.4))

            # «castiga más los errores grandes»
            self.en("castiga")
            self.play(*[FadeOut(m) for m in (v1, v2, s, ok)], run_time=0.25)
            self.play(FadeIn(cab), run_time=self.dur(0.4))

            # «equivocarse por dos cuesta cuatro»
            self.en("dos4")
            self.play(FadeIn(f2, shift=UP * 0.15), run_time=self.dur(0.5))

            # «equivocarse por tres cuesta nueve»
            self.en("tres9")
            self.play(FadeIn(f3, shift=UP * 0.15), run_time=self.dur(0.5))
            self.play(FadeIn(f1, shift=UP * 0.15), run_time=self.dur(0.4))

            # «La media de ese cuadrado»
            self.en("lamedia")
            self.play(*[FadeOut(m) for m in (cab, f1, f2, f3)], run_time=0.25)
            self.play(FadeIn(media_c, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «error cuadrático medio»
            self.en("ecm")
            self.play(LaggedStart(*[FadeIn(E[i], shift=UP * 0.1) for i in range(7)], lag_ratio=0.2), run_time=self.dur(1.4))
            self.play(FadeIn(etq), run_time=self.dur(0.4))

            # «lo más pequeño posible»
            self.en("pequeno")
            self.play(GrowArrow(baja), FadeIn(minimo), run_time=self.dur(0.6))
        self.wait(0.4)

    # ------------------------------------------------------------ b3
    def sombrero(self):
        yh = MathTex(r"\hat{y}", color=ESTIMACION).scale(3.2).move_to([-3.6, 1.1, 0])
        t1 = Text("= Lo que adivinamos", color=ESTIMACION, weight=BOLD).scale(0.85).move_to([0.8, 1.1, 0])
        Y = MathTex("Y", color=SENAL).scale(3.2).move_to([-3.6, -1.0, 0])
        t2 = Text("= Lo que sale", color=SENAL, weight=BOLD).scale(0.85).move_to([0.2, -1.0, 0])
        est = Text("Sombrero = Estimación", color=ESTIMACION, weight=BOLD).scale(0.95).move_to([0, -2.9, 0])
        d = dado_n(3).scale(1.7).move_to([0, 0, 0])
        curso = Text("Todo el curso", color=INK, weight=BOLD).scale(0.8).move_to([4.6, 2.6, 0])

        with self.narrar("b3"):
            # «se escribe con un sombrero»
            self.en("sombrero")
            self.corte()
            self.pop(yh)

            # «lo que adivinamos»
            self.en("adivinamos")
            self.play(FadeIn(t1, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «sobre i griega»
            self.en("sobrey")
            self.play(FadeIn(Y, scale=0.6), FadeIn(t2, shift=RIGHT * 0.2), run_time=self.dur(0.6))

            # «todo el curso»
            self.en("curso")
            self.play(FadeIn(curso, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «cada vez que lo veas»
            self.en("veas")
            self.resaltar(yh, color=ESTIMACION, escala=1.2, run_time=0.6)

            # «significa estimación»
            self.en("estimacion")
            self.pop(est)

            # «a probar apuestas con el dado»
            self.en("probar")
            self.corte()
            self.play(FadeIn(d, scale=0.6), run_time=self.dur(0.5))
