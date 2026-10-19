"""Escena 08 — El error σ²(1 − ρ²) con el seno; los casos ρ = 1 y ρ = 0; y la partición explicado / sin explicar."""
from comun.escena import *
from comun.figuras_c8e4 import *


class ElErrorEnGeneral(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.tr = ValueTracker(ANG8)
        self.fig = AnguloVivo8(self.tr)
        self.add(self.fig.todo)
        self.formula_general()
        self.casos_extremos()
        self.fig.apagar()
        self.reparto()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def formula_general(self):
        fig = self.fig
        f1 = formula(r"\text{Error}", "=", r"\sigma_Y", r"\cdot", r"\sin\theta", escala=1.15,
                     colores={0: ERROR, 2: SENAL}).move_to([3.7, 2.8, 0])
        f2 = formula(r"\text{Error}^2", "=", r"\sigma_Y^2", r"\cdot", r"\sin^2\theta", escala=1.15,
                     colores={0: ERROR, 2: SENAL}).move_to([3.7, 1.8, 0])
        f3 = formula("=", r"\sigma_Y^2", r"(1-\cos^2\theta)", escala=1.15, colores={1: SENAL}).move_to([3.7, 0.8, 0])
        f4 = formula("=", r"\sigma_Y^2", r"(1-\rho^2)", escala=1.3, colores={1: SENAL, 2: AMBAR}).move_to([3.7, -0.35, 0])
        marco = SurroundingRectangle(f4, color=AMBAR, buff=0.2, stroke_width=3)

        with self.narrar("b1"):
            # «el cateto opuesto al ángulo»
            self.en("opuesto")
            self.resaltar(fig.error, color=ERROR, escala=1.08)

            # «es la hipotenusa por el seno»
            self.en("seno")
            self.play(*[FadeIn(f1[i]) for i in range(len(f1))], run_time=self.dur(0.9))

            # «Al cuadrado»
            self.en("cuad")
            self.play(*[FadeIn(f2[i]) for i in range(len(f2))], run_time=self.dur(0.9))

            # «la varianza por el seno al cuadrado»
            self.en("varsen")
            self.resaltar(f2[2], f2[3], f2[4], color=AMBAR, escala=1.1)

            # «el seno al cuadrado es uno menos el coseno al cuadrado»
            self.en("sen2")
            self.play(*[FadeIn(f3[i]) for i in range(len(f3))], run_time=self.dur(1.0))

            # «uno menos rho al cuadrado»
            self.en("rho2")
            self.play(*[FadeIn(f4[i]) for i in range(len(f4))], run_time=self.dur(1.0))

            # «La fórmula del error»
            self.en("form")
            self.resaltar(f4, color=AMBAR, escala=1.1)

            # «no hay que memorizarla»
            self.en("memo")
            self.play(Create(marco), run_time=self.dur(0.6))

            # «el cateto que le falta a la sombra»
            self.en("falta")
            self.resaltar(fig.error, color=ERROR, escala=1.08)
        self.b1 = VGroup(f1, f2, f3, f4, marco)

    # ------------------------------------------------------------ b2
    def casos_extremos(self):
        fig, tr = self.fig, self.tr
        self.play(FadeOut(self.b1), run_time=0.3)  # (el bloque ya terminó; el panel se despeja)
        rho1 = formula(r"\rho", "=", "1", escala=1.3, colores={0: AMBAR}).move_to([3.7, 2.7, 0])
        err0 = formula(r"\text{Error}", "=", "0", escala=1.3, colores={0: ERROR}).move_to([3.7, 1.6, 0])
        rho0 = formula(r"\rho", "=", "0", escala=1.3, colores={0: AMBAR}).move_to([3.7, 2.7, 0])
        media = formula(r"\hat{y}", "=", r"\text{Media}", escala=1.3, colores={0: ESTIMACION}).move_to([3.7, 1.6, 0])
        varent = formula(r"\text{Error}", "=", r"\sigma_Y^2", escala=1.3, colores={0: ERROR, 2: SENAL}).move_to([3.7, 0.5, 0])
        punto = Dot(fig.o, radius=0.14, color=ESTIMACION)
        cruz_x = cruz(ERROR, 0.9).move_to(fig.o + RIGHT * 4.0 + UP * 0.6)

        with self.narrar("b2"):
            # «Los casos extremos»
            self.en("extremos")
            self.play(tr.animate.set_value(45), run_time=self.dur(0.8))
            self.play(tr.animate.set_value(ANG8), run_time=self.dur(0.8))

            # «apuntan en la misma dirección»
            self.en("misma")
            self.play(tr.animate.set_value(3), run_time=self.dur(1.3))

            # «rho igual a uno»
            self.en("rho1")
            self.play(FadeIn(rho1), run_time=self.dur(0.5))

            # «el error desaparece»
            self.en("desap")
            self.play(FadeIn(err0), run_time=self.dur(0.6))

            # «son perpendiculares»
            self.en("perp")
            self.play(FadeOut(rho1), FadeOut(err0), tr.animate.set_value(88), run_time=self.dur(1.6))

            # «rho igual a cero»
            self.en("rho0")
            self.play(FadeIn(rho0), run_time=self.dur(0.5))

            # «la sombra es un punto»
            self.en("punto")
            self.play(FadeIn(punto, scale=0.3), run_time=self.dur(0.5))

            # «la estimación es la media»
            self.en("media")
            self.play(FadeIn(media), run_time=self.dur(0.6))

            # «el error, la varianza entera»
            self.en("varent")
            self.play(FadeIn(varent), run_time=self.dur(0.7))
            self.resaltar(fig.error, color=ERROR, escala=1.05)

            # «Un dato perpendicular»
            self.en("datoperp")
            self.resaltar(fig.x_flecha, color=MEDIDA, escala=1.04)

            # «no ayuda en nada»
            self.en("nada")
            self.play(FadeIn(cruz_x, scale=0.4), run_time=self.dur(0.5))
        self.b2 = VGroup(rho0, media, varent, punto, cruz_x)

    # ------------------------------------------------------------ b3
    def reparto(self):
        L, x0 = 9.0, -5.0
        y1, y2 = 1.6, -1.7

        def barra(y, partes, colores):
            """Rectángulos contiguos que parten una barra de largo L; `partes` suman 1."""
            rects, x = [], x0
            for p, c in zip(partes, colores):
                rects.append(Rectangle(width=L * p, height=0.9, stroke_width=0).set_fill(c, 0.75)
                             .move_to([x + L * p / 2, y, 0]))
                x += L * p
            return rects

        r1a, r1b = barra(y1, (0.8, 0.2), (ESTIMACION, ERROR))
        r2a, r2b = barra(y2, (40.56 / 81.76, 41.2 / 81.76), (ESTIMACION, ERROR))
        marco1 = Rectangle(width=L, height=0.9, color=INK, stroke_width=2.5).move_to([x0 + L / 2, y1, 0])
        marco2 = Rectangle(width=L, height=0.9, color=INK, stroke_width=2.5).move_to([x0 + L / 2, y2, 0])
        tit1 = Text("Termómetro", color=TXT).scale(0.55).move_to([x0 + 1.0, y1 + 0.9, 0])
        tit2 = Text("Altura", color=TXT).scale(0.55).move_to([x0 + 0.6, y2 + 0.9, 0])
        tot1 = formula(r"\sigma_Y^2", "=", "4", escala=0.9, colores={0: SENAL}).move_to([x0 + L - 1.0, y1 + 0.9, 0])
        tot2 = MathTex(num_tex(81.76), color=TXT).scale(0.9).move_to([x0 + L - 0.9, y2 + 0.9, 0])
        n32 = MathTex(num_tex(3.2), color=TXT).scale(0.9).move_to(r1a)
        n08 = MathTex(num_tex(0.8), color=TXT).scale(0.9).move_to(r1b)
        n4056 = MathTex(num_tex(40.56), color=TXT).scale(0.9).move_to(r2a)
        n412 = MathTex(num_tex(41.2), color=TXT).scale(0.9).move_to(r2b)
        t_exp = Text("Explicado", color=ESTIMACION).scale(0.55).move_to([r1a.get_center()[0], y1 - 0.85, 0])
        t_sin = Text("Sin explicar", color=ERROR).scale(0.55).move_to([r1b.get_center()[0] + 0.3, y1 - 0.85, 0])
        t_cond = Text("Medias condicionales", color=INK).scale(0.55).move_to([x0 + L / 2, y2 - 0.85, 0])
        t_rec = Text("Una recta", color=INK).scale(0.55).move_to([x0 + L / 2, y1 - 1.4, 0])
        tri = Polygon([5.3, -0.6, 0], [6.6, -0.6, 0], [6.6, 0.5, 0], color=TXT, stroke_width=3).set_fill(TXT, 0.0)
        cuad = Square(0.2, color=TXT, stroke_width=2).move_to([6.5, -0.5, 0])
        t_pit = Text("Pitágoras", color=TXT).scale(0.5).move_to([5.95, -1.1, 0])

        with self.narrar("b3"):
            # «cuatro es tres coma dos más cero coma ocho»
            self.en("cuatro")
            self.corte()
            self.play(Create(marco1), FadeIn(tit1), FadeIn(tot1), run_time=self.dur(0.8))

            # «tres coma dos»
            self.en("t32")
            self.play(FadeIn(r1a), FadeIn(n32), run_time=self.dur(0.6))

            # «cero coma ocho. La varianza»
            self.en("t08")
            self.play(FadeIn(r1b), FadeIn(n08), run_time=self.dur(0.6))

            # «lo que la lectura explica»
            self.en("explica")
            self.play(FadeIn(t_exp), run_time=self.dur(0.5))
            self.resaltar(r1a, color=AMBAR, escala=1.03)

            # «lo que no, el error»
            self.en("noexp")
            self.play(FadeIn(t_sin), run_time=self.dur(0.5))
            self.resaltar(r1b, color=ERROR, escala=1.06)

            # «la misma partición que la de la altura»
            self.en("altura")
            self.play(Create(marco2), FadeIn(tit2), FadeIn(tot2), FadeIn(r2a), FadeIn(r2b), FadeIn(n4056), FadeIn(n412),
                      run_time=self.dur(1.2))

            # «lo que el grupo explica»
            self.en("grupo")
            self.resaltar(r2a, color=AMBAR, escala=1.03)

            # «Allí con medias condicionales»
            self.en("condic")
            self.play(FadeIn(t_cond), run_time=self.dur(0.5))

            # «aquí con una recta»
            self.en("conrecta")
            self.play(FadeIn(t_rec), run_time=self.dur(0.5))

            # «es Pitágoras»
            self.en("pitag")
            self.play(Create(tri), Create(cuad), FadeIn(t_pit), run_time=self.dur(0.8))
