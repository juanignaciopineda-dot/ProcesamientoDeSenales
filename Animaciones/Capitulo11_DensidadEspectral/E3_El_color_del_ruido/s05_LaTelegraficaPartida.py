"""Escena 05 — La cuenta prometida: partir la integral en dos mitades y la herramienta de la exponencial."""
from comun.escena import *


class LaTelegraficaPartida(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.partir()
        self.herramienta()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def partir(self):
        Lw = Lienzo(ancho=6.4, alto=1.3, t_rango=(0, 5.5), v_max=1.4, centro=(-3.6, 3.0))
        onda = onda_tel(Lw, color=AMBAR, ancho=4)
        Lr = Lienzo(ancho=6.0, alto=2.3, t_rango=(-3, 3), v_max=1.25, centro=(-3.6, -2.0))
        tt = np.linspace(-3, 3, 200)
        v = np.exp(-2 * np.abs(tt))
        curva = Lr.curva(tt, v, AMBAR, 4)
        fR = oculta(formula("R_{xx}(\\tau)", "=", "e^{-\\alpha |\\tau|}")).move_to([-3.6, 1.3, 0])
        fa = formula(r"\alpha", "=", "2", r"\lambda").move_to([-5.0, 0.3, 0])
        ritmo_t = Text("ritmo de saltos", color=INK).scale(0.5).move_to([-2.2, 0.3, 0])
        self.add(fR)
        esp = Espectro(w_max=6, y_max=1.2, ancho=5.4, alto=2.8, centro=(4.0, -2.2))
        graf = esp.curva(tele_S, AMBAR)
        with self.narrar("b1"):
            # «Hace dos episodios prometimos una cuenta»
            self.en("promesa")
            q = MathTex("S_{xx}(j\\omega)", "=", "?", color=AMBAR).scale(1.0).move_to([4.0, 1.0, 0])
            self.play(Create(esp.ejes), Create(graf), FadeIn(q), run_time=self.dur(0.9))
            # «la onda telegráfica»
            self.en("tele")
            self.play(Create(onda), run_time=self.dur(1.0))
            # «e elevado a menos alfa»
            self.en("ealfa")
            self.play(*revelar(fR[0], fR[1], fR[2]), run_time=self.dur(0.7))
            # «el valor absoluto de tau»
            self.en("abs")
            marco = SurroundingRectangle(fR[2][-3:], color=AMBAR, buff=0.08)
            marco.permitir_encima = True
            self.play(Create(marco), run_time=self.dur(0.4))
            # «alfa es dos lambda»
            self.en("dosl")
            self.play(FadeOut(marco), FadeIn(fa), run_time=self.dur(0.5))
            # «el doble del ritmo de saltos»
            self.en("doble")
            marcas = marcas_cambio(Lw)
            self.play(FadeIn(ritmo_t), Create(marcas), run_time=self.dur(0.6))
            # «El valor absoluto obliga»
            self.en("obliga")
            self.resaltar(fR[2], run_time=self.dur(0.6))
            # «partir la integral en dos mitades»
            self.en("partir")
            vert = Lr.vertical(0, INK, 3)
            self.play(Create(Lr.base()), Create(curva), Create(vert), run_time=self.dur(0.9))
            # «a la derecha del cero»
            self.en("der")
            td = np.linspace(0, 3, 100)
            ar_d = relleno_bajo(Lr, td, np.exp(-2 * td), AMBAR, 0.4)
            lab_d = MathTex("\\tau > 0", color=AMBAR).scale(0.85).move_to(Lr.p(1.6, 0.75))
            self.play(FadeIn(ar_d), FadeIn(lab_d), run_time=self.dur(0.5))
            # «a la izquierda»
            self.en("izq")
            ti = np.linspace(-3, 0, 100)
            ar_i = relleno_bajo(Lr, ti, np.exp(2 * ti), VERDE, 0.4)
            lab_i = MathTex("\\tau < 0", color=VERDE).scale(0.85).move_to(Lr.p(-1.6, 0.75))
            self.play(FadeIn(ar_i), FadeIn(lab_i), run_time=self.dur(0.5))
        self.limpiar()

    # ------------------------------------------------------------ b2
    def herramienta(self):
        ax, et = ejes([0, 3, 1], [0, 1.2, 0.4], ancho=5.0, alto=2.6, x_label=r"\tau")
        d = np.array([-6.1, -2.3, 0.0]) - ax.c2p(0, 0)
        ax.shift(d)
        et.shift(d)
        f1 = oculta(formula(r"\int_0^\infty", r"e^{-a\tau}", r"d\tau", "=", r"\frac{1}{a}").scale(1.0)).move_to([3.5, 2.6, 0])
        f2 = oculta(formula(r"\int_0^\infty", r"e^{-\alpha\tau}", r"e^{-j\omega\tau}", r"d\tau").scale(0.9)).move_to([3.5, 1.2, 0])
        f3 = oculta(formula("=", r"\int_0^\infty", r"e^{-(\alpha + j\omega)\tau}", r"d\tau").scale(0.9)).move_to([3.5, 0.0, 0])
        f4 = oculta(MathTex(r"a", "=", r"\alpha + j\omega", color=AMBAR).scale(0.9)).move_to([3.5, -1.2, 0])
        f5 = oculta(formula("=", r"\frac{1}{\alpha + j\omega}").scale(0.95)).move_to([3.5, -2.5, 0])
        self.add(f1, f2, f3, f4, f5)
        a2 = oculta(formula("a", "=", "2", "=", r"\tfrac{1}{2}")).move_to([-3.5, 1.6, 0])
        self.add(a2)
        g1 = ax.plot(lambda x: np.exp(-x), x_range=[0, 3, 0.02], color=AZUL, stroke_width=4)
        g2 = ax.plot(lambda x: np.exp(-2 * x), x_range=[0, 3, 0.02], color=AZUL, stroke_width=4)
        ar1 = ax.get_area(g1, x_range=[0, 3], color=AZUL, opacity=0.4)
        ar2 = ax.get_area(g2, x_range=[0, 3], color=AZUL, opacity=0.4)
        with self.narrar("b2"):
            # «Una herramienta primero»
            self.en("herr")
            tit = Text("una herramienta", color=AMBAR, weight=BOLD).scale(0.65).move_to([-3.5, 3.2, 0])
            self.play(FadeIn(tit), Create(ax), FadeIn(et), run_time=self.dur(0.6))
            # «el área bajo una exponencial que decae»
            self.en("areaexp")
            self.play(Create(g1), FadeIn(ar1), run_time=self.dur(0.9))
            # «e elevado a menos a por tau»
            self.en("eatau")
            self.play(*revelar(f1[1]), run_time=self.dur(0.4))
            # «desde cero hasta infinito»
            self.en("limites")
            self.play(*revelar(f1[0], f1[2]), run_time=self.dur(0.5))
            # «vale uno sobre a»
            self.en("unosoba")
            self.play(*revelar(f1[3], f1[4]), run_time=self.dur(0.5))
            # «Con a igual a dos»
            self.en("a2")
            self.play(ReplacementTransform(g1, g2), ReplacementTransform(ar1, ar2),
                      *revelar(a2[0], a2[1], a2[2]), run_time=self.dur(0.7))
            # «un medio»
            self.en("medio")
            self.play(*revelar(a2[3], a2[4]), run_time=self.dur(0.5))
            # «En la mitad derecha»
            self.en("mitadder")
            self.play(*revelar(f2[0], f2[1], f2[3]), run_time=self.dur(0.6))
            # «la exponencial compleja»
            self.en("compleja")
            self.play(*revelar(f2[2]), run_time=self.dur(0.5))
            # «da e elevado a menos alfa más jota omega»
            self.en("producto")
            self.play(*revelar(*f3), run_time=self.dur(0.7))
            # «por tau»
            self.en("portau")
            self.play(f3[2].animate.set_color(AMBAR), run_time=self.dur(0.4))
            # «Es lo mismo con a igual a alfa más jota omega»
            self.en("igual")
            self.play(*revelar(*f4), run_time=self.dur(0.6))
            # «uno sobre alfa más jota omega»
            self.en("resultado1")
            f5[1].set_color(AMBAR)
            self.play(*revelar(*f5), run_time=self.dur(0.6))
