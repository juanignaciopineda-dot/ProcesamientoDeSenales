"""Escena 01 — Gancho: un dado, un cable y un bit caben en una sola curva."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        d = dado().scale(1.7).move_to([-4.2, 1.3, 0])
        L = Lienzo(ancho=3.4, alto=1.8, t_rango=(0, 1), v_max=1.5, centro=(0, 1.3))
        t = np.linspace(0, 1, 120)
        cable = VGroup(L.base(), L.curva(t, 0.45 * np.sin(8 * np.pi * t) + 0.35 * serie(5, 120, 0.8), MEDIDA, 3.5))
        bit = moneda("1").scale(1.7).move_to([4.2, 1.3, 0])
        rot = [etiqueta(s, INK, 0.7).move_to([x, -0.1, 0]) for s, x in (("Dado", -4.2), ("Cable", 0), ("Bit", 4.2))]
        distintos = VGroup(*[Text("≠", color=INK, weight=BOLD).scale(0.9).move_to([x, 1.3, 0]) for x in (-2.1, 2.1)])

        with self.narrar("b1"):
            self.en("dado")                                   # «Un dado»
            self.play(FadeIn(d, scale=0.8), FadeIn(rot[0]), run_time=self.dur(0.5))
            self.en("cable")                                  # «un cable»
            self.play(Create(cable), FadeIn(rot[1]), run_time=self.dur(0.6))
            self.en("bit")                                    # «un bit»
            self.play(FadeIn(bit, scale=0.8), FadeIn(rot[2]), run_time=self.dur(0.4))
            self.en("nada")                                   # «no se parecen en nada»
            self.play(FadeIn(distintos), run_time=self.dur(0.4))
            self.en("sinembargo")                             # «Y sin embargo»
            self.play(FadeOut(distintos), d.animate.shift(RIGHT * 1.3), bit.animate.shift(LEFT * 1.3),
                      run_time=self.dur(0.8))
            self.en("tres")                                   # «de cualquiera de los tres»
            self.play(LaggedStart(*[m.animate(rate_func=there_and_back).scale(1.25) for m in (d, cable, bit)],
                                  lag_ratio=0.3), run_time=self.dur(1.0))
            self.en("cabe")                                   # «cabe en»
            ax, et = ejes([-3.2, 3.2, 1], [0, 0.5, 0.1], ancho=6.4, alto=2.6, tip=False)
            ax.move_to([0, -1.9, 0])
            self.play(FadeOut(VGroup(*rot)), FadeIn(ax), run_time=self.dur(0.4))
            self.en("curva")                                  # «una sola curva»
            campana = ax.plot(lambda x: gaussiana(x, 0, 1) * 1.15, x_range=[-3.2, 3.2, 0.05], color=AMBAR,
                              stroke_width=5)
            self.play(Create(campana), run_time=self.dur(1.2))
            marco = SurroundingRectangle(VGroup(ax, campana), color=AMBAR, buff=0.2, corner_radius=0.15,
                                         stroke_width=3)
            self.play(Create(marco), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
