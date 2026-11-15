"""Escena 04 — De las monedas a las muestras y vuelta, con w = 1, 2."""
from comun.escena import *


class MonedasYMuestras(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        yw, yx = 1.7, 0.2
        c1, c2 = -1.4, 1.0
        r_w = MathTex(r"w:", color=SENAL).scale(0.9).move_to([-3.4, yw, 0])
        r_x = MathTex(r"x:", color=MEDIDA).scale(0.9).move_to([-3.4, yx, 0])
        w1 = MathTex("1", color=SENAL).scale(1.1).move_to([c1, yw, 0])
        w2 = MathTex("2", color=SENAL).scale(1.1).move_to([c2, yw, 0])
        x1 = MathTex("1", color=MEDIDA).scale(1.1).move_to([c1, yx, 0])
        x2 = MathTex(r"2{,}6", color=MEDIDA).scale(1.1).move_to([c2, yx, 0])
        cuenta = MathTex(r"0{,}6\cdot 1+2", color=TXT).scale(0.8).move_to([c2, -0.9, 0])
        flecha_v = Arrow([c2 + 0.9, yx + 0.2, 0], [c2 + 0.9, yw - 0.2, 0], color=AMBAR, buff=0, stroke_width=5,
                         max_tip_length_to_length_ratio=0.25)
        resta = formula(r"2{,}6-0{,}6\cdot 1", "=", "2", escala=0.85, colores={2: ERROR}).move_to([4.4, 1.0, 0])
        oculta(resta)
        bq = caja_tex(r"1-0{,}6\,z^{-1}", AMBAR, ancho=3.4, alto=0.9, escala=0.8).move_to([4.4, -0.7, 0])
        l_bq = etiqueta("blanqueador · Cap. 11", INK, 0.5).next_to(bq, DOWN, buff=0.25)
        flecha_i = Arrow([-0.2, yw - 0.2, 0], [-0.2, yx + 0.2, 0], color=AZUL, buff=0, stroke_width=5,
                         max_tip_length_to_length_ratio=0.25)

        with self.narrar("b1"):
            # «Veámoslo con números»
            self.en("numeros")
            self.corte()
            self.play(FadeIn(r_w), FadeIn(r_x), run_time=self.dur(0.5))

            # «las monedas fueron uno y dos»
            self.en("monedas")
            self.pop(w1, w2)

            # «las muestras son uno»
            self.en("x1")
            self.pop(x1)

            # «cero coma seis por uno más dos»
            self.en("cuenta")
            self.play(FadeIn(cuenta, shift=UP * 0.2), run_time=self.dur(0.7))

            # «dos coma seis»
            self.en("x2")
            self.pop(x2)

            # «Al revés»
            self.en("reves")
            self.play(GrowArrow(flecha_v), run_time=self.dur(0.5))

            # «dos coma seis menos cero coma seis por uno»
            self.en("resta")
            self.add(resta)
            self.play(*revelar(resta[0]), run_time=self.dur(0.8))

            # «vale dos»
            self.en("vale2")
            self.play(*revelar(resta[1], resta[2]), run_time=self.dur(0.5))

            # «la moneda»
            self.en("lamoneda")
            self.play(w2.animate.set_color(VERDE), run_time=self.dur(0.4))
            self.resaltar(w2, color=VERDE)

            # «el blanqueador del capítulo once»
            self.en("blanq")
            self.play(FadeIn(bq), FadeIn(l_bq), run_time=self.dur(0.6))

            # «se recuperan las monedas»
            self.en("recup")
            self.play(flecha_v.animate.set_color(VERDE), run_time=self.dur(0.4))
            self.resaltar(flecha_v, color=VERDE)

            # «de las monedas»
            self.en("ida")
            self.play(GrowArrow(flecha_i), run_time=self.dur(0.5))

        self.wait(1.0)
        self.limpiar()
