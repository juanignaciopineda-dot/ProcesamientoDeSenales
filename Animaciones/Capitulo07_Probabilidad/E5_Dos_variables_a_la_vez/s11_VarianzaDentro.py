"""Escena 11 — Dos motivos de variación en las alturas; el primero: la varianza dentro de cada grupo."""
from comun.escena import *


class VarianzaDentro(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.al = Alturas7(centro=(-1.8, 1.0), ancho=7.4, alto=2.8)
        self.barras = BarrasVar7(origen=(-5.2, -2.7))
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        al = self.al
        base_y = al.cy - al.alto / 2
        cajas = VGroup(caja("motivo 1", AMBAR, ancho=3.0, scale=0.65), caja("motivo 2", AMBAR, ancho=3.0, scale=0.65)
                       ).arrange(DOWN, buff=0.5).move_to([4.7, 2.5, 0])
        hh = float(al.y(0.4 * gaussiana(175, 175, 7))) - 0.9
        hm = float(al.y(0.6 * gaussiana(162, 162, 6))) - 1.0
        dentro_h = DoubleArrow([float(al.x(167)), hh, 0], [float(al.x(183)), hh, 0], color=AZUL, buff=0, stroke_width=4,
                               max_tip_length_to_length_ratio=0.15)
        dentro_m = DoubleArrow([float(al.x(155)), hm, 0], [float(al.x(169)), hm, 0], color=MAGENTA, buff=0, stroke_width=4,
                               max_tip_length_to_length_ratio=0.15)
        alta, baja = persona(AZUL).scale(1.1), persona(AZUL).scale(0.7)
        pers = VGroup(alta, baja).arrange(RIGHT, buff=0.5, aligned_edge=DOWN).move_to([4.7, 0.0, 0])
        s7 = MathTex(r"\sigma_H=7\ \text{cm}", color=AZUL).scale(0.9).move_to([float(al.x(186)) + 0.1, 3.3, 0])
        s6 = MathTex(r"\sigma_M=6\ \text{cm}", color=MAGENTA).scale(0.9).move_to([float(al.x(150)) - 0.3, 3.3, 0])
        p175, p162 = Dot([float(al.x(175)), base_y, 0], radius=0.11, color=AZUL), Dot([float(al.x(162)), base_y, 0], radius=0.11, color=MAGENTA)
        entre = DoubleArrow([float(al.x(162)), base_y - 0.55, 0], [float(al.x(175)), base_y - 0.55, 0], color=AMBAR,
                            buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        contorno = Rectangle(width=81.76 * self.barras.esc, height=0.7, color=INK, stroke_width=3).move_to(
            self.barras.o + RIGHT * 81.76 * self.barras.esc / 2)
        rot_total = Text("varianza total", color=INK).scale(0.6).next_to(contorno, UP, buff=0.15)
        with self.narrar("b1"):
            # «dos motivos distintos»
            self.en("motivos")
            self.play(Create(al.base), Create(al.h), Create(al.m), run_time=self.dur(0.9), rate_func=linear)
            self.play(FadeIn(cajas, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «dentro de cada grupo»
            self.en("dentro")
            self.play(GrowFromCenter(dentro_h), GrowFromCenter(dentro_m), run_time=self.dur(0.6))
            self.resaltar(cajas[0], color=AMBAR, run_time=0.5)

            # «gente más alta y más baja»
            self.en("alta_baja")
            self.play(FadeIn(pers, shift=UP * 0.2), run_time=self.dur(0.5))

            # «Digamos que la desviación típica»
            self.en("desv")
            self.play(Indicate(dentro_h, color=AMBAR, scale_factor=1.15), Indicate(dentro_m, color=AMBAR, scale_factor=1.15), run_time=self.dur(0.8))

            # «siete centímetros en los hombres»
            self.en("s7")
            self.pop(s7)

            # «seis en las mujeres»
            self.en("s6")
            self.pop(s6)

            # «los grupos tienen medias distintas»
            self.en("medias")
            self.play(FadeOut(pers), FadeIn(p175), FadeIn(p162), run_time=self.dur(0.4))
            self.play(GrowFromCenter(entre), run_time=self.dur(0.5))
            self.resaltar(cajas[1], color=AMBAR, run_time=0.5)

            # «ciento setenta y cinco»
            self.en("h175")
            self.play(Indicate(p175, scale_factor=2.2), run_time=self.dur(0.6))

            # «ciento sesenta y dos»
            self.en("m162")
            self.play(Indicate(p162, scale_factor=2.2), run_time=self.dur(0.6))

            # «¿Cuánto aporta cada motivo»
            self.en("aporta")
            self.resaltar(cajas[0], cajas[1], color=AMBAR, escala=1.12, run_time=0.7)

            # «la varianza total»
            self.en("total")
            self.play(Create(contorno), FadeIn(rot_total), run_time=self.dur(0.6))
        self.panel = VGroup(cajas)
        self.fuera_b2 = VGroup(dentro_h, dentro_m, s7, s6, p175, p162, entre, rot_total)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        al = self.al
        bar = self.barras
        pesos = VGroup(MathTex(r"0{,}4", color=AZUL).scale(0.95).move_to([float(al.x(175)) + 0.05, 3.1, 0]),
                       MathTex(r"0{,}6", color=MAGENTA).scale(0.95).move_to([float(al.x(162)) - 0.1, 3.4, 0]))
        f1 = formula(r"0{,}4\cdot7^2", "=", r"19{,}6", escala=1.1).move_to([4.7, 2.4, 0])
        f2 = formula(r"+\,0{,}6\cdot6^2", "=", r"21{,}6", escala=1.1).move_to([4.8, 1.3, 0])
        raya = Line([2.7, 0.65, 0], [6.8, 0.65, 0], color=INK, stroke_width=2)
        f3 = MathTex(r"=\,41{,}2", color=AMBAR).scale(1.5).move_to([4.7, -0.1, 0])
        t41 = MathTex(r"41{,}2", color=TXT).scale(0.9).move_to(bar.dentro)
        rot1 = Text("dentro de cada grupo", color=ROJO).scale(0.55).next_to(bar.dentro, DOWN, buff=0.2)
        with self.narrar("b2"):
            # «El primer trozo»
            self.en("trozo1")
            self.play(FadeOut(self.panel), FadeOut(self.fuera_b2), run_time=0.3)
            self.play(FadeIn(bar.dentro, shift=RIGHT * 0.3), FadeIn(rot1), run_time=self.dur(0.7))

            # «dentro de cada grupo»
            self.en("dcg")
            self.play(Indicate(bar.dentro, color=AMBAR, scale_factor=1.1), run_time=self.dur(0.7))

            # «los pesos de los grupos»
            self.en("pesos")
            self.play(FadeIn(pesos, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «Cero coma cuatro por siete al cuadrado»
            self.en("cuenta1")
            self.play(FadeIn(f1[0], shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «diecinueve coma seis»
            self.en("r196")
            self.play(FadeIn(f1[1:], shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «Más cero coma seis por seis al cuadrado»
            self.en("cuenta2")
            self.play(FadeIn(f2[0], shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «veintiuno coma seis»
            self.en("r216")
            self.play(FadeIn(f2[1:], shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «cuarenta y uno coma dos»
            self.en("suma1")
            self.play(Create(raya), run_time=0.25)
            self.pop(f3)
            self.play(FadeIn(t41), run_time=0.3)
