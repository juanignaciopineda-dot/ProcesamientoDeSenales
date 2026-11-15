"""Escena 10 — Promediar las dos mediciones: sale un triángulo y la hipótesis uno nunca gana."""
from comun.escena import *

ESC = 2.0           # centímetros de pantalla por unidad de densidad (triángulos)


class ElPromedio(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.promedio()
        self.triangulos()
        self.siempre_cero()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def promedio(self):
        P = Plano2(centro=(-3.7, -0.3), u=1.6)
        diag = DashedLine(P.p(-1.45, -1.45), P.p(1.45, 1.45), color=AMBAR, stroke_width=3)
        pts = [(0.7, -0.4), (-0.3, 0.6), (-0.6, -0.5)]
        dots = VGroup(*[Dot(P.p(x, y), radius=0.13, color=MEDIDA) for x, y in pts])
        F = formula("a", "=", "(r_1", "+", "r_2)", "/", "2", escala=1.4,
                    colores={0: AMBAR}).move_to([3.5, 3.0, 0])
        Ra = RectaR(centro=(3.5, -0.8), ancho=6.2, x_rango=(-1.2, 1.2), rotulo="a")
        interrog = Text("?", color=AMBAR, weight=BOLD).scale(1.9).move_to([3.5, 0.8, 0])
        anti = DashedLine(P.p(1.15, -1.15), P.p(-1.15, 1.15), color=INK, stroke_width=2.5)
        pares = VGroup(*[Dot(P.p(x, -x), radius=0.13, color=MEDIDA) for x in (0.95, 0.4, -0.5)])
        flecha_c = Arrow(P.p(1.05, -0.5) + RIGHT * 0.4, Ra.p(0) + UP * 0.1, buff=0.1, color=AMBAR, stroke_width=3)
        altobajo = MathTex(r"(1,-1)\to 0", color=TXT).scale(1.1).move_to([3.5, -1.9, 0])
        borde = MathTex(r"(1,1)\to 1", color=TXT).scale(1.1).move_to([3.5, -2.8, 0])
        tri = tri_dens(Ra, -1, 1, 1.0, 2.0, MEDIDA)
        self.P, self.Ra, self.tri_a = P, Ra, tri
        self.quitar_b1 = VGroup(P.ejes, P.rot1, P.rot2, P.grande, P.pequeno, diag, dots, F, Ra, interrog, anti,
                                pares, flecha_c, altobajo, borde, tri)

        with self.narrar("b1"):
            # «Probemos la idea más natural»
            self.en("natural")
            self.corte()
            self.play(FadeIn(P.ejes), FadeIn(P.rot1), FadeIn(P.rot2), FadeIn(P.grande), FadeIn(P.pequeno),
                      Create(diag), run_time=self.dur(0.8))

            # «Tengo dos mediciones»
            self.en("tengo")
            self.play(P.rot1.animate(rate_func=there_and_back).scale(1.5).set_color(AMBAR),
                      P.rot2.animate(rate_func=there_and_back).scale(1.5).set_color(AMBAR), run_time=self.dur(0.7))

            # «decido promediarlas»
            self.en("promediar")
            self.play(FadeIn(dots), run_time=0.3)
            destinos = []
            for p in dots:
                x, y = (p.get_center()[0] - P.cx) / P.u, (p.get_center()[1] - P.cy) / P.u
                destinos.append(P.p((x + y) / 2, (x + y) / 2))
            self.play(*[p.animate.move_to(d) for p, d in zip(dots, destinos)], run_time=self.dur(0.8))

            # «a igual a»
            self.en("a")
            self.play(FadeIn(F[0]), FadeIn(F[1]), run_time=self.dur(0.4))

            # «erre uno»
            self.en("r1")
            self.play(FadeIn(F[2], shift=UP * 0.1), run_time=self.dur(0.4))

            # «más erre dos»
            self.en("r2")
            self.play(FadeIn(F[3]), FadeIn(F[4], shift=UP * 0.1), run_time=self.dur(0.5))

            # «entre dos»
            self.en("ent2")
            self.play(FadeIn(F[5]), FadeIn(F[6]), run_time=self.dur(0.5))

            # «¿Cómo se distribuye ese promedio?»
            self.en("distrib")
            self.play(FadeIn(Ra), FadeIn(interrog), run_time=self.dur(0.6))

            # «Hay muchas maneras»
            self.en("maneras")
            self.play(FadeOut(dots), FadeIn(anti), FadeIn(pares, lag_ratio=0.3), run_time=self.dur(1.0))

            # «cerca del centro»
            self.en("centro")
            self.play(FadeOut(interrog), GrowArrow(flecha_c), run_time=self.dur(0.7))

            # «un número alto y otro bajo»
            self.en("altobajo")
            self.play(FadeIn(altobajo), run_time=self.dur(0.5))

            # «en el borde»
            self.en("borde")
            self.play(FadeIn(borde), run_time=self.dur(0.5))

            # «Sale un triángulo»
            self.en("triangulo")
            self.play(Create(tri), run_time=self.dur(0.9))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def triangulos(self):
        R = self.R = RectaR(centro=(0.0, -2.0), ancho=10.0, x_rango=(-1.5, 1.5), rotulo="a")
        t0 = tri_dens(R, -1, 1, 1.0, ESC, RUIDO)
        t1 = tri_dens(R, -0.5, 0.5, 2.0, ESC, SENAL)
        t0s = tri_dens(R, -1, 1, 0.75, ESC, RUIDO)
        t1s = tri_dens(R, -0.5, 0.5, 0.5, ESC, SENAL)
        self.t0, self.t1 = t0, t1
        self.t0s, self.t1s = t0s, t1s
        b2a1 = MathTex(r"\text{base }2\cdot\text{altura }1", color=RUIDO).scale(1.05).move_to([-4.0, 3.4, 0])
        b1a2 = MathTex(r"\text{base }1\cdot\text{altura }2", color=SENAL).scale(1.05).move_to([4.0, 3.4, 0])
        xp0 = MathTex(r"\times\,p_0", color=RUIDO).scale(1.3).move_to([-4.6, 2.3, 0])
        xp1 = MathTex(r"\times\,p_1", color=SENAL).scale(1.3).move_to([4.6, 2.3, 0])
        y0 = -2.0 + 0.75 * ESC
        y1 = -2.0 + 0.5 * ESC
        g0 = DashedLine([R.p(-1)[0] - 0.3, y0, 0], [R.p(1)[0] + 0.3, y0, 0], color=RUIDO, stroke_width=2.5)
        g1 = DashedLine([R.p(-1)[0] - 0.3, y1, 0], [R.p(1)[0] + 0.3, y1, 0], color=SENAL, stroke_width=2.5)
        l34 = MathTex(r"\tfrac34", color=RUIDO).scale(1.3).move_to([R.p(-1)[0] - 0.8, y0 + 0.2, 0])
        l12 = MathTex(r"\tfrac12", color=SENAL).scale(1.3).move_to([R.p(1)[0] + 0.8, y1 - 0.3, 0])
        mas = MathTex(r"\tfrac34>\tfrac12", color=AMBAR).scale(1.7).move_to([0, 2.9, 0])
        self.fuera_b3 = VGroup(b2a1, b1a2, xp0, xp1, mas)

        with self.narrar("b2"):
            # «Bajo la hipótesis cero»
            self.en("t0")
            self.play(FadeOut(self.quitar_b1), run_time=0.3)
            self.add(R)
            self.play(Create(t0), run_time=self.dur(0.7))

            # «base dos y altura uno»
            self.en("b2a1")
            self.play(FadeIn(b2a1, shift=UP * 0.1), t0.animate.set_fill(RUIDO, 0.5), run_time=self.dur(0.6))

            # «Bajo la hipótesis uno»
            self.en("t1")
            self.play(Create(t1), run_time=self.dur(0.7))

            # «base uno y altura dos»
            self.en("b1a2")
            self.play(FadeIn(b1a2, shift=UP * 0.1), t1.animate.set_fill(SENAL, 0.5), run_time=self.dur(0.6))

            # «Ya sabes lo que sigue»
            self.en("sabes")
            self.play(FadeIn(xp0), FadeIn(xp1), run_time=self.dur(0.5))

            # «escalamos por el a priori»
            self.en("escalamos")
            self.play(Transform(t0, t0s), Transform(t1, t1s), run_time=self.dur(1.2))

            # «La hipótesis cero llega»
            self.en("llega")
            self.play(Create(g0), run_time=self.dur(0.5))

            # «tres cuartos en el centro»
            self.en("tc")
            self.play(FadeIn(l34), run_time=self.dur(0.4))

            # «a un medio»
            self.en("medio")
            self.play(Create(g1), FadeIn(l12), run_time=self.dur(0.6))

            # «Tres cuartos es más que un medio»
            self.en("mas")
            self.pop(mas)
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def siempre_cero(self):
        R = self.R
        self.play(FadeOut(self.fuera_b3), run_time=0.01)
        dot = Dot(R.p(0), radius=0.17, color=MEDIDA).shift(UP * 0.0)
        corte = DashedLine(R.p(0.5) + UP * 0.1, R.p(0.5) + UP * 1.0, color=AMBAR, stroke_width=3)
        rel = tri_dens(R, -1, 1, 0.75, ESC, RUIDO, 0.55)
        optima = Text("regla óptima", color=AMBAR, weight=BOLD).scale(1.0).move_to([-4.6, 2.8, 0])
        siempre = VGroup(Text("siempre", color=AMBAR, weight=BOLD).scale(1.0),
                         MathTex("H_0", color=RUIDO).scale(1.4)).arrange(RIGHT, buff=0.25).move_to([-4.6, 1.7, 0])
        uncuarto = MathTex(r"P_e=\tfrac14", color=ROJO).scale(1.8).move_to([4.7, 2.8, 0])
        igual = MathTex("=", color=INK).scale(1.5).move_to([4.7, 1.9, 0])
        cas = casillas(4, rojas=(0,), centro=(4.7, 1.1), lado=0.6)
        sola = Text("una sola medición", color=INK).scale(0.65).move_to([4.7, 0.4, 0])

        with self.narrar("b3"):
            # «a medida que nos alejamos»
            self.en("alejamos")
            self.play(FadeIn(dot), run_time=0.2)
            self.play(dot.animate.move_to(R.p(0.9)), run_time=self.dur(1.2))

            # «baja más deprisa»
            self.en("deprisa")
            self.play(Create(corte), self.t1.animate.set_stroke(AMBAR, 5), run_time=self.dur(0.8))

            # «En ningún punto le gana»
            self.en("ninguno")
            self.play(FadeIn(rel), run_time=self.dur(0.7))

            # «la regla óptima sobre el promedio»
            self.en("optima")
            self.pop(optima)

            # «decir siempre»
            self.en("siempre")
            self.pop(siempre)

            # «vuelve a ser un cuarto»
            self.en("uncuarto")
            self.pop(uncuarto)

            # «con una sola medición»
            self.en("igual")
            self.play(FadeIn(igual), FadeIn(cas), FadeIn(sola), run_time=self.dur(0.7))
        self.wait(0.3)
