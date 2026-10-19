"""Escena 05 — De la cuenta a la regla: el riesgo mínimo es otra vez la razón de verosimilitud contra un umbral."""
from comun.escena import *
from comun.figuras_c9e5 import *

CFA = r"C_{\mathrm{FA}}"
CM = r"C_{\mathrm{M}}"
COL_FA, COL_M = ESTIMACION, ERROR
XB = 5.6        # la barra de P(Enfermo | r)


class DeLaCuentaALaRegla(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.renglon1()
        self.renglon2()
        self.renglon3()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def renglon1(self):
        with self.narrar("b1"):
            # «Convirtamos esa cuenta en una regla»
            self.en("cuenta")
            a = MathTex(r"\text{Decir sano: } 5 \cdot 0{,}44 = 2{,}2", color=INK).scale(0.6)
            b = MathTex(r"\text{Decir enfermo: } 1 \cdot 0{,}56 = 0{,}56", color=INK).scale(0.6)
            VGroup(a, b).arrange(RIGHT, buff=1.0).move_to([0, 3.35, 0])
            self.play(FadeIn(a), FadeIn(b), run_time=self.dur(0.5))

            # «Se dice uno»
            self.en("uno")
            si = MathTex(r"\text{Decir } H_1 \text{ si:}", color=C1).scale(0.8).move_to([-5.0, 2.1, 0])
            self.play(FadeIn(si, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            f = MathTex(CFA, r"\,P(H_0 \mid r)", "<", CM, r"\,P(H_1 \mid r)").scale(0.9)
            f.next_to(si, RIGHT, buff=0.5)
            f[0].set_color(COL_FA)
            f[1].set_color(C0)
            f[3].set_color(COL_M)
            f[4].set_color(C1)
            self.f = f
            for marca, i in (("cfa", 0), ("ph0", 1), ("menor", 2), ("cm", 3), ("ph1", 4)):
                self.en(marca)
                self.play(FadeIn(f[i], shift=DOWN * 0.15), run_time=self.dur(0.35))

    # ------------------------------------------------------------ b2
    def renglon2(self):
        f = self.f
        with self.narrar("b2"):
            # «Pasamos las probabilidades a un lado»
            self.en("pasa")
            p1, p0 = f[4].copy(), f[1].copy()
            self.play(p1.animate.move_to([-3.6, 1.0, 0]), p0.animate.move_to([-3.6, 0.0, 0]),
                      run_time=self.dur(0.6))

            # «los costes al otro»
            self.en("costes")
            ca, cm = f[0].copy(), f[3].copy()
            self.play(ca.animate.move_to([0.4, 1.0, 0]), cm.animate.move_to([0.4, 0.0, 0]),
                      run_time=self.dur(0.6))

            # «La probabilidad a posteriori del uno»
            self.en("cociente")
            q = frac9(r"P(H_1 \mid r)", r"P(H_0 \mid r)", C1, 0.85, C0).move_to([-3.6, 0.5, 0])
            self.play(ReplacementTransform(p1, q.num), ReplacementTransform(p0, q.den), Create(q.barra),
                      run_time=self.dur(0.5))

            # «tiene que superar»
            self.en("supera")
            may = MathTex(">", color=TXT).scale(1.0).move_to([-1.6, 0.5, 0])
            self.play(FadeIn(may, scale=0.5), run_time=self.dur(0.3))

            # «al coste de la falsa alarma entre el coste del fallo»
            self.en("ccoc")
            c = frac9(CFA, CM, COL_FA, 0.85, COL_M).move_to([-0.4, 0.5, 0])
            self.play(ReplacementTransform(ca, c.num), ReplacementTransform(cm, c.den), Create(c.barra),
                      run_time=self.dur(0.5))

            # «Aquí, un quinto»
            self.en("quinto")
            quinto = MathTex(r"= \tfrac{1}{5}", color=TXT).scale(0.95).next_to(c, RIGHT, buff=0.25)
            self.pop(quinto)

            # «la probabilidad de estar enfermo»
            self.en("penf")
            alto, y0 = 3.0, -3.2
            caja_b = Rectangle(width=0.8, height=alto, color=C1, stroke_width=3).move_to([XB, y0 + alto / 2, 0])
            rot = MathTex(r"P(\text{Enfermo} \mid r)", color=C1).scale(0.55).next_to(caja_b, UP, buff=0.15)
            n0 = Text("0", color=INK).scale(0.38).next_to(caja_b.get_corner(DL), LEFT, buff=0.12)
            n1 = Text("1", color=INK).scale(0.38).next_to(caja_b.get_corner(UL), LEFT, buff=0.12)
            self.play(Create(caja_b), FadeIn(rot), FadeIn(n0), FadeIn(n1), run_time=self.dur(0.5))

            # «pase de un sexto»
            self.en("sexto")
            y6 = y0 + alto / 6
            raya = Line([XB - 0.55, y6, 0], [XB + 0.55, y6, 0], color=ESTIMACION, stroke_width=5)
            sexto = MathTex(r"\tfrac{1}{6}", color=ESTIMACION).scale(0.7).next_to(raya, LEFT, buff=0.15)
            self.play(Create(raya), FadeIn(sexto), run_time=self.dur(0.4))

            # «un diecisiete por ciento»
            self.en("diecisiete")
            pc = Text("≈ 17 %", color=ESTIMACION, weight=BOLD).scale(0.45).next_to(sexto, LEFT, buff=0.2)
            zona = Rectangle(width=0.8, height=alto * 5 / 6, stroke_width=0).set_fill(ESTIMACION, 0.25)
            zona.move_to([XB, y6 + alto * 5 / 12, 0])
            self.play(FadeIn(pc), FadeIn(zona), run_time=self.dur(0.4))

            # «para decir enfermo»
            self.en("enfermo")
            de = Text("Enfermo", color=ESTIMACION, weight=BOLD).scale(0.42).rotate(PI / 2).move_to(zona)
            self.pop(de)
            self.izq = VGroup(q, may, c, quinto)

    # ------------------------------------------------------------ b3
    def renglon3(self):
        q = self.izq[0]
        with self.narrar("b3"):
            # «la regla de Bayes a la izquierda»
            self.en("bayes")
            n = MathTex(r"p_1\, f_1(r)", r"\,/\,f(r)", color=C1).scale(0.8)
            d = MathTex(r"p_0\, f_0(r)", r"\,/\,f(r)", color=C0).scale(0.8)
            w = max(n.width, d.width) + 0.15
            barra = Line(LEFT * w / 2, RIGHT * w / 2, color=TXT, stroke_width=3)
            n.next_to(barra, UP, buff=0.12)
            d.next_to(barra, DOWN, buff=0.12)
            bay = VGroup(n, barra, d).move_to([-1.6, -1.5, 0])
            igual = MathTex("=", color=TXT).scale(0.9).next_to(bay, LEFT, buff=0.2)
            qc = q.copy().scale(0.8).next_to(igual, LEFT, buff=0.2)
            self.play(TransformFromCopy(q, qc), FadeIn(igual), FadeIn(bay), run_time=self.dur(0.6))

            # «El denominador común se cancela»
            self.en("cancela")
            t1, t2 = tachar(n[1]), tachar(d[1])
            self.sfx("tick")
            self.play(Create(t1), Create(t2), run_time=self.dur(0.4))

            # «pe uno entre pe cero»
            self.en("p1p0")
            pp = frac9("p_1", "p_0", C1, 0.8, C0).move_to([-3.6, -1.5, 0])
            self.play(FadeOut(VGroup(qc, igual)), ReplacementTransform(VGroup(bay, t1, t2), pp),
                      run_time=self.dur(0.5))
            g2 = VGroup(self.izq[1].copy(), self.izq[2].copy())
            self.play(g2.animate.arrange(RIGHT, buff=0.3).move_to([-0.6, -1.5, 0]), run_time=self.dur(0.4))

            # «por la razón de verosimilitud»
            self.en("lambda")
            lam = MathTex(r"\Lambda(r)", color=TXT).scale(0.9).next_to(pp, RIGHT, buff=0.15)
            self.play(g2.animate.shift(RIGHT * (lam.width + 0.2)), run_time=0.25)
            self.pop(lam)

            # «Despejamos»
            self.en("despeja")
            k = MathTex(r"\Lambda(r)", ">", r"p_0\, " + CFA, r"\;/\;", r"(p_1\, " + CM + ")").scale(0.95)
            k.move_to([-0.9, -3.0, 0])
            k[2].set_color(COL_FA)
            k[4].set_color(COL_M)
            self.play(TransformFromCopy(lam, k[0]), TransformFromCopy(g2[0], k[1]), run_time=self.dur(0.5))
            self.play(pp.copy().animate.move_to(k[3]).set_opacity(0), run_time=self.dur(0.4))

            # «pe cero por el coste de la falsa alarma»
            self.en("num")
            self.play(FadeIn(k[2], shift=UP * 0.15), run_time=self.dur(0.4))

            # «pe uno por el coste del fallo»
            self.en("den")
            self.play(FadeIn(k[3]), FadeIn(k[4], shift=UP * 0.15), run_time=self.dur(0.4))
            self.play(Create(SurroundingRectangle(k, color=AMBAR, buff=0.18, stroke_width=4)),
                      run_time=self.dur(0.4))
