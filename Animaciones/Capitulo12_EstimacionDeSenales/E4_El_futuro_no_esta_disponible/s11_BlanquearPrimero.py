"""Escena 11 — La estrategia: blanquear, resolver el caso fácil y deshacer; los dos filtros tienen que ser causales."""
from comun.escena import *


class BlanquearPrimero(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        bp = self.palabra("blanquear primero", AMBAR, 0.95).move_to([0, 3.2, 0])
        g, cajas, fl = cadena_cajas(["blanquear", "resolver el fácil", "deshacer"], centro=(0, 0.8),
                                    colores=[CIAN, AMBAR, VERDE], ancho=2.9, hueco=0.8, alto=0.9, escala=0.5)
        lx = MathTex("x", color=MEDIDA).scale(0.9).move_to([-6.3, 0.8, 0])
        lx_f = flecha([-6.0, 0.8, 0], cajas[0].get_left(), INK, 3)
        leps = MathTex(r"\varepsilon", color=TXT).scale(0.8).move_to(fl[0].get_center() + UP * 0.5)
        lyh = MathTex(r"\hat y", color=ESTIMACION).scale(0.9).move_to([6.4, 0.8, 0])
        ly_f = flecha(cajas[2].get_right(), [6.0, 0.8, 0], INK, 3)
        lfil = etiqueta("un filtro", INK, 0.45).move_to(cajas[0].get_center() + DOWN * 0.7)
        tira = tira_blanca((1, -1, -1, 1, -1, 1), lado=0.4).move_to([cajas[1].get_center()[0], 2.0, 0])
        cond = self.palabra("condición", ROJO, 0.8).move_to([0, -1.9, 0])
        s1 = sello("causal", VERDE).scale(0.7).move_to(cajas[0].get_center() + DOWN * 1.4)
        s3 = sello("causal", VERDE).scale(0.7).move_to(cajas[2].get_center() + DOWN * 1.4)
        pas = flecha([-4.0, -3.3, 0], [-0.4, -3.3, 0], AZUL, 4)
        fut = flecha([4.0, -3.3, 0], [0.4, -3.3, 0], ERROR, 4)
        lpas = etiqueta("pasado", AZUL, 0.5).move_to([-2.2, -2.8, 0])
        lfut = etiqueta("futuro", ERROR, 0.5).move_to([2.2, -2.8, 0])
        x_ = cruz(ROJO, 0.9).move_to([0, -3.3, 0])
        with self.narrar("b1"):
            # «blanquear primero»
            self.en("bp")
            self.pop(bp)

            # «Convertimos lo medido en ruido blanco»
            self.en("conv")
            self.play(FadeIn(lx), GrowArrow(lx_f), FadeIn(cajas[0]), GrowArrow(fl[0]), FadeIn(leps),
                      run_time=self.dur(1.0))

            # «con un filtro»
            self.en("filtro")
            self.play(FadeIn(lfil), run_time=self.dur(0.4))

            # «Resolvemos el problema fácil»
            self.en("facil")
            self.play(FadeIn(cajas[1]), run_time=self.dur(0.5))

            # «con esa señal blanca»
            self.en("conesa")
            self.play(FadeIn(tira, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «Y deshacemos el blanqueo»
            self.en("deshace")
            self.play(GrowArrow(fl[1]), FadeIn(cajas[2]), GrowArrow(ly_f), FadeIn(lyh), run_time=self.dur(0.8))

            # «una condición»
            self.en("cond")
            self.pop(cond)

            # «el blanqueador tiene que ser causal»
            self.en("bcausal")
            self.pop(s1, sonido="impacto")

            # «su inverso»
            self.en("inverso")
            self.pop(s3, sonido="impacto")

            # «el que deshace el blanqueo»
            self.en("quedesh")
            self.resaltar(cajas[2], run_time=self.dur(0.5))

            # «mezclaríamos pasado y futuro»
            self.en("mezcla")
            self.play(GrowArrow(pas), GrowArrow(fut), FadeIn(lpas), FadeIn(lfut), run_time=self.dur(0.7))
            self.play(Create(x_), run_time=0.3)
            self.sfx("error")

        self.wait(1.0)
        self.limpiar()
