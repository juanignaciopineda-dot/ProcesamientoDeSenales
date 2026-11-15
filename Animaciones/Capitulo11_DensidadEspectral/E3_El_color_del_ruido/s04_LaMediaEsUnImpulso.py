"""Escena 04 — R = C + μ²: la media es un impulso en el origen del espectro."""
from comun.escena import *


class LaMediaEsUnImpulso(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.auto()
        self.impulso()
        self.practica()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def auto(self):
        tau = np.linspace(-3, 3, 150)
        L1 = Lienzo(ancho=4.8, alto=1.7, t_rango=(-3, 3), v_max=1.3, centro=(-3.9, -0.1))
        L2 = Lienzo(ancho=4.8, alto=1.6, t_rango=(-3, 3), v_max=30, centro=(-3.9, -2.6))
        base1, base2 = L1.base(), L2.base()
        cov = L1.curva(tau, np.exp(-2 * np.abs(tau)), MAGENTA, 4)
        escalon = Rectangle(width=L2.ancho, height=float(L2.y(25) - L2.y(0)), stroke_width=0)
        escalon.set_fill(AZUL, 0.3).move_to(L2.p(0, 12.5))
        borde = Line(L2.p(-3, 25), L2.p(3, 25), color=AZUL, stroke_width=4)
        ft = oculta(formula("R_{xx}(\\tau)", "=", "C_{xx}(\\tau)", "+", r"\mu^2")).move_to([-3.4, 2.5, 0])
        self.add(ft)
        esp = Espectro(w_max=6, y_max=1.2, ancho=5.2, alto=2.6, centro=(3.9, -2.2))
        dxx = esp.curva(lambda w: 0.5 * tele_S(w), MAGENTA)
        with self.narrar("b1"):
            # «la autocorrelación es»
            self.en("auto")
            self.play(*revelar(ft[0], ft[1]), run_time=self.dur(0.5))
            # «la autocovarianza»
            self.en("cov")
            self.play(*revelar(ft[2]), Create(base1), Create(cov), run_time=self.dur(0.7))
            # «más la media al cuadrado»
            self.en("mu2")
            self.play(*revelar(ft[3], ft[4]), Create(base2), FadeIn(escalon), Create(borde), run_time=self.dur(0.7))
            # «mide solo las fluctuaciones»
            self.en("solofl")
            self.play(cov.animate.set_stroke(width=7), escalon.animate.set_fill(AZUL, 0.1), run_time=self.dur(0.6))
            # «su transformada»
            self.en("transf")
            fl = flecha([-1.1, -0.1, 0], [0.6, -0.1, 0], INK)
            self.play(Create(fl), Create(esp.ejes), run_time=self.dur(0.6))
            # «la densidad espectral de las fluctuaciones»
            self.en("dens")
            self.play(Create(dxx), run_time=self.dur(0.9))
            # «Se escribe»
            self.en("escribe")
            marco = RoundedRectangle(corner_radius=0.1, width=2.3, height=0.8, color=MAGENTA, stroke_width=2.5)
            marco.move_to([3.9, 1.0, 0])
            self.play(Create(marco), run_time=self.dur(0.4))
            # «de sub equis equis»
            self.en("dxx")
            dxx_t = MathTex("D_{xx}(j\\omega)", color=MAGENTA).scale(0.75).move_to(marco)
            self.play(FadeIn(dxx_t), run_time=self.dur(0.4))
            # «¿Y la media al cuadrado?»
            self.en("preg")
            q = Text("¿?", color=AMBAR, weight=BOLD).scale(0.9).move_to(L2.p(3, 25) + RIGHT * 0.5 + UP * 0.2)
            self.play(escalon.animate.set_fill(AZUL, 0.3), FadeIn(q), run_time=self.dur(0.4))
            # «una constante»
            self.en("constante")
            tcte = Text("constante", color=AZUL, weight=BOLD).scale(0.5).move_to(L2.p(0, 12.5))
            self.play(FadeIn(tcte), FadeOut(q), run_time=self.dur(0.4))
            # «un impulso»
            self.en("impulso")
            imp = esp.flecha(0, 1.15, AZUL)
            self.play(GrowArrow(imp), run_time=self.dur(0.5))
        self.limpiar(0.3)

    # ------------------------------------------------------------ b2
    def impulso(self):
        s = oculta(formula("S_{xx}", "=", "D_{xx}", "+", r"2\pi \mu^2 \delta(\omega)")).move_to([-2.2, 3.1, 0])
        self.add(s)
        pico = Espectro(w_max=2, y_max=4.0, ancho=4.2, alto=2.4, centro=(-3.6, -1.8), x_label=None)
        esp = Espectro(w_max=6, y_max=1.2, ancho=5.2, alto=2.6, centro=(3.9, -2.6))
        dxx = esp.curva(lambda w: 0.5 * tele_S(w), MAGENTA)
        imp = esp.flecha(0, 1.15, AZUL)

        def gauss(sig):
            return lambda x: 1.2 / (sig * np.sqrt(2 * np.pi)) * np.exp(-x ** 2 / (2 * sig ** 2))

        with self.narrar("b2"):
            # «un pico infinitamente estrecho»
            self.en("pico")
            g0 = pico.curva(gauss(0.9), AZUL)
            self.play(Create(pico.ejes), Create(g0), run_time=self.dur(0.6))
            self.play(Transform(g0, pico.curva(gauss(0.3), AZUL)), run_time=self.dur(0.9))
            # «con un área fija»
            self.en("area")
            ar = pico.area(g0, -2, 2, AZUL, 0.4)
            self.play(FadeIn(ar), run_time=self.dur(0.4))
            self.play(Transform(g0, pico.curva(gauss(0.12), AZUL)), FadeOut(ar), run_time=self.dur(0.9))
            # «toda la potencia concentrada»
            self.en("toda")
            self.play(g0.animate.set_stroke(width=7), run_time=self.dur(0.5))
            # «la frecuencia cero»
            self.en("cero")
            cero = MathTex(r"\omega = 0", color=INK).scale(0.7).move_to(pico.p(0, -0.75))
            self.play(FadeIn(cero), run_time=self.dur(0.4))
            # «la densidad espectral es la de las fluctuaciones»
            self.en("sumaesp")
            self.play(*revelar(s[0], s[1], s[2]), Create(esp.ejes), Create(dxx), run_time=self.dur(0.7))
            # «más un impulso en el origen»
            self.en("impo")
            self.play(*revelar(s[3], s[4]), GrowArrow(imp), run_time=self.dur(0.7))
            # «dos pi por la media al cuadrado»
            self.en("areaimp")
            self.play(s[4].animate.set_color(AZUL), run_time=self.dur(0.5))
            # «Comprobación»
            self.en("compro")
            c1 = formula("2\\pi", "\\to", "1").scale(0.9).set_color(MAGENTA).move_to([3.9, 2.5, 0])
            c25 = formula("2\\pi \\cdot 25", "\\to", "25").scale(0.9).set_color(AZUL).move_to([3.9, 1.5, 0])
            tot = formula("1", "+", "25", "=", "26").scale(1.0).move_to([3.4, 0.4, 0])
            tot[4].set_color(AMBAR)
            ok = tilde().scale(0.9).next_to(tot, RIGHT, buff=0.3)
            # «la curva aporta uno»
            self.en("aporta1")
            self.play(FadeIn(c1), run_time=self.dur(0.5))
            # «el impulso aporta veinticinco»
            self.en("aporta25")
            self.play(FadeIn(c25), run_time=self.dur(0.5))
            # «Veintiséis»
            self.en("total")
            self.play(FadeIn(tot), FadeIn(ok), run_time=self.dur(0.5))
        self.limpiar(0.3)

    # ------------------------------------------------------------ b3
    def practica(self):
        esp = Espectro(w_max=6, y_max=1.2, ancho=6.0, alto=2.8, centro=(-0.6, -2.4))
        dxx = esp.curva(lambda w: 0.5 * tele_S(w), MAGENTA)
        imp = esp.flecha(0, 1.15, AZUL)
        self.play(Create(esp.ejes), Create(dxx), GrowArrow(imp), run_time=0.7)
        with self.narrar("b3"):
            # «una consecuencia práctica»
            self.en("practica")
            ex = Text("!", color=AMBAR, weight=BOLD).scale(1.4).move_to([4.8, 2.6, 0])
            self.pop(ex)
            # «la media es grande»
            self.en("grande")
            gran = Arrow(esp.p(0, 0), esp.p(0, 2.3), buff=0, color=AZUL, stroke_width=14,
                         max_tip_length_to_length_ratio=0.15)
            self.play(Transform(imp, gran), run_time=self.dur(0.5))
            # «se lleva casi toda la potencia»
            self.en("lleva")
            self.play(imp.animate.set_stroke(width=18), dxx.animate.set_stroke(opacity=0.35), run_time=self.dur(0.5))
            # «se estima el espectro con datos»
            self.en("datos")
            arch = documento(INK).scale(1.1).move_to([-5.6, 2.8, 0])
            est = caja("estimador", AMBAR, ancho=2.2, alto=0.8, scale=0.5).move_to([-3.3, 2.8, 0])
            fl = flecha([-5.1, 2.8, 0], [-4.5, 2.8, 0], INK)
            self.play(FadeIn(arch), FadeIn(est), Create(fl), run_time=self.dur(0.7))
            # «derrama sobre las frecuencias vecinas»
            self.en("derrama")
            faldas = esp.curva(lambda w: 1.1 * np.exp(-np.abs(w) * 1.8), AZUL, ancho=3)
            fa = esp.ejes.get_area(faldas, x_range=[-3, 3], color=AZUL, opacity=0.3)
            self.play(FadeIn(fa), Create(faldas), run_time=self.dur(0.8))
            # «tapa lo que queríamos ver»
            self.en("tapa")
            self.play(dxx.animate.set_stroke(opacity=0.12), run_time=self.dur(0.5))
            # «Por eso»
            self.en("poreso")
            q = Text("!", color=AMBAR, weight=BOLD).scale(1.1).move_to([-1.2, 2.8, 0])
            self.play(FadeIn(q), run_time=self.dur(0.3))
            # «antes de estimar un espectro»
            self.en("antes")
            self.resaltar(est, run_time=self.dur(0.5))
            # «restar la media»
            self.en("resta")
            rm = MathTex("x", "-", r"\mu", color=AMBAR).scale(1.0).next_to(arch, DOWN, buff=0.4)
            self.play(FadeIn(rm), FadeOut(imp), FadeOut(fa), FadeOut(faldas),
                      dxx.animate.set_stroke(opacity=1.0), run_time=self.dur(0.8))
