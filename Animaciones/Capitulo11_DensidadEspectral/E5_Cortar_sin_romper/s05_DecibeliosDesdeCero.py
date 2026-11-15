"""Escena 05 — Decibelios desde cero: contar ceros con el logaritmo; ×10 = 10 dB; la mitad = −3 dB."""
from comun.escena import *


class DecibeliosDesdeCero(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        y0 = -1.4
        barra = Rectangle(width=1.0, height=3.2, color=SENAL, stroke_width=3).set_fill(SENAL, 0.5)
        barra.move_to([-4.6, y0 + 1.6, 0])
        punto = Dot([-3.0, y0 + 0.03, 0], radius=0.07, color=CIAN)
        base = Line([-5.6, y0, 0], [-1.8, y0, 0], color=INK, stroke_width=2)
        n1 = etiqueta("1", SENAL, 0.7).next_to(barra, UP, buff=0.15)
        n2 = etiqueta("0,000001", CIAN, 0.5).next_to(punto, RIGHT, buff=0.15)
        lineal = etiqueta("escala lineal", INK, 0.5).move_to([-3.7, y0 - 0.45, 0])
        brace = Brace(barra, LEFT, color=INK, buff=0.1)
        lab_alt = etiqueta("1/1.000.000", CIAN, 0.45).move_to([-6.2, 0.2, 0])
        ojo_ = ojo().scale(0.8).move_to([-4.0, 2.9, 0])
        doble = DoubleArrow(barra.get_top() + RIGHT * 0.1, punto.get_center() + UP * 0.12, color=INK, stroke_width=3,
                            buff=0.1, tip_length=0.15)
        ceros = Text("0,000001", color=TXT, weight=BOLD).scale(1.2).move_to([3.4, 1.7, 0])
        log = MathTex(r"\log_{10}", color=AMBAR).scale(1.4).move_to([3.4, 0.5, 0])
        db = self.palabra("decibelios (dB)", AMBAR, 1.0).move_to([3.4, 3.2, 0])
        F = formula("10", r"\cdot", r"\log_{10}", "(", r"\frac{P_1}{P_2}", ")", escala=1.4,
                    colores={0: AMBAR}).move_to([3.0, -2.3, 0])

        with self.narrar("b1"):
            # «un tono tiene potencia uno»
            self.en("p1")
            self.play(Create(base), GrowFromEdge(barra, DOWN), FadeIn(n1), run_time=self.dur(0.9))

            # «otro una millonésima»
            self.en("p2")
            self.play(FadeIn(punto, scale=0.4), FadeIn(n2), run_time=self.dur(0.6))

            # «en una gráfica normal»
            self.en("normal")
            self.play(FadeIn(lineal), run_time=0.4)

            # «el pequeño es invisible»
            self.en("invisible")
            self.play(Indicate(punto, scale_factor=2.2, color=CIAN), run_time=0.8)
            self.play(Create(tachar(n2)), run_time=0.3)

            # «una millonésima de la altura»
            self.en("altura")
            self.play(GrowFromCenter(brace), FadeIn(lab_alt), run_time=self.dur(0.7))

            # «Para ver a la vez»
            self.en("ver")
            self.play(FadeIn(ojo_, scale=0.6), run_time=0.4)

            # «cosas tan distintas»
            self.en("distintas")
            self.play(GrowFromCenter(doble), run_time=self.dur(0.6))

            # «se cuentan ceros»
            self.en("ceros")
            self.play(FadeIn(ceros), run_time=0.3)
            self.play(*[ceros[i].animate.set_color(AMBAR) for i in range(2, 7)], run_time=self.dur(1.0))

            # «se usa el logaritmo»
            self.en("log")
            self.pop(log)

            # «Los decibelios»
            self.en("db")
            self.pop(db)

            # «diez veces el logaritmo en base diez»
            self.en("formula1")
            self.play(FadeIn(F[0:3], shift=UP * 0.15), run_time=self.dur(0.9))

            # «del cociente entre dos potencias»
            self.en("cociente")
            self.play(FadeIn(F[3:], shift=UP * 0.15), run_time=self.dur(0.9))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        def y(db):
            return -2.2 + db * (5.0 / 60.0)

        xr = -5.6
        regla = VGroup(Line([xr, y(-5), 0], [xr, y(62), 0], color=INK, stroke_width=3),
                       *[Line([xr - 0.1, y(d), 0], [xr + 0.1, y(d), 0], color=INK, stroke_width=3) for d in (0, 10, 20, 30, 60)])

        def fila(txt, db, color=TXT):
            t = Text(txt, color=color).scale(0.6)
            t.move_to([xr + 0.35 + t.width / 2, y(db), 0])
            return t

        x10 = fila("×10", 10)
        d10 = fila("→ 10 dB", 10, AMBAR).next_to(x10, RIGHT, buff=0.15)
        x100 = fila("×100  →  20 dB", 20)
        x1000 = fila("×1.000  →  30 dB", 30)
        x1m = fila("×1.000.000  →  60 dB", 60)
        cero_mas = etiqueta("cada 10 dB: un cero más", AMBAR, 0.55).move_to([-1.3, y(45), 0])
        mitad = fila("½", -3)
        log10 = formula(r"10\cdot\log_{10}10", "=", r"10\cdot 1", escala=0.9).move_to([1.8, 3.1, 0])
        m3 = formula(r"10\cdot\log_{10}", r"0{,}5", r"\approx", r"-3\ \mathrm{dB}", escala=0.9,
                     colores={3: AMBAR}).move_to([1.8, 3.1, 0])
        e = Espectro(w_max=6, y_max=1.15, ancho=5.2, alto=2.6, centro=(3.6, -2.4))
        curva = e.curva(psd_tele, AMBAR, 4.0)
        lab_tele = etiqueta("la telegráfica", INK, 0.5).move_to([3.6, 0.45, 0])
        punto = Dot(e.p(2, 0.5), radius=0.1, color=AMBAR)
        vert = DashedLine(e.p(2, 0), e.p(2, 0.5), color=INK, stroke_width=3)
        horiz = DashedLine(e.p(2, 0.5), e.p(0, 0.5), color=INK, stroke_width=3)
        w_lab = formula(r"\omega=\alpha", escala=0.6, color=INK).move_to(e.p(2, 0) + DOWN * 0.4)
        m3b = etiqueta("−3 dB", AMBAR, 0.6).move_to(e.p(3.4, 0.62))

        with self.narrar("b2"):
            # «Con números»
            self.en("numeros")
            self.corte()
            self.play(Create(regla), run_time=self.dur(0.7))

            # «Diez veces más potencia»
            self.en("x10")
            self.play(FadeIn(x10, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «son diez decibelios»
            self.en("d10")
            self.play(FadeIn(d10, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «el logaritmo de diez es uno»
            self.en("log10")
            self.play(FadeIn(log10[0]), run_time=0.5)
            self.play(FadeIn(log10[1:]), run_time=self.dur(0.9))

            # «Cien veces, veinte»
            self.en("x100")
            self.play(FadeIn(x100, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «Mil veces, treinta»
            self.en("x1000")
            self.play(FadeIn(x1000, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «Un millón, sesenta»
            self.en("x1m")
            self.play(FadeIn(x1m, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «Cada diez decibelios, un cero más»
            self.en("cero_mas")
            self.pop(cero_mas)

            # «la mitad de la potencia»
            self.en("mitad")
            self.play(FadeOut(cero_mas), Create(Line([xr - 0.1, y(-3), 0], [xr + 0.1, y(-3), 0], color=INK, stroke_width=3)),
                      FadeIn(mitad), run_time=self.dur(0.6))

            # «unos menos tres decibelios»
            self.en("m3")
            self.play(FadeOut(log10), FadeIn(m3), run_time=self.dur(0.8))

            # «el punto de media altura de la telegráfica»
            self.en("telegrafica")
            self.play(Create(e.ejes), Create(curva), FadeIn(lab_tele), run_time=self.dur(1.4))

            # «en omega igual a alfa»
            self.en("w_alfa")
            self.play(Create(vert), Create(horiz), FadeIn(punto), FadeIn(w_lab), run_time=self.dur(1.2))

            # «estaba a menos tres decibelios»
            self.en("m3b")
            self.pop(m3b)
