"""Escena 06 — Con el umbral en 1 las dos colas valen Q(1) = 0,159; lo que cuenta es la separación en desvíos."""
from comun.escena import *
from comun.figuras_c9e2 import *


class DieciseisDeCien(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.dos_colas()
        self.separacion()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def dos_colas(self):
        C = Campanas9()
        eje = C.eje(marcas=(0, 1, 2))
        c0 = C.campana(0, 1, C0)
        c1 = C.campana(2, 1, C1)
        u = umbral9(C, 1)
        cola_fa = C.area(0, 1, 1, 5)
        cola_m = C.area(2, 1, -3, 1)
        centro = Dot(C.p(0), radius=0.1, color=C0)
        h = gaussiana(1.0, 0, 1)
        sigma_l = Line(C.p(0, h), C.p(1, h), color=ESTIMACION, stroke_width=4)
        sigma_t = MathTex(r"\sigma = 1", color=ESTIMACION).scale(0.7).next_to(sigma_l, UP, buff=0.1)
        sigma_t.shift(LEFT * 0.35)
        cota_fa = cota9(C.p(0) + DOWN * 0.75, C.p(1) + DOWN * 0.75, "1 desvío")
        cota_m = cota9(C.p(1) + DOWN * 0.75, C.p(2) + DOWN * 0.75, "1 desvío")
        cuenta_fa = MathTex(r"\tfrac{1-0}{1} = 1", r"\ \to\ ", "Q(1)", color=TXT).scale(0.8).move_to([-3.6, 3.2, 0])
        v_fa = MathTex(r"=\ 0{,}159", color=ERROR).scale(0.8).next_to(cuenta_fa, RIGHT, buff=0.2)
        cuenta_m = MathTex(r"\tfrac{2-1}{1} = 1", r"\ \to\ ", "Q(1)", color=TXT).scale(0.8).move_to([-3.6, 2.3, 0])
        v_m = MathTex(r"=\ 0{,}159", color=ERROR).scale(0.8).next_to(cuenta_m, RIGHT, buff=0.2)
        espejo = cola_m.copy()
        self.planos = VGroup(eje, c0, c1, u, cola_fa, cola_m)
        self.textos = VGroup(cuenta_fa, v_fa, cuenta_m, v_m, sigma_t)
        self.extras = VGroup(centro, sigma_l, cota_fa, cota_m)

        with self.narrar("b1"):
            # «La falsa alarma»
            self.en("fa")
            self.play(FadeIn(eje), Create(c0), Create(c1), FadeIn(u), run_time=self.dur(0.8))
            self.play(FadeIn(cola_fa), run_time=self.dur(0.4))

            # «la campana del cero tiene centro cero»
            self.en("centro")
            self.play(FadeIn(centro, scale=0.4), run_time=self.dur(0.4))

            # «y desvío uno»
            self.en("desvio1")
            self.play(Create(sigma_l), FadeIn(sigma_t), run_time=self.dur(0.6))

            # «a un desvío del centro»
            self.en("undesvio")
            self.play(FadeIn(cota_fa), run_time=self.dur(0.5))

            # «Cu de uno»
            self.en("cuenta_fa")
            self.play(Write(cuenta_fa), run_time=self.dur(0.8))

            # «cero coma ciento cincuenta y nueve»
            self.en("v_fa")
            self.pop(v_fa)

            # «El fallo es una cola izquierda»
            self.en("cola_m")
            self.play(FadeIn(cola_m), run_time=self.dur(0.5))

            # «la campana es simétrica»
            self.en("simetrica")
            self.add(espejo)
            self.play(espejo.animate.flip(UP, about_point=C.p(2)), run_time=self.dur(0.8))
            self.play(FadeOut(espejo), run_time=self.dur(0.3))

            # «del dos al uno hay también un desvío»
            self.en("cuenta_m")
            self.play(FadeIn(cota_m), Write(cuenta_m), run_time=self.dur(0.8))

            # «Otra vez cero coma ciento cincuenta y nueve»
            self.en("v_m")
            self.pop(v_m)

    # ------------------------------------------------------------ b2
    def separacion(self):
        iguales = MathTex(r"p_0 = p_1 = \tfrac{1}{2}", color=TXT).scale(0.85).move_to([3.6, 3.2, 0])
        pe = MathTex(r"P_e = \tfrac12\, 0{,}159 + \tfrac12\, 0{,}159", "=", r"0{,}159", color=TXT).scale(0.8)
        pe.move_to([2.8, 2.3, 0])
        pe[2].set_color(ERROR)
        bits = rejilla3(0, centro=(-2.6, -0.2), lado=0.42)
        mucho = Text("16 %", color=ERROR, weight=BOLD).scale(1.6).move_to([3.4, -0.2, 0])

        # plano nuevo, más ancho, para poder separar las campanas hasta 6 desvíos
        C = Campanas9(centro=(0.0, -2.3), ancho=12.0, alto=7.2, r_rango=(-3.0, 9.0))
        d = ValueTracker(2.0)
        c0 = C.campana(0, 1, C0)

        def c1_viva():
            return C.campana(d.get_value(), 1, C1)

        def colas_vivas():
            m = d.get_value() / 2
            return VGroup(C.area(0, 1, m, 9), C.area(d.get_value(), 1, -3, m))

        def cota_viva():
            dv = d.get_value()
            a, b = C.p(0) + UP * 3.6, C.p(dv) + UP * 3.6
            fl = DoubleArrow(a, b, buff=0, color=INK, stroke_width=3, tip_length=0.15,
                             max_tip_length_to_length_ratio=0.35)
            t = Text(f"{dv:.0f} desvíos", color=INK).scale(0.45).next_to(fl, UP, buff=0.1)
            return VGroup(fl, t)

        base = Line(C.p(-3), C.p(9), color=INK, stroke_width=2.4)
        sep = Text("Separación medida en desvíos", color=ESTIMACION, weight=BOLD).scale(0.6).move_to([0, 3.3, 0])
        q3 = MathTex(r"Q(3) = 0{,}0013", color=ERROR).scale(0.85).move_to([4.6, 2.3, 0])

        with self.narrar("b2"):
            # «igual de frecuentes»
            self.en("iguales")
            self.play(FadeOut(self.extras), Write(iguales), run_time=self.dur(0.6))

            # «la probabilidad de error es esa misma»
            self.en("pe")
            self.play(Write(pe), run_time=self.dur(1.0))

            # «dieciséis bits mal de cada cien»
            self.en("bits")
            self.corte()
            self.play(FadeIn(bits), run_time=self.dur(0.4))
            self.play(LaggedStart(*[p.animate.set_color(ERROR) for p in bits.pts[:16]], lag_ratio=0.1),
                      run_time=self.dur(1.0))

            # «Es mucho»
            self.en("mucho")
            self.pop(mucho)

            # «a solo dos desvíos»
            self.en("dos")
            self.corte()
            c1 = always_redraw(c1_viva)
            colas = always_redraw(colas_vivas)
            cota = always_redraw(cota_viva)
            self.play(Create(base), Create(c0), FadeIn(c1), FadeIn(colas), run_time=self.dur(0.6))
            self.play(FadeIn(cota), run_time=self.dur(0.4))

            # «separación medida en desvíos»
            self.en("sep")
            self.pop(sep)

            # «Con seis desvíos entre ellas»
            self.en("seis")
            self.play(d.animate.set_value(6.0), run_time=self.dur(1.6))

            # «el umbral quedaría a tres»
            self.en("tres")
            u = Line(C.p(3), C.p(3) + UP * 3.1, color=ESTIMACION, stroke_width=4)
            c3 = cota9(C.p(0) + DOWN * 0.75, C.p(3) + DOWN * 0.75, "3 desvíos")
            self.play(Create(u), FadeIn(c3), run_time=self.dur(0.6))

            # «un bit de cada mil»
            self.en("mil")
            self.pop(q3)
        for m in (c1, colas, cota):
            m.clear_updaters()
