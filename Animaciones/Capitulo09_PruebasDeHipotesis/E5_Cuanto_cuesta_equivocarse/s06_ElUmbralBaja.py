"""Escena 06 — El umbral baja: η = 0,47, umbral 0,62, la franja que cambia de decisión y dos comprobaciones."""
from comun.escena import *
from comun.figuras_c9e5 import *

CFA = r"C_{\mathrm{FA}}"
CM = r"C_{\mathrm{M}}"


class ElUmbralBaja(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.cuenta()
        self.franja()
        self.comprobaciones()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def cuenta(self):
        with self.narrar("b1"):
            # «Otra vez la razón de verosimilitud»
            self.en("marco")
            lrt = MathTex(r"\Lambda(r)", r"\gtrless", r"\eta", color=TXT).scale(1.1).move_to([0, 3.0, 0])
            lrt[2].set_color(AMBAR)
            mc = SurroundingRectangle(lrt, color=AMBAR, buff=0.2, stroke_width=4)
            self.play(FadeIn(lrt), Create(mc), run_time=self.dur(0.6))

            # «Solo ha cambiado eta»
            self.en("eta")
            ie = MathTex(r"\eta", "=", color=AMBAR).scale(1.0).move_to([-4.4, 1.25, 0])
            fr = frac9(r"p_0\, " + CFA, r"p_1\, " + CM, TXT, 0.9).next_to(ie, RIGHT, buff=0.2)
            self.play(TransformFromCopy(lrt[2], ie[0]), FadeIn(ie[1]), FadeIn(fr), run_time=self.dur(0.6))

            # «cero coma siete por uno»
            self.en("num")
            ig = MathTex("=", color=TXT).scale(1.0).next_to(fr, RIGHT, buff=0.25)
            fn = frac9(r"0{,}7 \cdot 1", r"0{,}3 \cdot 5", TXT, 0.9).next_to(ig, RIGHT, buff=0.25)
            self.play(FadeIn(ig), FadeIn(fn.num, shift=DOWN * 0.15), Create(fn.barra), run_time=self.dur(0.4))

            # «cero coma tres por cinco»
            self.en("den")
            self.play(FadeIn(fn.den, shift=UP * 0.15), run_time=self.dur(0.4))

            # «Cero coma cuarenta y siete»
            self.en("r047")
            r047 = MathTex(r"= 0{,}47", color=AMBAR).scale(1.0).next_to(fn, RIGHT, buff=0.25)
            self.pop(r047)

            # «el umbral sobre el análisis»
            self.en("umbral")
            u = MathTex(r"\text{Umbral}", "=", r"1 + \frac{\ln \eta}{2}", color=TXT).scale(0.9)
            u.move_to([-2.3, -0.7, 0])
            self.play(FadeIn(u, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «la mitad del logaritmo»
            self.en("log")
            l = MathTex("=", r"1 + \frac{\ln 0{,}47}{2}", "=", r"1 - 0{,}38", color=TXT).scale(0.9)
            l.next_to(u, DOWN, buff=0.45).align_to(u[1], LEFT)
            self.play(FadeIn(l[:2]), run_time=self.dur(0.4))
            self.play(FadeIn(l[2:]), run_time=self.dur(0.4))

            # «Cero coma sesenta y dos»
            self.en("r062")
            r062 = MathTex(r"= 0{,}62", color=AMBAR).scale(1.1).next_to(l, RIGHT, buff=0.3)
            self.pop(r062)
            self.play(Create(SurroundingRectangle(r062, color=AMBAR, buff=0.15, stroke_width=4)),
                      run_time=self.dur(0.4))

    # ------------------------------------------------------------ b2
    def franja(self):
        with self.narrar("b2"):
            # «El umbral ha bajado»
            self.en("campanas")
            self.corte()
            C = campanas_e5(centro=(-0.6, -2.6), ancho=10.4, alto=5.0)
            eje = C.eje((0, 1, 2), rotulo=False)
            c0, c1 = C.campana(0, P0, C0), C.campana(2, P1, C1)
            u = ValueTracker(U_MAP)
            linea = always_redraw(lambda: umbral9_e5(C, u.get_value(), alto=3.0))
            z0 = always_redraw(lambda: C.region(C.r0, u.get_value(), C0))
            z1 = always_redraw(lambda: C.region(u.get_value(), C.r1, C1))
            t142 = Text("1,42", color=AMBAR).scale(0.42).move_to(C.p(U_MAP) + UP * 3.25)
            self.play(FadeIn(VGroup(eje, c0, c1)), FadeIn(z0), FadeIn(z1), Create(linea), FadeIn(t142),
                      run_time=self.dur(0.6))

            # «a cero coma sesenta y dos»
            self.en("desliza")
            fantasma = umbral9_e5(C, U_MAP, alto=3.0).set_stroke(opacity=0.35)
            self.add(fantasma)
            self.play(u.animate.set_value(U_R), run_time=self.dur(1.0))
            t062 = Text("0,62", color=AMBAR, weight=BOLD).scale(0.42).move_to(C.p(U_R) + UP * 3.25)
            self.play(FadeIn(t062), run_time=self.dur(0.3))

            # «En toda esa franja»
            self.en("franja")
            fr = Rectangle(width=float(C.L.x(U_MAP) - C.L.x(U_R)), height=2.9, stroke_width=0)
            fr.set_fill(AMBAR, 0.2).move_to(C.p((U_R + U_MAP) / 2) + UP * 1.6)
            fr.permitir_encima = True
            self.play(FadeIn(fr), run_time=self.dur(0.4))

            # «ahora se dice enfermo»
            self.en("ahora")
            rg = C.regla(MEDICION, alto=2.2)
            aq = Text("Aquí ahora: Enfermo", color=C1, weight=BOLD).scale(0.5).move_to(C.p(1.0) + UP * 3.85)
            self.play(Create(rg), FadeIn(aq, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «sale caro»
            self.en("caro")
            mini = tabla_costes_mini9(centro=(5.0, 2.2))
            self.play(FadeIn(mini), run_time=self.dur(0.3))
            self.play(mini.cinco.animate(rate_func=there_and_back).scale(1.8), run_time=self.dur(0.5))

            # «pasarse de precavido»
            self.en("precavido")
            linea.clear_updaters()
            z1.clear_updaters()
            self.play(z1.animate(rate_func=there_and_back).stretch(2.2, 1), run_time=self.dur(0.6))

    # ------------------------------------------------------------ b3
    def comprobaciones(self):
        with self.narrar("b3"):
            # «Dos comprobaciones»
            self.en("dos")
            self.corte()
            n1 = Text("1", color=AMBAR, weight=BOLD).scale(0.9).move_to([-6.0, 2.0, 0])
            n2 = Text("2", color=AMBAR, weight=BOLD).scale(0.9).move_to([-6.0, -1.3, 0])
            self.play(FadeIn(n1), FadeIn(n2), run_time=self.dur(0.4))

            # «cuestan lo mismo»
            self.en("iguales")
            ig = MathTex(CFA, "=", CM, color=TXT).scale(0.9).next_to(n1, RIGHT, buff=0.6)
            self.play(FadeIn(ig, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «eta vuelve a ser pe cero entre pe uno»
            self.en("etamap")
            fl = MathTex(r"\Rightarrow", color=INK).scale(0.9).next_to(ig, RIGHT, buff=0.35)
            e = MathTex(r"\eta", "=", color=AMBAR).scale(0.9).next_to(fl, RIGHT, buff=0.35)
            fr = frac9("p_0", "p_1", TXT, 0.85).next_to(e, RIGHT, buff=0.15)
            self.play(FadeIn(fl), FadeIn(e), FadeIn(fr), run_time=self.dur(0.5))

            # «el máximo a posteriori»
            self.en("mapeti")
            mp = Text("Máximo a posteriori", color=ESTIMACION).scale(0.45).next_to(VGroup(e, fr), DOWN, buff=0.25)
            self.play(FadeIn(mp, shift=UP * 0.15), run_time=self.dur(0.4))

            # «un caso particular»
            self.en("caso")
            gr = Ellipse(width=3.6, height=2.4, color=AMBAR, stroke_width=4).move_to([4.6, 1.9, 0])
            tg = Text("Riesgo mínimo", color=AMBAR).scale(0.4).move_to(gr.get_top() + DOWN * 0.38)
            ch = Ellipse(width=2.4, height=1.0, color=ESTIMACION, stroke_width=3).move_to(gr.get_center() + DOWN * 0.35)
            tc = Text("Máximo a posteriori", color=ESTIMACION).scale(0.32).move_to(ch)
            self.play(Create(gr), FadeIn(tg), run_time=self.dur(0.4))
            self.play(Create(ch), FadeIn(tc), run_time=self.dur(0.4))

            # «si acertar también costara algo»
            self.en("acertar")
            e2 = MathTex(r"\eta", "=", color=AMBAR).scale(0.9).next_to(n2, RIGHT, buff=0.6)
            fg = frac9(r"p_0\,(c_{10} - c_{00})", r"p_1\,(c_{01} - c_{11})", TXT, 0.85).next_to(e2, RIGHT, buff=0.2)
            self.play(FadeIn(e2), FadeIn(fg), run_time=self.dur(0.5))

            # «la diferencia entre fallar y acertar»
            self.en("llave")
            ll = Brace(fg, DOWN, color=INK)
            self.play(GrowFromCenter(ll), run_time=self.dur(0.4))

            # «cuánto más cuesta equivocarse»
            self.en("lema")
            lm = Text("Cuánto más cuesta fallar que acertar", color=TXT).scale(0.5).next_to(ll, DOWN, buff=0.15)
            self.pop(lm)
