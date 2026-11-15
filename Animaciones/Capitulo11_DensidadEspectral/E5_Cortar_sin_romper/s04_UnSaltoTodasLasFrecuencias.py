"""Escena 04 — La fuga: un salto necesita todas las frecuencias; la raya se vuelve una sinc; los puntos de la FFT caen en sus ceros."""
from comun.escena import *


def aviso(color=AMBAR) -> VGroup:
    """Triángulo de aviso con un «!»."""
    tri = Triangle(color=color, stroke_width=5).scale(0.4)
    ex = Text("!", color=color, weight=BOLD).scale(0.5).move_to(tri.get_center() + DOWN * 0.04)
    return VGroup(tri, ex)


class UnSaltoTodasLasFrecuencias(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        Lt = Lienzo(ancho=4.8, alto=1.5, t_rango=(-1, 1), v_max=1.3, centro=(-4.2, 2.0))
        base_t = Lt.base()
        esc = traza(Lt.x([-1, 0, 0, 1]), Lt.y([0, 0, 1, 1]), SENAL, 4.0)
        tt = np.linspace(-1, 1, 400)

        def suma(K):
            v = 0.5 + (2 / np.pi) * sum(np.sin(k * np.pi * tt) / k for k in range(1, K + 1, 2))
            return Lt.curva(tt, v, SENAL, 3.0)

        barras = BarrasF(list(range(1, 13)), [1 / k for k in range(1, 13)], f_max=13, ancho=5.0, alto=1.8,
                         centro=(3.6, 2.0), color=AMBAR)
        puntos_susp = etiqueta("…", INK, 0.9).move_to([6.55, 1.5, 0])

        Lf = lienzo_f(6, 15, 2.3, ancho=10.0, cx=0.0, base_y=-1.9)
        base_f = Lf.base()
        raya = Line(Lf.p(10.5, 0), Lf.p(10.5, 1.0), color=AMBAR, stroke_width=8)
        sinc = curva_f(Lf, lambda f: sinc_abs(f, 10.5), 6, 15, AMBAR, 4.0, n=500)
        f_izq = area_f(Lf, lambda f: sinc_abs(f, 10.5), 6, 9.5, RUIDO, 0.5, n=120)
        f_der = area_f(Lf, lambda f: sinc_abs(f, 10.5), 11.5, 15, RUIDO, 0.5, n=140)
        interrog = VGroup(*[Text("?", color=RUIDO, weight=BOLD).scale(0.9).move_to(Lf.p(f, 0.55)) for f in (8.0, 13.0)])
        area_ppal = area_f(Lf, lambda f: sinc_abs(f, 10.5), 9.5, 11.5, AMBAR, 0.4, n=120)
        lab_ppal = etiqueta("lóbulo principal", AMBAR, 0.5).move_to(Lf.p(10.5, 1.0) + UP * 0.45)
        lab_lat = etiqueta("lóbulos laterales", RUIDO, 0.5).move_to(Lf.p(13.4, 0.55))
        envol = DashedVMobject(curva_f(Lf, lambda f: 1 / (np.pi * np.abs(f - 10.5)), 11.7, 15, TXT, 3.0, n=80))
        fl_i = flecha(Lf.p(9.2, 0.75), Lf.p(7.6, 0.75), RUIDO, 4)
        fl_d = flecha(Lf.p(11.8, 0.75), Lf.p(13.4, 0.75), RUIDO, 4)
        fuga = self.palabra("fuga (leakage)", AMBAR, 1.1).move_to([0, 3.3, 0])

        with self.narrar("b1"):
            # «un salto, como un escalón»
            self.en("escalon")
            self.play(Create(base_t), Create(esc), run_time=self.dur(1.0), rate_func=linear)

            # «necesita todas las frecuencias»
            self.en("todas")
            self.play(Create(barras.base), LaggedStart(*[Create(b) for b in barras.barras], lag_ratio=0.18),
                      LaggedStart(*[FadeIn(p) for p in barras.puntas], lag_ratio=0.18), FadeIn(puntos_susp),
                      run_time=self.dur(1.7))

            # «para dibujarse»
            self.en("dibuja")
            self.play(Transform(esc, suma(1)), run_time=0.6)
            self.play(Transform(esc, suma(3)), run_time=0.6)
            self.play(Transform(esc, suma(9)), run_time=self.dur(0.7))

            # «en el espectro aparece potencia»
            self.en("potencia")
            self.play(FadeOut(esc), FadeOut(base_t), FadeOut(barras), FadeOut(puntos_susp), run_time=0.3)
            self.play(Create(base_f), Create(raya), FadeIn(f_izq), FadeIn(f_der), run_time=self.dur(1.0))

            # «donde no debería haber»
            self.en("nohaber")
            self.play(FadeIn(interrog, scale=0.6), run_time=self.dur(0.5))

            # «la raya se convierte en una sinc»
            self.en("sinc")
            self.play(FadeOut(interrog), Transform(raya, sinc), run_time=self.dur(0.9))

            # «un lóbulo principal»
            self.en("principal")
            self.play(FadeIn(area_ppal), FadeIn(lab_ppal), run_time=self.dur(0.5))

            # «lóbulos laterales»
            self.en("laterales")
            self.play(FadeIn(lab_lat), run_time=self.dur(0.4))

            # «bajan muy despacio»
            self.en("despacio")
            self.play(Create(envol), run_time=self.dur(1.2))

            # «Esa potencia que se escapa a los lados»
            self.en("escapa")
            self.play(GrowArrow(fl_i), GrowArrow(fl_d), run_time=self.dur(0.6))

            # «se llama fuga»
            self.en("fuga")
            self.pop(fuga)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        Lf = lienzo_f(5, 16, 2.2, ancho=11.0, cx=0.0, base_y=-1.6)
        base = Lf.base()
        raya10 = Line(Lf.p(10, 0), Lf.p(10, 1), color=SENAL, stroke_width=8)
        lab10 = etiqueta("10 Hz", SENAL, 0.5).move_to(Lf.p(10, 0) + DOWN * 0.4)
        sinc10 = curva_f(Lf, lambda f: sinc_abs(f, 10), 5, 16, RUIDO, 3.5, n=500).set_stroke(opacity=0.5)
        sinc105 = curva_f(Lf, lambda f: sinc_abs(f, 10.5), 5, 16, AMBAR, 3.5, n=500)
        dx = float(Lf.x(10.5) - Lf.x(10))
        misma_l = etiqueta("la misma forma", INK, 0.55).move_to([4.2, 2.3, 0])
        enteros = list(range(6, 16))
        dots = VGroup(*[Dot(Lf.p(f, 0), radius=0.1, color=CIAN) for f in enteros])
        lab_pts = etiqueta("puntos de la FFT", CIAN, 0.5).move_to(Lf.p(14, 0.55))
        ceros_c = VGroup(*[Circle(radius=0.2, color=VERDE, stroke_width=4).move_to(Lf.p(f, 0)) for f in enteros if f != 10])
        ojo_ = ojo().scale(0.8).move_to([5.6, 2.4, 0])
        reales_l = etiqueta("datos reales", INK, 0.6).move_to([-4.6, 3.55, 0])
        Lr = Lienzo(ancho=3.4, alto=0.9, t_rango=(0, 1), v_max=1.0, centro=(-4.6, 2.3))
        registro = ruido_t(Lr, semilla=8, amp=0.5, color=SENAL, ancho=2.4)
        dots2 = VGroup(*[Dot(Lf.p(f + 0.37, float(sinc_abs(f + 0.37, 10))), radius=0.1, color=CIAN) for f in enteros])
        nolos = etiqueta("ya no caen en los ceros", ERROR, 0.55).move_to([3.8, 1.6, 0])
        av = aviso().move_to([-5.3, 3.2, 0])
        palabra_t = self.palabra("trampa", AMBAR, 0.9).next_to(av, RIGHT, buff=0.2)

        with self.narrar("b2"):
            # «Una trampa»
            self.en("trampa")
            self.corte()
            self.pop(av, palabra_t)

            # «en el caso de diez hercios»
            self.en("caso10")
            self.play(Create(base), Create(raya10), FadeIn(lab10), run_time=self.dur(0.7))

            # «la fuga también está»
            self.en("tambien")
            self.play(Create(sinc10), run_time=self.dur(1.2))

            # «La sinc es la misma»
            self.en("misma")
            self.play(Create(sinc105), run_time=0.6)
            self.play(sinc105.animate.shift(LEFT * dx), FadeIn(misma_l), run_time=self.dur(1.0))
            self.play(FadeOut(sinc105), run_time=0.3)

            # «solo mira el espectro en algunos puntos»
            self.en("puntos")
            self.play(FadeOut(misma_l), LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.1),
                      FadeIn(lab_pts), run_time=self.dur(1.5))

            # «esos puntos caen justo»
            self.en("justo")
            self.play(dots[enteros.index(10)].animate.move_to(Lf.p(10, 1.0)), run_time=self.dur(0.8))

            # «en los ceros de la sinc»
            self.en("ceros")
            self.play(LaggedStart(*[GrowFromCenter(c) for c in ceros_c], lag_ratio=0.1), run_time=self.dur(1.2))

            # «No es que no haya fuga»
            self.en("nohay")
            self.play(sinc10.animate.set_stroke(opacity=1.0, width=6), run_time=self.dur(0.6))

            # «no la estás mirando»
            self.en("nomiras")
            self.play(FadeIn(ojo_), Create(tachar(ojo_)), run_time=self.dur(0.6))

            # «En datos reales»
            self.en("reales")
            self.play(FadeOut(av), FadeOut(palabra_t), FadeIn(reales_l), Create(registro), run_time=self.dur(0.9),
                      rate_func=linear)

            # «esa coincidencia no ocurre nunca»
            self.en("nunca")
            self.play(FadeOut(ceros_c), Transform(dots, dots2), FadeIn(nolos), run_time=self.dur(1.0))

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        Lf = lienzo_f(5, 16, 2.0, ancho=9.0, cx=-1.2, base_y=-1.8)
        base = Lf.base()
        fuerte = Line(Lf.p(9, 0), Lf.p(9, 1), color=SENAL, stroke_width=8)
        debil = Line(Lf.p(12.5, 0), Lf.p(12.5, 0.07), color=CIAN, stroke_width=8).set_z_index(1)
        faldas = area_f(Lf, lambda f: sinc_abs(f, 9), 5, 16, RUIDO, 0.5, n=500).set_z_index(2)
        av = aviso().move_to([-3.4, 3.2, 0])
        fuga = self.palabra("fuga", AMBAR, 0.9).next_to(av, RIGHT, buff=0.2)
        interrog = Text("?", color=AMBAR, weight=BOLD).scale(0.9).move_to(Lf.p(12.5, 0.7))
        n_fuerte = etiqueta("1", SENAL, 0.6).move_to(Lf.p(9, 1.0) + UP * 0.35)
        n_debil = etiqueta("0,000001", CIAN, 0.5).move_to(Lf.p(12.5, 0.55))
        regla = VGroup(Arrow(Lf.p(16.4, 0), Lf.p(16.4, 1.15), buff=0, color=INK, stroke_width=4,
                             max_tip_length_to_length_ratio=0.1),
                       *[Line(Lf.p(16.3, v), Lf.p(16.5, v), color=INK, stroke_width=3) for v in (0.2, 0.45, 0.7, 0.95)])
        q_escala = etiqueta("¿qué escala?", AMBAR, 0.55).move_to([5.5, 2.45, 0])

        with self.narrar("b3"):
            # «La fuga es peligrosa»
            self.en("peligrosa")
            self.corte()
            self.pop(av, fuga)

            # «un tono fuerte y otro débil cerca»
            self.en("dos_tonos")
            self.play(Create(base), Create(fuerte), Create(debil), run_time=self.dur(0.8))

            # «las faldas del fuerte»
            self.en("faldas_f")
            self.play(FadeIn(faldas), run_time=self.dur(0.9))

            # «pueden tapar al débil»
            self.en("tapan")
            self.play(faldas.animate.set_fill(RUIDO, 0.92), run_time=self.dur(0.7))

            # «¿Cuánto más débil?»
            self.en("cuanto")
            self.pop(interrog)

            # «potencias tan distintas»
            self.en("distintas")
            self.play(FadeOut(interrog), FadeIn(n_fuerte), FadeIn(n_debil), run_time=self.dur(0.6))

            # «una escala adecuada»
            self.en("escala")
            self.play(Create(regla), FadeIn(q_escala), run_time=self.dur(0.8))
