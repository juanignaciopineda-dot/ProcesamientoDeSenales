"""Escena 10 — Interpolación, no información: los ceros no cambian la curva de fondo; para qué sí sirve rellenar; la resolución se compra con tiempo."""
from comun.escena import *


class InterpolacionNoInformacion(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        x64 = datos_dos_tonos(64)
        fp, Xp = espectro_fft(x64, 2000)
        f64, X64 = espectro_fft(x64, 0)
        nrm = Xp.max()
        m = (fp >= 7) & (fp <= 14)
        Lt = Lienzo(ancho=7.6, alto=1.6, t_rango=(0, 1), v_max=2.2, centro=(-3.0, 2.8))
        Lf = lienzo_f(7, 14, 1.7, ancho=8.0, cx=-2.2, base_y=-3.2, v_max=1.0)
        base_f = Lf.base()
        stems = VGroup(*[VGroup(Line(Lf.p(f, 0), Lf.p(f, X64[f] / nrm), color=CIAN, stroke_width=4),
                                Dot(Lf.p(f, X64[f] / nrm), radius=0.08, color=CIAN)) for f in range(7, 15)])
        datos = VGroup(*[Dot(Lt.p(k / 64, x64[k]), radius=0.05, color=SENAL) for k in range(64)])
        base_t = Lt.base()
        fondo = Lf.curva(fp[m], Xp[m] / nrm, INK, 4.0)
        cand = candado(AMBAR).scale(0.8).move_to([4.8, -1.6, 0])
        marco = SurroundingRectangle(datos, color=AMBAR, buff=0.12, stroke_width=3)
        lab_v = etiqueta("ventana de 64", AMBAR, 0.55).move_to([-3.0, 3.75, 0])
        ceros_row = VGroup(*[Dot([float(Lt.x(1.0)) + 0.1 + 0.12 * i, Lt.cy, 0], radius=0.035, color=INK) for i in range(46)])
        lab_c = etiqueta("ceros", INK, 0.55).move_to([4.0, 3.4, 0])
        masp = VGroup(*[Dot(Lf.p(f, float(np.interp(f, fp, Xp) / nrm)), radius=0.05, color=AMBAR)
                        for f in np.linspace(7.05, 13.95, 60)])
        interp = self.palabra("interpolación, no información", AMBAR, 0.9).move_to([-0.6, 0.45, 0])
        lab_fft = etiqueta("f (Hz)", INK, 0.45).move_to(Lf.p(13.6, 0) + DOWN * 0.35)

        with self.narrar("b1"):
            # «la FFT mira el espectro en algunos puntos»
            self.en("mira")
            self.play(Create(base_f), FadeIn(lab_fft), LaggedStart(*[FadeIn(s) for s in stems], lag_ratio=0.1),
                      run_time=self.dur(1.6))

            # «Con sesenta y cuatro muestras»
            self.en("c64")
            self.play(Create(base_t), LaggedStart(*[FadeIn(d, scale=0.3) for d in datos], lag_ratio=0.02),
                      run_time=self.dur(1.5))

            # «el espectro que hay debajo»
            self.en("debajo")
            self.play(Create(fondo), run_time=self.dur(1.5), rate_func=linear)

            # «ya está decidido»
            self.en("decidido")
            self.pop(cand)

            # «una ventana de sesenta y cuatro»
            self.en("v64")
            self.play(Create(marco), FadeIn(lab_v), run_time=self.dur(0.8))

            # «Los ceros no son datos»
            self.en("nodatos")
            self.play(LaggedStart(*[FadeIn(d, scale=0.3) for d in ceros_row], lag_ratio=0.03), FadeIn(lab_c),
                      run_time=self.dur(1.2))

            # «no cambian esa curva»
            self.en("nocambia")
            self.play(fondo.animate(rate_func=there_and_back).set_stroke(width=8), run_time=self.dur(0.9))

            # «la mire en más puntos»
            self.en("masp")
            self.play(LaggedStart(*[FadeIn(d, scale=0.3) for d in masp], lag_ratio=0.03), run_time=self.dur(1.8))

            # «interpolación, no información»
            self.en("interp")
            self.pop(interp)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        Lf = lienzo_f(7, 14, 2.2, ancho=7.0, cx=-3.3, base_y=-2.4, v_max=1.1)
        base = Lf.base()
        kern = lambda f0: curva_f(Lf, lambda f: nucleo_lin("rect", f - f0), 7, 14, SENAL, 4.0, n=500)
        un_pico = kern(10.3)
        pico105 = kern(10.5)
        marca = DashedLine(Lf.p(10.3, 0), Lf.p(10.3, 1.0), color=AMBAR, stroke_width=3)
        dos = curva_f(Lf, lambda f: nucleo_lin("rect", f - 10.0) + nucleo_lin("rect", f - 10.6), 7, 14, SENAL, 4.0, n=500)
        sub = [(10, float(nucleo_lin("rect", 0.5))), (11, float(nucleo_lin("rect", 0.5)))]
        stems = VGroup(*[VGroup(Line(Lf.p(f, 0), Lf.p(f, v), color=CIAN, stroke_width=4),
                                Dot(Lf.p(f, v), radius=0.09, color=CIAN)) for f, v in sub])
        techo = DashedLine(Lf.p(9.2, 1.0), Lf.p(11.8, 1.0), color=AMBAR, stroke_width=3)
        lab_real = etiqueta("altura real", AMBAR, 0.5).move_to(Lf.p(10.5, 1.0) + UP * 0.45)
        circulos = VGroup(*[Circle(radius=0.22, color=VERDE, stroke_width=4).move_to(Lf.p(f, v)) for f, v in sub])
        dos_l = VGroup(DashedLine(Lf.p(10, 0), Lf.p(10, 1.0), color=SENAL, stroke_width=3),
                       DashedLine(Lf.p(10.6, 0), Lf.p(10.6, 1.0), color=SENAL, stroke_width=3))
        ceros_txt = self.palabra("ceros", AMBAR, 1.0).move_to([-3.3, 3.0, 0])
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.5).next_to(ceros_txt, RIGHT, buff=0.3)
        ok_q = tilde().scale(1.0).move_to(q)
        x0 = 1.0
        item1 = VGroup(tilde(VERDE).scale(0.8), etiqueta("ubicar un pico único", TXT, 0.55))
        item2 = VGroup(tilde(VERDE).scale(0.8), etiqueta("no subestimar su altura", TXT, 0.55))
        item3 = VGroup(cruz(ERROR).scale(0.8), etiqueta("separar dos picos", TXT, 0.55))
        for g, y in ((item1, 2.0), (item2, 0.8), (item3, -0.4)):
            g[0].move_to([x0 + 0.3, y, 0])
            g[1].move_to([x0 + 0.8 + g[1].width / 2, y, 0])

        with self.narrar("b2"):
            # «¿Entonces rellenar con ceros no sirve?»
            self.en("pregunta")
            self.corte()
            self.pop(ceros_txt, q)

            # «Sí sirve»
            self.en("sirve")
            self.play(FadeOut(q), FadeIn(ok_q, scale=0.5), run_time=self.dur(0.5))

            # «ubicar con más precisión un pico»
            self.en("ubicar")
            self.play(Create(base), Create(un_pico), Create(marca), run_time=self.dur(1.2))

            # «que ya sabes que es único»
            self.en("unico")
            self.play(FadeIn(item1[0], scale=0.5), FadeIn(item1[1]), run_time=self.dur(0.6))

            # «no subestimar su altura»
            self.en("altura")
            self.play(Transform(un_pico, pico105), FadeOut(marca), FadeIn(stems), Create(techo), FadeIn(lab_real),
                      FadeIn(item2[0], scale=0.5), FadeIn(item2[1]), run_time=self.dur(1.2))

            # «entre dos puntos de la FFT»
            self.en("entre")
            self.play(GrowFromCenter(circulos), run_time=self.dur(0.7))

            # «Lo que no hace nunca»
            self.en("nunca")
            self.play(FadeIn(item3[0], scale=0.5), run_time=self.dur(0.5))

            # «separar dos cosas»
            self.en("separar")
            self.play(FadeOut(stems), FadeOut(circulos), FadeOut(techo), FadeOut(lab_real), FadeIn(item3[1]),
                      Create(dos_l), run_time=self.dur(0.8))

            # «que la ventana ya fundió»
            self.en("fundio")
            self.play(Transform(un_pico, dos), run_time=self.dur(1.0))

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        reloj_ = reloj().scale(1.0).move_to([-3.0, 2.2, 0])
        mon = moneda("t").scale(0.8).move_to([-1.4, 2.2, 0])
        cartel = caja("resolución", AMBAR, ancho=3.2, alto=1.0, scale=0.65).move_to([2.2, 2.2, 0])
        fl = flecha([-0.8, 2.2, 0], [0.5, 2.2, 0], INK, 4)
        piezas = fichas(["trozos", "ventana", "restar la media", "promedio"], AMBAR, ancho=2.8, alto=0.8,
                        escala=0.5, buff=0.3, direccion=RIGHT, encendidas=True).move_to([0, -0.3, 0])
        hueco = DashedVMobject(RoundedRectangle(corner_radius=0.15, width=7.5, height=1.2, color=AMBAR, stroke_width=4)
                               .move_to([0, -2.7, 0]))
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.5).move_to([0, -2.7, 0])
        flechas = VGroup(*[flecha(p.get_bottom() + DOWN * 0.1, [p.get_center()[0] * 0.5, -2.0, 0], INK, 3) for p in piezas])

        with self.narrar("b3"):
            # «la resolución solo se compra con tiempo grabado»
            self.en("compra")
            self.corte()
            self.play(FadeIn(reloj_, scale=0.7), FadeIn(mon, scale=0.7), GrowArrow(fl), FadeIn(cartel, scale=0.8),
                      run_time=self.dur(1.2))

            # «Y con esto ya tenemos»
            self.en("tenemos")
            self.play(reloj_.animate.scale(0.7), mon.animate.scale(0.7), cartel.animate.scale(0.8), run_time=self.dur(0.6))

            # «todas las piezas»
            self.en("piezas")
            self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.2) for p in piezas], lag_ratio=0.2), run_time=self.dur(1.2))

            # «el método que se usa de verdad»
            self.en("metodo")
            self.play(Create(hueco), FadeIn(flechas), run_time=self.dur(0.8))
            self.pop(q)
