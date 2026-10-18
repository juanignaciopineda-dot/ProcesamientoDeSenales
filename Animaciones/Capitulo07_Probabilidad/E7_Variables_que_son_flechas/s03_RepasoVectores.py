"""Escena 03 — Repaso: vectores y largo (flecha 3, 4 y Pitágoras)."""
from comun.escena import *

O = (-5.0, -2.2)
P = 0.8


class RepasoVectores(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.vectores()
        self.largo()
        self.wait(1.0)
        self.limpiar()

    def vectores(self):
        grilla = cuadricula7(O, P, 5, 6)
        t_vec = self.palabra("Vectores", AMBAR, 0.9).move_to([-2.9, 3.4, 0])
        origen = Dot(punto7(O, 0, 0, P), radius=0.09, color=TXT)
        anillo = Circle(radius=0.28, color=AMBAR, stroke_width=4).move_to(origen)
        u = vec7(O, 3, 4, P, COL_U7)
        casillas = MathTex(r"(\ \_\ ,\ \_\ )", color=TXT).scale(1.4).move_to([3.0, 1.6, 0])
        comp = self.palabra("Componentes", AMBAR, 0.7).move_to([3.0, 3.0, 0])
        horiz = Line(punto7(O, 0, 0, P), punto7(O, 3, 0, P), color=AMBAR, stroke_width=7)
        vert = Line(punto7(O, 3, 0, P), punto7(O, 3, 4, P), color=AMBAR, stroke_width=7)
        par = MathTex("(", "3", ",", "4", ")", color=TXT).scale(1.4).move_to([3.0, 1.6, 0])
        par[1].set_color(AMBAR)
        par[3].set_color(AMBAR)
        l3 = MathTex("3", color=AMBAR).scale(0.9).next_to(horiz, DOWN, buff=0.15)
        l4 = MathTex("4", color=AMBAR).scale(0.9).next_to(vert, RIGHT, buff=0.15)
        with self.narrar("b1"):
            self.en("repaso")
            self.play(FadeIn(grilla), run_time=self.dur(0.5))
            self.pop(t_vec)
            self.en("necesitar")
            self.play(FadeIn(origen), run_time=self.dur(0.4))
            self.en("flecha")
            self.play(GrowArrow(u), run_time=self.dur(0.9))
            self.en("origen")
            self.play(Create(anillo), run_time=self.dur(0.5))
            self.en("dos")
            self.play(FadeOut(anillo), FadeIn(casillas), run_time=self.dur(0.5))
            self.en("componentes")
            self.pop(comp)
            self.en("horiz")
            self.play(Create(horiz), run_time=self.dur(0.8))
            self.en("vert")
            self.play(Create(vert), run_time=self.dur(0.8))
            self.en("par")
            self.play(ReplacementTransform(casillas, par), run_time=self.dur(0.6))
            self.en("tres")
            self.play(FadeIn(l3), run_time=self.dur(0.4))
            self.resaltar(horiz, color=AMBAR, run_time=0.4)
            self.en("cuatro")
            self.play(FadeIn(l4), run_time=self.dur(0.4))
            self.resaltar(vert, color=AMBAR, run_time=0.4)
        self.v = dict(grilla=grilla, t_vec=t_vec, u=u, comp=comp, horiz=horiz, vert=vert, par=par,
                      l3=l3, l4=l4, origen=origen)

    def largo(self):
        v = self.v
        tri = Polygon(punto7(O, 0, 0, P), punto7(O, 3, 0, P), punto7(O, 3, 4, P),
                      color=COL_U7, fill_color=COL_U7, fill_opacity=0.18, stroke_width=0)
        preg = Text("¿Largo?", color=TXT).scale(0.7).move_to(punto7(O, 1.0, 3.2, P))
        F1 = oculta(formula(r"\text{Largo}^2", "=", "3^2", "+", "4^2", escala=1.1).move_to([3.2, 0.2, 0]))
        F2 = oculta(formula("=", "9", "+", "16", escala=1.1).move_to([3.2, -0.9, 0]))
        F3 = oculta(formula("=", "25", escala=1.1, colores={1: AMBAR}).move_to([3.2, -1.9, 0]))
        F4 = oculta(formula(r"\text{Largo}", "=", "5", escala=1.3, colores={2: AMBAR}).move_to([3.2, -3.0, 0]))
        l5 = MathTex("5", color=AMBAR).scale(1.0).move_to(punto7(O, 1.35, 2.35, P) + LEFT * 0.35)
        with self.narrar("b2"):
            self.en("mide")
            self.play(FadeOut(v["par"]), FadeOut(v["comp"]), FadeIn(preg), run_time=self.dur(0.4))
            self.en("triangulo")
            self.play(FadeIn(tri), run_time=self.dur(0.6))
            self.en("catetos")
            self.resaltar(v["l3"], v["l4"], run_time=0.5)
            self.en("pitagoras")
            self.add(F1, F2, F3, F4)
            self.play(*revelar(F1[0], F1[1]), run_time=0.4)
            self.play(*revelar(F1[2], F1[3], F1[4]), run_time=0.6)
            self.en("cuentas")
            self.play(*revelar(F2), run_time=self.dur(0.6))
            self.en("v25")
            self.play(*revelar(F3), run_time=self.dur(0.5))
            self.sfx("pop")
            self.en("cinco")
            self.play(FadeOut(preg), *revelar(F4), FadeIn(l5), run_time=self.dur(0.6))
