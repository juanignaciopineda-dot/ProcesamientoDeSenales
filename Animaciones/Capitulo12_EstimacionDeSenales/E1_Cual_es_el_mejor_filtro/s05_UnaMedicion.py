"""Escena 05 — Una sola medición: la parábola del error y su mínimo (h = 0,8)."""
from comun.escena import *


class UnaMedicion(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.planteo()
        self.cuenta()
        self.parabola()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def planteo(self):
        t, y, v, x = sensor12(40)
        L = Lienzo(ancho=8.0, alto=2.4, t_rango=(0, 39), v_max=7, centro=(0.0, 1.6))
        d = 0.9                                     # cuánto está levantada la curva antes de restar 20
        cur_x = L.curva(t, x, MEDIDA, 3.2)
        cur_y = L.curva(t, y, SENAL, 3.6)
        media = DashedLine(L.p(0, 0), L.p(39, 0), color=INK, stroke_width=2.2)
        l20 = Text("20 °C", color=INK).scale(0.42).next_to(L.p(0, 0), LEFT, buff=0.12)
        grupo = VGroup(cur_x, cur_y, media, l20).shift(UP * d)
        k = 30
        muestra = Circle(radius=0.2, color=AMBAR, stroke_width=4).move_to(L.p(k, x[k]) + UP * d)
        menos20 = MathTex(r"-\,20", color=AMBAR).scale(0.9).move_to([-5.6, 2.9, 0])
        # lo medido por un factor
        flecha_m = Arrow(L.p(k, 0) + DOWN * 1.45, L.p(k, 0) + DOWN * 2.3, buff=0, color=ESTIMACION,
                         stroke_width=4, max_tip_length_to_length_ratio=0.25)
        por_h = MathTex(r"\times\, h", color=ESTIMACION).scale(0.9).next_to(flecha_m, RIGHT, buff=0.15)
        f = formula(r"\hat{y}", "=", "h", r"\cdot", "x", escala=1.3,
                    colores={0: ESTIMACION, 2: ESTIMACION, 4: MEDIDA}).move_to([0, -1.5, 0])
        J = formula("J(h)", "=", r"E\big[", "(", "y", "-", "h", "x", ")^2", r"\big]", escala=1.2,
                    colores={4: SENAL, 6: ESTIMACION, 7: MEDIDA, 8: ERROR}).move_to([0, -2.8, 0])
        r_media = SurroundingRectangle(J[2], color=AMBAR, buff=0.06)
        r_dife = SurroundingRectangle(VGroup(J[3], J[4], J[5], J[6], J[7]), color=AMBAR, buff=0.1)
        r_cuad = SurroundingRectangle(J[8], color=ERROR, buff=0.06)
        h = ValueTracker(0.3)
        yh = Dot(color=ESTIMACION, radius=0.11)
        yh.add_updater(lambda m: m.move_to(L.p(k, h.get_value() * x[k])))
        err = Line(color=ERROR, stroke_width=4)
        err.add_updater(lambda m: m.put_start_and_end_on(L.p(k, h.get_value() * x[k]), L.p(k, y[k])))

        with self.narrar("b1"):
            # «con una sola medición»
            self.en("una")
            self.play(FadeIn(cur_x), run_time=self.dur(0.5))
            self.play(Create(muestra), run_time=self.dur(0.4))

            # «Trabajamos con la temperatura»
            self.en("trabajamos")
            self.play(Create(cur_y), run_time=self.dur(0.7))

            # «ya centrada»
            self.en("centrada")
            self.play(Create(media), FadeIn(l20), run_time=self.dur(0.5))

            # «restándole sus veinte grados»
            self.en("resta")
            self.pop(menos20)
            self.play(grupo.animate.shift(DOWN * d), muestra.animate.shift(DOWN * d), run_time=self.dur(0.8))

            # «un múltiplo de lo medido»
            self.en("multiplo")
            self.play(GrowArrow(flecha_m), run_time=self.dur(0.4))
            self.pop(por_h)

            # «igual a hache por equis»
            self.en("formula")
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in range(len(f))], run_time=self.dur(0.9))

            # «Probemos valores de hache»
            self.en("probar")
            self.add(yh, err)
            self.play(h.animate.set_value(1.3), run_time=self.dur(1.0))
            self.play(h.animate.set_value(0.8), run_time=self.dur(0.8))
            yh.clear_updaters()
            err.clear_updaters()

            # «el error cuadrático medio»
            self.en("ecm")
            self.play(*[FadeIn(J[i], shift=UP * 0.1) for i in range(len(J))], run_time=self.dur(1.0))

            # «la media de»
            self.en("media")
            self.play(Create(r_media), run_time=self.dur(0.4))

            # «i griega menos hache por equis»
            self.en("dife")
            self.play(FadeOut(r_media), Create(r_dife), run_time=self.dur(0.5))

            # «todo al cuadrado»
            self.en("cuadrado")
            self.play(FadeOut(r_dife), Create(r_cuad), run_time=self.dur(0.4))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def cuenta(self):
        fila = formula(r"(y-hx)^2", "=", "y^2", "-", r"2h\,y\,x", "+", r"h^2\,x^2", escala=1.3,
                       colores={2: SENAL, 4: MEDIDA, 6: MEDIDA}).move_to([0, 2.7, 0])
        fila[4].set_color(AMBAR)
        medias = formula(r"E[y^2]", "-", r"2h\,E[yx]", "+", r"h^2\,E[x^2]", escala=1.2).move_to([0, 1.2, 0])
        lineal = Text("linealidad", color=INK).scale(0.5).move_to([5.5, 1.2, 0])
        v4 = MathTex(r"E[y^2] = 4", color=SENAL).scale(0.95).move_to([-3.7, -0.3, 0])
        xyr = MathTex("x", "=", "y", "+", "v", color=TXT).scale(0.95).move_to([3.7, -0.3, 0])
        xyr[0].set_color(MEDIDA)
        xyr[2].set_color(SENAL)
        xyr[4].set_color(RUIDO)
        norel = MathTex(r"E[y\,v] = 0", color=RUIDO).scale(0.95).move_to([3.7, -1.3, 0])
        c4 = MathTex(r"E[y\,x] = 4 + 0 = 4", color=TXT).scale(0.95).move_to([-3.7, -1.5, 0])
        c5 = MathTex(r"E[x^2] = 4 + 1 = 5", color=TXT).scale(0.95).move_to([-3.7, -2.7, 0])
        r2 = SurroundingRectangle(medias[2], color=AMBAR, buff=0.08)
        r3 = SurroundingRectangle(medias[4], color=AMBAR, buff=0.08)

        with self.narrar("b2"):
            # «Desarrollamos el cuadrado»
            self.en("desarrollo")
            self.corte()
            self.play(FadeIn(fila[0]), FadeIn(fila[1]), run_time=self.dur(0.5))

            # «i griega al cuadrado»
            self.en("t1")
            self.play(FadeIn(fila[2]), run_time=self.dur(0.4))

            # «menos dos hache por i griega por equis»
            self.en("t2")
            self.play(FadeIn(fila[3]), FadeIn(fila[4]), run_time=self.dur(0.5))

            # «más hache al cuadrado por equis al cuadrado»
            self.en("t3")
            self.play(FadeIn(fila[5]), FadeIn(fila[6]), run_time=self.dur(0.6))

            # «Tomamos la media de cada término»
            self.en("media")
            self.play(*[FadeIn(medias[i], shift=DOWN * 0.1) for i in range(len(medias))], run_time=self.dur(0.9))

            # «por linealidad»
            self.en("lineal")
            self.pop(lineal)

            # «la varianza: cuatro»
            self.en("v4")
            self.play(FadeIn(v4, shift=UP * 0.1), run_time=self.dur(0.5))

            # «La de i griega por equis»
            self.en("yx")
            self.play(Create(r2), run_time=self.dur(0.4))

            # «equis es i griega más ruido»
            self.en("xyr")
            self.play(FadeIn(xyr), run_time=self.dur(0.6))

            # «el ruido no se relaciona»
            self.en("norel")
            self.play(FadeIn(norel), run_time=self.dur(0.5))

            # «también cuatro»
            self.en("c4")
            self.play(FadeIn(c4, shift=UP * 0.1), run_time=self.dur(0.6))

            # «La de equis al cuadrado»
            self.en("xx")
            self.play(FadeOut(r2), Create(r3), run_time=self.dur(0.4))

            # «cuatro más uno: cinco»
            self.en("c5")
            self.play(FadeIn(c5, shift=UP * 0.1), run_time=self.dur(0.6))
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def parabola(self):
        ax, et = ejes((-0.2, 1.8, 0.5), (0, 4.5, 1), ancho=7.0, alto=3.6, x_label="h", y_label="J")
        viejo = ax.get_center().copy()
        ax.move_to([0.3, -0.6, 0])
        et.shift(ax.get_center() - viejo)
        J = lambda h: 4 - 8 * h + 5 * h * h
        graf = ax.plot(J, x_range=[0, 1.6], color=ERROR, stroke_width=4)
        form = formula("J(h)", "=", "4", "-8h", "+5h^2", escala=1.3, colores={0: ERROR}).move_to([0, 3.2, 0])
        h = ValueTracker(0.1)
        punto = Dot(color=AMBAR, radius=0.12)
        punto.add_updater(lambda m: m.move_to(ax.c2p(h.get_value(), J(h.get_value()))))
        tang = Line(color=TXT, stroke_width=3)

        def poner_tangente(m):
            hv = h.get_value()
            s = -8 + 10 * hv
            m.put_start_and_end_on(ax.c2p(hv - 0.35, J(hv) - 0.35 * s), ax.c2p(hv + 0.35, J(hv) + 0.35 * s))
        tang.add_updater(poner_tangente)
        deriv = formula("J'(h)", "=", "-8+10h", "=", "0", escala=1.0).move_to([4.6, 2.3, 0])
        vert = ax.c2p(0.8, J(0.8))
        guia_v = DashedLine(vert, ax.c2p(0.8, 0), color=INK, stroke_width=2)
        guia_h = DashedLine(vert, [4.1, vert[1], 0], color=INK, stroke_width=2)
        h08 = MathTex("h = 0{,}8", color=AMBAR).scale(0.85).move_to(ax.c2p(0.8, 0) + DOWN * 0.5)
        j08 = MathTex(r"J_{\min} = 0{,}8", color=ERROR).scale(0.85).move_to([5.6, vert[1], 0])
        sel = sello("capítulo 10: 0,8", VERDE).move_to([4.9, -3.3, 0])

        with self.narrar("b3"):
            # «El error queda cuatro»
            self.en("j1")
            self.corte()
            self.play(*[FadeIn(form[i]) for i in range(3)], run_time=self.dur(0.5))

            # «menos ocho hache»
            self.en("j2")
            self.play(FadeIn(form[3], shift=UP * 0.1), run_time=self.dur(0.4))

            # «más cinco hache al cuadrado»
            self.en("j3")
            self.play(FadeIn(form[4], shift=UP * 0.1), run_time=self.dur(0.4))

            # «una parábola»
            self.en("parabola")
            self.play(Create(ax), FadeIn(et), run_time=self.dur(0.5))
            self.add(punto)
            self.play(Create(graf), h.animate.set_value(1.5), run_time=self.dur(1.6), rate_func=linear)

            # «abierta hacia arriba»
            self.en("arriba")
            self.resaltar(graf, color=AMBAR, escala=1.03)

            # «punto más bajo»
            self.en("bajo")
            self.play(h.animate.set_value(0.8), run_time=self.dur(1.0))

            # «la pendiente es la derivada»
            self.en("derivada")
            self.play(h.animate.set_value(0.25), run_time=0.3)
            self.add(tang)
            self.play(h.animate.set_value(1.2), run_time=self.dur(1.2))

            # «menos ocho más diez hache»
            self.en("deriv")
            self.play(*[FadeIn(deriv[i]) for i in range(3)], run_time=self.dur(0.7))

            # «Igualada a cero»
            self.en("cero")
            self.play(h.animate.set_value(0.8), run_time=self.dur(0.8))
            self.play(FadeIn(deriv[3]), FadeIn(deriv[4]), run_time=0.3)

            # «ocho décimos»
            self.en("h08")
            self.play(Create(guia_v), FadeIn(h08), run_time=self.dur(0.5))

            # «el error ahí es cero coma ocho»
            self.en("j08")
            self.play(Create(guia_h), FadeIn(j08), run_time=self.dur(0.6))

            # «el resultado del capítulo diez»
            self.en("cap10")
            self.pop(sel)
            punto.clear_updaters()
            tang.clear_updaters()
