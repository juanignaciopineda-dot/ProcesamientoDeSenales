"""Escena 15 — El error no tiene patrón: si lo tuviera, se podría mejorar; la perpendicular lo dice."""
from comun.escena import *


class SinPatron(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        a = PuntosErr8(centro=(-3.5, 0.6), ancho=6.0, alto=3.2, n=26, semilla=7)
        b = PuntosErr8(centro=(3.5, 0.6), ancho=6.0, alto=3.2, n=26, semilla=9)
        ta = caja("Recibo 1", MEDIDA, ancho=2.8, alto=0.85, scale=0.7).move_to([-3.5, 3.4, 0])
        tb = caja("Recibo 0", MEDIDA, ancho=2.8, alto=0.85, scale=0.7).move_to([3.5, 3.4, 0])
        et = Text("Error", color=ERROR, weight=BOLD).scale(0.65).move_to([-6.3, 2.5, 0])
        with self.narrar("b1"):
            # «ningún patrón»
            self.en("patron")
            self.play(FadeIn(ta), FadeIn(tb), FadeIn(et), Create(a.cero), Create(b.cero), run_time=self.dur(0.6))
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in list(a.pts) + list(b.pts)], lag_ratio=0.02),
                      run_time=self.dur(1.4))

            # «Si lo tuviera»
            self.en("tuviera")
            self.play(*[p.animate.shift(UP * 0.8) for p in a.pts], run_time=self.dur(0.7))

            # «nos quedáramos cortos siempre que llega un uno»
            self.en("cortos")
            cor = Text("Siempre cortos", color=ROJO).scale(0.8).move_to([-3.5, -1.9, 0])
            fl = Arrow([-3.5, -1.5, 0], [-3.5, -0.9, 0], color=ROJO, buff=0, stroke_width=7)
            self.play(FadeIn(cor), Create(fl), run_time=self.dur(0.5))

            # «sumar algo en esa columna»
            self.en("sumar")
            fl2 = Arrow([0, 1.8, 0], [0, 0.9, 0], color=AMBAR, buff=0, stroke_width=8)
            self.play(Create(fl2), *[p.animate.shift(DOWN * 0.8) for p in a.pts], run_time=self.dur(0.9))

            # «para mejorar»
            self.en("mejorar")
            ok = tilde(VERDE, 0.7).move_to([-3.9, -2.6, 0])
            mj = Text("Mejor", color=VERDE, weight=BOLD).scale(0.8).next_to(ok, RIGHT, buff=0.25)
            self.play(FadeOut(cor), FadeOut(fl), FadeOut(fl2), run_time=0.2)
            self.play(Create(ok), FadeIn(mj), run_time=self.dur(0.5))

            # «ortogonal a todo lo que se puede calcular con el dato»
            self.en("ortogonal")
            self.corte()
            o = np.array([-3.6, -1.6, 0.0])
            e = Arrow(o, o + UP * 4.0, color=ERROR, buff=0, stroke_width=8)
            g = Arrow(o, o + RIGHT * 4.2, color=MEDIDA, buff=0, stroke_width=8)
            ang = VMobject(color=AMBAR, stroke_width=6).set_points_as_corners(
                [o + UP * 0.55, o + UP * 0.55 + RIGHT * 0.55, o + RIGHT * 0.55])
            ne = Text("Error", color=ERROR, weight=BOLD).scale(0.8).next_to(e.get_end(), UP, buff=0.1)
            ng = Text("Datos", color=MEDIDA, weight=BOLD).scale(0.8).next_to(g.get_end(), RIGHT, buff=0.1)
            self.play(Create(e), Create(g), Create(ang), FadeIn(ne), FadeIn(ng), run_time=self.dur(0.9))

            # «lo que se puede calcular»
            self.en("calcular")
            fs = VGroup(*[MathTex(t, color=MEDIDA).scale(1.2) for t in (r"g_1(R)", r"g_2(R)", r"g_3(R)")])
            fs.arrange(DOWN, buff=0.5).move_to([3.8, 1.0, 0])
            self.play(LaggedStart(*[FadeIn(f, shift=LEFT * 0.2) for f in fs], lag_ratio=0.3), run_time=self.dur(1.0))

            # «toda la información»
            self.en("toda")
            ti = tilde(VERDE, 0.7).move_to([0.6, -2.7, 0])
            inf = Text("Toda la información usada", color=VERDE, weight=BOLD).scale(0.7).next_to(ti, RIGHT, buff=0.3)
            self.sfx("exito")
            self.play(Create(ti), FadeIn(inf), run_time=self.dur(0.6))

            # «volverá convertida en un dibujo»
            self.en("dibujo")
            self.play(FadeOut(fs), FadeOut(ti), FadeOut(inf), FadeOut(ne), FadeOut(ng), run_time=self.dur(0.4))
            self.play(VGroup(e, g, ang).animate.scale(1.25).move_to([0, -0.2, 0]), run_time=self.dur(0.9))
        self.wait(1.0)
        self.limpiar()
