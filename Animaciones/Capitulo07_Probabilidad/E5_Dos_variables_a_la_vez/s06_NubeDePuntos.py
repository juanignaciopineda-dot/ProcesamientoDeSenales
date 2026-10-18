"""Escena 06 — De la tabla a la nube: X lo enviado, Y = X + ruido, y la tabla que se afina hasta ser una colina."""
from comun.escena import *


def dens_xy(x, y, ruido=0.7):
    return gaussiana(x, 0, 1) * gaussiana(y, x, ruido)


class NubeDePuntos(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        ax, lab = ejes([-3, 3, 1], [-3.5, 3.5, 1], ancho=6.2, alto=4.6, x_label="x", y_label="y")
        grupo = VGroup(ax, lab).move_to([-0.8, -0.5, 0])
        self.ax = ax
        px, py = nube_xy7(130, 11)
        recta_x = Line([-6.4, 2.3, 0], [-4.4, 2.3, 0], color=INK, stroke_width=3)
        punto_x = Dot([-5.8, 2.3, 0], radius=0.1, color=SENAL)
        lx = MathTex("X", color=SENAL).scale(1.1).next_to(recta_x, UP, buff=0.25)
        recta_y = Line([4.4, 2.3, 0], [6.4, 2.3, 0], color=INK, stroke_width=3)
        punto_y = Dot([5.5, 2.3, 0], radius=0.1, color=MEDIDA)
        ly = MathTex("Y", color=MEDIDA).scale(1.1).next_to(recta_y, UP, buff=0.25)
        modelo = MathTex("Y", "=", "X", "+", r"\text{ruido}", color=TXT).scale(1.0).move_to([0, 3.4, 0])
        modelo[0].set_color(MEDIDA)
        modelo[2].set_color(SENAL)
        modelo[4].set_color(RUIDO)
        par = MathTex(r"(x,\,y)=(1{,}2\,;\,1{,}9)", color=TXT).scale(0.9).move_to([4.6, -0.2, 0])
        p0 = Dot(ax.c2p(1.2, 1.9), radius=0.11, color=AMBAR)
        guias = VGroup(DashedLine(ax.c2p(1.2, 0), ax.c2p(1.2, 1.9), color=AMBAR, stroke_width=2.5),
                       DashedLine(ax.c2p(0, 1.9), ax.c2p(1.2, 1.9), color=AMBAR, stroke_width=2.5))
        puntos = VGroup(*[Dot(ax.c2p(a, b), radius=0.055, color=SENAL) for a, b in zip(px, py)])
        elipse = Ellipse(width=6.6, height=2.0, color=AMBAR, stroke_width=4).rotate(np.deg2rad(36)).move_to(ax.c2p(0, 0))
        diag = Arrow(ax.c2p(-1.6, -1.6), ax.c2p(2.7, 2.7), color=AMBAR, buff=0, stroke_width=5,
                     max_tip_length_to_length_ratio=0.12)
        lejos = np.argsort(-np.abs(py - px))[:2]
        sep = VGroup(*[DashedLine(ax.c2p(px[k], px[k]), ax.c2p(px[k], py[k]), color=ERROR, stroke_width=3)
                       for k in lejos])
        with self.narrar("b1"):
            # «una tensión cualquiera»
            self.en("x")
            self.play(Create(recta_x), FadeIn(punto_x), run_time=self.dur(0.5))
            self.pop(lx)
            self.play(punto_x.animate.move_to([-4.9, 2.3, 0]), run_time=self.dur(0.6))

            # «Y lo que se recibe»
            self.en("recibe")
            self.play(Indicate(recta_y, color=MEDIDA, scale_factor=1.2), run_time=self.dur(0.6))

            # «i griega»
            self.en("y")
            self.play(Create(recta_y), FadeIn(punto_y), run_time=self.dur(0.5))
            self.pop(ly)

            # «más un ruido»
            self.en("ruido")
            self.play(FadeIn(modelo[0:3], shift=DOWN * 0.15), run_time=self.dur(0.5))
            self.play(FadeIn(modelo[3:], shift=DOWN * 0.15), run_time=self.dur(0.6))

            # «una pareja de números»
            self.en("pareja")
            self.play(FadeIn(par, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «un punto en el plano»
            self.en("punto")
            self.play(Create(ax), FadeIn(lab), run_time=self.dur(0.6))
            self.play(Create(guias), FadeIn(p0, scale=0.4), run_time=self.dur(0.5))

            # «Repitiendo muchas veces»
            self.en("repite")
            self.play(FadeOut(guias), FadeOut(par), run_time=0.25)
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in puntos], lag_ratio=0.03),
                      run_time=self.dur(2.2))

            # «una nube alargada»
            self.en("nube")
            self.play(Create(elipse), run_time=self.dur(0.8))

            # «suele recibirse más»
            self.en("mas")
            self.play(GrowArrow(diag), run_time=self.dur(0.6))

            # «con dispersión»
            self.en("dispersion")
            self.play(Create(sep), run_time=self.dur(0.6))
        self.quitar = VGroup(recta_x, punto_x, lx, recta_y, punto_y, ly, modelo, p0, puntos, elipse, diag, sep)
        self.grupo = grupo

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        ax = self.ax

        def rejilla(n):
            xs = np.linspace(-3, 3, n + 1)
            ys = np.linspace(-3.5, 3.5, n + 1)
            g = VGroup(*[Line(ax.c2p(x, -3.5), ax.c2p(x, 3.5), color=AMBAR, stroke_width=2.5) for x in xs],
                       *[Line(ax.c2p(-3, y), ax.c2p(3, y), color=AMBAR, stroke_width=2.5) for y in ys])
            return g

        n = 14
        xs = np.linspace(-3, 3, n + 1)
        ys = np.linspace(-3.5, 3.5, n + 1)
        celdas = VGroup()
        d = np.array([[dens_xy((xs[i] + xs[i + 1]) / 2, (ys[j] + ys[j + 1]) / 2) for j in range(n)] for i in range(n)])
        for i in range(n):
            for j in range(n):
                celdas.add(Rectangle(width=float(ax.c2p(xs[i + 1], 0)[0] - ax.c2p(xs[i], 0)[0]),
                                     height=float(ax.c2p(0, ys[j + 1])[1] - ax.c2p(0, ys[j])[1]),
                                     stroke_width=0, fill_color=AZUL, fill_opacity=float(min(1.0, 0.1 + 0.9 * d[i, j] / d.max())))
                             .move_to([float(ax.c2p((xs[i] + xs[i + 1]) / 2, 0)[0]), float(ax.c2p(0, (ys[j] + ys[j + 1]) / 2)[1]), 0]))
        g2, g4, g8, g14 = rejilla(2), rejilla(4), rejilla(8), rejilla(14)
        colina = Colina(centro=(0.3, -0.4), rho=0.82, ancho=6.4, prof=3.0, alto=2.8, n=17)
        pico = Circle(radius=0.45, color=AMBAR, stroke_width=5).move_to(colina.P(0, 0, 1.0))
        borde = Circle(radius=0.45, color=AMBAR, stroke_width=5).move_to(colina.P(2.0, -1.4, colina.h(2.0, -1.4)))
        efe = formula("f", r"_{XY}", "(", "x", ",", "y", ")", escala=1.6, colores={0: AMBAR}).move_to([0, 3.4, 0])
        with self.narrar("b2"):
            # «infinitas parejas posibles»
            self.en("infinitas")
            self.play(FadeOut(self.quitar), run_time=0.3)
            self.play(Create(g2), run_time=self.dur(0.6))

            # «cada vez más fina»
            self.en("fina")
            self.play(ReplacementTransform(g2, g4), run_time=self.dur(0.5))
            self.play(ReplacementTransform(g4, g8), run_time=self.dur(0.5))
            self.play(ReplacementTransform(g8, g14), run_time=self.dur(0.5))

            # «casillas más y más pequeñas»
            self.en("pequenas")
            self.play(FadeOut(g14), FadeIn(celdas), run_time=self.dur(1.0))

            # «En el límite»
            self.en("limite")
            lim = self.palabra("en el límite", AMBAR, 0.8).move_to([-4.6, 3.3, 0])
            self.pop(lim)

            # «una superficie sobre el plano»
            self.en("superficie")
            self.play(FadeOut(celdas), FadeOut(self.grupo), FadeOut(lim), run_time=0.3)
            self.play(FadeIn(colina.base), run_time=0.3)
            self.play(LaggedStart(*[AnimationGroup(FadeIn(r[0]), FadeIn(r[1]))
                                    for r in colina.filas], lag_ratio=0.06), run_time=self.dur(1.6))

            # «como una colina»
            self.en("colina")
            col = self.palabra("colina", AMBAR, 1.1).move_to([-5.2, 2.4, 0])
            self.pop(col)

            # «alta donde caen muchos puntos»
            self.en("alta")
            self.play(Create(pico), run_time=self.dur(0.4))

            # «baja donde caen pocos»
            self.en("baja")
            self.play(ReplacementTransform(pico, borde), run_time=self.dur(0.5))

            # «densidad conjunta»
            self.en("densidad")
            self.play(FadeOut(borde), FadeOut(col), run_time=0.25)
            pal = self.palabra("densidad conjunta", TXT, 0.8).move_to([-3.6, 3.4, 0])
            self.pop(pal)

            # «efe sub equis i griega»
            self.en("f_xy")
            self.play(FadeOut(pal), run_time=0.2)
            efe.move_to([-4.2, 3.2, 0]).scale(0.75)
            self.play(FadeIn(efe[0:2], shift=DOWN * 0.15), run_time=self.dur(0.5))
            self.play(FadeIn(efe[2:], shift=DOWN * 0.15), run_time=self.dur(0.7))
