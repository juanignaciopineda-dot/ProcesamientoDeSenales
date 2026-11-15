"""Escena 03 â€” FugaAparece: un tono de 10 Hz da una raya limpia; uno de 10,5 Hz, una raya con faldas. La FFT repite el trozo."""
from comun.escena import *


class FugaAparece(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        L1 = Lienzo(ancho=5.6, alto=1.7, t_rango=(0, 1), v_max=1.2, centro=(-4.0, 2.2))
        L2 = Lienzo(ancho=5.6, alto=1.7, t_rango=(0, 1), v_max=1.2, centro=(-4.0, -1.9))
        Lf = lienzo_f(6, 15, 2.2, ancho=5.2, cx=4.1, base_y=-1.2)
        t = np.linspace(0, 1, 500)
        s10 = L1.curva(t, np.cos(2 * np.pi * 10 * t), SENAL, 3.0)
        s105 = L2.curva(t, np.cos(2 * np.pi * 10.5 * t), AMBAR, 3.0)
        lab10 = etiqueta("10 Hz", SENAL, 0.55).move_to([-0.2, 2.2, 0])
        lab105 = etiqueta("10,5 Hz", AMBAR, 0.55).move_to([-0.1, -1.9, 0])
        brace = Brace(Line(L1.p(0, -1.0), L1.p(1, -1.0)), DOWN, color=AMBAR, buff=0.05)
        un_s = etiqueta("1 s", AMBAR, 0.55).next_to(brace, DOWN, buff=0.08)
        fft = caja("FFT", AZUL, ancho=1.5, alto=0.9, scale=0.6).move_to([-0.1, 0.3, 0])
        pc = ordenador().scale(0.7).move_to([-0.1, 1.7, 0])
        ejes_f = ejes_L(Lf, 0, 1.1, x_eje=6.0)
        lab_f = etiqueta("f (Hz)", INK, 0.45).move_to(Lf.p(14.4, 0) + DOWN * 0.35)
        raya10 = Line(Lf.p(10, 0), Lf.p(10, 1.0), color=SENAL, stroke_width=8)
        r10 = etiqueta("10 Hz", SENAL, 0.5).move_to(Lf.p(10, 0) + DOWN * 0.4)
        sinc = curva_f(Lf, lambda f: sinc_abs(f, 10.5), 6, 15, AMBAR, 4.0, n=400)
        faldas_i = area_f(Lf, lambda f: sinc_abs(f, 10.5), 6, 9.5, RUIDO, 0.55, n=120)
        faldas_d = area_f(Lf, lambda f: sinc_abs(f, 10.5), 11.5, 15, RUIDO, 0.55, n=140)
        x_cruz = cruz().scale(0.9).move_to(Lf.p(14.0, 0.8))
        fl_i = flecha(Lf.p(8.9, 0.55), Lf.p(7.5, 0.55), RUIDO, 4)
        fl_d = flecha(Lf.p(12.2, 0.55), Lf.p(13.6, 0.55), RUIDO, 4)
        fl1 = flecha([-1.1, 1.0, 0], [-0.55, 0.8, 0], INK, 3)
        fl2 = flecha([0.55, 0.3, 0], [1.4, 0.3, 0], INK, 3)

        with self.narrar("b1"):
            # Â«un tono puro de diez herciosÂ»
            self.en("tono10")
            self.play(Create(L1.base()), Create(s10), FadeIn(lab10), run_time=self.dur(1.4), rate_func=linear)

            # Â«durante un segundoÂ»
            self.en("un_s")
            self.play(GrowFromCenter(brace), FadeIn(un_s), run_time=self.dur(0.7))

            # Â«con la FFTÂ»
            self.en("fft")
            self.play(FadeIn(fft, scale=0.8), GrowArrow(fl1), run_time=self.dur(0.6))

            # Â«el algoritmo que usa cualquier ordenadorÂ»
            self.en("algoritmo")
            self.play(FadeIn(pc, shift=DOWN * 0.2), run_time=self.dur(0.6))

            # Â«hacer Fourier con datosÂ»
            self.en("fourier")
            self.play(Create(ejes_f), FadeIn(lab_f), GrowArrow(fl2), run_time=self.dur(0.9))

            # Â«Sale una raya limpiaÂ»
            self.en("raya")
            self.play(Create(raya10), run_time=self.dur(0.6))

            # Â«en diez herciosÂ»
            self.en("raya10")
            self.play(FadeIn(r10), run_time=0.3)

            # Â«un tono de diez hercios y medioÂ»
            self.en("tono105")
            self.play(Create(L2.base()), Create(s105), FadeIn(lab105), run_time=self.dur(1.3), rate_func=linear)

            # Â«La raya ya no es limpiaÂ»
            self.en("sucia")
            self.play(raya10.animate.set_stroke(opacity=0.25), FadeOut(r10), Create(sinc), FadeIn(x_cruz),
                      run_time=self.dur(0.8))

            # Â«unas faldasÂ»
            self.en("faldas")
            self.play(FadeIn(faldas_i), FadeIn(faldas_d), run_time=self.dur(0.7))

            # Â«a los ladosÂ»
            self.en("lados")
            self.play(GrowArrow(fl_i), GrowArrow(fl_d), run_time=self.dur(0.5))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        L = Lienzo(ancho=13.0, alto=2.4, t_rango=(-2, 3), v_max=1.2, centro=(0, 0.1))
        f10 = copias_trozo(L, 10, color=SENAL, ancho=2.4)
        f105 = copias_trozo(L, 10.5, color=AMBAR, ancho=2.4)
        marco = Rectangle(width=float(L.x(1) - L.x(0)), height=2.9, color=AMBAR, stroke_width=3).move_to(L.p(0.5, 0))
        fft = caja("FFT", AZUL, ancho=1.5, alto=0.9, scale=0.6).move_to([0, 3.2, 0])
        uniones = VGroup(*[DashedLine(L.p(k, -1.4), L.p(k, 1.4), color=INK, stroke_width=3) for k in (0, 1)])
        lab10 = etiqueta("10 Hz", SENAL, 0.6).move_to([-5.3, 2.5, 0])
        n_ciclos = Integer(0, group_with_commas=False, color=AMBAR).scale(0.9).move_to([-0.55, -2.55, 0])
        ciclos_txt = etiqueta("ciclos", AMBAR, 0.6).next_to(n_ciclos, RIGHT, buff=0.2)
        ok = tilde().scale(1.3).move_to(L.p(1, 0) + UP * 1.75)
        lab105 = etiqueta("10,5 Hz", AMBAR, 0.6).move_to([-5.2, 2.5, 0])
        ciclos105 = etiqueta("10,5 ciclos", AMBAR, 0.6).move_to([0, -2.55, 0])
        ar_i = flecha(L.p(0.7, -1.7), L.p(0.97, -1.7), AMBAR, 4)
        ar_d = flecha(L.p(1.3, -1.7), L.p(1.03, -1.7), AMBAR, 4)
        saltos = VGroup(*[Line(L.p(k, -1), L.p(k, 1), color=ERROR, stroke_width=6) for k in (0, 1)])
        lab_salto = etiqueta("salto", ERROR, 0.6).move_to(L.p(1, 0) + UP * 1.75)

        with self.narrar("b2"):
            # Â«cÃ³mo trabaja la FFTÂ»
            self.en("trabaja")
            self.corte()
            self.pop(fft)

            # Â«trata el trozoÂ»
            self.en("trozo")
            self.play(Create(L.base()), Create(f10[2]), Create(marco), run_time=self.dur(0.9))

            # Â«se repitiera para siempreÂ»
            self.en("repite")
            self.play(LaggedStart(*[FadeIn(f10[i]) for i in (1, 3, 0, 4)], lag_ratio=0.25), run_time=self.dur(1.3))

            # Â«pegado a sÃ­ mismoÂ»
            self.en("pegado")
            self.play(Create(uniones), run_time=self.dur(0.6))

            # Â«Con diez herciosÂ»
            self.en("c10")
            self.play(FadeIn(lab10), FadeOut(marco), run_time=0.4)

            # Â«caben diez ciclos exactosÂ»
            self.en("diez_ciclos")
            self.play(FadeIn(ciclos_txt), FadeIn(n_ciclos), run_time=0.3)
            self.play(ChangeDecimalToValue(n_ciclos, 10), run_time=self.dur(1.4), rate_func=linear)

            # Â«la uniÃ³n es perfectaÂ»
            self.en("perfecta")
            self.play(uniones.animate.set_color(VERDE), FadeIn(ok, scale=0.5), run_time=self.dur(0.6))

            # Â«Con diez y medioÂ»
            self.en("c105")
            self.play(Transform(f10, f105), FadeOut(lab10), FadeIn(lab105), FadeOut(ok), run_time=self.dur(0.8))

            # Â«caben diez ciclos y medioÂ»
            self.en("ciclos_y_medio")
            self.play(FadeOut(n_ciclos), FadeOut(ciclos_txt), FadeIn(ciclos105), run_time=0.4)

            # Â«al pegar el final con el principioÂ»
            self.en("pegar")
            self.play(GrowArrow(ar_i), GrowArrow(ar_d), uniones.animate.set_color(AMBAR), run_time=self.dur(0.8))

            # Â«queda un saltoÂ»
            self.en("salto")
            self.sfx("impacto", gain=-18)
            self.play(Create(saltos), FadeOut(ar_i), FadeOut(ar_d), FadeIn(lab_salto), run_time=self.dur(0.6))

