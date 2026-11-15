"""Escena 05 — La energía: finita para un pulso, infinita para la onda telegráfica."""
from comun.escena import *


class LaEnergia(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        L = Lienzo(ancho=6.0, alto=1.9, t_rango=(-1, 5), v_max=1.3, centro=(-2.3, 0.0))
        pulso = L.curva([-1, 0, 0, 3, 3, 5], [0, 0, 1, 1, 0, 0], SENAL, 4)
        area = area_bajo(L, [0, 0, 3, 3], [0, 1, 1, 0], AMBAR, 0.35)
        cf = caja("Fourier", AZUL, ancho=1.9, alto=0.8).move_to([4.8, 1.6, 0])
        spec = Curva(lambda w: abs(np.sinc(w * 0.6)), x_rango=(-4, 4), y_max=1.2, ancho=3.8, alto=1.8, color=AZUL) \
            .move_to([4.8, -1.9, 0])
        with self.narrar("b1"):
            # «la energía»
            self.en("energia")
            pal = self.palabra("energía", AMBAR, 0.9).move_to([-4.6, 3.2, 0])
            self.pop(pal)

            # «En Señales y Sistemas»
            self.en("ss")
            ss = etiqueta("Señales y Sistemas", INK, 0.5).move_to([-1.0, 3.2, 0])
            self.play(FadeIn(ss), run_time=self.dur(0.4))

            # «el área bajo su cuadrado»
            self.en("area")
            x2 = formula("x^2(t)", escala=1.1).move_to([-4.6, 2.1, 0])
            self.play(Create(L.base()), Create(pulso), FadeIn(area), run_time=self.dur(1.0))
            self.play(FadeIn(x2), run_time=0.3)

            # «Un pulso que vale uno»
            self.en("pulso")
            uno = etiqueta("1", TXT, 0.6).move_to(L.p(0.0, 1.0) + UP * 0.4 + LEFT * 0.25)
            self.pop(uno)

            # «durante tres segundos»
            self.en("tres")
            dim = DoubleArrow(L.p(0, -0.5), L.p(3, -0.5), color=INK, stroke_width=3, buff=0,
                              max_tip_length_to_length_ratio=0.1)
            s3 = etiqueta("3 s", TXT, 0.55).move_to(L.p(1.5, -0.95))
            self.play(Create(dim), FadeIn(s3), run_time=self.dur(0.6))

            # «energía tres»
            self.en("e3")
            e3 = formula("E", "=", "3", escala=1.0, colores={0: AMBAR}).move_to(L.p(1.5, 0.45))
            self.pop(e3)

            # «empiezan y terminan»
            self.en("terminan")
            d1 = Dot(L.p(0, 0), radius=0.1, color=VERDE)
            d2 = Dot(L.p(3, 0), radius=0.1, color=VERDE)
            self.play(FadeIn(d1), FadeIn(d2), run_time=0.4)

            # «energía finita»
            self.en("finita")
            fin = etiqueta("energía finita", VERDE, 0.6).move_to([4.8, 3.2, 0])
            self.pop(fin)

            # «la transformada de Fourier existe»
            self.en("existe")
            a1 = flecha([1.4, 0.6, 0], [3.55, 1.6, 0])
            self.play(GrowArrow(a1), FadeIn(cf), run_time=self.dur(0.6))

            # «se puede dibujar»
            self.en("dibujar")
            self.play(Create(spec.ejes), Create(spec.grafica), run_time=self.dur(1.0))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        L = Lienzo(ancho=10.0, alto=1.8, t_rango=(0, 6), v_max=1.4, centro=(-0.4, 0.4))
        onda = onda_tel(L, color=SENAL)
        marcas = marcas_cambio(L, color=AMBAR)
        Lc = Lienzo(ancho=9.0, alto=1.0, t_rango=(0, 6), v_max=1.5, centro=(-0.9, -2.2))
        cuad = Line(Lc.p(0, 1.0), Lc.p(6, 1.0), color=AMBAR, stroke_width=5)
        rel = reloj(TXT).scale(0.8).move_to([-5.2, 2.2, 0])
        with self.narrar("b2"):
            # «un ruido estacionario»
            self.en("estac")
            self.corte()
            pal = self.palabra("estacionario", AMBAR, 0.9).move_to([-1.6, 3.3, 0])
            self.pop(pal)

            # «en el capítulo anterior»
            self.en("anterior")
            ant = etiqueta("capítulo 10", INK, 0.5).move_to([2.2, 3.3, 0])
            self.play(FadeIn(ant), run_time=self.dur(0.4))

            # «reglas no cambian con el tiempo»
            self.en("reglas")
            self.play(FadeIn(rel), run_time=0.3)
            self.play(Rotate(rel.minutero, angle=-2 * PI, about_point=rel[0].get_center()),
                      run_time=self.dur(1.5), rate_func=linear)
            nc = etiqueta("mismas reglas", TXT, 0.55).move_to([-5.2, 1.5, 0])
            self.pop(nc)

            # «la onda telegráfica»
            self.en("telegrafica")
            self.play(Create(L.base()), Create(onda), run_time=self.dur(1.4), rate_func=linear)

            # «entre más uno y menos uno»
            self.en("saltos")
            p1 = etiqueta("+1", TXT, 0.5).move_to(L.p(-0.3, 1.0))
            m1 = etiqueta("−1", TXT, 0.5).move_to(L.p(-0.3, -1.0))
            self.play(FadeIn(p1), FadeIn(m1), run_time=self.dur(0.5))

            # «al azar»
            self.en("azar")
            self.play(Create(marcas), run_time=self.dur(0.8))

            # «No empieza ni termina»
            self.en("infinita")
            ai = flecha(L.p(6, 0.0) + RIGHT * 0.1, L.p(6, 0.0) + RIGHT * 0.9, AMBAR, 4)
            self.play(GrowArrow(ai), run_time=0.4)

            # «su cuadrado vale uno»
            self.en("cuadrado")
            tx = formula("x^2(t)=1", escala=0.8).move_to([5.0, -2.2, 0])
            self.play(Create(Lc.base()), Create(cuad), run_time=self.dur(0.6))
            self.pop(tx)

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        Lc = Lienzo(ancho=10.0, alto=1.8, t_rango=(0, 10), v_max=1.5, centro=(0.0, 0.5))
        base = Lc.base()
        lab = etiqueta("energía =", TXT, 0.8).move_to([-1.2, 2.6, 0])
        cero = etiqueta("0", AMBAR, 0.9).next_to(lab, RIGHT, buff=0.25)
        with self.narrar("b3"):
            # «Hagamos la cuenta»
            self.en("cuenta")
            self.corte()
            self.play(FadeIn(lab), FadeIn(cero), Create(base), run_time=self.dur(0.5))

            # «diez segundos»
            self.en("diez")
            area_diez = Rectangle(width=float(Lc.x(4.5) - Lc.x(0)), height=Lc.alto / 3, stroke_width=0) \
                .set_fill(AMBAR, 0.4).align_to(base, DOWN).align_to(Lc.p(0, 0), LEFT)
            self.play(FadeIn(area_diez), run_time=self.dur(0.7))
            t10 = etiqueta("10 s", INK, 0.5).move_to(Lc.p(4.5, 0) + DOWN * 0.45)
            self.play(FadeIn(t10), run_time=0.3)

            # «vale diez»
            self.en("vale10")
            diez = etiqueta("10", AMBAR, 0.9).next_to(lab, RIGHT, buff=0.3)
            self.play(ReplacementTransform(cero, diez), run_time=self.dur(0.4))

            # «Al cabo de mil segundos, mil»
            self.en("mil")
            area_mil = Rectangle(width=float(Lc.x(10) - Lc.x(0)), height=Lc.alto / 3, stroke_width=0) \
                .set_fill(AMBAR, 0.4).align_to(base, DOWN).align_to(Lc.p(0, 0), LEFT)
            t1000 = etiqueta("1.000 s", INK, 0.5).move_to(Lc.p(10, 0) + DOWN * 0.45 + LEFT * 0.3)
            mil = etiqueta("1.000", AMBAR, 0.9).next_to(lab, RIGHT, buff=0.3)
            self.play(ReplacementTransform(area_diez, area_mil), ReplacementTransform(t10, t1000),
                      ReplacementTransform(diez, mil), run_time=self.dur(1.0))

            # «sigue para siempre»
            self.en("siempre")
            fl = flecha(Lc.p(10, 0.5) + RIGHT * 0.05, Lc.p(10, 0.5) + RIGHT * 0.95, AMBAR, 4)
            self.play(GrowArrow(fl), run_time=0.5)

            # «energía total es infinita»
            self.en("inf")
            inf = MathTex(r"\infty", color=AMBAR).scale(1.2).next_to(lab, RIGHT, buff=0.3)
            self.play(ReplacementTransform(mil, inf), run_time=self.dur(0.5))

            # «Una señal de energía infinita»
            self.en("sinf")
            sx = Lienzo(ancho=2.6, alto=0.9, t_rango=(0, 3), v_max=1.3, centro=(-5.2, -1.4))
            mini = onda_tel(sx, tiempos=[0.5, 1.4, 2.1], color=SENAL, ancho=3)
            ei = MathTex(r"E=\infty", color=AMBAR).scale(0.7).move_to([-5.2, -2.3, 0])
            self.play(Create(mini), FadeIn(ei), run_time=self.dur(0.7))

            # «no tiene una transformada»
            self.en("notiene")
            cf = caja("Fourier", AZUL, ancho=1.9, alto=0.8).move_to([-1.8, -1.4, 0])
            af = flecha([-3.7, -1.4, 0], [-2.85, -1.4, 0])
            xf = cruz(ROJO, 0.9).move_to([-1.8, -1.4, 0])
            self.play(GrowArrow(af), FadeIn(cf), run_time=self.dur(0.5))
            self.play(Create(xf), run_time=0.3)

            # «algo lleno de impulsos»
            self.en("impulsos")
            eje = Line([0.3, -2.6, 0], [6.6, -2.6, 0], color=INK, stroke_width=2.5)
            picos = VGroup(*[Arrow([x, -2.6, 0], [x, -2.6 + h, 0], color=AZUL, stroke_width=4, buff=0,
                                   max_tip_length_to_length_ratio=0.25)
                             for x, h in [(0.9, 1.2), (1.6, 0.6), (2.5, 1.5), (3.3, 0.8), (4.2, 1.3), (5.0, 0.5),
                                          (5.8, 1.0)]])
            self.play(Create(eje), LaggedStart(*[GrowArrow(p) for p in picos], lag_ratio=0.1),
                      run_time=self.dur(1.0))

            # «Primer camino cerrado»
            self.en("cerrado")
            x1 = cruz(ROJO, 1.2).move_to([3.5, -1.5, 0])
            self.play(Create(x1), run_time=0.3)
            self.sfx("error")
