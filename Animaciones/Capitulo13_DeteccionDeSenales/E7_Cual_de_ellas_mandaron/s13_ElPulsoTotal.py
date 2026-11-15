"""Escena 13 — El pulso total, P·H_c·conj(P·H_c) = |P|²|H_c|², es real y positivo: Nyquist se impone a |P|²."""
from comun.escena import *


class ElPulsoTotal(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        tx = caja("transmisor", SENAL, ancho=2.4, alto=0.7, scale=0.45).move_to([-4.6, 3.0, 0])
        ca = caja("canal", INK, ancho=1.8, alto=0.7, scale=0.45).move_to([-0.8, 3.0, 0])
        rx = caja("receptor", AMBAR, ancho=2.4, alto=0.7, scale=0.45).move_to([3.4, 3.0, 0])
        a1 = Arrow([-3.4, 3.0, 0], [-1.7, 3.0, 0], buff=0.05, color=INK, stroke_width=3)
        a2 = Arrow([0.1, 3.0, 0], [2.2, 3.0, 0], buff=0.05, color=INK, stroke_width=3)
        cadena = VGroup(tx, ca, rx, a1, a2)
        marco = SurroundingRectangle(VGroup(ca, rx, a2), color=AMBAR, buff=0.2, stroke_width=3)
        marco.permitir_encima = True
        t_total = etiqueta("pulso total", AMBAR, 0.5, BOLD).move_to([1.6, 1.95, 0])
        f1 = MathTex(r"P\,H_c", r"\ \overline{P\,H_c}", color=TXT).scale(1.4).move_to([-3.3, 0.75, 0])
        f1[0].set_color(SENAL)
        f1[1].set_color(AMBAR)
        f2 = MathTex("=", "|P|^2", r"\,|H_c|^2", color=TXT).scale(1.4).move_to([-3.0, -0.65, 0])
        f2[1].set_color(SENAL)
        f2[2].set_color(INK)
        pl = plano_c(centro=(4.0, -0.1), radio=1.4)
        fl = flecha_c((4.0, -0.1), 1.4, 50, AMBAR, 7)
        fl_r = flecha_c((4.0, -0.1), 1.4, 0, VERDE, 7)
        real = etiqueta("real y positivo", VERDE, 0.55, BOLD).move_to([4.0, -2.0, 0])
        pl2 = plano_c(centro=(-5.2, -2.3), radio=0.6)
        gira = flecha_c((-5.2, -2.3), 0.6, 70, AMBAR, 5)
        recuerdo = etiqueta("el filtro en frecuencia", INK, 0.45).move_to([-5.0, -3.4, 0])
        nop = MathTex("P", color=SENAL).scale(1.4).move_to([-1.4, -3.0, 0])
        tach = cruz(ERROR, 0.9).move_to(nop)
        si = MathTex("|P|^2", color=SENAL).scale(1.4).move_to([1.6, -3.0, 0])
        tilde_ = tilde(VERDE, 0.9).next_to(si, RIGHT, buff=0.3)
        txt_n = etiqueta("la condición de Nyquist se impone a", INK, 0.5).move_to([0.2, -2.35, 0])
        with self.narrar("b1"):
            # «el pulso total»
            self.en("total")
            self.play(FadeIn(cadena), Create(marco), FadeIn(t_total), run_time=self.dur(0.8))
            # «tras el canal y el receptor»
            self.en("tras")
            self.resaltar(ca, rx, run_time=0.6)
            # «pe por hache de ce»
            self.paso("pehc", f1[0], t=0.7)
            # «por su conjugado»
            self.paso("porconj", f1[1], t=0.7)
            # «el cuadrado del módulo de pe»
            self.paso("modp", f2[0], f2[1], t=0.7)
            # «por el cuadrado del módulo de hache de ce»
            self.paso("modhc", f2[2], t=0.7)
            # «Es real y positivo»
            self.en("real")
            self.play(FadeIn(pl), GrowArrow(fl), run_time=self.dur(0.8))
            # «la fase se ha cancelado»
            self.en("fase")
            self.play(Transform(fl, fl_r), FadeIn(real), run_time=self.dur(0.9))
            # «cuando leímos el filtro en frecuencia»
            self.en("recuerdo")
            self.play(FadeIn(pl2), GrowArrow(gira), FadeIn(recuerdo), run_time=self.dur(0.7))
            # «la condición de Nyquist ya no se impone al pulso enviado»
            self.en("noenviado")
            self.play(FadeIn(txt_n), FadeIn(nop), run_time=0.4)
            self.play(Create(tach), run_time=self.dur(0.5))
            # «sino a su módulo al cuadrado»
            self.en("sino")
            self.play(FadeIn(si), FadeIn(tilde_), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
