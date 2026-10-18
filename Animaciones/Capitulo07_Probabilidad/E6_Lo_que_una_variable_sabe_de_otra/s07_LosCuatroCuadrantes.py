"""Escena 07 — Centrar la nube: cuatro cuadrantes y el signo del producto."""
from comun.escena import *


class LosCuatroCuadrantes(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        ax, et = ejes((0, 6, 1), (0, 6, 1), ancho=7.2, alto=5.6, x_label="x", y_label="y")
        g = VGroup(ax, et).move_to([-2.6, -0.2, 0])
        self.ax = ax
        c0 = ax.c2p(3, 3)
        ur, dl = ax.c2p(5.9, 5.9), ax.c2p(0.1, 0.1)

        def cuadrante(sx, sy, col):
            x1 = ur[0] if sx > 0 else dl[0]
            y1 = ur[1] if sy > 0 else dl[1]
            r = Rectangle(width=abs(x1 - c0[0]), height=abs(y1 - c0[1]), color=col, fill_opacity=0.2, stroke_width=0)
            return r.move_to([(x1 + c0[0]) / 2, (y1 + c0[1]) / 2, 0])

        def nube_de(aa, bb, colorear):
            return VGroup(*[Dot(self.P(u, v), radius=0.09,
                                color=(VERDE if u * v > 0 else ROJO) if colorear else SENAL) for u, v in zip(aa, bb)])

        a, b = puntos_corr(0.8, 34, 6)
        a, b = np.clip(a, -2.5, 2.5), np.clip(b, -2.5, 2.5)
        _, b0 = puntos_corr(0.0, 34, 6)
        b0 = np.clip(b0, -2.5, 2.5)
        nube = nube_de(a, b, False)

        def signos(txt, x, y, col):
            return Text(txt, color=col).scale(0.7).move_to(ax.c2p(x, y))

        with self.narrar("b1"):
            # «Movamos el origen»
            self.en("origen")
            self.play(Create(g), FadeIn(nube, scale=0.5), run_time=self.dur(0.6))
            h = Line(ax.c2p(0.2, 3), ax.c2p(5.9, 3), color=INK, stroke_width=3)
            v = Line(ax.c2p(3, 0.2), ax.c2p(3, 5.9), color=INK, stroke_width=3)
            self.play(FadeOut(g), Create(h), Create(v), run_time=self.dur(0.8))

            # «a cada variable le restamos su media»
            self.en("restar")
            lx = formula("X", "-", r"\mu_X", escala=1.0, colores={0: SENAL, 2: AMBAR}).next_to(h.get_end(), RIGHT, buff=0.2)
            ly = formula("Y", "-", r"\mu_Y", escala=1.0, colores={0: MEDIDA, 2: AMBAR}).next_to(v.get_end(), UP, buff=0.15)
            self.play(FadeIn(lx), FadeIn(ly), run_time=self.dur(0.6))

            # «su media»
            self.en("su_media")
            centro = Dot(c0, radius=0.16, color=AMBAR)
            self.pop(centro)

            # «Ahora el plano»
            self.en("ahora")
            self.resaltar(h, v, color=AMBAR, escala=1.05)

            # «cuatro cuadrantes»
            self.en("cuadrantes")
            q = [cuadrante(1, 1, INK), cuadrante(-1, -1, INK), cuadrante(-1, 1, INK), cuadrante(1, -1, INK)]
            for r in q:
                r.set_fill(INK, 0.08)
            self.play(*[FadeIn(r) for r in q], run_time=self.dur(0.6))

            # «Arriba a la derecha»
            self.en("ard")
            self.play(q[0].animate.set_fill(VERDE, 0.25), FadeIn(signos("+ · + = +", 4.6, 5.55, VERDE)),
                      run_time=self.dur(0.5))

            # «abajo a la izquierda»
            self.en("abi")
            self.play(q[1].animate.set_fill(VERDE, 0.25), FadeIn(signos("− · − = +", 1.4, 0.45, VERDE)),
                      run_time=self.dur(0.5))

            # «el producto es positivo»
            self.en("positivo")
            self.play(q[0].animate(rate_func=there_and_back).set_fill(VERDE, 0.5),
                      q[1].animate(rate_func=there_and_back).set_fill(VERDE, 0.5), run_time=self.dur(0.8))

            # «En los otros dos»
            self.en("otros_dos")
            self.play(q[2].animate(rate_func=there_and_back).set_fill(ROJO, 0.4),
                      q[3].animate(rate_func=there_and_back).set_fill(ROJO, 0.4), run_time=self.dur(0.8))

            # «negativo»
            self.en("neg")
            self.play(q[2].animate.set_fill(ROJO, 0.25), q[3].animate.set_fill(ROJO, 0.25),
                      FadeIn(signos("+ · − = −", 4.6, 0.45, ROJO)), FadeIn(signos("− · + = −", 1.4, 5.55, ROJO)),
                      run_time=self.dur(0.6))

            # «Si la nube sube hacia la derecha»
            self.en("sube")
            self.play(Transform(nube, nube_de(a, b, True)), run_time=self.dur(0.8))

            # «ganan los positivos»
            self.en("gana_pos")
            mas = Text("+", color=VERDE, weight=BOLD).scale(3.5).move_to([5.0, 1.4, 0])
            self.pop(mas)

            # «Si baja»
            self.en("baja")
            self.play(Transform(nube, nube_de(a, -b, True)), run_time=self.dur(0.8))

            # «ganan los negativos»
            self.en("gana_neg")
            menos = Text("−", color=ROJO, weight=BOLD).scale(3.5).move_to([5.0, 1.4, 0])
            self.play(FadeOut(mas), run_time=0.2)
            self.pop(menos)

            # «Si es redonda»
            self.en("redonda")
            self.play(Transform(nube, nube_de(a, b0, True)), FadeOut(menos), run_time=self.dur(0.8))

            # «se compensan»
            self.en("compensan")
            cero = Text("0", color=AMBAR, weight=BOLD).scale(3.5).move_to([5.0, 1.4, 0])
            self.pop(cero)
        self.wait(1.0)
        self.limpiar()

    def P(self, u, v):
        return self.ax.c2p(3 + 0.8 * u, 3 + 0.8 * v)
