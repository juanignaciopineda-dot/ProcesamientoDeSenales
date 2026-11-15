"""Escena 05 — μ_X(t) = E[X(t)]: la media como función del tiempo y como curva por el centro del ensemble."""
from comun.escena import *


class FormulaMedia(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        L = Lienzo(ancho=6.6, alto=3.0, t_rango=(-0.25, 1.75), v_max=3.4, centro=(-3.4, -1.0))
        t = np.linspace(-0.25, 1.75, 200)
        fantasmas = VGroup(*[L.curva(t, a * np.cos(2 * np.pi * t), SENAL, 3, 0.6) for a in (1, 1, 3, 3)])
        media = L.curva(t, 2 * np.cos(2 * np.pi * t), AMBAR, 5)
        F = formula(r"\mu_{X}", "(", "t", ")", "=", "E", "[", "X", "(", "t", ")", "]",
                    escala=1.5, colores={0: AMBAR}).move_to([0, 3.1, 0])
        with self.narrar("b1"):
            # «una función del tiempo»
            self.en("funcion")
            self.play(Create(L.base()), Create(media), run_time=self.dur(1.3), rate_func=linear)
            self.play(FadeIn(Text("t", color=INK).scale(0.5).move_to(L.p(1.75, 0) + DOWN * 0.5 + RIGHT * 0.15)), run_time=0.2)

            # «mu sub equis de te»
            self.en("mu")
            self.play(FadeIn(F[0:4], shift=DOWN * 0.15), run_time=self.dur(0.7))

            # «la esperanza de equis de te»
            self.en("esperanza")
            self.play(FadeIn(F[4:], shift=DOWN * 0.15), run_time=self.dur(1.0))

            # «la variable de ese corte»
            self.en("corte")
            corte = L.vertical(0.0, AMBAR, 3.5)
            puntos = VGroup(*[Dot(L.p(0.0, v), radius=0.09, color=SENAL) for v in (1, 1, 3, 3)])
            xt = formula("X", "(", "t", ")", escala=0.9).move_to([float(L.x(0.0)) + 0.1, 0.95, 0])
            self.play(FadeIn(fantasmas), Create(corte), FadeIn(puntos), FadeIn(xt), run_time=self.dur(0.9))

            # «cada valor por su probabilidad»
            self.en("suma")
            l1 = MathTex(r"1\cdot\tfrac14+1\cdot\tfrac14", color=TXT).scale(0.95).move_to([3.4, 0.6, 0])
            l2 = MathTex(r"+\,3\cdot\tfrac14+3\cdot\tfrac14=2", color=TXT).scale(0.95).move_to([3.4, -0.15, 0])
            self.play(FadeIn(l1, shift=LEFT * 0.2), run_time=self.dur(0.6))
            self.play(FadeIn(l2, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «todo sumado»
            self.en("sumado")
            sig = MathTex(r"\sum", color=AMBAR).scale(1.8).move_to([3.4, 1.9, 0])
            self.pop(sig)

            # «la integral con la densidad»
            self.en("integral")
            integral = MathTex(r"\int x\,f(x)\,dx", color=AMBAR).scale(1.1).move_to([3.4, -1.6, 0])
            self.pop(integral)

            # «continua»
            self.en("continua")
            self.play(sig.animate.set_opacity(0.3), l1.animate.set_opacity(0.3), l2.animate.set_opacity(0.3),
                      run_time=0.5)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        L2 = Lienzo(ancho=8.5, alto=4.0, t_rango=(0, 1), v_max=2.0, centro=(0, 0.3))
        pila = pila_de_curvas(L2, 26, semilla=3, a=0.9, color=SENAL, opacidad=0.45, ancho=2.0, escala=0.45)
        with self.narrar("b2"):
            # «una curva que pasa por el centro»
            self.en("centro")
            self.corte()
            plana = L2.base(AMBAR, 5)
            self.play(LaggedStart(*[Create(c) for c in pila], lag_ratio=0.04), Create(plana), run_time=self.dur(1.6))

            # «del ensemble»
            self.en("ensemble")
            w = self.palabra("ensemble", AMBAR, 1.2).move_to([0, 3.3, 0])
            self.pop(w)

            # «alrededor de qué valor»
            self.en("alrededor")
            flechas = VGroup(*[flecha([float(L2.x(tt)), y0, 0], [float(L2.x(tt)), y1, 0], AMBAR, 4)
                               for tt in (0.2, 0.5, 0.8) for y0, y1 in ((2.0, 0.8), (-1.4, -0.2))])
            self.play(LaggedStart(*[GrowArrow(f) for f in flechas], lag_ratio=0.1), run_time=self.dur(0.8))

            # «se mueven las grabaciones»
            self.en("grab")
            self.play(pila.animate(rate_func=there_and_back).set_stroke(opacity=0.9), FadeOut(flechas),
                      run_time=self.dur(0.9))

            # «los osciladores desfasados»
            self.en("desf")
            self.corte()
            Ll = Lienzo(ancho=6.0, alto=3.0, t_rango=(-0.25, 1.75), v_max=1.6, centro=(-3.6, 0.6))
            Lr = Lienzo(ancho=6.0, alto=3.0, t_rango=(-0.25, 1.75), v_max=3.4, centro=(3.6, 0.6))
            t = np.linspace(-0.25, 1.75, 200)
            izq = VGroup(*[Ll.curva(t, np.cos(2 * np.pi * t + np.deg2rad(f)), SENAL, 3, 0.75) for f in (0, 90, 180, 270)])
            self.play(Create(Ll.base()), Create(izq), run_time=self.dur(1.2), rate_func=linear)

            # «es plana»
            self.en("plana")
            plana_l = Ll.base(AMBAR, 6)
            lab_l = Text("plana", color=AMBAR, weight=BOLD).scale(0.8).move_to([-3.6, -1.6, 0])
            self.play(Create(plana_l), run_time=0.4)
            self.pop(lab_l)

            # «oscila»
            self.en("oscila")
            der = VGroup(*[Lr.curva(t, a * np.cos(2 * np.pi * t), SENAL, 3, 0.75) for a in (1, 1, 3, 3)])
            media_r = Lr.curva(t, 2 * np.cos(2 * np.pi * t), AMBAR, 6)
            lab_r = Text("oscila", color=AMBAR, weight=BOLD).scale(0.8).move_to([3.6, -1.6, 0])
            self.play(Create(Lr.base()), Create(der), Create(media_r), run_time=self.dur(1.0), rate_func=linear)
            self.pop(lab_r)

            # «Guarda esta diferencia»
            self.en("guarda")
            sep = Line([0, 2.6, 0], [0, -2.0, 0], color=INK, stroke_width=2)
            self.play(Create(sep), run_time=0.4)
            self.play(lab_l.animate(rate_func=there_and_back).scale(1.3),
                      lab_r.animate(rate_func=there_and_back).scale(1.3), run_time=0.7)

            # «va a ser importante»
            self.en("importante")
            rl = SurroundingRectangle(lab_l, color=AMBAR, buff=0.18, stroke_width=3)
            rr = SurroundingRectangle(lab_r, color=AMBAR, buff=0.18, stroke_width=3)
            self.play(Create(rl), Create(rr), run_time=0.5)

            # «no dice nada de la memoria»
            self.en("memoria")
            self.corte()
            m_media = self.palabra("media", TXT, 1.3).move_to([-3.2, 1.6, 0])
            m_mem = self.palabra("memoria", AMBAR, 1.3).move_to([3.0, 1.6, 0])
            m_q = self.palabra("?", AMBAR, 1.8).next_to(m_mem, RIGHT, buff=0.3)
            self.play(FadeIn(m_media), run_time=0.3)
            self.pop(m_mem, m_q)
            self.play(Create(tachar(m_media)), run_time=0.3)

            # «dos instantes a la vez»
            self.en("dos_inst")
            L3 = Lienzo(ancho=9.0, alto=2.6, t_rango=(0, 1), v_max=3.0, centro=(0, -1.5))
            curva = L3.curva(np.linspace(0, 1, 240), 1.3 * serie(21, 240, 0.93), SENAL, 3.5)
            c1 = L3.vertical(0.25, AMBAR, 3.5)
            c2 = L3.vertical(0.65, TXT, 3.5)
            t1 = formula("t_1", escala=0.8).move_to([float(L3.x(0.25)), -3.4, 0])
            t2 = formula("t_2", escala=0.8).move_to([float(L3.x(0.65)), -3.4, 0])
            self.play(Create(L3.base()), Create(curva), run_time=self.dur(0.7), rate_func=linear)
            self.play(Create(c1), Create(c2), FadeIn(t1), FadeIn(t2), run_time=self.dur(0.6))
