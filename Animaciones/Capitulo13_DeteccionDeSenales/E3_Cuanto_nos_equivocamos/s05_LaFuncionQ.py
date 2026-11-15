"""Escena 05 — Las colas de la campana son los errores; la función Q es el área de la cola de la estándar."""
from comun.escena import *


class LaFuncionQ(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.errores_son_areas()
        self.herramienta()
        self.valores()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def errores_son_areas(self):
        L = lienzo_g3(centro=(0.0, -1.2))
        base = eje_g3(L, marcas=(0, 9))
        cam0 = dens3(L, 0, 3, RUIDO)
        cam1 = dens3(L, 9, 3, SENAL)
        umb = umbral3(L, 4.5, alto=2.2)
        preg = Text("¿Cuánto nos equivocamos?", color=ESTIMACION, weight=BOLD).scale(0.8).move_to([0, 3.4, 0])
        fa = Text("falsa alarma", color=ERROR).scale(0.6).move_to([4.6, 1.5, 0])
        fa_f = Arrow(fa.get_bottom(), L.p(6.5, 0.12), buff=0.1, color=ERROR, stroke_width=3)
        punto = Dot(L.p(6.5, 0), radius=0.11, color=ESTIMACION)
        gtag = MathTex("g", color=ESTIMACION).scale(0.75).next_to(punto, DOWN, buff=0.12)
        cola_d = cola3(L, 0, 3, 4.5, 17)
        pfa = MathTex("P_{FA}", color=ERROR).scale(0.85).move_to(L.p(7.0, 0) + DOWN * 0.9)
        fl = Text("fallo (miss)", color=ERROR).scale(0.6).move_to([-3.8, 1.9, 0])
        fl_f = Arrow(fl.get_bottom(), L.p(2.0, 0.1), buff=0.1, color=ERROR, stroke_width=3)
        cola_i = cola3(L, 9, 3, -8, 4.5)
        pm = MathTex("P_{M}", color=ERROR).scale(0.85).move_to(L.p(2.2, 0) + DOWN * 0.9)

        with self.narrar("b1"):
            # «¿Cuánto nos equivocamos?»
            self.en("pregunta")
            self.play(FadeIn(preg), FadeIn(base), Create(cam0), Create(cam1), run_time=self.dur(0.9))
            self.play(Create(umb), run_time=self.dur(0.5))

            # «Una falsa alarma»
            self.en("fa")
            self.play(FadeIn(fa), Create(fa_f), run_time=self.dur(0.5))

            # «la campana de la hipótesis cero»
            self.en("campcero")
            self.play(cam0.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.7))

            # «por encima del umbral»
            self.en("encima")
            self.play(FadeIn(punto, scale=0.4), FadeIn(gtag), run_time=self.dur(0.5))

            # «el área de la cola derecha»
            self.en("coladcha")
            self.play(FadeIn(cola_d), FadeIn(pfa), run_time=self.dur(0.6))

            # «Un fallo»
            self.en("fallo")
            self.play(FadeOut(fa), FadeOut(fa_f), FadeIn(fl), Create(fl_f), run_time=self.dur(0.5))

            # «la campana de la hipótesis uno»
            self.en("campuno")
            self.play(cam1.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.7))

            # «sale por debajo»
            self.en("debajo")
            self.play(punto.animate.move_to(L.p(2.5, 0)), run_time=self.dur(0.6))
            self.play(gtag.animate.next_to(L.p(2.5, 0), DOWN, buff=0.12), run_time=0.2)

            # «el área de la cola izquierda»
            self.en("colaizq")
            self.play(FadeIn(cola_i), FadeIn(pm), run_time=self.dur(0.6))

            # «Las dos probabilidades son áreas»
            self.en("areas")
            self.play(cola_d.animate(rate_func=there_and_back).set_fill(ERROR, 0.95),
                      cola_i.animate(rate_func=there_and_back).set_fill(ERROR, 0.95), run_time=self.dur(0.9))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def herramienta(self):
        L = Lienzo(ancho=6.4, alto=3.4, t_rango=(-4, 4), v_max=1.2, centro=(-2.2, -0.9))
        base = L.base(ancho=2.4)
        std = dens3(L, 0, 1, TXT, sigma0=1.0)
        std_fantasma = dens3(L, 0, 1, INK, ancho=2.5, sigma0=1.0)
        std_fantasma.set_stroke(opacity=0.5)
        palabra_h = self.palabra("herramienta", AMBAR, 1.5).move_to([0, 0.3, 0])
        varias = VGroup(campana_mini((-4.2, 0.4), 2.6, 1.2, RUIDO, 4.0),
                        campana_mini((0.0, 0.6), 1.3, 1.7, SENAL, 4.0),
                        campana_mini((4.3, 0.3), 3.2, 0.8, MEDIDA, 4.0))
        et_std = Text("media 0 · desvío 1", color=TXT).scale(0.55).move_to(L.p(0, 0) + UP * 2.6)
        cam_x = dens3(L, 2.5, 1.6, MEDIDA, sigma0=1.0)
        resta = Text("− media", color=AMBAR, weight=BOLD).scale(0.6).move_to([-4.6, 2.3, 0])
        divide = Text("÷ desvío", color=AMBAR, weight=BOLD).scale(0.6).move_to([-4.6, 1.5, 0])
        cola = cola3(L, 0, 1, 1.0, 4.0, sigma0=1.0)
        marca_x = DashedLine(L.p(1.0, 0), L.p(1.0, 1.0), color=ESTIMACION, stroke_width=3)
        x_tag = MathTex("x", color=ESTIMACION).scale(0.8).move_to(L.p(1.0, 0) + DOWN * 0.35)
        q = MathTex("Q(x)", color=ESTIMACION).scale(1.2).move_to(L.p(2.3, 0) + UP * 1.9)
        integral = MathTex(r"\int_x^{\infty}\tfrac{1}{\sqrt{2\pi}}\,e^{-t^2/2}\,dt", color=TXT).scale(0.9)
        integral.move_to([4.3, 2.3, 0])
        tacha = Line(integral.get_corner(DL), integral.get_corner(UR), color=ERROR, stroke_width=7)
        duda = interrogante13(AMBAR, 1.4).move_to([6.4, 1.2, 0])
        tab = VGroup(Rectangle(width=3.0, height=2.0, color=INK, stroke_width=3),
                     Line([-1.5, 0.5, 0], [1.5, 0.5, 0], color=INK, stroke_width=3),
                     Line([-1.5, 0.0, 0], [1.5, 0.0, 0], color=INK, stroke_width=2),
                     Line([-1.5, -0.5, 0], [1.5, -0.5, 0], color=INK, stroke_width=2),
                     Line([0, -1.0, 0], [0, 1.0, 0], color=INK, stroke_width=2)).move_to([4.6, -0.5, 0])
        pc = ordenador(INK).scale(0.9).move_to([4.6, -2.9, 0])

        with self.narrar("b2"):
            # «hay una herramienta»
            self.en("herr")
            self.corte()
            self.pop(palabra_h)

            # «Cualquier campana»
            self.en("cualq")
            self.play(FadeOut(palabra_h), run_time=self.dur(0.3))
            self.play(LaggedStart(*[Create(c) for c in varias], lag_ratio=0.25), run_time=self.dur(1.2))

            # «la campana estándar»
            self.en("estandar")
            self.play(FadeOut(varias), run_time=self.dur(0.3))
            self.play(Create(base), Create(std), FadeIn(et_std), run_time=self.dur(0.8))
            self.add(std_fantasma)

            # «restando la media»
            self.en("resta")
            self.play(FadeIn(resta), Create(cam_x), run_time=self.dur(0.5))
            self.play(Transform(cam_x, dens3(L, 0, 1.6, MEDIDA, sigma0=1.0)), run_time=self.dur(0.8))

            # «dividiendo entre el desvío»
            self.en("divide")
            self.play(FadeIn(divide), Transform(cam_x, dens3(L, 0, 1.0, MEDIDA, sigma0=1.0)), run_time=self.dur(0.9))

            # «El área de la cola»
            self.en("cola")
            self.play(FadeOut(cam_x), FadeOut(resta), FadeOut(divide), FadeIn(cola), run_time=self.dur(0.6))

            # «a partir de un punto equis»
            self.en("desde")
            self.play(Create(marca_x), FadeIn(x_tag), run_time=self.dur(0.6))

            # «función cu de equis»
            self.en("q")
            self.pop(q)

            # «No tiene fórmula sencilla»
            self.en("nofor")
            self.play(FadeIn(integral), run_time=self.dur(0.6))
            self.play(Create(tacha), FadeIn(duda), run_time=self.dur(0.4))

            # «se mira en una tabla»
            self.en("tabla")
            self.play(FadeOut(integral), FadeOut(tacha), FadeOut(duda), run_time=self.dur(0.3))
            self.play(Create(tab), run_time=self.dur(0.6))

            # «o se calcula»
            self.en("calc")
            self.play(FadeIn(pc, shift=UP * 0.2), run_time=self.dur(0.5))
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def valores(self):
        L = Lienzo(ancho=6.4, alto=3.4, t_rango=(-4, 4), v_max=1.2, centro=(-2.6, -0.9))
        base = L.base(ancho=2.4)
        std = dens3(L, 0, 1, TXT, sigma0=1.0)
        enc = formula("x", r"\quad", "Q(x)", escala=0.9, colores={0: ESTIMACION, 2: ESTIMACION}).move_to([4.6, 2.6, 0])
        filas = [formula(f"{a}", r"\quad", f"{b}", escala=0.95, colores={0: TXT, 2: ERROR}) for a, b in
                 (("0", "0{,}5"), ("1", "0{,}16"), ("1{,}5", "0{,}0668"), ("3", "0{,}00135"))]
        filas_g = VGroup(*filas).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([4.6, 0.6, 0])
        marco = Rectangle(width=3.6, height=4.3, color=INK, stroke_width=3).move_to([4.6, 0.8, 0])
        area = cola3(L, 0, 1, 0.0, 4.0, sigma0=1.0)
        marca = DashedLine(L.p(0.0, 0), L.p(0.0, 1.1), color=ESTIMACION, stroke_width=3)
        flecha_baja = Arrow([6.7, 2.2, 0], [6.7, -1.5, 0], color=ERROR, stroke_width=6, buff=0)

        def a(x):
            return cola3(L, 0, 1, x, 4.0, sigma0=1.0)

        def mueve(x0, x1):
            return marca.animate.shift(RIGHT * (L.x(x1) - L.x(x0)))

        with self.narrar("b3"):
            # «Algunos valores»
            self.en("valores")
            self.corte()
            self.play(Create(base), Create(std), Create(marco), FadeIn(enc), run_time=self.dur(0.9))

            # «Cu de cero vale un medio»
            self.en("q0")
            self.play(FadeIn(filas_g[0], shift=LEFT * 0.2), FadeIn(area), Create(marca), run_time=self.dur(0.8))

            # «la mitad de la campana»
            self.en("mitad")
            self.play(area.animate(rate_func=there_and_back).set_fill(ERROR, 0.9), run_time=self.dur(0.8))

            # «Cu de uno, cero coma dieciséis»
            self.en("q1")
            self.play(FadeIn(filas_g[1], shift=LEFT * 0.2), Transform(area, a(1.0)), mueve(0.0, 1.0),
                      run_time=self.dur(0.8))

            # «Cu de uno coma cinco»
            self.en("q15")
            self.play(FadeIn(filas_g[2], shift=LEFT * 0.2), Transform(area, a(1.5)), mueve(1.0, 1.5),
                      run_time=self.dur(0.8))
            self.play(filas_g[2].animate.set_color(AMBAR), run_time=self.dur(0.3))

            # «cero coma cero seis seis ocho»
            self.en("v0668")
            self.play(filas_g[2].animate(rate_func=there_and_back).scale(1.2), run_time=self.dur(0.7))

            # «Cu de tres, menos de dos milésimas»
            self.en("q3")
            self.play(FadeIn(filas_g[3], shift=LEFT * 0.2), Transform(area, a(3.0)), mueve(1.5, 3.0),
                      run_time=self.dur(0.8))

            # «Cuanto más lejos, más pequeña la cola»
            self.en("lejos")
            self.play(Transform(area, a(1.0)), mueve(3.0, 1.0), run_time=self.dur(0.7))
            self.play(Transform(area, a(3.4)), mueve(1.0, 3.4), run_time=self.dur(1.2))

            # «cae muy deprisa»
            self.en("deprisa")
            self.play(Create(flecha_baja), run_time=self.dur(0.7))
        self.wait(0.3)
