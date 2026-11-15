"""Escena 08 — Dos multiplicaciones: la recursión ŷ[n] = 0,157 ŷ[n−1] + 0,7386 x[n], una iteración a mano y el error."""
from comun.escena import *


class DosMultiplicaciones(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        num_h = MathTex(r"0{,}7386", color=AMBAR).scale(1.0)
        den_h = formula(r"1-0{,}157\,z^{-1}", escala=1.0, colores={0: RUIDO})
        Hz = formula("H(z)", "=", escala=1.15, colores={0: AMBAR})
        fr_h = fraccion(num_h, den_h)
        fila_h = VGroup(Hz, fr_h).arrange(RIGHT, buff=0.3).move_to([-2.8, 3.1, 0])
        marco = SurroundingRectangle(fr_h, color=AMBAR, buff=0.12, corner_radius=0.1, stroke_width=3)
        despeje = formula(r"\hat y[n]", r"-0{,}157\,\hat y[n-1]", "=", r"0{,}7386\,x[n]", escala=1.05,
                          colores={0: ESTIMACION, 1: ESTIMACION, 3: MEDIDA}).move_to([-2.0, 1.75, 0])
        rec = oculta(formula(r"\hat y[n]", "=", r"0{,}157\,\hat y[n-1]", "+", r"0{,}7386\,x[n]", escala=1.25,
                             colores={0: ESTIMACION, 2: ESTIMACION, 4: MEDIDA}).move_to([-1.2, 0.35, 0]))
        flecha_r = flecha([-1.2, 1.3, 0], [-1.2, 0.85, 0], AMBAR)
        D = DiagramaRecursion(centro=(0.2, -1.1))
        fila = Tallos([2.2 * 0.157 ** (i * 0.6) * 0.62 ** i for i in range(8)], centro=(5.2, 2.4), paso=0.4, unidad=0.5,
                      color=ESTIMACION)
        puntos = Text("…", color=INK).scale(0.8).move_to([6.8, 1.95, 0])
        with self.narrar("b1"):
            # «Un filtro con un polo»
            self.en("unfiltro")
            self.play(FadeIn(Hz), FadeIn(fr_h.num), Create(fr_h.barra), FadeIn(fr_h.den), run_time=self.dur(0.9))

            # «se implementa con muy pocas cuentas»
            self.en("pocas")
            self.play(FadeIn(despeje, shift=UP * 0.2), run_time=self.dur(1.0))

            # «La ecuación que lo describe es esta»
            self.en("ecuacion")
            self.play(Create(marco), GrowArrow(flecha_r), run_time=self.dur(0.6))
            self.add(rec)

            # «la estimación de ahora»
            self.en("ahora")
            self.play(*revelar(rec[0], rec[1]), run_time=self.dur(0.6))

            # «cero coma uno cinco siete por la estimación anterior»
            self.en("anterior")
            self.play(*revelar(rec[2]), run_time=self.dur(0.8))

            # «más cero coma siete tres ocho seis por lo que acaba de llegar»
            self.en("llegar")
            self.play(*revelar(rec[3], rec[4]), run_time=self.dur(0.9))

            # «Dos multiplicaciones y una suma»
            self.en("dos")
            self.play(Create(D), run_time=self.dur(1.6))

            # «infinitos coeficientes»
            self.en("infinitos")
            self.play(Create(fila.base), LaggedStart(*[GrowFromEdge(t, DOWN) for t in fila.tallos], lag_ratio=0.1),
                      *[FadeIn(p, scale=0.3) for p in fila.puntos], FadeIn(puntos), run_time=self.dur(1.0))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        self.corte()
        rec = formula(r"\hat y[n]", "=", r"0{,}157\,\hat y[n-1]", "+", r"0{,}7386\,x[n]", escala=1.1,
                      colores={0: ESTIMACION, 2: ESTIMACION, 4: MEDIDA}).move_to([-0.5, 3.2, 0])
        D = DiagramaRecursion(centro=(0.2, 0.7))
        ret = D.P["ret"]
        f1 = ficha_numero("1", ESTIMACION)
        f2 = ficha_numero("2", MEDIDA)
        g157 = ficha_numero("0,157", ESTIMACION, 0.42)
        g1477 = ficha_numero("1,477", MEDIDA, 0.42)
        g1634 = ficha_numero("1,634", AMBAR, 0.5)
        suma_p = D.P["suma"]
        with self.narrar("b2"):
            # «la estimación anterior era uno»
            self.en("anterior1")
            self.add(rec, D)
            f1.move_to(ret + UP * 0.85)
            self.play(FadeIn(f1, scale=0.3), run_time=self.dur(0.5))

            # «llega una medición de dos»
            self.en("llega2")
            f2.move_to([-6.6, 1.55, 0])
            self.play(FadeIn(f2), run_time=0.2)
            self.play(f2.animate.move_to([-4.65, 1.55, 0]), run_time=self.dur(0.9))

            # «cero coma uno cinco siete por uno»
            self.en("por1")
            self.play(f1.animate.move_to(ret + LEFT * 1.1 + UP * 0.85), run_time=self.dur(0.6))
            g157.move_to(ret + LEFT * 1.1 + UP * 0.85)
            self.play(ReplacementTransform(f1, g157), run_time=0.3)
            self.play(g157.animate.move_to(suma_p + RIGHT * 0.85 + DOWN * 0.95), run_time=self.dur(0.6))

            # «más cero coma siete tres ocho seis por dos»
            self.en("por2")
            self.play(f2.animate.move_to(D.P["amp1"] + RIGHT * 0.3 + UP * 0.85), run_time=self.dur(0.6))
            g1477.move_to(D.P["amp1"] + RIGHT * 0.3 + UP * 0.85)
            self.play(ReplacementTransform(f2, g1477), run_time=0.3)
            self.play(g1477.animate.move_to(suma_p + LEFT * 0.5 + UP * 1.15), run_time=self.dur(0.6))

            # «uno coma seis tres cuatro»
            self.en("suma")
            self.play(g157.animate.move_to(suma_p + UP * 1.2 + RIGHT * 0.5),
                      g1477.animate.move_to(suma_p + UP * 1.2 + LEFT * 0.5), run_time=self.dur(0.6))
            g1634.move_to(suma_p + UP * 1.2)
            self.play(FadeOut(g157), FadeOut(g1477), FadeIn(g1634, scale=0.5), run_time=0.3)
            self.sfx("exito")
            self.play(g1634.animate.move_to(D.P["sal"] + LEFT * 0.4 + UP * 0.85), run_time=self.dur(0.7))
            # los dos sumandos quedan de referencia
            r157 = formula(r"0{,}157", escala=0.95, colores={0: ESTIMACION}).move_to([-2.3, -2.9, 0])
            r1477 = formula(r"1{,}477", escala=0.95, colores={0: MEDIDA}).move_to([-0.2, -2.9, 0])
            self.add(r157, r1477)

            # «una memoria pequeña»
            self.en("pequena")
            self.play(FadeIn(r157, scale=0.5), run_time=0.3)
            lp = Brace(r157, DOWN, color=ESTIMACION, buff=0.08, sharpness=1.0)
            lp.stretch(0.5, 1)
            tp = etiqueta("memoria", ESTIMACION, 0.45).next_to(lp, DOWN, buff=0.08)
            self.play(GrowFromCenter(lp), FadeIn(tp), run_time=self.dur(0.6))

            # «casi todo el peso lo lleva la medición nueva»
            self.en("peso")
            self.play(FadeIn(r1477, scale=0.5), run_time=0.3)
            lg = Brace(r1477, DOWN, color=MEDIDA, buff=0.08)
            tg = etiqueta("medición", MEDIDA, 0.55, BOLD).next_to(lg, DOWN, buff=0.08)
            self.play(GrowFromCenter(lg), FadeIn(tg), run_time=self.dur(0.7))

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        self.corte()
        be = barras_error([4, 0.8, 0.7401, 0.7387, 0.7386], ["0", "1", "2", "3", "∞"],
                          centro=(-3.0, -0.3), ancho=5.6, alto=3.6, v_max=4.0)
        l_e = etiqueta("error según los coeficientes", INK, 0.45).move_to([-3.0, 2.3, 0])
        v_fin = etiqueta("0,7386", ERROR, 0.6, BOLD).next_to(be.barras[-1], UP, buff=0.12)
        v_tres = etiqueta("0,7387", TXT, 0.5).next_to(be.barras[3], UP, buff=0.5)
        caja_w = caja("Wiener causal", AMBAR, ancho=2.6, alto=0.8, scale=0.5).move_to([2.3, 2.5, 0])
        caja_f = caja("filtro finito", VERDE, ancho=2.2, alto=0.8, scale=0.5).move_to([5.9, 2.5, 0])
        desig = MathTex(r"\neq", color=INK).scale(1.0).move_to([4.1, 2.5, 0])
        aspa = cruz(ROJO, 0.7).move_to(desig)
        igual = MathTex("=", color=VERDE).scale(1.2).move_to([4.1, 2.5, 0])
        mat = MathTex(r"\begin{pmatrix}5&2{,}4&1{,}44\\2{,}4&5&2{,}4\\1{,}44&2{,}4&5\end{pmatrix}", color=TXT).scale(0.8)
        mat.move_to([4.6, 0.6, 0])
        l_mat = etiqueta("matrices de Toeplitz", INK, 0.45).next_to(mat, UP, buff=0.15)
        xs = fila_puntos(9, ancho=5.0, centro=(4.3, -1.5), color=MEDIDA, radio=0.09)
        l_x = MathTex("x[n]", color=MEDIDA).scale(0.7).next_to(xs, LEFT, buff=0.2)
        vent = Rectangle(width=1.2, height=0.6, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.12).move_to(xs[1].get_center())
        c_h = caja("H(z)", AMBAR, ancho=1.6, alto=0.8, scale=0.6).move_to([4.3, -3.0, 0])
        l_gol = etiqueta("de un golpe", AMBAR, 0.45).next_to(c_h, RIGHT, buff=0.2)
        with self.narrar("b3"):
            # «el error de este filtro»
            self.en("error")
            self.play(Create(be.base), FadeIn(l_e), *[FadeIn(e) for e in be.etiquetas], run_time=0.3)
            self.play(GrowFromEdge(be.barras[-1], DOWN), run_time=self.dur(0.6))

            # «cero coma siete tres ocho seis»
            self.en("e07386")
            self.play(be.barras[-1].animate.set_fill(ROJO, 1), run_time=0.2)
            self.pop(v_fin, sonido="impacto")

            # «el número al que convergía el filtro finito»
            self.en("converge")
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in be.barras[:4]], lag_ratio=0.3), run_time=self.dur(1.5))

            # «Con tres coeficientes»
            self.en("tres")
            self.resaltar(be.barras[3], color=AMBAR, escala=1.1, run_time=0.6)

            # «cero coma siete tres ocho siete»
            self.en("e07387")
            self.play(FadeIn(v_tres, scale=0.5), run_time=self.dur(0.5))

            # «Es decir»
            self.en("esdecir")
            self.play(FadeIn(caja_w), FadeIn(caja_f), run_time=self.dur(0.6))

            # «no es un filtro distinto»
            self.en("distinto")
            self.play(FadeIn(desig), run_time=0.3)
            self.play(Create(aspa), run_time=self.dur(0.4))

            # «al que resolvíamos con matrices»
            self.en("matrices")
            self.play(FadeIn(mat), FadeIn(l_mat), run_time=self.dur(0.8))

            # «es aquel»
            self.en("aquel")
            self.play(FadeOut(desig), FadeOut(aspa), FadeIn(igual), run_time=self.dur(0.5))
            self.sfx("exito")

            # «con la ventana llevada hasta el infinito»
            self.en("ventana")
            self.play(FadeIn(xs), FadeIn(l_x), FadeIn(vent), run_time=0.4)
            self.play(vent.animate.stretch_to_fit_width(5.3).move_to(xs.get_center()), run_time=self.dur(1.3))

            # «calculado de un golpe»
            self.en("golpe")
            self.play(FadeIn(c_h, scale=0.6), FadeIn(l_gol), run_time=self.dur(0.6))
