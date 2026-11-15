"""Escena 06 — Sumar las dos mitades: 2α / (α² + ω²), y con α = 2, 4 / (4 + ω²)."""
from comun.escena import *


class SumarLasMitades(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.sumar()
        self.resultado()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def sumar(self):
        Lr = Lienzo(ancho=3.6, alto=1.3, t_rango=(-3, 3), v_max=1.25, centro=(-4.6, 2.5))
        tt = np.linspace(-3, 3, 150)
        td, ti = np.linspace(0, 3, 80), np.linspace(-3, 0, 80)
        curva = Lr.curva(tt, np.exp(-2 * np.abs(tt)), AMBAR, 3.5)
        ar_d = relleno_bajo(Lr, td, np.exp(-2 * td), AMBAR, 0.45)
        ar_i = relleno_bajo(Lr, ti, np.exp(2 * ti), VERDE, 0.45)
        self.Lr = Lr
        A = formula(r"\frac{1}{\alpha + j\omega}", "+", r"\frac{1}{\alpha - j\omega}").scale(0.95).move_to([2.6, 2.5, 0])
        A[0].set_color(AMBAR)
        A[2].set_color(VERDE)
        oculta(A[1])
        oculta(A[2])
        igual = oculta(MathTex("=", color=TXT)).move_to([-0.3, 0.4, 0])
        bar = Line([0.0, 0.4, 0], [5.2, 0.4, 0], color=TXT, stroke_width=3)
        oculta(bar)
        num = oculta(formula(r"\alpha", r"-j\omega", "+", r"\alpha", r"+j\omega").scale(0.9)).move_to([2.6, 1.15, 0])
        den = oculta(formula(r"(\alpha + j\omega)", r"(\alpha - j\omega)").scale(0.9)).move_to([2.6, -0.35, 0])
        self.add(A, igual, bar, num, den)
        self.play(FadeIn(Lr.base()), FadeIn(curva), FadeIn(ar_d), FadeIn(A[0]), run_time=0.5)
        self.num, self.den = num, den
        with self.narrar("b1"):
            # «La mitad izquierda es su espejo»
            self.en("espejo")
            fl = CurvedArrow(Lr.p(1.2, 0.5) + UP * 0.35, Lr.p(-1.2, 0.5) + UP * 0.35, angle=TAU / 5, color=INK)
            self.play(Create(fl), FadeIn(ar_i), run_time=self.dur(0.7))
            # «uno sobre alfa menos jota omega»
            self.en("izq")
            self.play(*revelar(A[2]), run_time=self.dur(0.5))
            # «sumamos las dos fracciones»
            self.en("suma")
            self.play(*revelar(A[1]), run_time=self.dur(0.4))
            # «denominador común»
            self.en("comun")
            self.play(*revelar(igual, bar), run_time=self.dur(0.5))
            # «Arriba»
            self.en("arriba")
            self.play(*revelar(num[0], num[1]), run_time=self.dur(0.5))
            # «más alfa más jota omega»
            self.en("masalfa")
            self.play(*revelar(num[2], num[3], num[4]), run_time=self.dur(0.6))
            # «Las jotas se cancelan»
            self.en("cancelan")
            self.play(num[1].animate.set_color(ROJO), num[4].animate.set_color(ROJO), run_time=self.dur(0.5))
            self.play(num[1].animate.set_opacity(0.15), num[4].animate.set_opacity(0.15), run_time=self.dur(0.4))
            # «dos alfa»
            self.en("dosalfa")
            num2 = MathTex(r"2\alpha", color=AMBAR).scale(1.0).move_to(num)
            self.play(ReplacementTransform(num, num2), run_time=self.dur(0.6))
            self.num = num2
            # «Abajo»
            self.en("abajo")
            self.play(*revelar(*den), run_time=self.dur(0.6))
            # «alfa al cuadrado menos jota omega al cuadrado»
            self.en("difcuad")
            den2 = MathTex(r"\alpha^2 - (j\omega)^2", color=TXT).scale(0.9).move_to(den)
            self.play(ReplacementTransform(den, den2), run_time=self.dur(0.7))
            self.den = den2
        self.fl_b1 = VGroup(Lr.base(), curva, ar_d, ar_i, fl, A)
        self.bar, self.igual = bar, igual

    # ------------------------------------------------------------ b2
    def resultado(self):
        self.play(*[FadeOut(m) for m in self.mobjects if m not in
                    (self.num, self.den, self.bar, self.igual) and m is not self.camera.frame], run_time=0.3)
        j2 = MathTex(r"j^2", "=", "-1", color=AMBAR).scale(1.0).move_to([-4.6, 2.2, 0])
        raiz = MathTex(r"j", "=", r"\sqrt{-1}", color=TXT).scale(1.0).move_to([-4.6, 1.2, 0])
        menos = VGroup(MathTex(r"-(j\omega)^2 = -(-1)\,\omega^2", color=TXT).scale(0.85),
                       MathTex(r"= +\omega^2", color=TXT).scale(0.85)).arrange(DOWN, buff=0.2).move_to([-4.2, -0.8, 0])
        lhs = MathTex(r"S_{xx}(j\omega)", color=AMBAR).scale(0.9).move_to([-1.5, 0.4, 0])
        alfa2 = MathTex(r"\alpha = 2", color=AMBAR).scale(1.0).move_to([-4.6, -2.4, 0])
        fila2 = oculta(formula(r"S_{xx}(j\omega)", "=", r"\frac{4}{4 + \omega^2}").scale(1.0)).move_to([0.0, -1.9, 0])
        fila2[2].set_color(AMBAR)
        self.add(fila2)
        esp = Espectro(w_max=6, y_max=1.2, ancho=4.2, alto=1.9, centro=(4.7, -3.6))
        graf = esp.curva(tele_S, AMBAR)
        with self.narrar("b2"):
            # «jota al cuadrado es menos uno»
            self.en("j2")
            self.play(FadeIn(j2), run_time=self.dur(0.5))
            # «la raíz de menos uno»
            self.en("raiz")
            self.play(FadeIn(raiz), run_time=self.dur(0.5))
            # «Menos por menos»
            self.en("menosmenos")
            self.play(FadeIn(menos), run_time=self.dur(0.8))
            # «alfa al cuadrado más omega al cuadrado»
            self.en("den")
            den3 = MathTex(r"\alpha^2 + \omega^2", color=TXT).scale(0.9).move_to(self.den)
            self.play(ReplacementTransform(self.den, den3), run_time=self.dur(0.7))
            # «Resultado»
            self.en("res")
            self.play(FadeIn(lhs), run_time=self.dur(0.4))
            # «dos alfa dividido entre»
            self.en("frac")
            marco = SurroundingRectangle(VGroup(self.num, self.bar, den3), color=AMBAR, buff=0.15)
            marco.permitir_encima = True
            self.play(Create(marco), run_time=self.dur(0.5))
            # «alfa al cuadrado más omega al cuadrado»
            self.en("denfin")
            self.resaltar(den3, run_time=self.dur(0.5))
            # «Con alfa igual a dos»
            self.en("alfa2")
            self.play(FadeIn(alfa2), run_time=self.dur(0.4))
            # «cuatro dividido entre cuatro más omega al cuadrado»
            self.en("cuatro")
            self.play(*revelar(*fila2), run_time=self.dur(0.7))
            # «La que usamos»
            self.en("usamos")
            self.play(Create(esp.ejes), Create(graf), run_time=self.dur(0.8))
            # «Promesa cumplida»
            self.en("cumplida")
            ok = tilde().scale(1.0).move_to([2.7, -1.9, 0])
            self.sfx("exito")
            self.play(FadeIn(ok), run_time=self.dur(0.4))
