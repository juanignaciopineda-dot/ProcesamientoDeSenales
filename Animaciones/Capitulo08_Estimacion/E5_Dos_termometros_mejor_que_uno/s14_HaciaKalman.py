"""Escena 14 — Vieja + ganancia · sorpresa: cuándo la ganancia es grande y la semilla del filtro de Kalman."""
from comun.escena import *
from comun.figuras_c8e5 import *


class HaciaKalman(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        f = formula(r"\hat{y}_{\text{nueva}}", "=", r"\hat{y}_{\text{vieja}}", "+", "K", r"\cdot", r"\text{sorpresa}",
                    escala=1.1, colores={0: ESTIMACION, 2: ESTIMACION, 4: AMBAR, 6: CIAN}).move_to([0, 3.05, 0])
        pos = [(-4.6, 0.9), (-1.4, 0.9), (-1.4, -1.5), (-4.6, -1.5)]
        cajas = [caja(t, c, ancho=2.4, scale=0.5).move_to([x, y, 0])
                 for t, c, (x, y) in zip(("Estimación", "Predecir", "Sorpresa", "× Ganancia"),
                                         (ESTIMACION, INK, CIAN, AMBAR), pos)]
        kw = dict(buff=0.12, color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.2)
        flechas = [Arrow(cajas[0].get_right(), cajas[1].get_left(), **kw),
                   Arrow(cajas[1].get_bottom(), cajas[2].get_top(), **kw),
                   Arrow(cajas[2].get_left(), cajas[3].get_right(), **kw),
                   Arrow(cajas[3].get_top(), cajas[0].get_bottom(), **kw)]
        medios = [fl.get_center() for fl in flechas]
        camino = VMobject().set_points_as_corners([*medios, medios[0]])
        ficha = Dot(medios[0], radius=0.14, color=AMBAR)
        ficha.permitir_encima = True
        kf = MathTex(r"K=\frac{\text{error}}{\text{error}+\text{ruido}}", color=TXT).scale(0.9).move_to([3.9, 1.2, 0])
        kf[0][0].set_color(AMBAR)
        k1 = MathTex(r"\text{error}\gg\text{ruido}\;\Rightarrow\;K\approx 1", color=TXT).scale(0.75).move_to([3.9, -0.3, 0])
        k0 = MathTex(r"\text{error}\ll\text{ruido}\;\Rightarrow\;K\approx 0", color=TXT).scale(0.75).move_to([3.9, -1.1, 0])
        fila = VGroup(*[Square(side_length=0.42, color=MEDIDA, stroke_width=3).set_fill(MEDIDA, 0.15)
                        for _ in range(9)]).arrange(RIGHT, buff=0.16).move_to([-3.0, -3.3, 0])
        kal = Text("Filtro de Kalman", color=AMBAR, weight=BOLD).scale(0.75).move_to([3.9, -2.4, 0])
        c12 = Text("Capítulo 12", color=INK).scale(0.55).move_to([3.9, -3.1, 0])

        with self.narrar("b1"):
            # «la estimación vieja»
            self.en("vieja")
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.5))

            # «más una ganancia»
            self.en("gan")
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in range(3, 6)], run_time=self.dur(0.4))

            # «por la sorpresa»
            self.en("sorp")
            self.play(FadeIn(f[6], shift=UP * 0.1), run_time=self.dur(0.4))

            # «una de las ideas más útiles»
            self.en("util")
            self.play(LaggedStart(*[AnimationGroup(FadeIn(c), GrowArrow(fl)) for c, fl in zip(cajas, flechas)],
                                  lag_ratio=0.3), run_time=self.dur(1.4))

            # «La ganancia es grande»
            self.en("grande")
            self.play(FadeIn(kf, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «comparado con el ruido de la medición»
            self.en("comp")
            self.play(FadeIn(k1, shift=UP * 0.1), run_time=self.dur(0.5))

            # «pequeña en el caso contrario»
            self.en("peq")
            self.play(FadeIn(k0, shift=UP * 0.1), run_time=self.dur(0.5))

            # «Repetida en el tiempo»
            self.en("tiempo")
            self.play(FadeIn(ficha, scale=0.4), run_time=0.2)
            self.play(MoveAlongPath(ficha, camino), run_time=self.dur(1.3), rate_func=linear)

            # «muestra a muestra»
            self.en("muestras")
            self.play(FadeIn(fila), run_time=0.3)
            self.play(LaggedStart(*[s.animate(rate_func=there_and_back).set_fill(AMBAR, 0.8) for s in fila],
                                  lag_ratio=0.25), MoveAlongPath(ficha, camino), run_time=self.dur(1.6))

            # «el filtro de Kalman»
            self.en("kalman")
            self.pop(kal)

            # «en el capítulo doce»
            self.en("c12")
            self.play(FadeIn(c12, shift=UP * 0.1), run_time=self.dur(0.4))
        self.wait(1.0)
        self.limpiar()
