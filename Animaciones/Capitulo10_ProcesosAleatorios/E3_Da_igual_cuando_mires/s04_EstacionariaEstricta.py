"""Escena 04 — Estacionariedad en sentido estricto: desplazar los cortes no cambia la conjunta."""
from comun.escena import *


class EstacionariaEstricta(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        L = Lienzo(ancho=9.0, alto=3.0, t_rango=(0, 1), v_max=2.2, centro=(0, 0.6))
        pila = pila_de_curvas(L, 14, semilla=7, a=0.93, color=SENAL, opacidad=0.5, ancho=2.2, escala=0.55)
        ts = [0.2, 0.4, 0.6]
        lineas = VGroup(*[L.vertical(t, AMBAR, 3.5) for t in ts])
        cab = caja("estricta · SSS", AZUL, ancho=3.4, alto=0.7).move_to([-4.6, 3.35, 0])
        formula_c = formula(r"f(t_1,t_2,t_3)", "=", r"f(t_1{+}\alpha,\,t_2{+}\alpha,\,t_3{+}\alpha)",
                            escala=0.8).move_to([0, -2.4, 0])

        with self.narrar("b1"):
            # «La versión fuerte»
            self.en("fuerte")
            self.pop(cab)

            # «en sentido estricto»
            self.en("estricto")
            est = etiqueta("en sentido estricto", INK, 0.55).move_to([1.8, 3.35, 0])
            self.play(FadeIn(est), run_time=0.3)

            # «varios cortes del ensemble»
            self.en("cortes")
            self.play(FadeIn(pila), run_time=0.5)
            self.play(*[Create(l) for l in lineas], run_time=self.dur(0.6))

            # «desplázalos todos a la vez»
            self.en("desplaza")
            desp = 0.2 * L.ancho
            flecha_a = Arrow([float(L.x(0.2)), 2.7, 0], [float(L.x(0.4)), 2.7, 0], color=AMBAR, buff=0, stroke_width=4)
            alfa = MathTex(r"+\alpha", color=AMBAR).scale(0.8).next_to(flecha_a, UP, buff=0.08)
            self.play(lineas.animate.shift(RIGHT * desp), FadeIn(flecha_a), FadeIn(alfa), run_time=self.dur(0.9))

            # «la misma cantidad»
            self.en("cantidad")
            self.resaltar(flecha_a, alfa)

            # «la conjunta de esos cortes no cambia»
            self.en("no_cambia")
            self.play(FadeIn(formula_c[0]), run_time=0.3)
            self.play(FadeIn(formula_c[1]), FadeIn(formula_c[2]), run_time=self.dur(0.6))

            # «cualquier grupo de cortes»
            self.en("cualquier")
            self.play(lineas[0].animate.move_to(L.vertical(0.1).get_center()),
                      lineas[1].animate.move_to(L.vertical(0.55).get_center()),
                      lineas[2].animate.move_to(L.vertical(0.9).get_center()), run_time=self.dur(0.7))

            # «cualquier desplazamiento»
            self.en("desplazamiento")
            self.play(lineas.animate.shift(LEFT * 0.09 * L.ancho), run_time=self.dur(0.6))

            # «el proceso es estacionario»
            self.en("proceso")
            s = sello("SSS", VERDE).move_to([5.3, 3.3, 0])
            self.pop(s)

            # «La moneda lo es»
            self.en("moneda")
            self.play(*[FadeOut(m) for m in (pila, lineas, flecha_a, alfa, formula_c, est, cab, s)], run_time=0.3)
            tira = tira_pm1([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1], lado=0.9, escala_txt=0.6).move_to([0, -0.2, 0])
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in tira.celdas], lag_ratio=0.08), run_time=self.dur(0.9))

            # «más uno, más uno y menos uno»
            self.en("trio")
            marco = Rectangle(width=3 * 0.96 + 0.06, height=1.2, color=AMBAR, stroke_width=4)
            marco.move_to((tira.celdas[1].get_center() + tira.celdas[3].get_center()) / 2)
            self.play(Create(marco), run_time=self.dur(0.4))

            # «un octavo»
            self.en("octavo")
            oct_ = MathTex(r"\frac{1}{8}", color=AMBAR).scale(1.6).next_to(marco, UP, buff=0.35)
            self.pop(oct_)

            # «cualquier trío de tiradas seguidas»
            self.en("cualquier_trio")
            paso = tira.celdas[5].get_center() - tira.celdas[1].get_center()
            self.play(marco.animate.shift(paso), oct_.animate.shift(paso), run_time=self.dur(1.0))
        self.wait(1.0)
        self.limpiar()
