"""Escena 15 — Decodificador y tasa de error de bit: la curva del cuaderno, en canal plano y con eco."""
from comun.escena import *
from comun.figuras_lora import *


class LaCurvaDeErrores(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        self.decodificador()
        self.curva()
        self.eco()
        self.wait(1.0)
        self.limpiar()

    def decodificador(self):
        deco = bloque("Decodificador", AZUL, ancho=3.4, alto=1.0, escala=0.65).move_to([-0.6, 2.7, 0])
        v20 = Text("20", color=AMBAR, weight=BOLD).scale(1.2).move_to([-5.2, 2.7, 0])
        f1 = Arrow([-4.5, 2.7, 0], [-2.4, 2.7, 0], color=INK, stroke_width=4, buff=0)
        f2 = Arrow([1.2, 2.7, 0], [2.3, 2.7, 0], color=INK, stroke_width=4, buff=0)
        bits = fila_bits(BITS_EJEMPLO, centro=(4.6, 2.7), lado=0.5)
        ber = MathTex(r"\mathrm{BER}", "=", color=AMBAR).scale(1.6).move_to([-3.4, -0.6, 0])
        num = Text("Bits erróneos", color=ERROR, weight=BOLD).scale(0.85).move_to([1.3, 0.0, 0])
        raya = Line([-1.2, -0.6, 0], [3.8, -0.6, 0], color=TXT, stroke_width=4)
        den = Text("Bits enviados", color=TXT, weight=BOLD).scale(0.85).move_to([1.3, -1.2, 0])
        with self.narrar("b1"):
            # «el decodificador»
            self.en("deco")
            self.play(FadeIn(deco, shift=DOWN * 0.2), run_time=self.dur(0.5))
            # «del número veinte»
            self.en("veinte")
            self.pop(v20)
            self.play(GrowArrow(f1), run_time=self.dur(0.4))
            # «los siete bits»
            self.en("bits")
            self.play(GrowArrow(f2), run_time=0.3)
            self.play(LaggedStart(*[FadeIn(VGroup(c, n), shift=RIGHT * 0.1) for c, n in zip(bits.cas, bits.nums)],
                                  lag_ratio=0.12), run_time=self.dur(0.9))
            # «los bits equivocados»
            self.en("equiv")
            self.pop(num)
            # «sobre los enviados»
            self.en("sobre")
            self.play(Create(raya), FadeIn(den, shift=UP * 0.15), run_time=self.dur(0.6))
            # «la tasa de error de bit»
            self.en("ber")
            self.pop(ber)

    def curva(self):
        E = self.E = EjesXY(centro=(-2.3, -0.2), ancho=6.4, alto=5.2, x=(-12, -6), y=(1e-5, 1), log_y=True,
                            x_marcas=(-12, -10, -8, -6), y_marcas=(1, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5),
                            rot_x="SNR (dB)", rot_y="BER", escala=0.45)
        self.plano = E.curva(BER_SNR, BER_PLANO, AMBAR, 5)
        p12 = E.punto(-12, BER_PLANO[0], AMBAR, 0.13)
        p7 = E.punto(-7, BER_PLANO[5], VERDE, 0.13)
        t10 = Text("1 de cada 10", color=AMBAR, weight=BOLD).scale(0.7).move_to([4.4, 1.9, 0])
        tmil = Text("1 de cada 10.000", color=VERDE, weight=BOLD).scale(0.7).move_to([4.4, 0.8, 0])
        c5 = cota(E.p(-12, 0.45), E.p(-7, 0.45), "5 dB", TXT, UP, 0.55)
        ok = tilde(VERDE, 0.9).move_to([4.4, -0.5, 0])
        self.extras = (p12, p7, t10, tmil, c5, ok)
        with self.narrar("b2"):
            # «para muchos niveles de ruido»
            self.en("niveles")
            self.corte()
            self.play(FadeIn(E.todo), run_time=self.dur(0.7))
            # «la curva del artículo»
            self.en("curva")
            self.play(Create(self.plano, rate_func=linear), run_time=self.dur(1.2))
            # «menos doce decibelios»
            self.en("m12")
            self.pop(p12)
            # «uno de cada diez bits»
            self.en("diez")
            self.play(FadeIn(t10, shift=LEFT * 0.2), run_time=self.dur(0.5))
            # «Con menos siete»
            self.en("m7")
            self.pop(p7)
            # «uno de cada diez mil»
            self.en("mil")
            self.play(FadeIn(tmil, shift=LEFT * 0.2), run_time=self.dur(0.5))
            # «Cinco decibelios»
            self.en("cinco")
            self.play(FadeIn(c5), run_time=self.dur(0.6))
            # «casi perfecto»
            self.en("perfecto")
            self.play(Create(ok), run_time=self.dur(0.5))
            self.sfx("exito")

    def eco(self):
        E = self.E
        y0, x1, x2, u = -3.3, 3.7, 4.9, 1.5
        base = Line([3.0, y0, 0], [5.9, y0, 0], color=INK, stroke_width=2.5)
        t1 = VGroup(Line([x1, y0, 0], [x1, y0 + u * np.sqrt(0.8), 0], color=SENAL, stroke_width=6),
                    Dot([x1, y0 + u * np.sqrt(0.8), 0], radius=0.11, color=SENAL))
        t2 = VGroup(Line([x2, y0, 0], [x2, y0 + u * np.sqrt(0.2), 0], color=CIAN, stroke_width=6),
                    Dot([x2, y0 + u * np.sqrt(0.2), 0], radius=0.11, color=CIAN))
        v1 = MathTex(r"\sqrt{0{,}8}", color=SENAL).scale(0.8).next_to(t1, UP, buff=0.12)
        v2 = MathTex(r"\sqrt{0{,}2}", color=CIAN).scale(0.8).next_to(t2, UP, buff=0.12)
        eco = E.curva(BER_SNR, BER_ECO, CIAN, 5)
        fsk = Text("FSK", color=RUIDO, weight=BOLD).scale(1.0).move_to([4.55, 2.9, 0])
        igual = Text("Canal plano: FSCM = FSK", color=AMBAR, weight=BOLD).scale(0.56).move_to([4.55, 2.0, 0])
        mejor = Text("Con eco: FSCM gana", color=VERDE, weight=BOLD).scale(0.56).move_to([4.55, 1.3, 0])
        porque = Text("¿Por qué?", color=AMBAR, weight=BOLD).scale(0.95).move_to([4.55, 0.2, 0])
        with self.narrar("b3"):
            # «un canal con eco»
            self.en("eco")
            self.play(*[FadeOut(m) for m in self.extras], run_time=0.3)
            self.play(Create(base), FadeIn(t1, shift=UP * 0.2), FadeIn(t2, shift=UP * 0.2), run_time=self.dur(0.7))
            # «una segunda copia»
            self.en("copia")
            self.resaltar(t2, color=CIAN, escala=1.25, run_time=self.dur(0.6))
            # «retrasada una muestra»
            self.en("retras")
            self.play(FadeIn(v1), FadeIn(v2), run_time=self.dur(0.6))
            # «algo más de señal»
            self.en("mas")
            self.play(Create(eco, rate_func=linear), run_time=self.dur(1.3))
            # «la modulación clásica de tonos fijos»
            self.en("fsk")
            self.pop(fsk)
            # «rinden igual»
            self.en("igual")
            self.play(FadeIn(igual, shift=LEFT * 0.2), run_time=self.dur(0.5))
            # «gana con claridad»
            self.en("mejor")
            self.pop(mejor)
            # «¿Por qué?»
            self.en("porque")
            self.pop(porque)
