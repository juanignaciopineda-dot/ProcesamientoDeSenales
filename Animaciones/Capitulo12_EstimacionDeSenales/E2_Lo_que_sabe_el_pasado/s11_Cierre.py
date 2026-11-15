"""Escena 11 — Cierre: resumen y anuncio del E3, «Mirar el registro entero»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        uno = self.palabra("1", AMBAR, 1.3).move_to([-5.8, 1.9, 0])
        dos = self.palabra("2", AMBAR, 1.3).move_to([-5.8, -1.2, 0])
        B = barras_error([0.8, 0.74, 0.7387, 0.7386, 0.7386], ["1", "2", "3", "5", "10"], centro=(-0.8, 1.9),
                         ancho=6.0, alto=2.0, v_max=1.0)
        y_lin = B.base.get_center()[1] + 0.7386 * 2.0
        linea = DashedLine([-3.8, y_lin, 0], [2.2, y_lin, 0], color=AMBAR, stroke_width=3)
        lim = MathTex(r"0{,}7386", color=AMBAR).scale(0.91).move_to([3.7, y_lin, 0])
        F = FilaMuestras([r"x[n-1]", r"x[n]"], centro=(-2.5, -1.2), lado=1.62, color=MEDIDA, escala=0.75)
        sinc = Text("correlación = 0", color=ERROR).scale(0.65).next_to(F.cas[0], DOWN, buff=0.3)
        flecha_l = CurvedArrow(F.cas[0].get_top() + UP * 0.05, F.cas[1].get_top() + UP * 0.05, angle=-PI / 2.5,
                               color=VERDE, stroke_width=4, tip_length=0.18)
        limp = Text("limpia la pista", color=VERDE).scale(0.65).move_to([1.8, -1.2, 0])
        ep3 = Text("Episodio 3", color=INK).scale(0.91).move_to([0, 1.4, 0])
        tit = self.palabra("Mirar el registro entero", AMBAR, 1.1).move_to([0, 0.2, 0])
        tira = VGroup(*[Square(side_length=0.5, color=INK, stroke_width=2).set_fill(AMBAR, 0.15) for _ in range(17)])
        tira.arrange(RIGHT, buff=0.06).move_to([0, -1.4, 0])
        div = MathTex(r"H", "=", r"\frac{S_{yx}}{S_{xx}}", color=TXT).scale(1.3).move_to([0, -2.9, 0])
        div[0].set_color(ESTIMACION)
        lim.permitir_fuera = True

        with self.narrar("b1"):
            # «Nos llevamos dos ideas»
            self.en("dos")
            self.pop(uno, dos)
            # «Más pasado baja el error cada vez menos»
            self.en("menos")
            self.play(FadeIn(B), run_time=self.dur(0.7))
            # «cero coma siete tres ocho seis»
            self.en("limite")
            self.play(Create(linea), FadeIn(lim), run_time=0.6)
            # «una muestra que no se parece en nada»
            self.en("nada")
            self.play(FadeIn(F), FadeIn(sinc), run_time=0.5)
            # «si ayuda a limpiar otra»
            self.en("limpiar")
            self.play(Create(flecha_l), FadeIn(limp), run_time=0.6)
            # «En el próximo episodio»
            self.en("proximo")
            self.corte()
            self.play(FadeIn(ep3), run_time=0.4)
            # «Mirar el registro entero»
            self.en("titulo")
            self.pop(tit)
            self.play(FadeIn(tira), run_time=0.5)
            # «esa división»
            self.en("division")
            self.play(FadeIn(div), run_time=0.5)
        self.wait(1.0)
        self.limpiar()
