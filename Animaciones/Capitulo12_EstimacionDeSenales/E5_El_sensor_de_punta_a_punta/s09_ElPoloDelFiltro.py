"""Escena 09 — Por qué el polo no es 0,6: los dos extremos de ruido, y la ganancia en continua causal frente a no causal."""
from comun.escena import *


class ElPoloDelFiltro(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        x0, ancho, y_eje = -4.0, 8.0, 1.4
        px = lambda v: x0 + ancho * v
        eje = Line([px(0) - 0.3, y_eje, 0], [px(1) + 0.3, y_eje, 0], color=INK, stroke_width=2.5)
        t0 = Text("0", color=INK).scale(0.45).move_to([px(0), y_eje - 0.3, 0])
        t1 = Text("1", color=INK).scale(0.45).move_to([px(1), y_eje - 0.3, 0])
        d157 = Dot([px(0.157), y_eje, 0], radius=0.14, color=ESTIMACION)
        e157 = etiqueta("polo del filtro  0,157", ESTIMACION, 0.5).move_to([px(0.157) + 0.9, y_eje + 0.65, 0])
        d6 = Dot([px(0.6), y_eje, 0], radius=0.14, color=SENAL)
        e6 = etiqueta("polo de la señal  0,6", SENAL, 0.5).move_to([px(0.6) + 0.4, y_eje + 1.25, 0])
        # deslizador de ruido
        y_d = -0.5
        desl = Line([-3.0, y_d, 0], [3.0, y_d, 0], color=INK, stroke_width=4)
        l_poco = etiqueta("poco ruido", RUIDO, 0.5).move_to([-3.0, y_d - 0.5, 0])
        l_mucho = etiqueta("mucho ruido", RUIDO, 0.5).move_to([3.0, y_d - 0.5, 0])
        perilla_ = Dot([-0.5, y_d, 0], radius=0.18, color=RUIDO)
        # el filtro se fía del dato o del pasado
        c_x = MathTex("x[n]", color=MEDIDA).scale(0.8).move_to([-4.5, -2.2, 0])
        c_p = MathTex(r"\hat y[n-1]", color=ESTIMACION).scale(0.8).move_to([-4.5, -3.3, 0])
        c_y = MathTex(r"\hat y[n]", color=ESTIMACION).scale(1.0).move_to([0.5, -2.75, 0])
        a_x = Arrow([-3.6, -2.2, 0], [-0.3, -2.7, 0], color=MEDIDA, stroke_width=4, buff=0.0, max_tip_length_to_length_ratio=0.15)
        a_p = Arrow([-3.4, -3.3, 0], [-0.3, -2.9, 0], color=ESTIMACION, stroke_width=4, buff=0.0, max_tip_length_to_length_ratio=0.15)
        self.add(c_x, c_p, c_y)
        for m in (c_x, c_p, c_y):
            m.set_opacity(0)
        with self.narrar("b1"):
            # «Queda una pregunta»
            self.en("pregunta")
            self.play(Create(eje), FadeIn(t0), FadeIn(t1), run_time=self.dur(0.7))

            # «el polo del filtro, cero coma uno cinco siete»
            self.en("polo157")
            self.play(FadeIn(d157, scale=0.3), FadeIn(e157), run_time=self.dur(0.8))

            # «el de la señal, cero coma seis»
            self.en("polo6")
            self.play(FadeIn(d6, scale=0.3), FadeIn(e6), run_time=self.dur(0.8))

            # «Mira los extremos»
            self.en("extremos")
            self.play(Create(desl), FadeIn(l_poco), FadeIn(l_mucho), FadeIn(perilla_), run_time=self.dur(0.8))
            self.play(*revelar(c_x, c_p, c_y), run_time=0.01)
            self.add(a_x, a_p)
            a_x.set_opacity(0), a_p.set_opacity(0)
            self.play(a_x.animate.set_opacity(1), a_p.animate.set_opacity(1), run_time=0.4)

            # «Con muy poco ruido»
            self.en("poco")
            self.play(perilla_.animate.move_to([-3.0, y_d, 0]), run_time=self.dur(0.8))

            # «el filtro se fía del dato de ahora»
            self.en("fia")
            self.play(a_x.animate.set_stroke(width=11), a_p.animate.set_stroke(width=2), run_time=self.dur(0.6))

            # «casi no usa el pasado»
            self.en("nopasado")
            self.play(a_p.animate.set_opacity(0.2), c_p.animate.set_opacity(0.4), run_time=self.dur(0.6))

            # «el polo se acerca a cero»
            self.en("acerca0")
            self.play(d157.animate.move_to([px(0.02), y_eje, 0]), e157.animate.shift(LEFT * 0.7), run_time=self.dur(0.9))

            # «Con muchísimo ruido»
            self.en("mucho")
            self.play(perilla_.animate.move_to([3.0, y_d, 0]), run_time=self.dur(1.0))

            # «se fía de la memoria de la señal»
            self.en("memoria")
            self.play(a_p.animate.set_opacity(1).set_stroke(width=11), c_p.animate.set_opacity(1),
                      a_x.animate.set_stroke(width=2), c_x.animate.set_opacity(0.5), run_time=self.dur(0.6))

            # «el polo se acerca a cero coma seis»
            self.en("acerca06")
            self.play(d157.animate.move_to([px(0.55), y_eje, 0]), e157.animate.shift(RIGHT * 2.5 + DOWN * 0.0),
                      run_time=self.dur(1.2))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        self.corte()
        # el eje vertical empieza en 0,4 (se marca con 0,5 y 1) para que se vea la diferencia
        OFF = 0.4
        L = Lienzo(ancho=6.6, alto=4.6, t_rango=(0, PI), v_max=0.6, centro=(-2.0, -0.3))
        base = L.base(INK, 2.5)
        vert = Line(L.p(0, 0), L.p(0, 0.62), color=INK, stroke_width=2.5)
        w0 = Text("0", color=INK).scale(0.45).move_to(L.p(0, -0.04) + DOWN * 0.15)
        wp = MathTex(r"\pi", color=INK).scale(0.6).move_to(L.p(PI, 0) + DOWN * 0.35)
        l_w = MathTex(r"\Omega", color=INK).scale(0.6).move_to(L.p(PI, 0) + RIGHT * 0.35)
        y5 = Text("0,5", color=INK).scale(0.42).move_to(L.p(0, 0.1) + LEFT * 0.38)
        y1 = Text("1", color=INK).scale(0.42).move_to(L.p(0, 0.6) + LEFT * 0.25)
        causal = lambda w: 0.7386 / np.sqrt(1 + 0.157 ** 2 - 2 * 0.157 * np.cos(w)) - OFF
        syy = lambda w: 2.56 / (1.36 - 1.2 * np.cos(w))
        nocausal = lambda w: syy(w) / (syy(w) + 1) - OFF
        c_c = curva_f(L, causal, 0.0, PI, ESTIMACION, 5.0)
        c_n = curva_f(L, nocausal, 0.0, PI, VERDE, 5.0)
        p_c = Dot(L.p(0, causal(0)), radius=0.12, color=ESTIMACION)
        p_n = Dot(L.p(0, nocausal(0)), radius=0.12, color=VERDE)
        t_c = etiqueta("0,88", ESTIMACION, 0.55, BOLD).move_to(L.p(0.5, causal(0.0)) + DOWN * 0.55)
        t_n = etiqueta("0,94", VERDE, 0.55, BOLD).move_to(L.p(0.5, nocausal(0.0)) + UP * 0.5)
        n_c = etiqueta("causal", ESTIMACION, 0.5).move_to(L.p(2.6, causal(2.6)) + UP * 0.4)
        n_n = etiqueta("no causal", VERDE, 0.5).move_to(L.p(2.6, nocausal(2.6)) + DOWN * 0.4)
        duda = etiqueta("duda más", ESTIMACION, 0.5).move_to([1.6, 2.4, 0])
        media = etiqueta("y tira más hacia la media", INK, 0.5).move_to([-2.0, -3.3, 0])
        # las dos barras de error
        be = barras_error([0.7386, 0.686], ["causal", "no causal"], centro=(4.6, -0.5), ancho=3.0, alto=3.0, v_max=0.8,
                          colores=[ESTIMACION, VERDE])
        v1 = etiqueta("0,7386", ESTIMACION, 0.5).next_to(be.barras[0], UP, buff=0.1)
        v2 = etiqueta("0,686", VERDE, 0.5).next_to(be.barras[1], UP, buff=0.1)
        llave = Brace(Line(be.barras[1].get_corner(UR), be.barras[0].get_corner(UL)), UP, color=ERROR, buff=0.0)
        l_prec = etiqueta("precio", ERROR, 0.5, BOLD)
        interr = etiqueta("¿cuánto?", ERROR, 0.6, BOLD)
        with self.narrar("b2"):
            # «la ganancia en continua»
            self.en("continua")
            self.play(Create(base), Create(vert), FadeIn(w0), FadeIn(wp), FadeIn(l_w), FadeIn(y5), FadeIn(y1), run_time=0.4)
            self.play(Create(c_c), FadeIn(n_c), run_time=self.dur(0.9))
            self.play(FadeIn(p_c, scale=0.3), run_time=0.3)

            # «cero coma ocho ocho»
            self.en("g088")
            self.pop(t_c)

            # «Menor que la del filtro no causal»
            self.en("menor")
            self.play(Create(c_n), FadeIn(n_n), run_time=self.dur(1.0))

            # «cero coma nueve cuatro»
            self.en("g094")
            self.play(FadeIn(p_n, scale=0.3), run_time=0.3)
            self.pop(t_n)

            # «sin poder mirar el futuro, duda más»
            self.en("duda")
            self.play(FadeIn(duda), run_time=self.dur(0.5))

            # «tira más hacia la media»
            self.en("media")
            self.play(FadeIn(media), c_c.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(1.0))

            # «cero coma siete tres ocho seis frente a»
            self.en("frente")
            self.play(Create(be.base), FadeIn(be.etiquetas[0]), FadeIn(be.etiquetas[1]),
                      GrowFromEdge(be.barras[0], DOWN), run_time=0.7)
            self.play(FadeIn(v1), run_time=0.3)

            # «del no causal»
            self.en("delno")
            self.play(GrowFromEdge(be.barras[1], DOWN), FadeIn(v2), run_time=self.dur(0.6))

            # «lo que cuesta no ver el futuro»
            self.en("cuesta")
            llave.move_to([4.6, be.barras[0].get_top()[1] + 0.65, 0])
            llave.set_width(be.barras[0].get_width() * 2.4)
            l_prec.next_to(llave, UP, buff=0.1)
            self.play(GrowFromCenter(llave), FadeIn(l_prec), run_time=self.dur(0.6))

            # «Vamos a ponerle precio exacto»
            self.en("exacto")
            self.play(FadeOut(l_prec), FadeIn(interr.next_to(llave, UP, buff=0.1)), run_time=self.dur(0.5))
