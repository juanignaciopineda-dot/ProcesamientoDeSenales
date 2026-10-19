"""Escena 04 — La curva gana (1/24 contra 1/18) y el trato: conformarnos con la mejor recta."""
from comun.escena import *
from comun.figuras_cap08_e3 import *


class LaCurvaGanaLaRectaSeConforma(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.C = CarpaE3()
        self.add(*self.C.base())            # el mismo dibujo de la escena 03, sin animar
        self.curva()
        self.covarianza()
        self.trato()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def curva(self):
        C = self.C
        pts = [C.p(0, 0), C.p(1, 0.5), C.p(2, 0)]
        tent = traza([p[0] for p in pts], [p[1] for p in pts], AMBAR, 5)
        x0 = ValueTracker(0.02)
        reb = Line(color=SENAL, stroke_width=8)
        reb.add_updater(lambda m: m.put_start_and_end_on(
            C.p(x0.get_value(), 0), C.p(x0.get_value(), C.techo(x0.get_value()))))
        pc = Dot(color=ESTIMACION, radius=0.11)
        pc.add_updater(lambda m: m.move_to(C.p(x0.get_value(), C.techo(x0.get_value()) / 2)))
        alt = Text("Altura 0,5", color=AMBAR).scale(0.45).move_to(C.p(1, 0.78))
        f_esa = formula("E[", "y", r"\mid", "x", "]", escala=1.3, color=AMBAR,
                        colores={1: SENAL, 3: MEDIDA}).move_to([5.5, 2.0, 0])
        norec = Text("No es una recta", color=ROJO, weight=BOLD).scale(0.55).move_to([5.5, 1.2, 0])
        sube = Arrow(C.p(0.4, 0.34), C.p(0.9, 0.59), buff=0, color=TXT, stroke_width=5,
                     max_tip_length_to_length_ratio=0.3)
        baja = Arrow(C.p(1.1, 0.59), C.p(1.6, 0.34), buff=0, color=TXT, stroke_width=5,
                     max_tip_length_to_length_ratio=0.3)
        reb2 = C.rebanada(1.5)
        brace = Brace(reb2, direction=RIGHT, color=INK, buff=0.08)
        a_lbl = MathTex("a", color=SENAL).scale(0.8).next_to(brace, RIGHT, buff=0.1)
        unif = Text("Uniforme", color=SENAL, weight=BOLD).scale(0.55).move_to([5.5, -0.1, 0])
        var = formula(r"\sigma^2", "=", r"\frac{a^2}{12}", escala=1.0, colores={0: ERROR}).move_to([5.5, -1.0, 0])
        finas = VGroup(*[C.rebanada(x, SENAL, 3) for x in np.linspace(0.15, 1.85, 9)])
        prom = Text("Promedio de σ²", color=ERROR).scale(0.55).move_to([5.5, 0.1, 0])
        integral = MathTex(r"=\int \sigma^2 f_X\,dx", color=TXT).scale(0.8).move_to([5.5, -0.7, 0])
        v24 = MathTex(r"=\frac{1}{24}", color=ERROR).scale(1.0).move_to([5.5, -1.8, 0])
        v042 = MathTex(r"\approx 0{,}042", color=ERROR).scale(1.1).move_to([5.5, -2.8, 0])
        self.tent, self.arrs = tent, VGroup(sube, baja)
        self.col1 = VGroup(f_esa, norec, prom, integral, v24, v042, alt)
        self.finas = finas

        with self.narrar("b1"):
            # «Uniendo los centros»
            self.en("unir")
            self.add(reb, pc)
            self.play(x0.animate.set_value(1.98), Create(tent), run_time=self.dur(2.3), rate_func=linear)
            reb.clear_updaters()
            pc.clear_updaters()
            self.play(FadeOut(reb), FadeOut(pc), run_time=0.2)

            # «otra carpa, de la mitad de altura»
            self.en("carpa2")
            self.play(FadeIn(alt), run_time=self.dur(0.4))
            self.resaltar(tent, color=ESTIMACION, escala=1.03)

            # «Esa es la media condicional»
            self.en("esa")
            self.play(FadeIn(f_esa, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «y no es una recta»
            self.en("norecta")
            self.pop(norec)

            # «sube y luego baja»
            self.en("sube")
            self.play(GrowArrow(sube), run_time=self.dur(0.4))
            self.play(GrowArrow(baja), run_time=self.dur(0.4))

            # «Cada rebanada es una uniforme»
            self.en("unif")
            self.play(FadeOut(sube), FadeOut(baja), tent.animate.set_stroke(opacity=0.4), Create(reb2),
                      run_time=self.dur(0.6))
            self.pop(unif)

            # «su ancho al cuadrado entre doce»
            self.en("var")
            self.play(GrowFromCenter(brace), FadeIn(a_lbl), run_time=self.dur(0.5))
            self.play(FadeIn(var, shift=UP * 0.1), run_time=self.dur(0.7))

            # «el promedio de esas varianzas»
            self.en("prom")
            self.play(FadeOut(unif), FadeOut(var), FadeOut(brace), FadeOut(a_lbl), FadeOut(reb2),
                      run_time=self.dur(0.3))
            self.play(LaggedStart(*[Create(f) for f in finas], lag_ratio=0.12), run_time=self.dur(1.3))
            self.pop(prom)

            # «una integral»
            self.en("integral")
            self.pop(integral)

            # «un veinticuatroavo»
            self.en("v24")
            self.pop(v24)

            # «cero coma cero cuatro dos»
            self.en("v042")
            self.pop(v042)
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def covarianza(self):
        C = self.C
        cov = MathTex(r"\sigma_{xy}", color=TXT).scale(1.3).move_to([5.5, 2.0, 0])
        cero = MathTex(r"\sigma_{xy}=0", color=AMBAR).scale(1.3).move_to([5.5, 2.0, 0])
        p_izq = Polygon(C.p(0, 0), C.p(1, 1), C.p(1, 0), stroke_width=0).set_fill(AZUL, 0.4)
        p_der = Polygon(C.p(1, 1), C.p(2, 0), C.p(1, 0), stroke_width=0).set_fill(AZUL, 0.4)
        a_sube = Arrow(C.p(0.2, 0.15), C.p(0.7, 0.62), buff=0, color=ESTIMACION, stroke_width=6,
                       max_tip_length_to_length_ratio=0.3)
        a_baja = Arrow(C.p(1.3, 0.62), C.p(1.8, 0.15), buff=0, color=ESTIMACION, stroke_width=6,
                       max_tip_length_to_length_ratio=0.3)
        # la parábola del capítulo 7, en pequeño
        xs = np.linspace(-1, 1, 40)
        cp = np.array([5.5, -0.3, 0.0])
        parab = traza(cp[0] + 1.1 * xs, cp[1] - 0.5 + 1.0 * xs ** 2, SENAL, 4)
        base_p = Line(cp + [-1.3, -0.5, 0], cp + [1.3, -0.5, 0], color=INK, stroke_width=2)
        cap7 = Text("Capítulo 7", color=INK).scale(0.45).move_to(cp + [0, -1.0, 0])
        una = Text("Solo una recta", color=TXT).scale(0.6).move_to([5.5, 0.6, 0])
        recta = Line(C.p(-0.1, 1 / 3), C.p(2.1, 1 / 3), color=ESTIMACION, stroke_width=5)
        tercio = MathTex(r"\frac{1}{3}", color=AMBAR).scale(0.9).move_to(C.p(2.1, 1 / 3) + RIGHT * 0.75)
        err = Text("Error", color=ERROR, weight=BOLD).scale(0.6).move_to([5.5, -0.7, 0])
        e18 = MathTex(r"=\frac{1}{18}", color=ERROR).scale(1.0).move_to([5.5, -1.6, 0])
        e056 = MathTex(r"\approx 0{,}056", color=ERROR).scale(1.1).move_to([5.5, -2.8, 0])

        with self.narrar("b2"):
            # «Ahora, la covarianza»
            self.en("cov")
            self.play(FadeOut(self.col1), FadeOut(self.finas), self.tent.animate.set_stroke(opacity=0.3),
                      run_time=self.dur(0.5))
            self.pop(cov)

            # «En la mitad izquierda»
            self.en("izq")
            self.play(FadeIn(p_izq), run_time=self.dur(0.5))

            # «tiende a subir»
            self.en("sube2")
            self.play(GrowArrow(a_sube), run_time=self.dur(0.5))

            # «en la derecha»
            self.en("der")
            self.play(FadeOut(p_izq), FadeIn(p_der), run_time=self.dur(0.4))

            # «tiende a bajar»
            self.en("baja")
            self.play(GrowArrow(a_baja), run_time=self.dur(0.5))

            # «Como en la parábola del capítulo siete»
            self.en("parab7")
            self.play(Create(base_p), Create(parab), FadeIn(cap7), run_time=self.dur(0.8))

            # «se cancelan»
            self.en("cancel")
            self.play(FadeOut(a_sube), FadeOut(a_baja), FadeOut(p_der), FadeOut(parab), FadeOut(base_p),
                      FadeOut(cap7), ReplacementTransform(cov, cero), run_time=self.dur(0.8))

            # «Si solo pudiéramos usar una recta»
            self.en("recta")
            self.pop(una)

            # «horizontal, a la altura de la media»
            self.en("horiz")
            self.play(Create(recta), run_time=self.dur(0.8))

            # «un tercio»
            self.en("tercio")
            self.pop(tercio)

            # «un dieciochoavo»
            self.en("e18")
            self.play(FadeIn(err), run_time=self.dur(0.3))
            self.pop(e18)

            # «cero coma cero cinco seis»
            self.en("e056")
            self.pop(e056)
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def trato(self):
        base_y, esc = -2.4, 45
        b1 = Rectangle(width=1.5, height=0.042 * esc, stroke_width=0).set_fill(ERROR, 0.85)
        b1.move_to([-5.0, base_y + 0.042 * esc / 2, 0])
        b2 = Rectangle(width=1.5, height=0.056 * esc, stroke_width=0).set_fill(ERROR, 0.85)
        b2.move_to([-2.7, base_y + 0.056 * esc / 2, 0])
        eje = Line([-6.2, base_y, 0], [-1.4, base_y, 0], color=INK, stroke_width=2)
        n1 = Text("Curva", color=TXT).scale(0.5).move_to([-5.0, base_y - 0.35, 0])
        n2 = Text("Recta", color=TXT).scale(0.5).move_to([-2.7, base_y - 0.35, 0])
        v1 = MathTex(r"0{,}042", color=ERROR).scale(0.8).move_to([-5.0, base_y + 0.042 * esc + 0.4, 0])
        v2 = MathTex(r"0{,}056", color=ERROR).scale(0.8).move_to([-2.7, base_y + 0.056 * esc + 0.4, 0])
        ti = tilde(VERDE, 0.6).move_to([-5.0, base_y + 0.042 * esc + 1.1, 0])
        toda = caja("Toda la distribución", INK, ancho=4.8, alto=0.8, scale=0.5).move_to([3.8, 3.0, 0])
        cruz_t = tachar(toda)
        chips = VGroup(*[caja(txt, AMBAR, ancho=3.0, alto=0.65, scale=0.5).move_to([3.4, y, 0])
                         for txt, y in (("Medias", 1.8), ("Varianzas", 1.0), ("Covarianzas", 0.2))])
        tildes = VGroup(*[tilde(VERDE, 0.5).move_to([5.6, y, 0]) for y in (1.8, 1.0, 0.2)])
        trato = Text("Un trato", color=AMBAR, weight=BOLD).scale(1.0).move_to([3.6, -1.0, 0])
        solo = caja("Solo rectas", ESTIMACION, ancho=3.0, alto=0.7, scale=0.55).move_to([3.6, -1.9, 0])
        y_c, y_r = base_y + 0.042 * esc, base_y + 0.056 * esc
        guia = DashedLine([-5.75, y_c, 0], [-1.95, y_c, 0], color=INK, stroke_width=2)
        dif = Arrow([-1.5, y_c, 0], [-1.5, y_r, 0], buff=0, color=ERROR, stroke_width=5,
                    max_tip_length_to_length_ratio=0.35)
        mas = MathTex(r"+0{,}014", color=ERROR).scale(0.8).move_to([-0.5, (y_c + y_r) / 2, 0])
        sel = sello("Estimador lineal óptimo", VERDE).move_to([3.6, -3.0, 0])
        sig = Text("LMMSE", color=INK).scale(0.4).move_to([6.4, -3.0, 0])

        with self.narrar("b3"):
            # «La curva gana»
            self.en("gana")
            self.corte()
            self.play(Create(eje), GrowFromEdge(b1, DOWN), GrowFromEdge(b2, DOWN), FadeIn(n1), FadeIn(n2),
                      run_time=self.dur(0.9))
            self.play(FadeIn(v1), FadeIn(v2), run_time=self.dur(0.4))
            self.pop(ti, sonido="exito")

            # «toda la distribución»
            self.en("toda")
            self.play(FadeIn(toda), run_time=self.dur(0.5))
            self.play(Create(cruz_t), run_time=self.dur(0.4))

            # «casi nunca la tenemos»
            self.en("nunca")
            self.resaltar(toda, color=ROJO, escala=1.06)

            # «medias, varianzas y covarianzas»
            self.en("pocos")
            self.play(LaggedStart(*[FadeIn(c, shift=LEFT * 0.2) for c in chips], lag_ratio=0.3),
                      run_time=self.dur(1.0))
            self.play(LaggedStart(*[FadeIn(t) for t in tildes], lag_ratio=0.3), run_time=self.dur(0.8))

            # «hagamos un trato»
            self.en("trato")
            self.pop(trato)

            # «Nos conformamos con la mejor recta»
            self.en("conformamos")
            self.play(FadeIn(solo, shift=UP * 0.2), run_time=self.dur(0.5))

            # «que solo pide esos pocos números»
            self.en("solopide")
            self.resaltar(*chips, color=AMBAR, escala=1.08)

            # «a cambio de perder algo»
            self.en("perder")
            self.play(Create(guia), run_time=self.dur(0.4))
            self.play(GrowArrow(dif), FadeIn(mas), run_time=self.dur(0.6))

            # «el estimador lineal óptimo»
            self.en("lineal")
            self.pop(sel, sonido="exito")
            self.play(FadeIn(sig), run_time=self.dur(0.3))
        self.wait(0.3)
