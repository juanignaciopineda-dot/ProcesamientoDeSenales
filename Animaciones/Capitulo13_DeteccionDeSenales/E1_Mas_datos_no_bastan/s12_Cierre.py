"""Escena 12 — Cierre: resumen y anuncio del episodio 2, «Toda la señal en un solo número»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        resumen = self.palabra("resumen", AMBAR, 1.7).move_to([0, 3.2, 0])
        F = formula("p_1", r"f(\mathbf{r}\mid H_1)", r"\gtrless", "p_0", r"f(\mathbf{r}\mid H_0)", escala=1.5,
                    colores={0: SENAL, 1: SENAL, 3: RUIDO, 4: RUIDO}).move_to([-0.4, 1.7, 0])
        candado_ic = candado(AMBAR).scale(1.1).next_to(F, RIGHT, buff=0.4)
        R = RectaR(centro=(-4.6, 0.0), ancho=3.0, x_rango=(-1.5, 1.5))
        P = Plano2(centro=(0.0, -0.1), u=0.7, rango=1.6)
        cubo_ic = VGroup(*[Square(side_length=1.4, color=INK, stroke_width=3).shift(RIGHT * d * 0.4 + UP * d * 0.4)
                           for d in (0, 1, 2)]).move_to([4.2, -0.1, 0])
        mil = MathTex(r"\cdots", color=INK).scale(1.8).next_to(cubo_ic, RIGHT, buff=0.3)
        x_p0 = MathTex(r"\times\,p_0", color=RUIDO).scale(1.2).move_to([-3.4, -1.6, 0])
        x_p1 = MathTex(r"\times\,p_1", color=SENAL).scale(1.2).move_to([-1.6, -1.6, 0])
        alta = Arrow([0.4, -2.2, 0], [0.4, -1.4, 0], buff=0, color=AMBAR, stroke_width=5)
        alta_t = etiqueta("la más alta", AMBAR, 0.75).next_to(alta, DOWN, buff=0.1)
        prom = MathTex(r"\frac{r_1+r_2}{2}", color=AMBAR).scale(1.5).move_to([3.6, -2.3, 0])
        tira = Arrow([2.6, -3.2, 0], [4.8, -3.2, 0], buff=0, color=ROJO, stroke_width=5)
        nobastan = VGroup(Text("más datos", color=TXT, weight=BOLD).scale(1.2),
                          Text("mejor decisión", color=INK, weight=BOLD).scale(1.2)).arrange(RIGHT, buff=0.6)
        nobastan.move_to([-1.2, -3.55, 0])
        tach = tachar(nobastan[1])
        sinperder = RoundedRectangle(corner_radius=0.15, width=4.0, height=2.4, color=VERDE, stroke_width=4,
                                     fill_color=VERDE, fill_opacity=0.08).move_to([0, 0.0, 0])
        tl = tilde(VERDE, 1.6).move_to(sinperder.get_center())
        tarjeta = caja("Episodio 2", AMBAR, ancho=4.6, alto=1.2, scale=0.95).move_to([0, 2.6, 0])
        titulo_e2 = self.palabra("Toda la señal en un solo número", AMBAR, 1.0).move_to([0, 0.6, 0])

        with self.narrar("b1"):
            # «Resumimos»
            self.en("resumen")
            self.corte()
            self.pop(resumen)

            # «no cambia»
            self.en("nocambia")
            self.play(*[FadeIn(F[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(0.8))
            self.play(FadeIn(candado_ic, scale=0.5), run_time=self.dur(0.4))

            # «uno, dos o mil datos»
            self.en("datos")
            self.play(FadeIn(R), FadeIn(P.ejes), FadeIn(P.rot1), FadeIn(P.rot2), FadeIn(cubo_ic, lag_ratio=0.3),
                      FadeIn(mil), run_time=self.dur(1.2))

            # «escalar por el a priori»
            self.en("escalar")
            self.play(FadeIn(x_p0), FadeIn(x_p1), run_time=self.dur(0.5))

            # «quedarse con la más alta»
            self.en("alta")
            self.play(GrowArrow(alta), FadeIn(alta_t), run_time=self.dur(0.6))

            # «promediar los datos»
            self.en("promediar")
            self.play(FadeIn(prom, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «puede tirar justo lo que necesitabas»
            self.en("tirar")
            self.play(GrowArrow(tira), run_time=self.dur(0.6))

            # «más datos no bastan»
            self.en("nobastan")
            self.play(FadeIn(nobastan), run_time=self.dur(0.4))
            self.play(Create(tach), run_time=self.dur(0.4))

            # «sin perder nada»
            self.en("sinperder")
            self.corte()
            self.play(FadeIn(sinperder), FadeIn(tl, scale=0.5), run_time=self.dur(0.6))

            # «el próximo episodio»
            self.en("proximo")
            self.corte()
            self.play(FadeIn(tarjeta, scale=0.7), run_time=self.dur(0.5))

            # «toda la señal en un solo número»
            self.en("titulo")
            self.pop(titulo_e2)
        self.wait(1.0)
        self.limpiar()
