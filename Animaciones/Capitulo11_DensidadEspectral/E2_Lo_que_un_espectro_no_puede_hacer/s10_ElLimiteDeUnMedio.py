"""Escena 10 — Por qué rho no pasa de un medio, y la pregunta de si el espectro positivo basta."""
from comun.escena import *


class ElLimiteDeUnMedio(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        c7 = etiqueta("capítulo 7", INK, 0.6).move_to([-3.6, 3.0, 0])
        aqui = etiqueta("aquí", INK, 0.6).move_to([-3.6, 1.8, 0])
        f1 = formula(r"|\rho|\le", "1", escala=1.2).move_to([-1.0, 3.0, 0])
        f2 = formula(r"|\rho|\le", r"\tfrac12", escala=1.2).move_to([-1.0, 1.8, 0])
        f2[1].set_color(AMBAR)
        punt = [Dot([x, -1.0, 0], radius=0.14, color=SENAL) for x in (-3.5, 0, 3.5)]
        a12 = Arrow(punt[0].get_center() + RIGHT * 0.2, punt[1].get_center() + LEFT * 0.2, color=AMBAR, buff=0, stroke_width=9,
                    max_tip_length_to_length_ratio=0.2)
        a23 = Arrow(punt[1].get_center() + RIGHT * 0.2, punt[2].get_center() + LEFT * 0.2, color=AMBAR, buff=0, stroke_width=9,
                    max_tip_length_to_length_ratio=0.2)
        arco = CurvedArrow(punt[0].get_center() + DOWN * 0.2, punt[2].get_center() + DOWN * 0.2, color=SENAL, angle=PI / 3)
        arco.set_stroke(width=5)
        se_parecen = etiqueta("se parecen", SENAL, 0.5).move_to([0, -3.0, 0])
        cero = MathTex("0", color=ROJO).scale(1.1).move_to([0, -3.0, 0])
        porque = self.palabra("¿por qué?", AMBAR, 0.9).move_to([5.0, 2.4, 0])
        with self.narrar("b1"):
            self.en("sorpresa")
            self.corte()
            self.play(FadeIn(c7), FadeIn(f1), FadeIn(aqui), run_time=0.5)
            self.en("hastauno")
            self.resaltar(f1[1], color=AMBAR, escala=1.5)
            self.en("mitad")
            self.play(Create(tachar(f1[1])), FadeIn(f2), run_time=self.dur(0.6))
            self.en("porque")
            self.pop(porque)
            self.play(FadeIn(VGroup(*punt)), run_time=0.4)
            self.en("mucho")
            self.play(Create(a12), run_time=0.5)
            self.en("esa")
            self.play(Create(a23), run_time=0.5)
            self.en("tercera")
            self.play(Create(arco), FadeIn(se_parecen), run_time=self.dur(0.8))
            self.en("dospasos")
            self.play(FadeOut(se_parecen), FadeIn(cero), run_time=0.4)
            self.play(Create(tachar(cero)), run_time=0.3)
            self.en("pedir")
            self.resaltar(a12, a23, color=AMBAR, escala=1.1)
            self.en("contradictorio")
            self.play(Flash(arco.get_center(), color=ROJO, flash_radius=0.6), run_time=0.6)
            self.sfx("error")

    def parte_b2(self):
        Pl = Lienzo(ancho=5.2, alto=2.4, t_rango=(-3.4, 3.4), v_max=2.4, centro=(-3.6, 1.0))
        Pr = Lienzo(ancho=5.2, alto=2.4, t_rango=(-3.4, 3.4), v_max=2.4, centro=(3.6, 1.0))
        el, er = ejes_L(Pl, -0.6, 2.2), ejes_L(Pr, -0.6, 2.2)
        mal = curva_f(Pl, espectro_3b(0.6), -np.pi, np.pi, ROJO, 5)
        bien = curva_f(Pr, espectro_3b(0.4), -np.pi, np.pi, AMBAR, 5)
        cr = cruz(ROJO, 0.55).move_to([-3.6, -1.4, 0])
        tl = tilde(VERDE, 0.45).move_to([3.6, -1.4, 0])
        ge0 = MathTex(r"\ge 0", color=VERDE).scale(1.0).move_to([6.0, 2.6, 0])
        bloque = RoundedRectangle(corner_radius=0.12, width=2.4, height=1.1, color=INK, stroke_width=2.5).set_fill(INK, 0.12).move_to([-0.6, -2.7, 0])
        interr = MathTex("?", color=AMBAR).scale(1.4).move_to(bloque)
        rho = MathTex(r"\rho=0{,}4", color=AMBAR).scale(0.9).move_to(bloque)
        gear = engranaje(INK).scale(0.9).move_to([1.6, -2.7, 0])
        gran = MathTex("?", color=AMBAR).scale(2.0).move_to([3.4, -2.7, 0])
        with self.narrar("b2"):
            self.en("imposible")
            self.corte()
            self.play(Create(el), Create(mal), FadeIn(cr), run_time=self.dur(0.8))
            self.en("aprueba")
            self.play(Create(er), Create(bien), FadeIn(tl), run_time=self.dur(0.8))
            self.en("positivo")
            self.pop(ge0)
            self.en("garantiza")
            self.play(FadeIn(bloque), FadeIn(interr), run_time=0.5)
            self.en("proceso04")
            self.play(ReplacementTransform(interr, rho), run_time=0.4)
            self.en("fabricar")
            self.play(FadeIn(gear), run_time=0.3)
            self.pop(gran)
