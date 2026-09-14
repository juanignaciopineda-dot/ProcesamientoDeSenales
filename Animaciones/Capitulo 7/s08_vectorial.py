"""Escena 8 - Las variables aleatorias como vectores.

El cierre del capitulo: E[XY] es un producto interno legitimo, la norma
al cuadrado es el segundo momento, y con variables centradas el
coeficiente de correlacion es literalmente el coseno del angulo. De aca
sale toda la interpretacion geometrica del capitulo 8.

    manim -pql s08_vectorial.py Vectorial
"""
from manim import *
import numpy as np
from comun import *


class Vectorial(Scene):
    def construct(self):
        configurar()

        tit = titulo("Las variables aleatorias son vectores")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.4)

        # ============================================ las tres propiedades
        idea = Text("Si E[XY] es un producto interno de verdad, "
                    "toda la geometría se aplica.", color=TXT).scale(0.55)
        idea.next_to(tit, DOWN, buff=0.4)
        self.play(FadeIn(idea))
        self.wait(1.2)

        props = VGroup(
            VGroup(Text("simetría", color=INK).scale(0.5),
                   MathTex(r"\langle X,Y\rangle=\langle Y,X\rangle",
                           color=VERDE).scale(0.62)).arrange(RIGHT, buff=0.35),
            VGroup(Text("linealidad", color=INK).scale(0.5),
                   MathTex(r"\langle X,a_1Y_1+a_2Y_2\rangle="
                           r"a_1\langle X,Y_1\rangle+a_2\langle X,Y_2\rangle",
                           color=VERDE).scale(0.62)).arrange(RIGHT, buff=0.35),
            VGroup(Text("positividad", color=INK).scale(0.5),
                   MathTex(r"\langle X,X\rangle=E[X^2]>0",
                           color=VERDE).scale(0.62)).arrange(RIGHT, buff=0.35),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        props.next_to(idea, DOWN, buff=0.5)

        for p in props:
            self.play(FadeIn(p, shift=RIGHT * 0.15), run_time=0.65)
        self.wait(1.0)
        ok = veredicto(True, "las tres se cumplen: es un producto interno legítimo")
        ok.next_to(props, DOWN, buff=0.45)
        self.play(FadeIn(ok))
        self.wait(2.0)
        self.play(FadeOut(VGroup(idea, props, ok)))

        # ============================================ el diccionario
        dicc = VGroup(
            MathTex(r"\|X\|^2 = E[X^2]", color=AZUL).scale(0.72),
            MathTex(r"\langle X,Y\rangle = E[XY] = r_{X,Y}", color=AMBAR).scale(0.72),
        ).arrange(DOWN, buff=0.35)
        dicc.next_to(tit, DOWN, buff=0.55)
        self.play(Write(dicc[0]))
        self.wait(0.5)
        self.play(Write(dicc[1]))
        self.wait(1.4)

        centrar = Text("Ahora, con las variables CENTRADAS:", color=INK).scale(0.55)
        centrar.next_to(dicc, DOWN, buff=0.5)
        cent = MathTex(r"\tilde{X}=X-\mu_X\ ,\qquad \tilde{Y}=Y-\mu_Y",
                       color=TXT).scale(0.68)
        cent.next_to(centrar, DOWN, buff=0.28)
        self.play(FadeIn(centrar), Write(cent))
        self.wait(1.0)

        dicc2 = VGroup(
            MathTex(r"\|\tilde{X}\| = \sigma_X", color=AZUL).scale(0.72),
            MathTex(r"\langle \tilde{X},\tilde{Y}\rangle = \sigma_{X,Y}",
                    color=AMBAR).scale(0.72),
        ).arrange(RIGHT, buff=1.1)
        dicc2.next_to(cent, DOWN, buff=0.45)
        self.play(Write(dicc2))
        self.wait(1.0)
        remate = nota("la norma pasa a ser el desvío y el producto interno, "
                      "la covarianza", scale=0.48)
        remate.next_to(dicc2, DOWN, buff=0.25)
        self.play(FadeIn(remate))
        self.wait(2.2)
        self.play(FadeOut(VGroup(dicc, centrar, cent, dicc2, remate)))

        # ============================================ el dibujo
        tit2 = titulo("ρ es el coseno del ángulo")
        self.play(Transform(tit, tit2))

        origen = LEFT * 2.6 + DOWN * 0.9
        LX, LY = 3.4, 2.6
        rho = ValueTracker(0.6)

        vx = Arrow(origen, origen + RIGHT * LX, color=AZUL, buff=0,
                   stroke_width=6, max_tip_length_to_length_ratio=0.09)
        vx_lbl = MathTex(r"\tilde{X}", color=AZUL).scale(0.75)
        vx_lbl.next_to(vx.get_end(), DR, buff=0.12)

        def vec_y():
            th = np.arccos(np.clip(rho.get_value(), -1, 1))
            fin = origen + np.array([LY * np.cos(th), LY * np.sin(th), 0])
            return Arrow(origen, fin, color=VERDE, buff=0, stroke_width=6,
                         max_tip_length_to_length_ratio=0.12)

        vy = always_redraw(vec_y)
        vy_lbl = always_redraw(lambda: MathTex(r"\tilde{Y}", color=VERDE)
                               .scale(0.75).next_to(vec_y().get_end(), UR,
                                                    buff=0.1))
        arco = always_redraw(lambda: Angle(
            Line(origen, origen + RIGHT * LX), Line(origen, vec_y().get_end()),
            radius=0.75, color=AMBAR, stroke_width=3))
        th_lbl = always_redraw(lambda: MathTex(r"\theta", color=AMBAR).scale(0.62)
                               .move_to(origen + np.array([
                                   1.05 * np.cos(np.arccos(np.clip(rho.get_value(), -1, 1)) / 2),
                                   1.05 * np.sin(np.arccos(np.clip(rho.get_value(), -1, 1)) / 2),
                                   0])))

        self.play(GrowArrow(vx), FadeIn(vx_lbl))
        self.play(GrowArrow(vy), FadeIn(vy_lbl))
        self.play(Create(arco), FadeIn(th_lbl))
        self.wait(0.6)

        # las normas, con llaves
        n_x = MathTex(r"\|\tilde{X}\|=\sigma_X", color=AZUL).scale(0.55)
        n_x.next_to(vx, DOWN, buff=0.32)
        self.play(FadeIn(n_x))
        self.wait(0.5)

        # el panel de la derecha
        formula = MathTex(r"\sigma_{X,Y}", r"=", r"\sigma_X\,\sigma_Y\,\cos\theta")
        formula[0].set_color(AMBAR)
        formula.scale(0.8).to_edge(RIGHT, buff=1.0).shift(UP * 0.9)
        despeje = MathTex(r"\rho_{X,Y}", r"=", r"\cos\theta")
        despeje[0].set_color(AMBAR); despeje[2].set_color(AMBAR)
        despeje.scale(0.95).next_to(formula, DOWN, buff=0.55)

        self.play(Write(formula))
        self.wait(0.8)
        self.play(Write(despeje))
        self.wait(0.6)

        lector = always_redraw(lambda: VGroup(
            VGroup(MathTex(r"\rho =", color=INK).scale(0.65),
                   DecimalNumber(rho.get_value(), num_decimal_places=2,
                                 color=AMBAR, include_sign=True).scale(0.65)
                   ).arrange(RIGHT, buff=0.12),
            VGroup(MathTex(r"\theta =", color=INK).scale(0.65),
                   DecimalNumber(np.degrees(np.arccos(np.clip(rho.get_value(), -1, 1))),
                                 num_decimal_places=0, color=AMBAR,
                                 unit=r"^{\circ}").scale(0.65),
                   ).arrange(RIGHT, buff=0.12),
        ).arrange(DOWN, buff=0.2).next_to(despeje, DOWN, buff=0.6))
        self.play(FadeIn(lector))
        self.wait(0.8)

        # ------------------------------------------------ barrer rho
        casos = [
            (0.98, "casi alineados: casi la misma información"),
            (0.0, "perpendiculares: no correlacionadas"),
            (-0.95, "opuestos: relación lineal negativa"),
            (0.6, None),
        ]
        for destino, txt in casos:
            self.play(rho.animate.set_value(destino), run_time=2.0,
                      rate_func=rate_functions.ease_in_out_sine)
            if txt:
                c = Text(txt, color=INK).scale(0.5)
                c.to_edge(DOWN, buff=0.45)
                self.play(FadeIn(c))
                self.wait(1.4)
                self.play(FadeOut(c))
            else:
                self.wait(0.4)

        # ------------------------------------------------ ortogonalidad
        orto = MathTex(r"E[XY]=0 \iff X\perp Y", color=VERDE).scale(0.78)
        orto.to_edge(DOWN, buff=0.5)
        self.play(Write(orto))
        self.wait(0.6)
        orto_n = nota("por eso decimos “ortogonales”: es literalmente la "
                      "condición de ortogonalidad", scale=0.47)
        orto_n.next_to(orto, UP, buff=0.2)
        self.play(FadeIn(orto_n))
        self.wait(2.4)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(vx, vx_lbl, vy, vy_lbl, arco, th_lbl, n_x,
                                 formula, despeje, lector, orto, orto_n)))
        cierre = VGroup(
            Text("Todo lo que sabés de vectores se aplica.", color=TXT).scale(0.62),
            nota("Y esto no es una analogía forzada: la correlación cumple las\n"
                 "tres propiedades de un producto interno, así que ES uno.",
                 scale=0.5),
            Text("En el capítulo 8, estimar va a ser proyectar.",
                 color=AMBAR).scale(0.6),
        ).arrange(DOWN, buff=0.35)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.12))
        self.wait(0.5)
        self.play(FadeIn(cierre[1]))
        self.wait(0.8)
        self.play(FadeIn(cierre[2], shift=UP * 0.12))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
