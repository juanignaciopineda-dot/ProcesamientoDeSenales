"""Escena 06 — Dos opciones extremas (h = 0 y h = 1) y el error de cualquier h."""
from comun.escena import *


class DosOpciones(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.extremos()
        self.cuenta()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def extremos(self):
        f = formula(r"\hat{y}", "=", "20", "+", "h", "(", "x", "-", "20", ")", escala=1.3,
                    colores={0: ESTIMACION, 4: ESTIMACION, 6: MEDIDA}).move_to([0, 3.2, 0])
        card_i = RoundedRectangle(width=5.2, height=4.4, corner_radius=0.15, color=INK, stroke_width=2.5)
        card_i.move_to([-3.6, 0.4, 0])
        card_d = card_i.copy().move_to([3.6, 0.4, 0])
        h0 = MathTex("h=0", color=AMBAR).scale(1.2).move_to([-3.6, 2.0, 0])
        termo_i = termometro(1.1, ROJO, 0.6).move_to([-5.3, 0.7, 0])
        tach = tachar(termo_i)
        a20 = MathTex(r"\hat{y}=20", color=ESTIMACION).scale(1.0).move_to([-3.3, 0.9, 0])
        err_i = Text("Error", color=ERROR).scale(0.5).move_to([-5.8, -0.4, 0], aligned_edge=LEFT)
        bar_i = Rectangle(width=3.4, height=0.45, stroke_width=0).set_fill(ERROR, 0.85)
        bar_i.move_to([-5.8 + 1.7, -1.0, 0])
        v4 = MathTex("4", color=ERROR).scale(0.9).move_to([-1.8, -1.0, 0])
        h1 = MathTex("h=1", color=AMBAR).scale(1.2).move_to([3.6, 2.0, 0])
        termo_d = termometro(1.1, ROJO, 0.6).move_to([1.9, 0.7, 0])
        a23 = MathTex(r"\hat{y}=23", color=ESTIMACION).scale(1.0).move_to([4.2, 0.9, 0])
        err_d = Text("Error", color=ERROR).scale(0.5).move_to([1.4, -0.4, 0], aligned_edge=LEFT)
        bar_d = Rectangle(width=0.85, height=0.45, stroke_width=0).set_fill(ERROR, 0.85)
        bar_d.move_to([1.4 + 0.425, -1.0, 0])
        v1 = MathTex("1", color=ERROR).scale(0.9).move_to([2.7, -1.0, 0])
        flecha_m = Arrow([-3.4, -2.6, 0], [3.4, -2.6, 0], buff=0, color=ESTIMACION, stroke_width=5,
                         max_tip_length_to_length_ratio=0.1)
        mejor = Text("Mucho mejor", color=ESTIMACION, weight=BOLD).scale(0.6).move_to([0, -3.2, 0])
        entre = MathTex(r"h=?", color=AMBAR).scale(0.9).move_to([0, 0.4, 0])

        with self.narrar("b1"):
            # «Queda elegir hache»
            self.en("elegir")
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in range(10)], run_time=self.dur(0.8))
            self.play(Indicate(f[4], color=AMBAR), run_time=self.dur(0.7))

            # «Dos opciones extremas»
            self.en("dos")
            self.play(Create(card_i), Create(card_d), run_time=self.dur(0.8))

            # «hache igual a cero»
            self.en("h0")
            self.pop(h0)

            # «ignoramos el termómetro»
            self.en("ign")
            self.play(FadeIn(termo_i), run_time=self.dur(0.4))
            self.play(Create(tach), run_time=self.dur(0.4))

            # «apostamos veinte»
            self.en("a20")
            self.play(FadeIn(a20, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «la varianza de la temperatura, cuatro»
            self.en("e4")
            self.play(FadeIn(err_i), GrowFromEdge(bar_i, LEFT), run_time=self.dur(0.8))
            self.pop(v4)

            # «hache igual a uno»
            self.en("h1")
            self.pop(h1)

            # «nos lo creemos a ciegas»
            self.en("ciegas")
            self.play(FadeIn(termo_d), run_time=self.dur(0.4))
            self.resaltar(termo_d, color=AMBAR, escala=1.15)

            # «apostamos veintitrés»
            self.en("a23")
            self.play(FadeIn(a23, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «el del ruido, uno»
            self.en("e1")
            self.play(FadeIn(err_d), GrowFromEdge(bar_d, LEFT), run_time=self.dur(0.6))
            self.pop(v1)

            # «Mucho mejor»
            self.en("mejor")
            self.play(GrowArrow(flecha_m), run_time=self.dur(0.6))
            self.pop(mejor)

            # «¿y si lo mejor está entre medias?»
            self.en("entre")
            self.pop(entre)
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def cuenta(self):
        nota_c = Text("Todo centrado: restamos 20", color=INK).scale(0.55).move_to([0, 3.5, 0])
        J = formula("J(h)", "=", r"E\big[", "(", "y", "-", "h", "x", ")^2", r"\big]", escala=1.3,
                    colores={0: ERROR, 4: SENAL, 6: ESTIMACION, 7: MEDIDA, 8: ERROR}).move_to([0, 2.5, 0])
        fila = formula(r"(y-hx)^2", "=", "y^2", "-", r"2h\,y\,x", "+", r"h^2\,x^2", escala=1.3,
                       colores={2: SENAL, 4: MEDIDA, 6: MEDIDA}).move_to([0, 1.1, 0])
        fila[4].set_color(AMBAR)
        medias = formula(r"E[y^2]", "-", r"2h\,E[yx]", "+", r"h^2\,E[x^2]", escala=1.2).move_to([0, -0.2, 0])
        r_yy = SurroundingRectangle(medias[0], color=AMBAR, buff=0.08)
        r_yx = SurroundingRectangle(medias[2], color=AMBAR, buff=0.08)
        r_xx = SurroundingRectangle(medias[4], color=AMBAR, buff=0.08)
        v4 = MathTex(r"E[y^2]=4", color=SENAL).scale(0.95).move_to([-4.2, -1.5, 0])
        c4 = MathTex(r"E[y\,x]=4", color=TXT).scale(0.95).move_to([-4.2, -2.4, 0])
        c5 = MathTex(r"E[x^2]=4+1=5", color=TXT).scale(0.95).move_to([-4.2, -3.3, 0])
        xyr = MathTex("x", "=", "y", "+", "v", color=TXT).scale(0.95).move_to([3.8, -1.5, 0])
        xyr[0].set_color(MEDIDA)
        xyr[2].set_color(SENAL)
        xyr[4].set_color(RUIDO)
        norel = MathTex(r"E[y\,v]=0", color=RUIDO).scale(0.95).move_to([3.8, -2.4, 0])

        with self.narrar("b2"):
            # «Con todo centrado»
            self.en("centrado")
            self.corte()
            self.play(FadeIn(nota_c), run_time=self.dur(0.5))

            # «es la media»
            self.en("jmedia")
            self.play(FadeIn(J[0]), FadeIn(J[1]), FadeIn(J[2]), FadeIn(J[9]), run_time=self.dur(0.4))

            # «de la temperatura menos hache por la lectura»
            self.en("jdif")
            self.play(*[FadeIn(J[i], shift=UP * 0.1) for i in range(3, 8)], run_time=self.dur(0.6))

            # «al cuadrado»
            self.en("jcuad")
            self.play(FadeIn(J[8], shift=UP * 0.1), run_time=self.dur(0.4))

            # «Desarrollamos el cuadrado»
            self.en("des")
            self.play(*[FadeIn(fila[i], shift=UP * 0.1) for i in range(7)], run_time=self.dur(1.2))

            # «tomamos la media de cada término»
            self.en("medias")
            self.play(*[FadeIn(medias[i], shift=DOWN * 0.1) for i in range(5)], run_time=self.dur(1.0))

            # «La de la temperatura al cuadrado»
            self.en("yy")
            self.play(Create(r_yy), FadeIn(v4, shift=UP * 0.1), run_time=self.dur(0.6))

            # «La de la temperatura por la lectura»
            self.en("yx")
            self.play(FadeOut(r_yy), Create(r_yx), run_time=self.dur(0.4))

            # «también es cuatro»
            self.en("c4")
            self.play(FadeIn(c4, shift=UP * 0.1), run_time=self.dur(0.5))

            # «porque el ruido no tiene nada que ver»
            self.en("norel")
            self.play(FadeIn(xyr), run_time=self.dur(0.5))
            self.play(FadeIn(norel, shift=UP * 0.1), run_time=self.dur(0.5))

            # «la de la lectura al cuadrado»
            self.en("xx")
            self.play(FadeOut(r_yx), Create(r_xx), run_time=self.dur(0.4))

            # «cuatro más uno: cinco»
            self.en("c5")
            self.play(FadeIn(c5, shift=UP * 0.1), run_time=self.dur(0.6))
