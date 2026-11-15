"""Escena 09 — Encuesta: ¿rellenar con ceros separa dos tonos? No: la curva sale suave, pero sigue siendo un solo bulto."""
from comun.escena import *


class EncuestaDeLosCeros(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        # datos: 64 muestras de dos tonos a 10 y 10,6 Hz (con fs = 64 Hz); y 256 muestras de lo mismo
        x64 = datos_dos_tonos(64)
        x256 = datos_dos_tonos(256)
        fp, Xp = espectro_fft(x64, 2000)
        nrm = Xp.max()
        f64, X64 = espectro_fft(x64, 0)
        f256, X256 = espectro_fft(x256, 2000)
        nrm256 = X256.max()

        self.Lt = Lienzo(ancho=7.6, alto=1.6, t_rango=(0, 1), v_max=2.2, centro=(-3.0, 2.8))
        self.Lf = lienzo_f(7, 14, 1.7, ancho=8.0, cx=-2.2, base_y=-3.2, v_max=1.0)
        Lt, Lf = self.Lt, self.Lf
        m = (fp >= 7) & (fp <= 14)

        self.datos = VGroup(*[Dot(Lt.p(k / 64, x64[k]), radius=0.05, color=SENAL) for k in range(64)])
        self.base_t = Lt.base()
        self.ceros_row = VGroup(*[Dot([float(Lt.x(1.0)) + 0.1 + 0.12 * i, Lt.cy, 0], radius=0.035, color=INK)
                                  for i in range(46)])
        self.base_f = Lf.base()
        self.stems = VGroup(*[VGroup(Line(Lf.p(f, 0), Lf.p(f, X64[f] / nrm), color=CIAN, stroke_width=4),
                                     Dot(Lf.p(f, X64[f] / nrm), radius=0.08, color=CIAN)) for f in range(7, 15)])
        self.curva = Lf.curva(fp[m], Xp[m] / nrm, AMBAR, 3.5)
        self.lab_f = etiqueta("f (Hz)", INK, 0.45).move_to(Lf.p(13.6, 0) + DOWN * 0.35)
        self.fft = caja("FFT", AZUL, ancho=1.5, alto=0.8, scale=0.6).move_to([-2.2, 0.35, 0])
        self.fl_a = flecha([-2.2, 1.8, 0], [-2.2, 0.8, 0], INK, 3)
        self.fl_b = flecha([-2.2, -0.05, 0], [-2.2, -1.1, 0], INK, 3)

        self.bloque1()
        self.bloque2(x256, f256, X256, nrm256, Lf)
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        Lt = self.Lt
        self.lab_cerc = lab_cerc = etiqueta("dos tonos muy cercanos", TXT, 0.55).move_to([-3.0, 3.75, 0])
        lab_cer = etiqueta("+ 2.000 ceros", INK, 0.55).move_to([4.0, 3.4, 0])
        fin = DashedLine([float(Lt.x(1.0)), 1.9, 0], [float(Lt.x(1.0)), 3.7, 0], color=AMBAR, stroke_width=3)
        pers = persona(AZUL).scale(0.9).move_to([5.9, -1.2, 0])
        globo = burbuja_dialogo(ancho=3.1, alto=1.0).move_to([4.6, 0.3, 0])
        txt_globo = etiqueta("añade ceros", TXT, 0.5).move_to(globo.globo.get_center())
        si = caja("sí", AZUL, ancho=1.5, alto=0.8, scale=0.6).move_to([3.4, 0.7, 0])
        no = caja("no", AZUL, ancho=1.5, alto=0.8, scale=0.6).move_to([5.4, 0.7, 0])
        pregunta = etiqueta("¿dos picos?", TXT, 0.6).move_to([4.4, 1.7, 0])
        contador = Integer(3, group_with_commas=False, color=AMBAR).scale(1.0).move_to([4.4, -0.7, 0])
        self.si, self.no = si, no
        self.cuenta = contador
        self.pregunta = pregunta
        self.lab_cer = lab_cer

        with self.narrar("b1"):
            # «sesenta y cuatro muestras»
            self.en("m64")
            self.play(Create(self.base_t), LaggedStart(*[FadeIn(d, scale=0.3) for d in self.datos], lag_ratio=0.02),
                      run_time=self.dur(1.3))

            # «dos tonos muy cercanos»
            self.en("cercanos")
            self.play(FadeIn(lab_cerc), run_time=self.dur(0.5))

            # «unos pocos puntos con un solo bulto»
            self.en("bulto")
            self.play(GrowArrow(self.fl_a), FadeIn(self.fft), run_time=0.5)
            self.play(Create(self.base_f), FadeIn(self.lab_f), GrowArrow(self.fl_b), run_time=0.5)
            self.play(LaggedStart(*[FadeIn(s) for s in self.stems], lag_ratio=0.1), run_time=self.dur(1.2))

            # «Alguien te sugiere»
            self.en("alguien")
            self.play(FadeIn(pers, shift=LEFT * 0.3), FadeIn(globo), FadeIn(txt_globo), run_time=self.dur(0.7))

            # «añadir dos mil ceros»
            self.en("ceros")
            self.play(LaggedStart(*[FadeIn(d, scale=0.3) for d in self.ceros_row], lag_ratio=0.03), FadeIn(lab_cer),
                      run_time=self.dur(1.2))

            # «al final de los datos»
            self.en("final")
            self.play(Create(fin), run_time=self.dur(0.6))

            # «volver a calcular la FFT»
            self.en("recalcula")
            self.resaltar(self.fft, run_time=0.6)

            # «muchos más puntos»
            self.en("mas_puntos")
            self.play(Create(self.curva), run_time=self.dur(1.5), rate_func=linear)

            # «¿Aparecerán los dos picos?»
            self.en("encuesta")
            self.play(FadeOut(pers), FadeOut(globo), FadeOut(txt_globo), run_time=0.3)
            self.play(FadeIn(pregunta), FadeIn(si), FadeIn(no), run_time=self.dur(0.6))

            # «Piénsalo»
            self.en("piensa")
            self.play(FadeIn(contador), run_time=0.2)
            self.play(ChangeDecimalToValue(contador, 1), run_time=self.dur(1.3), rate_func=linear)

    # ---------------------------------------------------------------- b2
    def bloque2(self, x256, f256, X256, nrm256, Lf):
        Lt = self.Lt
        m = (f256 >= 7) & (f256 <= 14)
        verde = Lf.curva(f256[m], X256[m] / nrm256, VERDE, 4.0)
        t = np.linspace(0, 1, 256)
        reg256 = traza(np.linspace(-6.8, 6.8, 256), 2.8 + 0.3 * x256, SENAL, 2.2)
        lab256 = etiqueta("256 muestras", SENAL, 0.55).move_to([-3.0, 3.75, 0])
        elipse = Ellipse(width=1.6, height=1.7, color=AMBAR, stroke_width=4).move_to(Lf.p(10.3, 0.5))
        suave_l = etiqueta("suave y completa", AMBAR, 0.5).move_to([-5.4, -0.9, 0])
        marca10 = DashedLine(Lf.p(10, 0), Lf.p(10, 1.0), color=INK, stroke_width=3)
        marca106 = DashedLine(Lf.p(10.6, 0), Lf.p(10.6, 1.0), color=INK, stroke_width=3)
        l10 = etiqueta("10 Hz", INK, 0.45).move_to(Lf.p(9.6, 0) + DOWN * 0.35)
        l106 = etiqueta("10,6 Hz", INK, 0.45).move_to(Lf.p(11.2, 0) + DOWN * 0.35)

        with self.narrar("b2"):
            # «No»
            self.en("no")
            self.tachon = tachar(self.si)
            self.play(self.no[0].animate.set_stroke(VERDE, 5), Create(self.tachon), FadeOut(self.cuenta),
                      run_time=self.dur(0.6))

            # «La curva sale mucho más suave»
            self.en("suave")
            self.play(self.curva.animate.set_stroke(width=6), run_time=self.dur(0.7))

            # «bonita y completa»
            self.en("bonita")
            self.play(FadeIn(suave_l), run_time=self.dur(0.6))

            # «sigue siendo un solo bulto»
            self.en("unbulto")
            self.play(Create(elipse), run_time=self.dur(0.7))

            # «en lugar de ceros»
            self.en("enlugar")
            self.play(FadeOut(self.ceros_row), FadeOut(self.lab_cer), FadeOut(self.datos), FadeOut(self.base_t),
                      FadeOut(self.stems), FadeOut(self.pregunta), FadeOut(self.si), FadeOut(self.no), FadeOut(self.tachon),
                      FadeOut(suave_l), FadeOut(self.lab_cerc), run_time=0.4)

            # «doscientas cincuenta y seis muestras de verdad»
            self.en("m256")
            self.play(Create(reg256), FadeIn(lab256), run_time=self.dur(1.5), rate_func=linear)

            # «aparecen dos picos»
            self.en("dos_picos")
            self.play(FadeOut(elipse), Create(verde), run_time=self.dur(1.2))

            # «justo en las dos frecuencias»
            self.en("frecs")
            self.play(Create(marca10), Create(marca106), FadeIn(l10), FadeIn(l106), run_time=self.dur(0.7))
