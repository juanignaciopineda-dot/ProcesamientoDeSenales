"""Escena 06 — El tercer valor es ge; el retardo; el filtro adaptado."""
from comun.escena import *


class ElRetardo(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        cas = CasillasSalida13(5, centro=(0, 0.2), lado=0.95)
        vals = [cas.poner(i, str(v), TXT, 0.8) for i, v in enumerate(SAL13)]
        marco = SurroundingRectangle(cas.cas[2], color=AMBAR, buff=0.06)
        ge = formula("g", "=", "10", escala=1.3, colores={2: AMBAR}).move_to([0, 2.3, 0])
        n2 = MathTex("n=2", color=AMBAR).scale(0.8).move_to(cas.c(2) + UP * 0.95)
        bl = BloqueLTI("h", centro=(-3.7, 3.0), ancho=1.3, alto=0.9, color=ESTIMACION, largo=0.9, escala=0.7)
        r = Tallos(R13, centro=(-6.15, 3.0), paso=0.35, unidad=0.14, color=MEDIDA)
        a_ini, a_fin = cas.c(0) + DOWN * 1.15, cas.c(2) + DOWN * 1.15
        retardo = DoubleArrow(a_ini, a_fin, color=AMBAR, buff=0, stroke_width=4, tip_length=0.2)
        t_ret = etiqueta("retardo de 2 muestras", AMBAR, 0.5).move_to([0, -1.7, 0])
        nota_l = etiqueta("el libro: h[k] = s[−k], se muestrea en 0", INK, 0.5).move_to([0, -2.6, 0])
        rl = reloj().scale(0.9).move_to([5.3, -2.0, 0])
        pal = self.palabra("filtro adaptado", AMBAR, 1.0).move_to([0, -3.5, 0])
        self.add(cas, *vals)
        with self.narrar("b1"):
            # «el tercer valor: diez»
            self.en("tercero")
            self.play(Create(marco), run_time=0.4)
            self.resaltar(vals[2], color=AMBAR, escala=1.5)

            # «el ge que calculamos antes»
            self.en("ge")
            self.pop(ge)

            # «en el instante dos»
            self.en("instante")
            self.play(FadeIn(n2, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «ya ha entrado en el filtro»
            self.en("entrado")
            self.play(FadeIn(bl), FadeIn(r), run_time=self.dur(0.5))
            self.play(r.animate.shift(RIGHT * 1.2), run_time=self.dur(0.8))

            # «un retardo de dos muestras»
            self.en("retardo")
            self.play(Create(retardo), FadeIn(t_ret), run_time=self.dur(0.7))

            # «sin retardo»
            self.en("sinret")
            self.play(FadeIn(nota_l), run_time=self.dur(0.5))

            # «el reloj corrido»
            self.en("reloj")
            self.play(FadeIn(rl), run_time=0.3)
            self.play(Rotate(rl.minutero, angle=-PI / 2, about_point=rl.aro.get_center()), run_time=self.dur(0.8))

            # «filtro adaptado a la señal»
            self.en("adaptado")
            self.pop(pal)
        self.wait(1.0)
        self.limpiar()
