"""Escena 11 — Leer la recta: arranca de la media y corrige según ρ; ρ² es lo que el dato explica."""
from comun.escena import *
from comun.figuras_cap08_e3 import *


class LeerLaRecta(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.leer()
        self.rho_y_explicado()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def leer(self):
        f = formula(r"\hat{y}", "=", r"\mu_y", "+", r"\rho", r"\frac{\sigma_y}{\sigma_x}", "(", "x", "-", r"\mu_x",
                    ")", escala=1.3, colores={0: ESTIMACION, 2: SENAL, 4: AMBAR, 7: MEDIDA, 9: MEDIDA})
        f.move_to([0, 3.0, 0])
        r_mu = SurroundingRectangle(f[2], color=AMBAR, buff=0.1)
        r_ap = SurroundingRectangle(VGroup(*[f[i] for i in range(6, 11)]), color=AMBAR, buff=0.1)
        llave = Brace(VGroup(f[4], f[5]), direction=DOWN, color=INK, buff=0.1)
        tam = Text("Tamaño de la corrección", color=INK).scale(0.5).next_to(llave, DOWN, buff=0.1)
        r_rho = SurroundingRectangle(f[4], color=AMBAR, buff=0.08)
        nube = NubeRhoE3(centro=(-3.0, -1.3), sx=1.2, sy=0.85, n=48, rho=0.0)
        recta = nube.recta(0.0)
        l0 = MathTex(r"\rho=0", color=AMBAR).scale(1.2).move_to([1.1, -0.7, 0])
        mini = carpa_mini_e3(centro=(4.8, -1.3), ancho=2.8, alto=1.5)
        t_mini = Text("La carpa", color=INK).scale(0.5).move_to([4.8, -2.5, 0])
        self.nube, self.recta_n, self.l0, self.mini, self.t_mini = nube, recta, l0, mini, t_mini

        with self.narrar("b1"):
            # «Leamos la fórmula»
            self.en("formula")
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in range(11)], run_time=self.dur(1.0))

            # «Arranca de la media de lo que quieres adivinar»
            self.en("arranca")
            self.play(Create(r_mu), run_time=self.dur(0.5))

            # «cuánto se aparta el dato de la suya»
            self.en("aparta")
            self.play(FadeOut(r_mu), Create(r_ap), run_time=self.dur(0.5))

            # «El tamaño de la corrección»
            self.en("tamano")
            self.play(FadeOut(r_ap), GrowFromCenter(llave), FadeIn(tam), run_time=self.dur(0.7))

            # «depende de rho»
            self.en("rho")
            self.play(Create(r_rho), run_time=self.dur(0.5))

            # «Si rho vale cero»
            self.en("r0")
            self.play(FadeOut(r_rho), FadeIn(nube), FadeIn(l0), run_time=self.dur(0.8))

            # «la recta es horizontal»
            self.en("horiz")
            self.play(Create(recta), run_time=self.dur(0.8))

            # «Es lo que le pasaba a la carpa»
            self.en("carpa")
            self.play(FadeIn(mini), FadeIn(t_mini), run_time=self.dur(0.8))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def rho_y_explicado(self):
        nube, recta = self.nube, self.recta_n
        tr = ValueTracker(0.0)
        nube.add_updater(lambda m: m.colocar(tr.get_value()))
        recta.add_updater(lambda m: m.become(nube.recta(tr.get_value())))
        l1 = MathTex(r"\rho=1", color=AMBAR).scale(1.2).move_to(self.l0)
        lm1 = MathTex(r"\rho=-1", color=AMBAR).scale(1.2).move_to(self.l0)
        e0 = MathTex(r"\sigma_y^2\,(1-1)=0", color=ERROR).scale(1.0).move_to([4.8, -1.0, 0])
        ok = tilde(VERDE, 0.6).move_to([4.8, -2.2, 0])
        titulo = MathTex(r"\sigma_y^2=4", color=SENAL).scale(1.0).move_to([-2.6, 1.6, 0])
        r2 = MathTex(r"\rho^2", color=AMBAR).scale(1.8).move_to([0, 2.8, 0])
        bar = Rectangle(width=7.2, height=0.9, stroke_width=0).set_fill(SENAL, 0.7).move_to([0, 0.4, 0])
        g = Rectangle(width=5.76, height=0.9, stroke_width=0).set_fill(VERDE, 0.85).move_to([-0.72, 0.4, 0])
        r = Rectangle(width=1.44, height=0.9, stroke_width=0).set_fill(ERROR, 0.85).move_to([2.88, 0.4, 0])
        p80 = Text("Explicado: 80 %", color=VERDE, weight=BOLD).scale(0.6).move_to([-0.72, -0.5, 0])
        p20 = Text("20 %", color=ERROR, weight=BOLD).scale(0.6).move_to([2.88, 1.3, 0])
        c08 = Text("0,8 de 4", color=ERROR).scale(0.55).move_to([2.88, -0.4, 0])
        sin = Text("Sin explicar", color=ERROR, weight=BOLD).scale(0.6).move_to([2.88, -1.1, 0])

        with self.narrar("b2"):
            # «Si rho vale uno»
            self.en("r1")
            self.play(FadeOut(self.mini), FadeOut(self.t_mini), tr.animate.set_value(1.0),
                      ReplacementTransform(self.l0, l1), run_time=self.dur(0.9))

            # «o menos uno»
            self.en("rm1")
            self.play(tr.animate.set_value(-1.0), ReplacementTransform(l1, lm1), run_time=self.dur(1.8))

            # «la varianza por uno menos uno»
            self.en("e0")
            self.pop(e0)

            # «el dato lo dice todo»
            self.en("todo")
            self.pop(ok, sonido="exito")

            # «rho al cuadrado es la parte de la varianza»
            self.en("r2")
            nube.clear_updaters()
            recta.clear_updaters()
            self.corte()
            self.pop(r2)
            self.play(FadeIn(bar), FadeIn(titulo), run_time=self.dur(0.6))

            # «que el dato consigue explicar»
            self.en("explica")
            self.play(FadeOut(bar), FadeIn(g), FadeIn(r), run_time=self.dur(0.6))

            # «un ochenta por ciento»
            self.en("p80")
            self.play(FadeIn(p80, shift=UP * 0.1), run_time=self.dur(0.5))

            # «El veinte por ciento restante»
            self.en("p20")
            self.pop(p20)

            # «cero coma ocho de cuatro»
            self.en("c08")
            self.play(FadeIn(c08, shift=UP * 0.1), run_time=self.dur(0.5))

            # «se queda sin explicar»
            self.en("sin")
            self.play(FadeIn(sin, shift=UP * 0.1), run_time=self.dur(0.5))
