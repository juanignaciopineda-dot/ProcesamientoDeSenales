"""Escena 12 — El segundo trozo: cuánto se dispersan las medias de los grupos alrededor de la media total."""
from comun.escena import *


class VarianzaEntre(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        al = Alturas7(centro=(-1.8, 1.0), ancho=7.4, alto=2.8)
        bar = BarrasVar7(origen=(-5.2, -2.7))
        base_y = al.cy - al.alto / 2
        yo = base_y - 0.55
        t41 = MathTex(r"41{,}2", color=TXT).scale(0.9).move_to(bar.dentro)
        bar.dentro.set_opacity(0.35)
        rot2 = Text("entre los grupos", color=VERDE).scale(0.55).next_to(bar.entre, DOWN, buff=0.2)
        p175 = Dot([float(al.x(175)), base_y, 0], radius=0.12, color=AZUL)
        p162 = Dot([float(al.x(162)), base_y, 0], radius=0.12, color=MAGENTA)
        total = al.marca(167.2, AMBAR, 5, 3.2)
        l1672 = MathTex(r"167{,}2", color=AMBAR).scale(0.85).move_to([float(al.x(167.2)), base_y - 0.45, 0])
        d78 = DoubleArrow([float(al.x(167.2)), yo - 0.45, 0], [float(al.x(175)), yo - 0.45, 0], color=AMBAR, buff=0,
                          stroke_width=4, max_tip_length_to_length_ratio=0.25)
        d52 = DoubleArrow([float(al.x(162)), yo - 0.45, 0], [float(al.x(167.2)), yo - 0.45, 0], color=AMBAR, buff=0,
                          stroke_width=4, max_tip_length_to_length_ratio=0.35)
        n78 = MathTex(r"7{,}8", color=AMBAR).scale(0.8).next_to(d78, DOWN, buff=0.12).shift(RIGHT * 0.3)
        n52 = MathTex(r"5{,}2", color=AMBAR).scale(0.8).next_to(d52, DOWN, buff=0.12).shift(LEFT * 0.3)
        f1 = formula(r"0{,}4\cdot7{,}8^2", "=", r"24{,}34", escala=1.05).move_to([4.7, 2.4, 0])
        f2 = formula(r"+\,0{,}6\cdot5{,}2^2", "=", r"16{,}22", escala=1.05).move_to([4.8, 1.3, 0])
        raya = Line([2.7, 0.65, 0], [6.8, 0.65, 0], color=INK, stroke_width=2)
        f3 = MathTex(r"=\,40{,}56", color=AMBAR).scale(1.5).move_to([4.7, -0.1, 0])
        t4056 = MathTex(r"40{,}56", color=TXT).scale(0.9).move_to(bar.entre)
        self.add(al, bar.dentro, t41)
        with self.narrar("b1"):
            # «El segundo trozo»
            self.en("trozo2")
            self.play(FadeOut(t41), run_time=0.3)

            # «las medias de los grupos»
            self.en("medias")
            self.play(FadeIn(p175), FadeIn(p162), run_time=self.dur(0.5))

            # «alrededor de la media total»
            self.en("total")
            self.play(Create(total), FadeIn(l1672), run_time=self.dur(0.7))

            # «La media de los hombres»
            self.en("hombres")
            self.resaltar(p175, color=AZUL, escala=1.8, run_time=0.5)

            # «siete coma ocho centímetros»
            self.en("d78")
            self.play(GrowFromCenter(d78), FadeIn(n78), run_time=self.dur(0.6))

            # «de ciento sesenta y siete coma dos»
            self.en("de1672")
            self.play(Indicate(l1672, scale_factor=1.5, color=TXT), run_time=self.dur(0.7))

            # «la de las mujeres»
            self.en("mujeres")
            self.resaltar(p162, color=MAGENTA, escala=1.8, run_time=0.5)

            # «cinco coma dos»
            self.en("d52")
            self.play(GrowFromCenter(d52), FadeIn(n52), run_time=self.dur(0.6))

            # «Al cuadrado y con sus pesos»
            self.en("cuadrado")
            self.play(FadeIn(f1[0], shift=LEFT * 0.2), run_time=self.dur(0.5))
            self.play(FadeIn(f2[0], shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «veinticuatro coma treinta y cuatro»
            self.en("r2434")
            self.play(FadeIn(f1[1:], shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «dieciséis coma veintidós»
            self.en("r1622")
            self.play(FadeIn(f2[1:], shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «Cuarenta coma cinco seis»
            self.en("suma2")
            self.play(Create(raya), run_time=0.25)
            self.pop(f3)
            self.play(FadeIn(bar.entre, shift=LEFT * 0.3), FadeIn(rot2), FadeIn(t4056), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
