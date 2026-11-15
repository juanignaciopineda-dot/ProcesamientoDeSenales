"""Escena 03 — El pico de la respiración: el espectro de la frecuencia cardíaca delata algo que no se ve."""
from comun.escena import *


def pico(w):
    w = np.asarray(w, dtype=float)
    return 0.1 + 0.85 * np.exp(-((w - 0.166) / 0.011) ** 2)


class ElPicoDeLaRespiracion(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        L1 = Lienzo(ancho=6.0, alto=1.7, t_rango=(0, 6), v_max=1.2, centro=(-3.7, 2.3))
        L2 = Lienzo(ancho=6.0, alto=1.7, t_rango=(0, 6), v_max=1.2, centro=(-3.7, -0.1))
        ecg = ecg_t(L1, latidos=6)
        fc = pulsaciones_t(L2, color=INK, ancho=3.0)
        tit1 = etiqueta("electrocardiograma", INK, 0.5).move_to([-3.7, 3.6, 0])
        tit2 = etiqueta("pulsaciones por minuto", INK, 0.5).move_to([-3.7, 1.3, 0])
        vals = VGroup(*[etiqueta(s, TXT, 0.7) for s in ("70", "68", "72")])
        for v, x in zip(vals, (-5.6, -3.7, -1.8)):
            v.move_to([x, -1.7, 0])
        t_tiempo = etiqueta("en el tiempo", INK, 0.55).move_to([-3.7, -2.9, 0])
        welch = caja("Welch", AMBAR, ancho=1.7, alto=0.9).move_to([1.4, 1.1, 0])
        a1 = flecha([-0.6, 1.1, 0], [0.5, 1.1, 0])
        a2 = flecha([2.3, 1.1, 0], [3.2, 1.1, 0])
        E = Lienzo(ancho=3.4, alto=1.8, t_rango=(0, 0.5), v_max=1.0, centro=(5.3, 1.1))
        ej = ejes_L(E, 0, 1.0)
        interr = MathTex("?", color=AMBAR).scale(1.6).move_to([5.3, 1.7, 0])
        with self.narrar("b1"):
            # «Un electrocardiograma»
            self.en("ecg")
            self.play(Create(L1.base()), FadeIn(tit1), run_time=0.4)
            self.play(Create(ecg), run_time=self.dur(1.4), rate_func=linear)

            # «los latidos del corazón»
            self.en("latidos")
            self.sfx("latido")
            self.play(ecg.animate(rate_func=there_and_back).set_stroke(width=6), run_time=0.8)

            # «frecuencia cardíaca instante a instante»
            self.en("fc")
            self.play(Create(L2.base()), FadeIn(tit2), Create(fc), run_time=self.dur(1.6), rate_func=linear)

            # «setenta, sesenta y ocho, setenta y dos»
            self.en("valores")
            self.play(LaggedStart(*[FadeIn(v, shift=DOWN * 0.2) for v in vals], lag_ratio=0.5), run_time=self.dur(1.8))

            # «Vista en el tiempo»
            self.en("tiempo")
            self.play(FadeIn(t_tiempo), run_time=0.4)

            # «sube y baja sin ningún orden»
            self.en("desorden")
            self.play(fc.animate.set_stroke(color=AMBAR, width=4.5), run_time=0.6)

            # «le estimamos la densidad espectral»
            self.en("estimamos")
            self.play(GrowArrow(a1), FadeIn(welch), run_time=self.dur(0.6))

            # «a simple vista no se ve»
            self.en("novese")
            self.play(GrowArrow(a2), Create(ej), run_time=self.dur(0.6))
            self.pop(interr)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        E = Lienzo(ancho=6.4, alto=2.8, t_rango=(0, 0.5), v_max=1.0, centro=(-3.0, 1.4))
        ej = ejes_L(E, 0, 1.05)
        lh = etiqueta("Hz", INK, 0.5).move_to(E.p(0.5, 0) + [0.35, -0.1, 0])
        pk = curva_f(E, pico, 0.0, 0.5, AMBAR, 5, n=300)
        l_hz = etiqueta("0,166 Hz", AMBAR, 0.65).move_to(E.p(0.166, 1.0) + [1.4, 0.15, 0])
        Lt = Lienzo(ancho=6.4, alto=1.3, t_rango=(0, 18), v_max=1.0, centro=(-3.0, -1.7))
        lent = lentas_t(Lt, AMBAR, 4.0, ciclos=3.0)
        formula_c = formula("1", "/", num_tex(0.166, 3), r"\approx", "6", r"\,\text{s}", escala=0.95,
                            colores={0: TXT}).move_to([4.2, 2.6, 0])
        llave = DoubleArrow(Lt.p(0, -1.0), Lt.p(6, -1.0), color=CIAN, stroke_width=4, buff=0,
                            max_tip_length_to_length_ratio=0.1, max_stroke_width_to_length_ratio=8)
        l6 = etiqueta("6 s", CIAN, 0.6).next_to(llave, DOWN, buff=0.12)
        f10 = formula("60", "/", "6", "=", "10", escala=1.0).move_to([4.2, 1.2, 0])
        porm = etiqueta("por minuto", TXT, 0.6).move_to([4.2, 0.45, 0])
        pec = pecho(CIAN).scale(0.9).move_to([4.6, -1.7, 0])
        fl = Arrow([0.6, 1.0, 0], [4.0, -0.7, 0], color=AMBAR, stroke_width=3, buff=0.1)
        with self.narrar("b2"):
            # «Un pico nítido»
            self.en("pico")
            self.corte()
            self.play(Create(ej), FadeIn(lh), run_time=0.4)
            self.play(Create(pk), run_time=self.dur(0.9))

            # «cero coma uno seis seis hercios»
            self.en("hz")
            self.pop(l_hz)

            # «Una oscilación que se repite»
            self.en("osc")
            self.play(Create(Lt.base()), Create(lent), run_time=self.dur(1.6), rate_func=linear)

            # «cada uno entre cero coma uno seis seis segundos»
            self.en("cuenta")
            self.play(FadeIn(formula_c[0:3]), run_time=self.dur(0.9))

            # «unos seis segundos»
            self.en("seis")
            self.play(FadeIn(formula_c[3:]), GrowFromCenter(llave), run_time=self.dur(0.7))
            self.play(FadeIn(l6), run_time=0.3)

            # «Diez veces por minuto»
            self.en("diez")
            self.play(FadeIn(f10), run_time=self.dur(0.8))
            self.play(FadeIn(porm), run_time=0.3)

            # «justo el ritmo al que respiraba la persona»
            self.en("pecho")
            self.play(FadeIn(pec), run_time=0.5)
            self.play(pec.pulmones.animate(rate_func=there_and_back).scale(1.3), run_time=self.dur(1.3))

            # «El espectro revela»
            self.en("revela")
            self.play(GrowArrow(fl), run_time=0.5)

            # «al respirar el corazón acelera y frena»
            self.en("acelera")
            self.play(pec.pulmones.animate(rate_func=there_and_back).scale(1.3),
                      lent.animate(rate_func=there_and_back).set_stroke(width=7), run_time=self.dur(1.2))
