"""Escena 01 — Gancho: osciladores que arrancan a la vez frente a osciladores con fase al azar."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        ys = [2.0, 0.65, -0.7, -2.05]
        izq = [Lienzo(ancho=5.6, alto=1.0, t_rango=(0, 2), v_max=1.25, centro=(-3.7, y)) for y in ys]
        der = [Lienzo(ancho=5.6, alto=1.0, t_rango=(0, 2), v_max=1.25, centro=(3.7, y)) for y in ys]
        bases = [L.base() for L in izq + der]
        c_izq = [coseno(L, 0, 1, SENAL, 3.5) for L in izq]
        c_der = [coseno(L, f, 1, SENAL, 3.5) for L, f in zip(der, (0, 90, 180, 270))]
        marco_i = RoundedRectangle(corner_radius=0.15, width=6.1, height=5.2, color=INK, stroke_width=2.5).move_to([-3.7, -0.02, 0])
        marco_d = marco_i.copy().move_to([3.7, -0.02, 0])

        with self.narrar("b1"):
            # «Dos grupos de osciladores»
            self.en("dos")
            self.play(FadeIn(marco_i), FadeIn(marco_d), *[Create(b) for b in bases], run_time=self.dur(0.6))

            # «la misma frecuencia»
            self.en("frec")
            self.play(*[Create(c) for c in c_izq + c_der], run_time=self.dur(1.2), rate_func=linear)

            # «arrancan todos a la vez»
            self.en("a_la_vez")
            v_i = Line([float(izq[0].x(0)), 2.75, 0], [float(izq[0].x(0)), -2.75, 0], color=AMBAR, stroke_width=3.5)
            pts_i = VGroup(*[Dot(L.p(0, 1.0), radius=0.1, color=AMBAR) for L in izq])
            self.play(Create(v_i), FadeIn(pts_i), run_time=self.dur(0.6))

            # «cada uno con la fase al azar»
            self.en("azar")
            v_d = Line([float(der[0].x(0)), 2.75, 0], [float(der[0].x(0)), -2.75, 0], color=AMBAR, stroke_width=3.5)
            pts_d = VGroup(*[Dot(L.p(0, float(np.cos(np.deg2rad(f)))), radius=0.1, color=AMBAR)
                             for L, f in zip(der, (0, 90, 180, 270))])
            self.play(Create(v_d), FadeIn(pts_d), run_time=self.dur(0.6))

            # «Solo el segundo»
            self.en("segundo")
            self.play(*[c.animate.set_stroke(opacity=0.25) for c in c_izq],
                      *[m.animate.set_opacity(0.25) for m in (v_i, pts_i, marco_i)],
                      *[c.animate.set_stroke(width=5) for c in c_der],
                      marco_d.animate.set_stroke(AMBAR, width=4), run_time=self.dur(0.6))

            # «un secreto»
            self.en("secreto")
            cand = candado(AMBAR).scale(0.9).move_to([3.7, 3.35, 0])
            self.pop(cand)

            # «da igual a qué hora lo mires»
            self.en("hora")
            r = reloj().scale(1.0).move_to([6.4, 3.3, 0])
            banda = Rectangle(width=5.6, height=4.7, color=AMBAR, stroke_width=0).set_fill(AMBAR, 0.09).move_to([3.7, -0.02, 0])
            self.play(FadeIn(r), FadeIn(banda), run_time=0.3)
            self.play(Rotate(r.minutero, angle=-4 * PI, about_point=r.aro.get_center()),
                      run_time=self.dur(2.0), rate_func=linear)
        self.wait(0.6)
        self.limpiar()
