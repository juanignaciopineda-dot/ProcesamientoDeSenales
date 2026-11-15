"""Escena 09 — Cauchy-Schwarz otra vez: X no baja de −E y la igualdad es la señalización antipodal."""
from comun.escena import *


class LaCotaDeCauchySchwarz(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        f_x = MathTex("X", "=", "s_0", r"\cdot", "s_1", color=TXT).scale(1.3).move_to([-3.8, 3.2, 0])
        f_x[0].set_color(AMBAR)
        f_x[2].set_color(AZUL_C7)
        f_x[4].set_color(SENAL)
        e = MathTex("E_0=E_1=E", color=AMBAR).scale(1.2).move_to([-3.8, 2.3, 0])
        cota = MathTex("X", r"\ge", "-E", color=TXT).scale(1.5).move_to([-3.8, 1.2, 0])
        cota[0].set_color(AMBAR)
        cota[2].set_color(AMBAR)
        sgn = MathTex("s_1", "=", "-s_0", color=TXT).scale(1.3).move_to([-3.8, -0.1, 0])
        sgn[0].set_color(SENAL)
        sgn[2].set_color(AZUL_C7)
        pa = pulso7([2, 2, 1], centro=(-6.0, -1.15), color=AZUL_C7, paso=0.55, unidad=0.2)
        pb = pulso7([-2, -2, -1], centro=(-6.0, -1.65), color=SENAL, paso=0.55, unidad=0.2)
        anti = self.palabra("antipodal", AMBAR, 1.0).move_to([-3.3, -1.6, 0])
        # recta numérica de X
        y_r = -3.0
        recta = Line([-6.4, y_r, 0], [-0.3, y_r, 0], color=INK, stroke_width=2)
        cero = MathTex("0", color=INK).scale(0.8).move_to([-0.9, y_r - 0.4, 0])
        tope = Line([-5.4, y_r - 0.25, 0], [-5.4, y_r + 0.25, 0], color=AMBAR, stroke_width=5)
        menos_e = MathTex("-E", color=AMBAR).scale(0.9).move_to([-5.4, y_r - 0.5, 0])
        punto = Dot([-3.2, y_r, 0], radius=0.13, color=SENAL)
        xr = MathTex("X", color=SENAL).scale(0.9).move_to([-3.2, y_r + 0.45, 0])
        interr = Text("?", color=AMBAR, weight=BOLD).scale(1.0).move_to([-6.2, y_r + 0.5, 0])
        # panel de la parábola
        panel = RoundedRectangle(corner_radius=0.15, width=5.4, height=3.0, color=INK, stroke_width=2,
                                 stroke_opacity=0.5).move_to([3.8, 0.4, 0])
        vez = etiqueta("cuarta vez", AMBAR, 0.6, BOLD).move_to([3.8, 3.3, 0])
        par = parabola_l(centro=(3.8, 0.2), ancho=4.4, alto=2.4, fondo=0.0)
        t_cs = etiqueta("Cauchy-Schwarz", AMBAR, 0.6).move_to([3.8, 2.55, 0])
        c1 = MathTex("X^2", r"\le", "E\\cdot E", "=E^2", color=TXT).scale(1.2).move_to([3.8, -1.6, 0])
        with self.narrar("b1"):
            # «Equis es la suma de una señal por la otra»
            self.paso("equis", f_x, t=0.7)
            # «las dos tienen la misma energía»
            self.paso("energia", e, t=0.6)
            # «¿Hasta dónde puede bajar?»
            self.en("bajar")
            self.play(FadeIn(recta), FadeIn(cero), FadeIn(punto), FadeIn(xr), FadeIn(interr), run_time=self.dur(0.6))
            # «Aquí aparece»
            self.paso("aparece", panel, t=0.5)
            # «por última vez en el capítulo»
            self.paso("ultima", vez, t=0.5)
            # «Cauchy-Schwarz»
            self.en("cs")
            self.play(FadeIn(t_cs), Create(par.eje), Create(par.curva), run_time=self.dur(0.9))
            # «equis al cuadrado no supera»
            self.paso("cuadrado", c1[0], c1[1], t=0.6)
            # «la energía por la energía»
            self.paso("ee", c1[2], c1[3], t=0.6)
            # «equis no baja de menos la energía»
            self.en("cota")
            self.play(FadeIn(cota), FadeIn(tope), FadeIn(menos_e), FadeOut(interr), run_time=self.dur(0.7))
            # «llega justo ahí»
            self.en("justo")
            self.play(punto.animate.move_to([-5.4, y_r, 0]), xr.animate.move_to([-5.4, y_r + 0.45, 0]),
                      run_time=self.dur(0.9))
            # «la otra con el signo cambiado»
            self.paso("signo", sgn, pa, pb, t=0.7)
            # «señalización antipodal»
            self.en("antipodal")
            self.pop(anti)
        self.wait(1.0)
        self.limpiar()
