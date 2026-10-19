"""Escena 06 — De la razón al umbral en voltios: r ≷ 1 + ln(η)/2."""
from comun.escena import *
from comun.figuras_c9e3 import *

XD = 3.9          # columna de las cuentas, a la derecha del gráfico


class UnSoloUmbral(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.GL = CurvaLambda9(origen=(-5.9, -3.0), ancho=6.2, alto=5.6, r_rango=(-0.6, 2.1), v_top=9.0)
        self.valores()
        self.logaritmo()
        self.dos_umbrales()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def valores(self):
        G = self.GL
        with self.narrar("b1"):
            # «Probemos valores»
            self.en("ejes")
            arriba = formula(LAMBDA, "=", r"e^{2r-2}", escala=0.85, colores={0: MEDIDA, 2: ESTIMACION})
            arriba.move_to([XD, 3.3, 0])
            self.play(FadeIn(arriba), Create(G.ejes), run_time=self.dur(0.8))

            # «En cero voltios»
            self.en("r0")
            d0 = Dot(G.p(0), radius=0.1, color=C0)
            self.play(FadeIn(d0, scale=0.5), run_time=self.dur(0.3))

            # «cero coma ciento treinta y cinco»
            self.en("v0")
            t0 = Text("0,135", color=TXT).scale(0.42).move_to(G.p(0) + UP * 0.55 + RIGHT * 0.1)
            self.play(d0.animate.move_to(G.p(0, G.lam(0))), FadeIn(t0), run_time=self.dur(0.5))

            # «apoya al cero»
            self.en("apoya0")
            a0 = Text("Apoya al 0", color=C0, weight=BOLD).scale(0.42).next_to(t0, UP, buff=0.18)
            self.play(FadeIn(a0, shift=UP * 0.1), run_time=self.dur(0.4))

            # «En un voltio vale uno»
            self.en("r1")
            d1 = G.punto(1, TXT)
            t1 = Text("1", color=TXT).scale(0.42).next_to(d1, UR, buff=0.08)
            self.play(FadeIn(d1, scale=0.5), FadeIn(t1), run_time=self.dur(0.4))

            # «empate»
            self.en("empate")
            em = Text("Empate", color=TXT, weight=BOLD).scale(0.42).move_to(d1.get_center() + UP * 0.8)
            self.play(FadeIn(em, shift=UP * 0.1), run_time=self.dur(0.4))

            # «siete coma cuatro»
            self.en("r2")
            d2 = G.punto(2, C1)
            t2 = Text("7,39", color=TXT).scale(0.42).next_to(d2, LEFT, buff=0.15)
            a2 = Text("Apoya al 1", color=C1, weight=BOLD).scale(0.42).next_to(t2, DOWN, buff=0.18)
            self.play(FadeIn(d2, scale=0.5), FadeIn(t2), FadeIn(a2), run_time=self.dur(0.5))

            # «crece siempre con erre»
            self.en("curva")
            curva = G.curva()
            self.play(Create(curva), run_time=self.dur(1.2))

            # «compararla con eta»
            self.en("eta")
            linea = G.linea(ETA9)
            te = MathTex(r"\eta", color=ESTIMACION).scale(0.8).next_to(linea.get_end(), RIGHT, buff=0.12)
            self.play(FadeOut(VGroup(a0, em, a2)), Create(linea), FadeIn(te), run_time=self.dur(0.6))

            # «comparar erre con un umbral»
            self.en("umbral")
            baja = G.bajada(ETA9)
            tu = Text("Umbral", color=ESTIMACION, weight=BOLD).scale(0.42).move_to(G.p(G.corte(ETA9)) + DOWN * 0.65)
            cruce = Dot(G.p(G.corte(ETA9), ETA9), radius=0.1, color=ESTIMACION)
            self.play(FadeIn(cruce, scale=0.5), Create(baja), FadeIn(tu), run_time=self.dur(0.6))
        self.grafico = VGroup(G.ejes, d0, t0, d1, t1, d2, t2, curva)
        self.curva, self.linea, self.te, self.extra_u = curva, linea, te, VGroup(baja, tu, cruce)

    # ------------------------------------------------------------------ b2
    def logaritmo(self):
        with self.narrar("b2"):
            # «el logaritmo natural»
            self.en("ln")
            ln = MathTex(r"\ln", color=ESTIMACION).scale(1.1).move_to([XD, 2.25, 0])
            self.pop(ln)

            # «la operación inversa de la exponencial»
            self.en("inversa")
            inv = MathTex(r"\ln(e^x) = x", color=TXT).scale(0.9).move_to([XD, 2.25, 0])
            self.play(ReplacementTransform(ln, inv), run_time=self.dur(0.5))

            # «conserva el orden»
            self.en("orden")
            orden = MathTex(r"a < b \;\Rightarrow\; \ln a < \ln b", color=INK).scale(0.8).move_to([XD, 1.45, 0])
            self.play(FadeIn(orden, shift=UP * 0.1), run_time=self.dur(0.5))

            # «Queda dos erre menos dos»
            self.en("q")
            q = formula("2r-2", r"\gtrless", r"\ln\eta", escala=1.0, colores={2: ESTIMACION}).move_to([XD, 0.4, 0])
            self.play(FadeIn(q[0], shift=UP * 0.1), run_time=self.dur(0.4))

            # «comparado con el logaritmo de eta»
            self.en("lneta")
            self.play(FadeIn(q[1:3], shift=LEFT * 0.1), run_time=self.dur(0.4))

            # «Despejando»
            self.en("desp")
            dsp = MathTex(r"2r \gtrless 2 + \ln\eta", color=TXT).scale(1.0).move_to([XD, -0.6, 0])
            self.play(FadeIn(dsp, shift=UP * 0.1), run_time=self.dur(0.5))

            # «uno más la mitad del logaritmo de eta»
            self.en("fin")
            fin = formula("r", r"\gtrless", r"1 + \frac{\ln\eta}{2}", escala=1.1, colores={2: ESTIMACION})
            fin.move_to([XD, -1.85, 0])
            marco = SurroundingRectangle(fin, color=ESTIMACION, buff=0.2, stroke_width=4)
            self.play(Write(fin), run_time=self.dur(0.6))
            self.play(Create(marco), run_time=self.dur(0.4))
        self.cuentas = VGroup(inv, orden, q, dsp)
        self.fin = VGroup(fin, marco)

    # ------------------------------------------------------------------ b3
    def dos_umbrales(self):
        Cm = Campanas9(centro=(XD, -3.35), ancho=6.0, alto=2.6, r_rango=(-1.9, 3.9), v_max=0.45)
        Y1, Y2, Y3 = 1.35, 0.35, -0.6
        with self.narrar("b3"):
            # «Con eta igual a uno»
            self.en("eta1")
            self.play(FadeOut(self.cuentas), self.fin.animate.scale(0.8).move_to([XD, 2.2, 0]),
                      run_time=self.dur(0.5))
            e1 = MathTex(r"\eta = 1", color=ESTIMACION).scale(0.8).move_to([1.55, Y1, 0])
            self.play(FadeIn(e1, shift=DOWN * 0.1), run_time=self.dur(0.3))

            # «el logaritmo es cero»
            self.en("ln0")
            l0 = MathTex(r"\ln 1 = 0", color=TXT).scale(0.8).move_to([3.4, Y1, 0])
            self.play(FadeIn(l0, shift=LEFT * 0.1), run_time=self.dur(0.4))

            # «el umbral es un voltio»
            self.en("u1")
            u1 = MathTex(r"r_u = 1", color=VERDE).scale(0.8).move_to([5.35, Y1, 0])
            eje = Cm.eje((0, 1, 2), rotulo=False, escala=0.38)
            c0, c1 = Cm.campana(0, 1, C0, 3), Cm.campana(2, 1, C1, 3)
            m1 = Cm.regla(1, color=VERDE, alto=1.45, ancho=3)
            self.play(FadeIn(u1), FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.7))
            self.play(Create(m1), run_time=self.dur(0.3))

            # «dos coma treinta y tres»
            self.en("eta233")
            e2 = MathTex(r"\eta = 2{,}33", color=ESTIMACION).scale(0.8).move_to([1.85, Y2, 0])
            self.play(FadeIn(e2, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «cero coma ochenta y cinco»
            self.en("ln085")
            l2 = MathTex(r"\ln 2{,}33 = 0{,}85", color=TXT).scale(0.8).move_to([4.75, Y2, 0])
            self.play(FadeIn(l2, shift=LEFT * 0.1), run_time=self.dur(0.4))

            # «uno coma cuarenta y dos»
            self.en("u142")
            u2 = MathTex(r"r_u = 1 + \frac{0{,}85}{2} = 1{,}42", color=VERDE).scale(0.8).move_to([XD, Y3, 0])
            m2 = Cm.regla(CRUCE9, color=ESTIMACION, alto=1.45, ancho=3)
            self.play(FadeIn(u2, shift=UP * 0.1), Create(m2), run_time=self.dur(0.6))

            # «Los mismos cruces de antes»
            self.en("cruces")
            ti1 = tilde(VERDE, 0.32).next_to(u1, RIGHT, buff=0.12)
            ti2 = tilde(VERDE, 0.32).next_to(u2, RIGHT, buff=0.12)
            self.play(Create(ti1), Create(ti2), run_time=self.dur(0.4))
            self.sfx("exito")

            # «Una razón que siempre crece»
            self.en("siempre")
            derecha = VGroup(e1, l0, u1, e2, l2, u2, ti1, ti2, eje, c0, c1, m1, m2, self.fin)
            self.play(FadeOut(derecha), FadeOut(self.extra_u), run_time=self.dur(0.4))
            self.play(Indicate(self.curva, color=MEDIDA, scale_factor=1.03), run_time=self.dur(0.7))

            # «da un solo umbral»
            self.en("solo")
            G = self.GL
            cruce = Dot(G.p(G.corte(ETA9), ETA9), radius=0.12, color=ESTIMACION)
            uno = Text("Un solo corte", color=ESTIMACION, weight=BOLD).scale(0.5).move_to([XD, 1.0, 0])
            self.play(FadeIn(cruce, scale=0.4), Indicate(self.linea, color=ESTIMACION), FadeIn(uno),
                      run_time=self.dur(0.6))

            # «Pero no siempre crece»
            self.en("nosiempre")
            q = Text("?", color=ERROR, weight=BOLD).scale(2.2).move_to([XD, -0.6, 0])
            self.pop(q, sonido="error")
