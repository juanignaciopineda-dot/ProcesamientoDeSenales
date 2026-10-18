"""Escena 14 — Cierre: tabla y colina lo contienen todo; falta un número que diga cuánto sabe una de otra (E6)."""
from comun.escena import *

VALORES = [[r"0{,}63", r"0{,}07"], [r"0{,}03", r"0{,}27"]]


class Cierre(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        t = Tabla2x2(centro=(-3.6, 0.0), lado=1.8)
        vals = [[t.valor(i, j, VALORES[i][j], VERDE, 1.1) for j in range(2)] for i in range(2)]
        colina = Colina(centro=(3.6, 0.2), rho=0.82, ancho=5.0, prof=2.4, alto=2.4, n=15)
        par = MathTex("(", "S", ",", "R", ")", color=TXT).scale(1.6).move_to([0, 3.3, 0])
        par[1].set_color(SENAL)
        par[3].set_color(MEDIDA)
        llaves = VGroup(*[Brace(VGroup(t.cel[i][0], t.cel[i][1]), RIGHT, color=AMBAR, buff=0.08) for i in range(2)],
                        *[Brace(VGroup(t.cel[0][j], t.cel[1][j]), DOWN, color=AMBAR, buff=0.08) for j in range(2)])
        marco = Rectangle(width=t.lado, height=2 * t.lado, color=AMBAR, stroke_width=5).move_to(
            (t.c(0, 1) + t.c(1, 1)) / 2)
        r79 = MathTex(r"0{,}79", color=VERDE).scale(1.5).move_to([-3.6, -3.1, 0])
        with self.narrar("b1"):
            # «con una tabla, o con una colina»
            self.en("tabla_colina")
            self.play(Create(VGroup(*[c for f in t.cel for c in f])), FadeIn(VGroup(*t.rot_f, *t.rot_c)),
                      FadeIn(VGroup(*[v for f in vals for v in f])), run_time=self.dur(0.7))
            self.play(FadeIn(colina.base), LaggedStart(*[AnimationGroup(FadeIn(r[0]), FadeIn(r[1])) for r in colina.filas],
                                                       lag_ratio=0.04), run_time=self.dur(1.1))

            # «dos variables a la vez»
            self.en("dos")
            self.pop(par)

            # «las marginales»
            self.en("marginales")
            self.play(*[GrowFromCenter(l) for l in llaves], run_time=self.dur(0.6))

            # «las condicionales»
            self.en("condicionales")
            self.play(FadeOut(llaves), Create(marco), run_time=self.dur(0.4))
            self.pop(r79)

            # «la media de una sabiendo la otra»
            self.en("esperanza")
            self.corte()
            ax, lab = ejes([-3, 3, 1], [-3.5, 3.5, 1], ancho=6.0, alto=4.4, x_label="x", y_label="y")
            g = VGroup(ax, lab).move_to([0, -0.2, 0])
            px, py = nube_xy7(110, 6)
            pts = VGroup(*[Dot(ax.c2p(a, b), radius=0.055, color=SENAL) for a, b in zip(px, py)])
            recta = Line(ax.c2p(-2.8, -2.8), ax.c2p(2.8, 2.8), color=AMBAR, stroke_width=6)
            etq = MathTex(r"E[Y\mid X=x]", color=AMBAR).scale(1.0).move_to([-3.9, 2.9, 0])
            self.play(Create(ax), FadeIn(lab), FadeIn(pts), run_time=self.dur(0.6))
            self.play(Create(recta), FadeIn(etq), run_time=self.dur(0.7))

            # «la varianza se parte»
            self.en("parte")
            self.corte()
            bar = BarrasVar7(origen=(-3.06, 0.0), esc=0.075, alto=1.0)
            lv = Text("lo que explica el grupo", color=VERDE).scale(0.65).next_to(bar.entre, DOWN, buff=0.3)
            lr = Text("lo que no", color=ROJO).scale(0.65).next_to(bar.dentro, UP, buff=0.3)
            self.play(FadeIn(bar.dentro, shift=RIGHT * 0.3), FadeIn(bar.entre, shift=LEFT * 0.3), run_time=self.dur(0.6))
            self.play(FadeIn(lv), FadeIn(lr), run_time=0.4)

            # «lo que el grupo explica»
            self.en("explica")
            self.play(Indicate(bar.entre, color=AMBAR, scale_factor=1.1), run_time=self.dur(0.7))

            # «Pero falta algo»
            self.en("falta")
            falta = Text("?", color=AMBAR, weight=BOLD).scale(2.0).move_to([0, -2.4, 0])
            self.pop(falta)

            # «un solo número»
            self.en("numero")
            self.corte()
            cuadro = caja("?", AMBAR, ancho=2.4, alto=1.8, scale=1.6)
            cuadro.move_to([0, 0.4, 0])
            self.pop(cuadro)

            # «cuánto sabe una variable de otra»
            self.en("sabe")
            x = MathTex("X", color=SENAL).scale(1.6).move_to([-4.2, 0.4, 0])
            y = MathTex("Y", color=MEDIDA).scale(1.6).move_to([4.2, 0.4, 0])
            a1 = Arrow(x.get_right() + RIGHT * 0.1, cuadro.get_left() + LEFT * 0.1, color=SENAL, buff=0.1, stroke_width=6)
            a2 = Arrow(y.get_left() + LEFT * 0.1, cuadro.get_right() + RIGHT * 0.1, color=MEDIDA, buff=0.1, stroke_width=6)
            self.play(FadeIn(x), FadeIn(y), run_time=0.3)
            self.play(GrowArrow(a1), GrowArrow(a2), run_time=self.dur(0.6))

            # «el próximo episodio»
            self.en("proximo")
            self.corte()
            prox = etiqueta("próximo episodio", INK, 0.6).move_to([0, 2.0, 0])
            a = self.palabra("Lo que una variable", TXT, 1.3).move_to([0, 0.5, 0])
            b = self.palabra("sabe de otra", AMBAR, 1.3).move_to([0, -0.9, 0])
            self.play(FadeIn(prox), run_time=0.3)

            # «Lo que una variable»
            self.en("t1")
            self.pop(a)

            # «sabe de otra»
            self.en("t2")
            self.pop(b)
        self.wait(1.0)
        self.limpiar()
