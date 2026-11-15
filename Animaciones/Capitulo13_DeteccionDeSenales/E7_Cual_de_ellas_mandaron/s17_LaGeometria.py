"""Escena 17 — Una geometría para todo: flechas, nubes redondas, proyección y distancias en desvíos."""
from comun.escena import *

O = np.array([-3.0, -0.2, 0.0])


class LaGeometria(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        plano = planito7(centro=(O[0], O[1]), ancho=5.4, alto=4.6)
        a1 = flecha_c(O, 2.3, 35, SENAL, 6)
        a0 = flecha_c(O, 2.0, 160, AZUL_C7, 6)
        p1 = Dot(a1.get_end(), radius=0.1, color=SENAL)
        p0 = Dot(a0.get_end(), radius=0.1, color=AZUL_C7)
        n1 = Circle(radius=0.65, color=RUIDO, stroke_width=3).set_fill(RUIDO, 0.15).move_to(p1)
        n0 = Circle(radius=0.65, color=RUIDO, stroke_width=3).set_fill(RUIDO, 0.15).move_to(p0)
        u = np.array([np.cos(np.deg2rad(35)), np.sin(np.deg2rad(35)), 0.0])
        dire = DashedLine(O - 2.4 * u, O + 2.7 * u, color=AMBAR, stroke_width=3)
        v = O + np.array([1.5, 2.1, 0.0])
        av = Arrow(O, v, buff=0, color=MEDIDA, stroke_width=5, max_tip_length_to_length_ratio=0.15)
        s = O + u * float(np.dot(v - O, u))
        sombra = Arrow(O, s, buff=0, color=VERDE, stroke_width=7, max_tip_length_to_length_ratio=0.15)
        perp = DashedLine(v, s, color=INK, stroke_width=3)
        d01 = p1.get_center() - p0.get_center()
        nrm = np.array([-d01[1], d01[0], 0.0]) / np.linalg.norm(d01)
        medir = DoubleArrow(p0.get_center() + d01 * 0.08, p1.get_center() - d01 * 0.08, color=AMBAR, stroke_width=3,
                            buff=0, max_tip_length_to_length_ratio=0.05)
        reg = VGroup(*[Line(p0.get_center() + d01 * k / 6 - nrm * 0.15, p0.get_center() + d01 * k / 6 + nrm * 0.15,
                            color=RUIDO, stroke_width=3) for k in range(1, 6)])
        F, R = flechas_xy(origen=(2.6, -1.6), largo=3.4, angulo=45)
        cap = etiqueta("capítulo 8", INK, 0.5).move_to([4.6, 3.3, 0])
        nums = VGroup(*[Text(str(n), color=INK, weight=BOLD).scale(0.55) for n in range(7, 14)]).arrange(RIGHT, buff=0.45)
        nums.move_to([-3.0, -3.4, 0])
        with self.narrar("b1"):
            # «la misma geometría»
            self.paso("geometria", plano, t=0.6)
            # «Las señales son flechas, o puntos»
            self.en("flechas")
            self.play(GrowArrow(a1), GrowArrow(a0), FadeIn(p1), FadeIn(p0), run_time=self.dur(0.9))
            # «El ruido es una nube redonda»
            self.paso("nube", n1, n0, t=0.7)
            # «en la dirección que importa»
            self.paso("direccion", Create(dire), t=0.7)
            # «se queda»
            self.en("queda")
            self.play(GrowArrow(av), run_time=0.5)
            self.play(GrowArrow(sombra), run_time=self.dur(0.6))
            # «lo perpendicular se tira»
            self.en("tira")
            self.play(Create(perp), run_time=0.4)
            self.play(FadeOut(perp), av.animate.set_color(INK), run_time=self.dur(0.6))
            # «decidir es medir distancias»
            self.paso("medir", GrowArrow(medir), t=0.6)
            # «en desvíos del ruido»
            self.paso("desvios", reg, t=0.6)
            # «la flecha y su sombra»
            self.en("sombra")
            self.play(GrowArrow(F.presente), GrowArrow(F.futuro), Create(F.sombra), Create(F.error), Create(F.recto),
                      FadeIn(R["x"]), FadeIn(R["y"]), FadeIn(R["yh"]), FadeIn(R["e"]), FadeIn(cap), run_time=self.dur(1.2))
            # «la misma idea, una y otra vez»
            self.en("otravez")
            self.play(LaggedStart(*[FadeIn(m, scale=0.6) for m in nums], lag_ratio=0.25), run_time=self.dur(1.6))
        self.wait(1.0)
        self.limpiar()
