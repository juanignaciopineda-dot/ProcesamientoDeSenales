"""Escena 05 — El giro del prior: el mismo dato, otras probabilidades, otra decisión."""
from comun.escena import *

COLS = [SENAL, AZUL_C7, CIAN]
YS = [1.5, 0.3, -0.9]


class ElGiroDelPrior(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        g_ini = [r"g_0=1{,}4", r"g_1=1{,}6", r"g_2=-0{,}6"]
        gs = [MathTex(g_ini[i], color=COLS[i]).scale(1.25).move_to([-5.0, YS[i], 0]) for i in range(3)]
        giro = self.palabra("giro", AMBAR, 1.0).move_to([0, 3.2, 0])
        corona_v = corona(VERDE).scale(0.7).next_to(gs[1], RIGHT, buff=0.3)
        pr = [MathTex(f"P(H_{i})", color=AMBAR).scale(1.15).move_to([-1.5, YS[i], 0]) for i in range(3)]
        val = [MathTex(r"=\tfrac{1}{2}", color=AMBAR).scale(1.15).next_to(pr[0], RIGHT, buff=0.1),
               MathTex(r"=\tfrac{1}{4}", color=AMBAR).scale(1.15).next_to(pr[1], RIGHT, buff=0.1),
               MathTex(r"=\tfrac{1}{4}", color=AMBAR).scale(1.15).next_to(pr[2], RIGHT, buff=0.1)]
        h_suma = MathTex(r"+\ln P(H_i)", color=AMBAR).scale(1.0).move_to([2.1, 2.7, 0])
        h_resta = MathTex(r"-\tfrac{E_i}{2}=-1", color=SENAL).scale(1.0).move_to([5.4, 2.7, 0])
        res = [MathTex(r"1{,}4-0{,}69-1=-0{,}29", color=TXT).scale(1.0),
               MathTex(r"1{,}6-1{,}39-1=-0{,}79", color=TXT).scale(1.0),
               MathTex(r"-0{,}6-1{,}39-1=-2{,}99", color=TXT).scale(1.0)]
        for i in range(3):
            res[i].move_to([3.6, YS[i], 0])
        antes = etiqueta("antes: gana 1", INK, 0.6).move_to([-3.3, -2.5, 0])
        ahora = etiqueta("ahora: gana 0", VERDE, 0.6, BOLD).move_to([1.0, -2.5, 0])
        flecha_c_ = Arrow([-1.4, -2.5, 0], [-0.7, -2.5, 0], buff=0, color=INK, stroke_width=4,
                          max_tip_length_to_length_ratio=0.35)
        prior_pesa = etiqueta("el prior pesa si la evidencia está reñida", AMBAR, 0.6).move_to([0, -3.4, 0])
        with self.narrar("b1"):
            # «Ahora un giro»
            self.en("giro")
            self.play(FadeIn(gs[0]), FadeIn(gs[1]), FadeIn(gs[2]), FadeIn(corona_v), run_time=0.6)
            self.pop(giro)
            # «la primera señal es la más probable»
            self.paso("probable", pr[0], t=0.5)
            # «un medio»
            self.en("medio")
            self.pop(val[0])
            # «las otras, un cuarto»
            self.paso("cuarto", pr[1], pr[2], val[1], val[2], t=0.6)
            # «le sumamos el logaritmo de su prior»
            self.paso("suma", h_suma, t=0.6)
            # «le restamos la energía entre dos, uno»
            self.paso("resta", h_resta, t=0.6)
            # «menos cero coma veintinueve»
            self.paso("r0", res[0], t=0.6)
            # «menos cero coma setenta y nueve»
            self.paso("r1", res[1], t=0.6)
            # «menos dos coma noventa y nueve»
            self.paso("r2", res[2], t=0.6)
            # «¡Ahora gana la primera!»
            self.en("ganaprimera")
            self.sfx("exito")
            self.play(res[0].animate.set_color(VERDE), corona_v.animate.next_to(gs[0], RIGHT, buff=0.3),
                      run_time=self.dur(0.7))
            # «Mismo dato, otra decisión»
            self.en("mismodato")
            self.play(FadeIn(antes), GrowArrow(flecha_c_), FadeIn(ahora), run_time=self.dur(0.8))
            # «pesa cuando la evidencia está reñida»
            self.paso("renida", prior_pesa, t=0.6)
        self.wait(1.0)
        self.limpiar()
