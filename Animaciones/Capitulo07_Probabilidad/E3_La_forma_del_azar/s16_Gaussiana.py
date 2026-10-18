"""Escena 16 — La gaussiana: la campana con sus dos parámetros, y por qué el ruido es gaussiano."""
from comun.escena import *


class Gaussiana(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        self.g, self.huecos, self.centros = huecos_tres(["Bernoulli", "uniforme"])
        self.add(self.g)
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        mu, sg = ValueTracker(0.0), ValueTracker(1.0)
        c = Curva(lambda x: 0, x_rango=(-5, 5), y_max=0.9, ancho=8.6, alto=3.4,
                  x_label="x", y_label="f_X(x)").move_to([-1.0, -1.0, 0])
        ax = c.ejes

        def campana():
            return ax.plot(lambda x: float(gaussiana(x, mu.get_value(), sg.get_value())), x_range=[-5, 5, 0.05],
                           color=AMBAR, stroke_width=5)

        def centro():
            m = mu.get_value()
            return DashedLine(ax.c2p(m, 0), ax.c2p(m, float(gaussiana(m, m, sg.get_value())) * 1.05),
                              color=VERDE, stroke_width=3)

        def ancho_():
            m, s = mu.get_value(), sg.get_value()
            y = float(gaussiana(m, m, s)) * 0.6
            return DoubleArrow(ax.c2p(m - s, y), ax.c2p(m + s, y), color=CIAN, buff=0, stroke_width=4, tip_length=0.15)

        def area():
            return ax.get_area(ax.plot(lambda x: float(gaussiana(x, mu.get_value(), sg.get_value())),
                                       x_range=[-5, 5, 0.1]), x_range=[-5, 5], color=AMBAR, opacity=0.25)

        def slider(y, tr, rango, nom, color):
            linea = Line([4.8, y, 0], [6.6, y, 0], color=INK, stroke_width=3)
            punto = always_redraw(lambda: Dot([4.8 + (tr.get_value() - rango[0]) / (rango[1] - rango[0]) * 1.8, y, 0],
                                              radius=0.12, color=color))
            et = MathTex(nom, color=color).scale(0.9).next_to(linea, UP, buff=0.2)
            return VGroup(linea, et), punto

        s_mu, p_mu = slider(1.6, mu, (-2, 2), r"\mu", VERDE)
        s_sg, p_sg = slider(0.2, sg, (0.5, 2), r"\sigma", CIAN)

        with self.narrar("b1"):
            self.en("gaussiana")                              # «la gaussiana»
            nom = Text("Gaussiana", color=AMBAR, weight=BOLD).scale(0.65).move_to(self.centros[2])
            self.pop(nom)
            curva = always_redraw(campana)
            self.play(FadeIn(ax), run_time=0.4)
            self.add(curva)
            self.en("dos")                                    # «Tiene dos parámetros»
            self.play(FadeIn(s_mu), FadeIn(s_sg), FadeIn(p_mu), FadeIn(p_sg), run_time=self.dur(0.7))
            self.add(p_mu, p_sg)
            self.en("mu")                                     # «Mu dice dónde está el centro»
            cen = always_redraw(centro)
            self.add(cen)
            self.play(Flash(s_mu[1], color=VERDE, flash_radius=0.4), run_time=0.5)
            self.en("desplaza")                               # «se desplaza sin deformarse»
            self.play(mu.animate.set_value(-1.6), run_time=self.dur(0.9))
            self.play(mu.animate.set_value(1.6), run_time=self.dur(1.1))
            self.play(mu.animate.set_value(0.0), run_time=self.dur(0.6))
            self.en("sigma")                                  # «Sigma dice lo ancha que es»
            anc = always_redraw(ancho_)
            self.add(anc)
            self.play(Flash(s_sg[1], color=CIAN, flash_radius=0.4), run_time=0.5)
            self.en("ensancha")                               # «se ensancha y se aplana»
            self.play(sg.animate.set_value(1.9), run_time=self.dur(1.5))
            self.en("sigue_uno")                              # «el área tiene que seguir valiendo uno»
            ar = always_redraw(area)
            self.add(ar)
            u = Text("Área = 1", color=AMBAR, weight=BOLD).scale(0.6).move_to([5.7, -1.6, 0])
            self.play(sg.animate.set_value(0.7), FadeIn(u), run_time=self.dur(1.3))
            for m in (curva, cen, anc, ar, p_mu, p_sg):
                m.clear_updaters()
        self.corte(self.g)

    # ---------------------------------------------------------------- b2
    def figs(self, k):
        """Cinco efectos pequeños con formas distintas (k = 0, 1)."""
        formas = [
            [(0, 0), (0.5, 0), (0.5, 0.6), (0, 0.6)],
            [(0, 0), (0.5, 0), (0.25, 0.7)],
            [(0, 0), (0.5, 0), (0.5, 0.3), (0.25, 0.7), (0, 0.3)],
            [(0, 0), (0.5, 0), (0.5, 0.7), (0.3, 0.7), (0.3, 0.2), (0, 0.2)],
            [(0, 0), (0.5, 0), (0.5, 0.2), (0.25, 0.5), (0, 0.2)],
        ]
        cols = [AZUL, VERDE, CIAN, AMBAR, MAGENTA]
        out = VGroup()
        for i in range(5):
            pts = formas[(i + 2 * k) % 5]
            poli = Polygon(*[np.array([x, y, 0]) for x, y in pts], stroke_color=cols[i], stroke_width=3,
                           fill_color=cols[i], fill_opacity=0.5).scale(1.9)
            out.add(poli)
        return out

    def bloque2(self):
        ef0, ef1 = self.figs(0), self.figs(1)
        for e in (ef0, ef1):
            e.arrange(RIGHT, buff=1.0).move_to([-1.5, 1.6, 0])
        sep = self.figs(0).arrange(RIGHT, buff=1.0).move_to([-1.5, 1.6, 0])
        junto = self.figs(0).arrange(RIGHT, buff=0.15).move_to([-1.5, 1.6, 0])
        c = Curva(lambda x: float(gaussiana(x)), x_rango=(-4, 4), y_max=0.5, ancho=7.0, alto=2.6,
                  color=AMBAR).move_to([-1.0, -1.7, 0])
        chip_ = chip(INK, "").scale(1.5).move_to([-5.4, 1.6, 0])
        L = Lienzo(ancho=6.0, alto=1.8, t_rango=(0, 1), v_max=1.5, centro=(0.2, 1.6))
        t = np.linspace(0, 1, 160)
        ruido = L.curva(t, 0.6 * serie(11, 160, 0.3), RUIDO, 3)
        with self.narrar("b2"):
            self.en("importante")                             # «tan importante»
            self.play(c.animate.scale(1.0), FadeIn(c.ejes), run_time=self.dur(0.5))
            self.en("efectos")                                # «muchos efectos pequeños»
            self.play(LaggedStart(*[FadeIn(e, scale=0.6) for e in junto], lag_ratio=0.15), run_time=self.dur(0.9))
            self.en("indep")                                  # «independientes»
            self.play(Transform(junto, sep), run_time=self.dur(0.8))
            self.en("forma")                                  # «forma de campana»
            self.play(Create(c.grafica), run_time=self.dur(1.2))
            self.en("cada")                                   # «sea cual sea la forma de cada efecto»
            self.play(Transform(junto, ef1), run_time=self.dur(1.0))
            self.en("circuito")                               # «el ruido de un circuito»
            self.play(FadeOut(junto), FadeIn(chip_), Create(ruido), run_time=self.dur(1.0))
            self.en("electrones")                             # «millones de electrones»
            rng = np.random.default_rng(4)
            pun = VGroup(*[Dot(chip_.get_center() + np.array([rng.uniform(-0.7, 0.7), rng.uniform(-0.55, 0.55), 0]),
                               radius=0.05, color=AMBAR) for _ in range(34)])
            self.add(pun)
            for _ in range(3):
                self.play(*[d.animate.shift(np.array([rng.uniform(-0.35, 0.35), rng.uniform(-0.3, 0.3), 0]))
                            for d in pun], run_time=self.dur(0.9))
            self.en("materia")                                # «casi todo el ruido de esta materia»
            self.play(c.grafica.animate.set_color(RUIDO), run_time=self.dur(0.7))
            self.en("gauss")                                  # «gaussiano»
            pal = self.palabra("Gaussiano", RUIDO, 0.9).move_to([4.6, -1.6, 0])
            self.pop(pal)
