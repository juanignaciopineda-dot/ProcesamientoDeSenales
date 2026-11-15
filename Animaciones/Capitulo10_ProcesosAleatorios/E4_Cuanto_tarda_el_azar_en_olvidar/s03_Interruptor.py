"""Escena 03 — Interruptor: la onda telegráfica aleatoria."""
from comun.escena import *


class Interruptor(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        L = Lienzo(ancho=8.4, alto=2.4, t_rango=(0, 6), v_max=1.3, centro=(1.5, 0.7))
        sw = interruptor().scale(1.5).move_to([-5.3, 0.7, 0])
        base = L.base()
        marcas = marcas_cambio(L, CAMBIOS, AMBAR, 0.25)
        onda = onda_tel(L, CAMBIOS, 1, AMBAR, 4.5)
        lin_p = DashedLine(L.p(0, 1), L.p(6, 1), color=INK, stroke_width=1.6, stroke_opacity=0.6)
        lin_m = DashedLine(L.p(0, -1), L.p(6, -1), color=INK, stroke_width=1.6, stroke_opacity=0.6)
        t_p = etiqueta("+1", TXT, 0.6).move_to(L.p(0, 1) + LEFT * 0.45)
        t_m = etiqueta("−1", TXT, 0.6).move_to(L.p(0, -1) + LEFT * 0.45)
        flechas = VGroup(*[DoubleArrow(L.p(a, -1.55), L.p(b, -1.55), color=INK, buff=0, stroke_width=3,
                                       max_tip_length_to_length_ratio=0.08)
                           for a, b in zip(CAMBIOS[:-1], CAMBIOS[1:])])
        contador = caja("λ = 1 cambio por segundo, de media", AMBAR, ancho=6.4, alto=0.8).move_to([1.5, -2.5, 0])
        nombre = self.palabra("onda telegráfica aleatoria", TXT, 0.95).move_to([0, 3.2, 0])

        with self.narrar("b1"):
            # «un interruptor»
            self.en("interruptor")
            self.pop(sw)

            # «en momentos al azar»
            self.en("azar")
            self.play(Create(base), run_time=0.4)
            self.play(LaggedStart(*[GrowFromCenter(m) for m in marcas], lag_ratio=0.3), run_time=self.dur(1.5))

            # «sin ningún patrón»
            self.en("patron")
            self.resaltar(marcas, color=ROJO, escala=1.05)

            # «más uno o menos uno»
            self.en("valores")
            self.play(Create(lin_p), Create(lin_m), FadeIn(t_p), FadeIn(t_m), run_time=self.dur(0.6))

            # «cambia de signo»
            self.en("cambia")
            self.play(Create(onda), *voltear(sw, False), run_time=self.dur(3.4), rate_func=linear)
            self.play(*voltear(sw, True), run_time=0.3)

            # «una vez por segundo»
            self.en("ritmo")
            self.pop(contador)

            # «sin ponerse de acuerdo»
            self.en("indep")
            self.play(LaggedStart(*[Create(f) for f in flechas], lag_ratio=0.2), run_time=self.dur(1.0))

            # «entre ellos»
            self.en("entre")
            self.resaltar(flechas, color=AMBAR, escala=1.05)

            # «onda telegráfica aleatoria»
            self.en("nombre")
            self.pop(nombre)
            self.play(onda.animate.set_stroke(width=6), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
