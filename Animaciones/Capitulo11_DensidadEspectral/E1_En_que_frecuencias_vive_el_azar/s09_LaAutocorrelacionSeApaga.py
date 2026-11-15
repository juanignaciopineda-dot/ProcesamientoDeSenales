"""Escena 09 — La autocorrelación de la telegráfica: e^(−2|τ|), una curva que sí se apaga."""
from comun.escena import *


class LaAutocorrelacionSeApaga(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        Lp = Lienzo(ancho=5.2, alto=1.6, t_rango=(0, 1), v_max=1.5, centro=(-3.7, 1.0))
        pila = pila_de_curvas(Lp, 6, semilla=8, a=0.9, color=SENAL, opacidad=0.6, ancho=2.4, escala=0.5)
        Lt = Lienzo(ancho=5.2, alto=1.2, t_rango=(0, 6), v_max=1.5, centro=(3.7, 1.0))
        tele = onda_tel(Lt, color=SENAL, ancho=3.5)
        marcas = marcas_cambio(Lt, color=AMBAR)
        P = MathTex("P", "=", "R_{xx}(0)", "=", "1", color=TXT).scale(1.0).move_to([3.8, 3.3, 0])
        P[0].set_color(AMBAR)
        c = Curva(autocorr_tele, x_rango=(-2, 2), y_max=1.2, ancho=5.0, alto=2.2, color=AMBAR, x_label=r"\tau") \
            .move_to([3.2, -2.0, 0])
        F = formula("R_{xx}(\\tau)", "=", "e^{-2|\\tau|}", escala=1.1, colores={0: AMBAR}).move_to([-3.4, -1.5, 0])
        with self.narrar("b1"):
            # «la potencia esperada»
            self.en("esperada")
            pe = self.palabra("potencia esperada", AMBAR, 0.75).move_to([-3.6, 3.3, 0])
            self.pop(pe)
            self.play(FadeIn(P[0]), run_time=0.3)

            # «la autocorrelación en cero»
            self.en("encero")
            self.play(FadeIn(P[1:3]), run_time=self.dur(0.5))

            # «es estacionario»
            self.en("estac")
            self.play(Create(Lp.base()), LaggedStart(*[Create(c_) for c_ in pila], lag_ratio=0.1),
                      run_time=self.dur(1.2), rate_func=linear)

            # «da igual en qué instante»
            self.en("igual")
            corte = Lp.vertical(0.15, AMBAR, 3.5)
            self.play(Create(corte), run_time=0.3)
            self.play(corte.animate.shift(RIGHT * float(Lp.x(0.85) - Lp.x(0.15))), run_time=self.dur(1.6))

            # «Para la onda telegráfica»
            self.en("paratele")
            self.play(Create(Lt.base()), Create(tele), run_time=self.dur(0.9), rate_func=linear)

            # «si salta en promedio una vez por segundo»
            self.en("salta")
            self.play(Create(marcas), run_time=self.dur(0.8))

            # «e elevado a menos dos»
            self.en("exp")
            self.play(FadeIn(F[0:2]), run_time=0.3)
            self.play(FadeIn(F[2]), run_time=self.dur(0.7))

            # «el valor absoluto de tau»
            self.en("abs")
            va = etiqueta("valor absoluto", INK, 0.5).move_to([-3.4, -2.7, 0])
            ar = flecha([-2.4, -2.45, 0], [-2.0, -1.9, 0], INK, 3)
            self.play(FadeIn(va), GrowArrow(ar), run_time=self.dur(0.5))

            # «En cero vale uno»
            self.en("uno")
            self.play(Create(c.ejes), FadeIn(c.etiquetas), run_time=self.dur(0.4))
            self.play(Create(c.grafica), run_time=self.dur(0.9))
            self.play(FadeIn(c.punto(0)), run_time=0.3)

            # «la potencia que contamos a mano»
            self.en("mano")
            self.play(FadeIn(P[3:]), run_time=self.dur(0.6))
            self.resaltar(P, color=AMBAR)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        c = Curva(autocorr_tele, x_rango=(-2, 2), y_max=1.2, ancho=7.0, alto=3.0, color=AMBAR, x_label=r"\tau") \
            .move_to([-1.2, -0.7, 0])
        Lt = Lienzo(ancho=8.0, alto=1.0, t_rango=(0, 8), v_max=1.5, centro=(0.0, 3.1))
        tele = onda_tel(Lt, tiempos=[0.7, 1.2, 2.6, 3.1, 3.9, 5.0, 6.3, 7.1], color=SENAL, ancho=3.5)
        cf = caja("Fourier", AZUL, ancho=1.9, alto=0.9).move_to([5.1, -0.6, 0])
        with self.narrar("b2"):
            # «la forma de esa curva»
            self.en("forma")
            self.corte()
            self.play(Create(c.ejes), FadeIn(c.etiquetas), Create(c.grafica), run_time=self.dur(1.2))

            # «A medio segundo»
            self.en("medio")
            p1 = c.punto(0.5)
            self.play(FadeIn(p1), run_time=0.3)

            # «cero coma tres siete»
            self.en("t37")
            l1 = etiqueta("0,37", AMBAR, 0.6).move_to(c.ejes.c2p(0.5, 0.368) + UR * 0.45)
            self.pop(l1)

            # «a un segundo»
            self.en("uno_s")
            p2 = c.punto(1.0)
            self.play(FadeIn(p2), run_time=0.3)

            # «cero coma uno cuatro»
            self.en("t14")
            l2 = etiqueta("0,14", AMBAR, 0.6).move_to(c.ejes.c2p(1.0, 0.135) + UR * 0.45)
            self.pop(l2)

            # «sigue bajando hacia cero»
            self.en("baja")
            fl = flecha(c.ejes.c2p(1.4, 0.3), c.ejes.c2p(1.9, 0.04), AMBAR, 3)
            self.play(GrowArrow(fl), run_time=0.4)

            # «La señal no se apaga nunca»
            self.en("nunca")
            self.play(Create(Lt.base()), Create(tele), run_time=self.dur(1.2), rate_func=linear)

            # «su autocorrelación sí»
            self.en("si")
            self.resaltar(c.grafica, color=AMBAR)

            # «área finita»
            self.en("area")
            self.play(FadeIn(c.area(-2, 2, AMBAR, 0.35)), run_time=self.dur(0.7))

            # «transformada de Fourier»
            self.en("fourier")
            a = flecha([2.5, -0.6, 0], [4.1, -0.6, 0])
            self.play(GrowArrow(a), FadeIn(cf), run_time=self.dur(0.6))

            # «Ahí está la salida»
            self.en("salida")
            a2 = flecha([2.5, -0.6, 0], [4.1, -0.6, 0], VERDE, 4)
            sa = etiqueta("salida", VERDE, 0.6).move_to([5.1, -1.5, 0])
            self.play(Transform(a, a2), run_time=0.3)
            self.pop(sa, sonido="exito")
