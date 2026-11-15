"""Escena 11 — Cuántas parejas hay de cada separación: el triángulo de pesos."""
from comun.escena import *


class ElTriangulo(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        lado = 0.9
        cx, cy = -4.6, 1.3
        celdas = {(i, j): Square(lado, color=INK, stroke_width=2.5).move_to([cx + (j - 1) * lado, cy - (i - 1) * lado, 0])
                  for i in range(3) for j in range(3)}
        tabla = VGroup(*celdas.values())
        grupos = {0: ([(0, 0), (1, 1), (2, 2)], AMBAR), 1: ([(0, 1), (1, 0), (1, 2), (2, 1)], CIAN),
                  2: ([(0, 2), (2, 0)], MAGENTA)}
        base, dx, y0, esc = ejes_k(2, ancho=6.0, alto=2.4, v_max=3.0, centro=(3.3, 0.0))
        cxb = 3.3
        alturas = {0: 3, 1: 2, 2: 1}

        with self.narrar("b1"):
            # «cuántas parejas»
            self.en("cuantas")
            self.play(Create(tabla), run_time=self.dur(0.6))
            self.play(*[celdas[ij].animate.set_fill(col, 0.4).set_stroke(col, 3)
                        for (lst, col) in grupos.values() for ij in lst], Create(base), run_time=self.dur(0.8))

            # «Tres a separación cero»
            self.en("cero")
            b0 = barra_k(0, 3, dx * 1.3, y0, esc / 1.0, cxb, AMBAR)
            self.play(GrowFromEdge(b0, DOWN), run_time=self.dur(0.7))
            n0 = Text("3", color=AMBAR, weight=BOLD).scale(0.6).next_to(b0, UP, buff=0.1)
            self.play(FadeIn(n0), run_time=0.2)

            # «Dos a un paso»
            self.en("uno")
            b1 = VGroup(*[barra_k(k, 2, dx * 1.3, y0, esc, cxb, CIAN) for k in (-1, 1)])
            for b in b1:
                b.set_x(cxb + (1 if b.get_x() > cxb else -1) * dx * 1.3)
            n1 = VGroup(*[Text("2", color=CIAN, weight=BOLD).scale(0.6).next_to(b, UP, buff=0.1) for b in b1])
            self.play(*[GrowFromEdge(b, DOWN) for b in b1], FadeIn(n1), run_time=self.dur(0.7))

            # «Una a dos pasos»
            self.en("dos")
            b2 = VGroup(*[barra_k(k, 1, dx * 1.3, y0, esc, cxb, MAGENTA) for k in (-1, 1)])
            for b in b2:
                b.set_x(cxb + (1 if b.get_x() > cxb else -1) * dx * 2.6)
            n2 = VGroup(*[Text("1", color=MAGENTA, weight=BOLD).scale(0.6).next_to(b, UP, buff=0.1) for b in b2])
            self.play(*[GrowFromEdge(b, DOWN) for b in b2], FadeIn(n2), run_time=self.dur(0.7))

            # «Uno, dos, tres, dos, uno»
            self.en("cuenta")
            self.play(*[m.animate.scale(1.25) for m in (n0, *n1, *n2)], run_time=0.5)

            # «un triángulo»
            self.en("tri")
            pts = [[cxb - 2.5 * dx * 1.3, y0, 0], [cxb, y0 + 3 * esc * 1.0 + 0.85, 0], [cxb + 2.5 * dx * 1.3, y0, 0]]
            tri = Polygon(*pts, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.08)
            self.play(Create(tri), run_time=self.dur(0.8))

            # «Con ene muestras»
            self.en("ene")
            todo = VGroup(b0, b1, b2, n0, n1, n2)
            self.play(FadeOut(todo), FadeOut(tabla), FadeOut(base), tri.animate.stretch(2.2, 0).move_to([0.0, tri.get_center()[1], 0]),
                      run_time=self.dur(1.0))

            # «La varianza del promedio»
            self.en("var")
            f = MathTex(r"\mathrm{Var}", "=", r"\frac{1}{N^2}", r"\sum_k", r"(N-|k|)", "C[k]", color=TXT).scale(1.1)
            f.move_to([0.5, -2.7, 0])
            f[4].set_color(AMBAR)
            f[5].set_color(CIAN)
            for p in f:
                p.set_opacity(0)
            self.add(f)
            self.play(f[0].animate.set_opacity(1), f[1].animate.set_opacity(1), run_time=0.4)

            # «la suma de la autocovarianza»
            self.en("suma")
            self.play(f[3].animate.set_opacity(1), f[5].animate.set_opacity(1), run_time=0.5)

            # «pesada por ese triángulo»
            self.en("pesada")
            self.play(f[4].animate.set_opacity(1), run_time=0.4)
            self.resaltar(tri, escala=1.0)

            # «entre ene al cuadrado»
            self.en("n2")
            self.play(f[2].animate.set_opacity(1), run_time=0.5)
        self.wait(1.0)
        self.limpiar()
