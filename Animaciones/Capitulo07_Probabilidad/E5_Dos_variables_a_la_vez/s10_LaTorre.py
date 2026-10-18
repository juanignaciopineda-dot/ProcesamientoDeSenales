"""Escena 10 — La propiedad de la torre: con la tabla, con la nube y con las alturas."""
from comun.escena import *


class LaTorre(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        m1 = MathTex(r"R=1:\ 0{,}79", color=VERDE).scale(0.95)
        m0 = MathTex(r"R=0:\ 0{,}045", color=VERDE).scale(0.95)
        medias = VGroup(m1, m0).arrange(DOWN, buff=0.7, aligned_edge=LEFT).move_to([-3.2, 0.9, 0])
        w1 = MathTex(r"0{,}34", color=MEDIDA).scale(1.0).next_to(m1, LEFT, buff=0.35)
        w0 = MathTex(r"0{,}66", color=MEDIDA).scale(1.0).next_to(m0, LEFT, buff=0.35)
        c1 = MathTex(r"0{,}34\cdot0{,}79\approx0{,}27", color=TXT).scale(0.95).move_to([2.6, 1.7, 0])
        c2 = MathTex(r"+\ 0{,}66\cdot0{,}045\approx0{,}03", color=TXT).scale(0.95).move_to([2.9, 0.7, 0])
        raya = Line([-0.2, 0.15, 0], [6.0, 0.15, 0], color=INK, stroke_width=2)
        da = MathTex(r"=\,0{,}3", color=AMBAR).scale(1.4).move_to([1.4, -0.7, 0])
        media = formula("E[S]", "=", r"0\cdot0{,}7+1\cdot0{,}3", "=", r"0{,}3", escala=1.0,
                        colores={0: SENAL, 4: AMBAR}).move_to([2.2, -2.0, 0])
        torre = formula("E[S]", "=", r"E\big[", r"E[S\mid R]", r"\big]", escala=1.3,
                        colores={0: SENAL, 3: ESTIMACION}).move_to([0, 3.3, 0])
        with self.narrar("b1"):
            # «el promedio de esos promedios»
            self.en("promedio")
            self.play(FadeIn(medias, shift=RIGHT * 0.2), run_time=self.dur(0.7))

            # «lo probable que es su columna»
            self.en("pesos")
            self.play(FadeIn(w1, shift=RIGHT * 0.2), FadeIn(w0, shift=RIGHT * 0.2), run_time=self.dur(0.6))

            # «Cero coma treinta y cuatro por cero coma setenta y nueve»
            self.en("cuenta1")
            self.play(FadeIn(c1, shift=LEFT * 0.2), run_time=self.dur(0.7))

            # «más cero coma sesenta y seis»
            self.en("cuenta2")
            self.play(FadeIn(c2, shift=LEFT * 0.2), run_time=self.dur(0.7))

            # «cero coma cero cuatro cinco»
            self.en("c045")
            self.play(Indicate(m0, color=AMBAR, scale_factor=1.2), run_time=self.dur(0.7))

            # «Da cero coma tres»
            self.en("da")
            self.play(Create(raya), run_time=0.3)
            self.pop(da)

            # «la media de lo enviado»
            self.en("media")
            self.play(FadeIn(media[0:4], shift=UP * 0.15), run_time=self.dur(0.9))
            self.play(FadeIn(media[4], shift=UP * 0.15), run_time=self.dur(0.4))

            # «Promediar por grupos»
            self.en("grupos")
            self.resaltar(medias, w1, w0, color=VERDE, escala=1.08, run_time=0.7)

            # «y después promediar los grupos»
            self.en("despues")
            self.play(Indicate(c1, color=AMBAR, scale_factor=1.15), Indicate(c2, color=AMBAR, scale_factor=1.15), run_time=self.dur(0.8))

            # «da lo mismo»
            self.en("lo_mismo")
            self.play(Indicate(da, color=VERDE, scale_factor=1.3), Indicate(media[4], color=VERDE, scale_factor=1.4), run_time=self.dur(0.8))

            # «propiedad de la torre»
            self.en("torre")
            self.play(FadeIn(torre[0:2], shift=DOWN * 0.15), run_time=self.dur(0.5))
            self.play(FadeIn(torre[2:], shift=DOWN * 0.15), run_time=self.dur(0.7))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        ax, lab = ejes([-3, 3, 1], [-3.5, 3.5, 1], ancho=7.0, alto=5.0, x_label="x", y_label="y")
        g = VGroup(ax, lab).move_to([0, -0.3, 0])
        px, py = nube_xy7(190, 9)
        puntos = VGroup(*[Dot(ax.c2p(a, b), radius=0.055, color=SENAL) for a, b in zip(px, py)])
        for p in puntos:
            p.permitir_encima = True
        centros_x = np.arange(-2.25, 2.3, 0.5)
        lineas = VGroup(*[DashedLine(ax.c2p(x - 0.25, -3.5), ax.c2p(x - 0.25, 3.5), color=INK, stroke_width=1.5)
                          for x in np.arange(-2.5, 3.01, 0.5)])
        puntos_c = []
        for x in centros_x:
            sel = (px >= x - 0.25) & (px < x + 0.25)
            puntos_c.append(Dot(ax.c2p(x, float(np.mean(py[sel])) if sel.any() else x), radius=0.12, color=AMBAR))
        curva = traza([float(p.get_center()[0]) for p in puntos_c], [float(p.get_center()[1]) for p in puntos_c], AMBAR, 5)
        banda = Rectangle(width=float(ax.c2p(0.5, 0)[0] - ax.c2p(0, 0)[0]), height=5.0, stroke_width=0
                          ).set_fill(AMBAR, 0.22).move_to([float(ax.c2p(1.0, 0)[0]), float(ax.c2p(0, 0)[1]), 0])
        xv = MathTex("x", color=AMBAR).scale(1.0).next_to(banda, UP, buff=0.1)
        g_x = formula("g(x)", "=", r"E[Y\mid X=x]", escala=1.2, colores={0: AMBAR}).move_to([-3.6, 3.3, 0])
        cursor = Dot(ax.c2p(-2, -2), radius=0.15, color=ESTIMACION)
        lect = Text("Y esperada", color=ESTIMACION).scale(0.6)
        lect.add_updater(lambda m: m.next_to(cursor, RIGHT, buff=0.2))
        lect.permitir_encima = True
        with self.narrar("b2"):
            # «en continuo»
            self.en("continuo")
            self.corte()
            self.play(Create(ax), FadeIn(lab), run_time=self.dur(0.4))
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in puntos], lag_ratio=0.01), run_time=self.dur(0.8))

            # «rebanadas finas»
            self.en("rebanadas")
            self.play(LaggedStart(*[Create(l) for l in lineas], lag_ratio=0.08), run_time=self.dur(1.2))

            # «una para cada valor de equis»
            self.en("cada_x")
            self.play(FadeIn(banda), FadeIn(xv), run_time=self.dur(0.5))

            # «el centro de cada rebanada»
            self.en("centros")
            self.play(FadeOut(banda), FadeOut(xv), run_time=0.2)
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in puntos_c], lag_ratio=0.12), run_time=self.dur(1.5))

            # «forman una curva»
            self.en("curva")
            self.play(Create(curva), run_time=self.dur(1.0), rate_func=linear)

            # «la esperanza de i griega dado equis»
            self.en("g_x")
            self.play(FadeIn(g_x[0:2], shift=DOWN * 0.15), run_time=self.dur(0.5))
            self.play(FadeIn(g_x[2], shift=DOWN * 0.15), run_time=self.dur(0.7))

            # «rebanada a rebanada»
            self.en("reb")
            self.play(LaggedStart(*[Indicate(p, scale_factor=1.8, color=ESTIMACION) for p in puntos_c], lag_ratio=0.12),
                      run_time=self.dur(1.6))

            # «lo que cabe esperar»
            self.en("cabe")
            self.play(FadeIn(cursor), FadeIn(lect), run_time=0.3)
            self.play(MoveAlongPath(cursor, curva), run_time=min(5.0, max(2.0, self.margen() - 0.3)), rate_func=smooth)
            lect.clear_updaters()

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        al = Alturas7(centro=(0, 0.9), ancho=9.0, alto=2.8)
        t40 = MathTex(r"40\,\%", color=AZUL).scale(1.0).move_to([float(al.x(175)), 3.2, 0])
        t60 = MathTex(r"60\,\%", color=MAGENTA).scale(1.0).move_to([float(al.x(162)) - 0.9, 3.3, 0])
        mh = al.marca(175, AZUL, 3, 2.3)
        mm = al.marca(162, MAGENTA, 3, 2.9)
        l175 = MathTex(r"175\ \text{cm}", color=AZUL).scale(0.85).next_to(mh, DOWN, buff=0.45)
        l162 = MathTex(r"162\ \text{cm}", color=MAGENTA).scale(0.85).next_to(mm, DOWN, buff=0.45)
        # los dos rótulos de cm caen en la misma altura: se separan hacia afuera
        l175.shift(RIGHT * 0.45)
        l162.shift(LEFT * 0.45)
        total = al.marca(167.2, AMBAR, 5, 3.3)
        c1 = MathTex(r"0{,}4\cdot175=70", color=TXT).scale(0.9).move_to([-4.0, -2.6, 0])
        c2 = MathTex(r"+\ 0{,}6\cdot162=97{,}2", color=TXT).scale(0.9).move_to([0.9, -2.6, 0])
        r_ = MathTex(r"=\,167{,}2", color=AMBAR).scale(1.2).move_to([5.0, -2.6, 0])
        var = Text("¿y la varianza?", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, 3.4, 0])
        with self.narrar("b3"):
            # «Un ejemplo cotidiano»
            self.en("ejemplo")
            self.corte()
            tor = self.palabra("la torre", AMBAR, 1.4).move_to([0, 0.3, 0])
            self.pop(tor)

            # «el cuarenta por ciento son hombres»
            self.en("hombres")
            self.play(FadeOut(tor), run_time=0.2)
            self.play(Create(al.base), Create(al.h), run_time=self.dur(0.9), rate_func=linear)
            self.pop(t40)

            # «ciento setenta y cinco centímetros»
            self.en("h175")
            self.play(Create(mh), FadeIn(l175), run_time=self.dur(0.6))

            # «el sesenta por ciento son mujeres»
            self.en("mujeres")
            self.play(Create(al.m), run_time=self.dur(0.9), rate_func=linear)
            self.pop(t60)

            # «ciento sesenta y dos»
            self.en("m162")
            self.play(Create(mm), FadeIn(l162), run_time=self.dur(0.6))

            # «La altura media de todos»
            self.en("todos")
            self.play(Create(total), run_time=self.dur(0.6))

            # «cero coma cuatro por ciento setenta y cinco»
            self.en("cuenta1")
            self.play(FadeIn(c1, shift=UP * 0.15), run_time=self.dur(0.6))

            # «cero coma seis por ciento sesenta y dos»
            self.en("cuenta2")
            self.play(FadeIn(c2, shift=UP * 0.15), run_time=self.dur(0.6))

            # «ciento sesenta y siete coma dos»
            self.en("r1672")
            self.pop(r_)

            # «con la varianza»
            self.en("varianza")
            self.play(FadeOut(t40), FadeOut(t60), run_time=0.2)
            self.pop(var)
