"""Escena 03 — El cajón de pilas: cada realización es una constante."""
from comun.escena import *


class CajonDePilas(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        L = Lienzo(ancho=6.0, alto=4.2, t_rango=(0, 1), v_max=3.0, centro=(2.0, 0.4))
        etiquetas = ["+1", "−2", "+2", "0"]
        pilas = VGroup(*[pila(t).scale(0.9).move_to([-6.0 + 0.85 * i + 0.5, 1.6, 0]) for i, t in enumerate(etiquetas)])
        x0 = pilas.get_center()[0]
        borde = VGroup(Line([x0 - 2.0, 2.6, 0], [x0 - 2.0, 0.95, 0]), Line([x0 - 2.0, 0.95, 0], [x0 + 2.0, 0.95, 0]),
                       Line([x0 + 2.0, 0.95, 0], [x0 + 2.0, 2.6, 0]))
        borde.set_color(INK).set_stroke(width=4)
        pilas.move_to([x0, 1.6, 0])
        rectas = rectas_pilas(L)
        rec2 = rectas[2]                      # la pila de +2

        with self.narrar("b1"):
            # «Un cajón lleno de pilas»
            self.en("cajon")
            self.play(Create(borde), LaggedStart(*[FadeIn(p, shift=DOWN * 0.3) for p in pilas], lag_ratio=0.15),
                      run_time=self.dur(1.2))

            # «un poco distinto»
            self.en("distinto")
            self.play(*[p.etiqueta.animate.set_color(AMBAR) for p in pilas], run_time=0.4)

            # «El experimento»
            self.en("exp")
            exp = self.palabra("experimento", AMBAR, 0.6).move_to([-4.0, 3.4, 0])
            self.pop(exp)

            # «sacas una al azar»
            self.en("saca")
            p = pilas[2]
            self.play(p.animate.move_to([-5.6, -0.6, 0]), run_time=self.dur(0.9))
            volt = VGroup(Circle(radius=0.42, color=CIAN, stroke_width=4).set_fill(FONDO, 1),
                          Text("V", color=CIAN, weight=BOLD).scale(0.6)).move_to([-3.6, -0.6, 0])
            cable = Line([-5.3, -0.6, 0], [-4.02, -0.6, 0], color=INK, stroke_width=3)
            self.play(FadeIn(volt), Create(cable), run_time=0.4)

            # «durante una hora»
            self.en("hora")
            r = reloj().scale(0.9).move_to([-4.6, -2.3, 0])
            self.play(FadeIn(r), Create(L.base()), run_time=0.3)
            self.play(Rotate(r.minutero, angle=-2 * PI, about_point=r.aro.get_center()),
                      run_time=self.dur(1.6), rate_func=linear)

            # «una línea recta»
            self.en("recta")
            self.play(Create(rec2.set_color(AMBAR).set_stroke(width=6)), run_time=self.dur(1.2), rate_func=linear)

            # «no cambia»
            self.en("nocambia")
            t_cte = etiqueta("constante", AMBAR, 0.6, BOLD).move_to(L.p(0.5, 2.0) + UP * 0.45)
            self.play(FadeIn(t_cte), run_time=0.4)

            # «Cada realización es una constante»
            self.en("cte")
            self.resaltar(rec2, escala=1.0)

            # «cada pila da una constante diferente»
            self.en("varias")
            otras = VGroup(rectas[0], rectas[1], rectas[3])
            self.play(FadeOut(t_cte), *[Create(o) for o in otras], run_time=self.dur(1.0))

            # «medidos respecto del nominal»
            self.en("nominal")
            nom = DashedLine(L.p(0, 0), L.p(1, 0), color=INK, stroke_width=2)
            tn = etiqueta("nominal", INK, 0.45).move_to(L.p(0.92, 0) + DOWN * 0.3)
            self.play(Create(nom), FadeIn(tn), run_time=0.5)

            # «media cero»
            self.en("media")
            mu = MathTex(r"\mu=0", color=AMBAR).scale(0.9).move_to([-1.5, 0.4, 0])
            self.pop(mu)

            # «varianza cuatro»
            self.en("var")
            llave = BraceBetweenPoints(L.p(1.0, -2), L.p(1.0, 2), color=AMBAR).shift(RIGHT * 0.05)
            sg = MathTex(r"\sigma^2=4", color=AMBAR).scale(0.75).next_to(llave, RIGHT, buff=0.1)
            self.play(Create(llave), FadeIn(sg), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
