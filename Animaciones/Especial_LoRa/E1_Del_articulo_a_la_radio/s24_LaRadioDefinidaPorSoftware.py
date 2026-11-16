"""Escena 24 — Qué es una radio definida por software y cómo es por dentro el ADALM-Pluto."""
from comun.escena import *
from comun.figuras_lora import *


def _fl(a, b):
    return Arrow(a, b, color=INK, stroke_width=3, buff=0.06, max_tip_length_to_length_ratio=0.35)


class LaRadioDefinidaPorSoftware(EscenaCurso):
    ESCENA = "24"

    def construct(self):
        self.radio()
        self.transmitir()
        self.recibir()
        self.wait(1.0)
        self.limpiar()

    def radio(self):
        pc = ordenador(TXT).scale(2.4).move_to([-4.7, 0.4, 0])
        sdr = Text("SDR", color=AMBAR, weight=BOLD).scale(1.5).move_to([0, 3.0, 0])
        forma = onda_radio(pc.pantalla.get_left() + RIGHT * 0.3, pc.pantalla.get_right() + LEFT * 0.3, SENAL, 3, 0.3, 4)
        pts = VGroup(*[Dot([-2.9 + 0.5 * i, 0.6, 0], radius=0.09, color=SENAL) for i in range(7)])
        iq = MathTex("I", "+", "j", "Q", color=AMBAR).scale(1.3).move_to([-1.4, 1.5, 0])
        caja_r = RoundedRectangle(corner_radius=0.12, width=2.4, height=1.2, color=AZUL, stroke_width=3.5)
        caja_r.set_fill(AZUL, 0.15).move_to([2.2, 0.6, 0])
        onda = onda_radio([3.6, 0.6, 0], [6.7, 0.6, 0], CIAN, 5, 0.35, 4)
        pl = pluto().scale(1.1)
        pl.shift(caja_r.get_center() - pl.cuerpo.get_center())
        nom = Text("ADALM-Pluto", color=TXT, weight=BOLD).scale(0.6).move_to([2.2, -0.6, 0])
        with self.narrar("b1"):
            # «todo era simulación»
            self.en("sim")
            self.play(FadeIn(pc, shift=UP * 0.2), run_time=self.dur(0.6))
            # «una radio definida por software»
            self.en("sdr")
            self.pop(sdr)
            # «la forma de la señal»
            self.en("forma")
            self.play(Create(forma), run_time=self.dur(0.8))
            # «la decide el ordenador»
            self.en("orden")
            self.resaltar(pc.marco, color=AMBAR, escala=1.06, run_time=self.dur(0.6))
            # «calcula las muestras»
            self.en("muestras")
            self.play(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.2) for p in pts], lag_ratio=0.15), run_time=self.dur(1.0))
            # «números complejos»
            self.en("complejos")
            self.pop(iq)
            # «las convierte en una onda»
            self.en("onda")
            self.play(FadeIn(caja_r), run_time=0.3)
            self.play(Create(onda, rate_func=linear), run_time=self.dur(0.9))
            # «un Pluto»
            self.en("pluto")
            self.play(FadeOut(caja_r), FadeIn(pl), run_time=0.4)
            self.pop(nom)

    def transmitir(self):
        yt, yr = 1.9, -1.9
        self.tx = Text("TX", color=AMBAR, weight=BOLD).scale(0.9).move_to([-6.5, yt, 0])
        self.rx = Text("RX", color=CIAN, weight=BOLD).scale(0.9).move_to([-6.5, yr, 0])
        xs = (-3.6, -1.5, 1.0, 3.5)
        mk = lambda t, c, x, y, w=1.7: bloque(t, c, ancho=w, alto=0.95, escala=0.5).move_to([x, y, 0])
        iq = self.iq_tx = MathTex("I,\\,Q", color=AMBAR).scale(1.1).move_to([-5.3, yt, 0])
        cs = self.cs_tx = [mk("DAC", AMBAR, xs[0], yt), mk("Filtro", AMBAR, xs[1], yt),
                           mk("Mezclador", AMBAR, xs[2], yt, 2.2), mk("Ampl.", AMBAR, xs[3], yt)]
        ant = self.ant_tx = antena_simple(TXT, 1.2).move_to([5.7, yt + 0.3, 0])
        fl = [_fl(iq.get_right(), cs[0].get_left())] + [_fl(a.get_right(), b.get_left()) for a, b in zip(cs[:-1], cs[1:])]
        fl.append(_fl(cs[3].get_right(), [5.6, yt, 0]))
        self.osc = oscilador(VERDE, 0.42).move_to([xs[2], 0.0, 0])
        ol = self.ol = Text("OL", color=VERDE, weight=BOLD).scale(0.6).move_to([xs[2] + 0.95, 0.0, 0])
        up = Arrow(self.osc.get_top(), cs[2].get_bottom(), color=VERDE, stroke_width=3, buff=0.05,
                   max_tip_length_to_length_ratio=0.3)
        mhz = Text("905 MHz", color=VERDE, weight=BOLD).scale(0.7).move_to([xs[2] - 1.9, 0.0, 0])
        guia_t = Line([-4.6, yt, 0], [5.4, yt, 0], color=INK, stroke_width=1.5, stroke_opacity=0.25)
        guia_r = Line([-4.6, yr, 0], [5.4, yr, 0], color=INK, stroke_width=1.5, stroke_opacity=0.25)
        with self.narrar("b2"):
            # «dos caminos»
            self.en("dos")
            self.corte()
            self.play(FadeIn(self.tx), FadeIn(self.rx), Create(guia_t), Create(guia_r), run_time=self.dur(0.7))
            # «Para transmitir»
            self.en("tx")
            self.resaltar(self.tx, color=AMBAR, escala=1.3, run_time=self.dur(0.5))
            # «la parte real y la imaginaria»
            self.en("iq")
            self.pop(iq)
            # los bloques, uno por marca
            for marca, c, f in zip(("dac", "filtro", "mez"), cs[:3], fl[:3]):
                self.en(marca)
                self.play(GrowArrow(f), FadeIn(c, shift=RIGHT * 0.15), run_time=self.dur(0.5))
            # «la frecuencia de la portadora»
            self.en("porta")
            self.play(FadeIn(self.osc), FadeIn(ol), GrowArrow(up), run_time=self.dur(0.6))
            # «novecientos cinco megahercios»
            self.en("mhz")
            self.pop(mhz)
            # «Un amplificador»
            self.en("amp")
            self.play(GrowArrow(fl[3]), FadeIn(cs[3], shift=RIGHT * 0.15), run_time=self.dur(0.5))
            # «a la antena»
            self.en("antena")
            self.play(GrowArrow(fl[4]), FadeIn(ant), run_time=self.dur(0.5))

    def recibir(self):
        yt, yr = 1.9, -1.9
        xs = (-3.4, -1.0, 1.0, 3.5)
        mk = lambda t, x, w=1.7: bloque(t, CIAN, ancho=w, alto=0.95, escala=0.5).move_to([x, yr, 0])
        cs = [mk("LNA", xs[3]), mk("Mezclador", xs[2], 2.2), mk("Filtro", xs[1]), mk("ADC 12 bits", xs[0], 2.3)]
        ant = antena_simple(TXT, 1.2).move_to([5.7, yr + 0.3, 0])
        iq = MathTex("I,\\,Q", color=CIAN).scale(1.1).move_to([-5.4, yr, 0])
        fl = [_fl([5.6, yr, 0], cs[0].get_right())] + [_fl(a.get_left(), b.get_right()) for a, b in zip(cs[:-1], cs[1:])]
        fl.append(_fl(cs[3].get_left(), iq.get_right()))
        down = Arrow(self.osc.get_bottom(), cs[1].get_top(), color=VERDE, stroke_width=3, buff=0.05,
                     max_tip_length_to_length_ratio=0.3)
        p1 = Dot([-4.8, yt + 0.75, 0], radius=0.14, color=AMBAR)
        p2 = Dot([5.3, yr + 0.75, 0], radius=0.14, color=CIAN)
        aire = onda_radio([6.5, yt + 0.4, 0], [6.5, yr + 0.8, 0], TXT, 5, 0.2, 3.5)
        with self.narrar("b3"):
            # «el camino inverso»
            self.en("inv")
            self.resaltar(self.rx, color=CIAN, escala=1.3, run_time=0.4)
            self.play(FadeIn(ant), run_time=self.dur(0.4))
            # «un amplificador de bajo ruido»
            self.en("lna")
            self.play(GrowArrow(fl[0]), FadeIn(cs[0], shift=LEFT * 0.15), run_time=self.dur(0.5))
            # «baja la señal a banda base»
            self.en("baja")
            self.play(GrowArrow(fl[1]), FadeIn(cs[1], shift=LEFT * 0.15), GrowArrow(down), run_time=self.dur(0.6))
            # «el filtro»
            self.en("filtro")
            self.play(GrowArrow(fl[2]), FadeIn(cs[2], shift=LEFT * 0.15), run_time=self.dur(0.4))
            # «un conversor de doce bits»
            self.en("adc")
            self.play(GrowArrow(fl[3]), FadeIn(cs[3], shift=LEFT * 0.15), run_time=self.dur(0.5))
            # «muestras complejas»
            self.en("muestras")
            self.play(GrowArrow(fl[4]), run_time=0.3)
            self.pop(iq)
            # «entra como números»
            self.en("entra")
            self.play(FadeIn(p1), run_time=0.2)
            self.play(p1.animate.move_to([5.3, yt + 0.75, 0]), run_time=self.dur(0.9), rate_func=linear)
            # «sale como números»
            self.en("sale")
            self.play(FadeOut(p1), FadeIn(p2), run_time=0.2)
            self.play(p2.animate.move_to([-4.8, yr + 0.75, 0]), run_time=self.dur(1.2), rate_func=linear)
            # «una onda de radio»
            self.en("radio")
            self.play(FadeOut(p2), Create(aire), run_time=self.dur(0.9))
