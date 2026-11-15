"""Escena 20 — Cierre: repaso del episodio y el título del siguiente, «El sensor, de punta a punta»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "20"

    def construct(self):
        rel = reloj().scale(1.2).move_to([-5.6, 2.4, 0])
        tach = Line([-6.2, 2.0, 0], [-5.0, 2.8, 0], color=ROJO, stroke_width=7)
        izq = Line([-2.0, 2.4, 0], [0.0, 2.4, 0], color=AZUL, stroke_width=9)
        der = Line([0.0, 2.4, 0], [2.0, 2.4, 0], color=AZUL, stroke_width=9)
        izq.set_stroke(opacity=0.2)
        lm = MathTex("m", color=INK).scale(0.7).move_to([2.5, 2.4, 0])
        fr = formula(r"\frac{S_{yx}}{S_{xx}}", escala=0.9).move_to([5.4, 2.4, 0])
        tfr = tachar(fr)
        tj = tijeras().scale(0.9).move_to([-5.4, 0.2, 0])
        tj.permitir_encima = True
        tabla = Tallos([1, 0.5, 0.25], centro=(-3.2, 0.1), paso=0.7, unidad=0.7, color=ESTIMACION)
        cad, cajas, fl = cadena_cajas(["x", "1/F", "ε"], centro=(1.8, 0.2), colores=[MEDIDA, CIAN, SENAL],
                                      ancho=1.4, hueco=0.6, alto=0.8, escala=0.5)
        corch = formula(r"\bigg[\ \cdot\ \bigg]_{+}", escala=1.0, colores={0: AMBAR}).move_to([5.8, 0.2, 0])
        fh = formula("H(z)", "=", r"\frac{1}{\sigma^2 F(z)}", r"\bigg[", r"\frac{S_{yx}(z)}{F(z^{-1})}", r"\bigg]_{+}",
                     escala=1.0, colores={0: ESTIMACION, 2: COLOR_PASO[3], 3: COLOR_PASO[2], 4: COLOR_PASO[1],
                                          5: COLOR_PASO[2]}).move_to([-2.0, -1.7, 0])
        term = termometro(1.5, ROJO, 0.6).move_to([4.4, -1.7, 0])
        fin = Arrow([2.6, -2.9, 0], [6.4, -2.9, 0], color=AMBAR, stroke_width=5, buff=0)
        tit = self.palabra("El sensor, de punta a punta", AMBAR, 0.85).move_to([0, -3.6, 0])
        with self.narrar("b1"):
            # «Sin el futuro»
            self.en("sinfut")
            self.play(FadeIn(rel, scale=0.7), run_time=self.dur(0.4))
            self.play(Create(tach), run_time=0.3)

            # «solo vale en media recta»
            self.en("media")
            self.play(Create(izq), Create(der), FadeIn(lm), run_time=self.dur(0.7))

            # «ya no se puede transformar y dividir»
            self.en("nodiv")
            self.play(FadeIn(fr), run_time=self.dur(0.4))
            self.play(Create(tfr), run_time=0.3)
            self.sfx("error", gain=-18)

            # «Con mediciones blancas basta cortar»
            self.en("cortar")
            self.play(FadeIn(tabla), FadeIn(tj, scale=0.7), run_time=self.dur(0.7))

            # «se blanquean primero»
            self.en("blanq")
            self.play(FadeIn(cad), run_time=self.dur(0.8))

            # «un corchete»
            self.en("corch")
            self.play(FadeIn(corch, shift=UP * 0.1), run_time=self.dur(0.5))

            # «La fórmula ya está»
            self.en("ya")
            self.play(FadeIn(fh, shift=UP * 0.15), run_time=self.dur(0.9))

            # «Falta usarla»
            self.en("usar")
            self.play(FadeIn(term, scale=0.7), run_time=self.dur(0.5))

            # «de principio a fin»
            self.en("fin")
            self.play(GrowArrow(fin), run_time=self.dur(0.8))

            # «En el próximo episodio»
            self.en("proximo")
            self.play(Rotate(rel.minutero, angle=-PI / 2, about_point=rel.aro.get_center()), run_time=self.dur(0.8))

            # «el sensor, de punta a punta»
            self.en("titulo")
            self.pop(tit)

        self.wait(1.0)
        self.limpiar()
