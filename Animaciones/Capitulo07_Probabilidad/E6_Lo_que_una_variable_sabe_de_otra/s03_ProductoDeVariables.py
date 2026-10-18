"""Escena 03 — La correlación: multiplicar equis por i griega y promediar."""
from comun.escena import *


class ProductoDeVariables(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        ax, et = ejes((-3, 3, 1), (-3, 3, 1), ancho=6.6, alto=5.4, x_label="x", y_label="y")
        g = VGroup(ax, et).move_to([-3.3, -0.6, 0])
        a, b = puntos_corr(0.8, 30, 4)
        a, b = np.clip(a, -2.6, 2.6), np.clip(b, -2.6, 2.6)
        pts = [Dot(ax.c2p(x, y), radius=0.1, color=SENAL) for x, y in zip(a, b)]
        # puntos elegidos: los dos más grandes (arriba a la derecha) y tres cualquiera
        orden = np.argsort(-(a * b))
        grandes = [int(orden[0]), int(orden[1])]
        sueltos = [int(i) for i in orden[[8, 14, 20]]]
        elegidos = [grandes[0]] + sueltos
        filas = VGroup(*[Text(f"{num(a[i], 1)} · {num(b[i], 1)} = {num(a[i] * b[i], 1)}", color=TXT).scale(0.8)
                         for i in elegidos]).arrange(DOWN, buff=0.28).move_to([4.4, 1.4, 0])
        anillos = [Circle(radius=0.24, color=AMBAR, stroke_width=4).move_to(pts[i].get_center()) for i in elegidos]
        with self.narrar("b1"):
            # «¿Cómo medimos»
            self.en("pregunta")
            q = Text("¿Se mueven juntas?", color=AMBAR).scale(0.75).move_to([-3.3, 3.4, 0])
            self.play(Create(g), run_time=self.dur(0.5))
            self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in pts], lag_ratio=0.03), FadeIn(q),
                      run_time=self.dur(1.0))

            # «tienden a moverse juntas»
            self.en("juntas")
            recta = Line(ax.c2p(-2.6, -2.6), ax.c2p(2.6, 2.6), color=ESTIMACION, stroke_width=4)
            self.play(Create(recta), run_time=self.dur(0.7))

            # «Una idea sencilla»
            self.en("idea")
            self.play(FadeOut(recta), run_time=0.3)
            self.resaltar(q, color=TXT, escala=1.1)

            # «multiplicar equis por i griega»
            self.en("producto")
            xy = formula("x", r"\cdot", "y", colores={0: SENAL, 2: MEDIDA}, escala=1.5).move_to([4.4, 3.1, 0])
            self.play(FadeIn(anillos[0], scale=2), FadeIn(xy), run_time=self.dur(0.5))
            self.play(FadeIn(filas[0], shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «en cada caso»
            self.en("cada_caso")
            self.play(*[FadeIn(r, scale=2) for r in anillos[1:]],
                      LaggedStart(*[FadeIn(f, shift=LEFT * 0.2) for f in filas[1:]], lag_ratio=0.3),
                      run_time=self.dur(1.0))

            # «y promediar»
            self.en("promediar")
            barra = Rectangle(width=1.4, height=0.55, color=AMBAR, fill_opacity=0.6, stroke_width=0)
            barra.move_to([3.1, -0.7, 0])
            barra.align_to([2.4, 0, 0], LEFT)
            rot = Text("Promedio", color=AMBAR).scale(0.7).next_to(barra, DOWN, buff=0.2, aligned_edge=LEFT)
            self.play(FadeIn(barra, shift=RIGHT * 0.2), FadeIn(rot), run_time=self.dur(0.6))

            # «cuando una es grande»
            self.en("grande")
            extra = [Circle(radius=0.24, color=VERDE, stroke_width=4).move_to(pts[i].get_center()) for i in grandes]
            self.play(*[FadeIn(c, scale=2) for c in extra], run_time=self.dur(0.5))

            # «los productos serán grandes»
            self.en("prod_grandes")
            self.resaltar(*filas, color=VERDE, escala=1.15)

            # «el promedio también»
            self.en("prom_grande")
            nueva = Rectangle(width=3.8, height=0.55, color=AMBAR, fill_opacity=0.6, stroke_width=0)
            nueva.align_to([2.4, 0, 0], LEFT).align_to(barra, UP)
            self.play(Transform(barra, nueva), run_time=self.dur(0.7))

            # «Esa esperanza del producto»
            self.en("esperanza")
            e = formula("r_{XY}", "=", "E", "[", "X", "Y", "]", colores={0: AMBAR, 4: SENAL, 5: MEDIDA},
                        escala=1.5).move_to([4.4, -2.3, 0])
            oculta(e)
            self.add(e)
            self.play(*revelar(e[2], e[3], e[4], e[5], e[6]), run_time=self.dur(0.9))

            # «correlación»
            self.en("correlacion")
            w = self.palabra("Correlación", AMBAR, 0.9).move_to([4.4, -3.4, 0])
            self.play(*revelar(e[0], e[1]), run_time=0.3)
            self.pop(w)
        self.wait(1.0)
        self.limpiar()
