"""Escena 05 — La autocorrelación es real y par; el seno es impar."""
from comun.escena import *


class LaAutocorrelacionEsPar(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        L = Lienzo(ancho=8.0, alto=2.6, t_rango=(-3, 3), v_max=1.2, centro=(0.0, 0.7))
        ej = ejes_L(L, -0.1, 1.2)
        curva = curva_f(L, r_tele, -3, 3, SENAL, 5)
        r = MathTex(r"R_{xx}(\tau)", color=TXT).scale(1.1).move_to([-2.4, 3.3, 0])
        rp = etiqueta("real y par", AMBAR, 0.7).move_to([1.6, 3.3, 0])
        espejo = DashedLine(L.p(0, -0.1), L.p(0, 1.25), color=AMBAR, stroke_width=3)
        d1, d2 = Dot(L.p(-0.5, r_tele(0.5)), radius=0.1, color=AMBAR), Dot(L.p(0.5, r_tele(0.5)), radius=0.1, color=AMBAR)
        h = DashedLine(d1.get_center(), d2.get_center(), color=AMBAR, stroke_width=2.5)
        tt = VGroup(MathTex(r"-\tau", color=AMBAR).scale(0.7).move_to(L.p(-0.5, -0.28)),
                    MathTex(r"\tau", color=AMBAR).scale(0.7).move_to(L.p(0.5, -0.28)))
        T = Lienzo(ancho=7.0, alto=1.3, t_rango=(0, 6), v_max=2.4, centro=(0.0, -2.9))
        t = np.linspace(0, 6, 200)
        s = 0.9 * serie(53, 200, 0.95)
        orig = T.curva(t, s, SENAL, 3.5)
        copia = T.curva(t + 0.35, s, RUIDO, 3.0, 0.8)
        despues = Arrow(L.p(0, -0.75), L.p(1, -0.75), color=AMBAR, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        antes = Arrow(L.p(0, -0.75), L.p(-1, -0.75), color=AMBAR, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        dt = etiqueta("+1 s", AMBAR, 0.5).next_to(despues, DOWN, buff=0.08)
        at = etiqueta("−1 s", AMBAR, 0.5).next_to(antes, DOWN, buff=0.08)
        with self.narrar("b1"):
            self.en("realpar")
            self.play(FadeIn(r), run_time=0.4)
            self.pop(rp)
            self.en("espejo")
            self.play(Create(ej), Create(curva), run_time=self.dur(0.8))
            self.play(Create(espejo), run_time=0.4)
            self.en("taumenos")
            self.play(FadeIn(d1), FadeIn(d2), Create(h), FadeIn(tt), run_time=self.dur(0.7))
            self.en("parecerse")
            self.play(Create(T.base()), Create(orig), Create(copia), run_time=self.dur(1.0))
            self.en("despues")
            self.play(Create(despues), FadeIn(dt), run_time=0.5)
            self.en("antes")
            self.play(Create(antes), FadeIn(at), run_time=0.5)

    def parte_b2(self):
        f = formula(r"S_{xx}(j\omega)", "=", r"\int R_{xx}(\tau)", r"e^{-j\omega\tau}", r"d\tau",
                    escala=1.0).move_to([0, 3.3, 0])
        g = formula(r"e^{-j\omega\tau}", "=", r"\cos(\omega\tau)", r"-\,j\,\sin(\omega\tau)", escala=1.0).move_to([0, 2.15, 0])
        A = formula(r"\int R_{xx}(\tau)\cos(\omega\tau)\,d\tau", escala=0.9).move_to([-2.6, 1.0, 0])
        B = formula(r"-\,j\int R_{xx}(\tau)\,", r"\sin(\omega\tau)", r"\,d\tau", escala=0.9).move_to([2.2, 1.0, 0])
        Ls = Lienzo(ancho=5.6, alto=1.9, t_rango=(-3, 3), v_max=1.3, centro=(-3.6, -2.0))
        sen = curva_f(Ls, lambda x: np.sin(2 * x), -3, 3, RUIDO, 4)
        etq_s = etiqueta("seno: impar", RUIDO, 0.5).move_to([-3.6, -3.45, 0])
        p1 = Dot(Ls.p(0.6, np.sin(1.2)), radius=0.1, color=AMBAR)
        p2 = Dot(Ls.p(-0.6, -np.sin(1.2)), radius=0.1, color=AMBAR)
        Lp = Lienzo(ancho=5.6, alto=1.9, t_rango=(-3, 3), v_max=0.5, centro=(3.6, -2.0))
        prod = curva_f(Lp, lambda x: r_tele(x) * np.sin(2 * x), -3, 3, AMBAR, 4)
        txt = etiqueta("par × impar = impar", AMBAR, 0.5).move_to([3.6, -3.45, 0])
        with self.narrar("b2"):
            self.en("transf")
            self.corte()
            self.play(FadeIn(f), run_time=0.7)
            self.en("expcompleja")
            self.resaltar(f[3], color=AMBAR, escala=1.2)
            self.en("cosseno")
            self.play(FadeIn(g), run_time=self.dur(0.9))
            self.en("partes")
            self.play(FadeIn(A), FadeIn(B[0]), FadeIn(B[2]), run_time=self.dur(0.7))
            self.en("lleva")
            self.resaltar(B[0], color=AMBAR, escala=1.1)
            self.en("porseno")
            self.play(FadeIn(B[1]), run_time=0.4)
            self.en("impar")
            self.play(Create(Ls.base()), Create(sen), FadeIn(etq_s), run_time=self.dur(0.9))
            self.en("contrario")
            self.play(FadeIn(p1), FadeIn(p2), run_time=0.4)
            self.en("parimpar")
            self.play(Create(Lp.base()), Create(prod), FadeIn(txt), run_time=self.dur(0.9))
