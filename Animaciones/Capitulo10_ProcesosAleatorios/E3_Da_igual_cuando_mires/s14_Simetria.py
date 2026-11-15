"""Escena 14 — La autocorrelación es par: R(−τ) = R(τ)."""
from comun.escena import *


class Simetria(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        L = Lienzo(ancho=9.0, alto=2.2, t_rango=(0, 1), v_max=2.4, centro=(0, 1.0))
        t = np.linspace(0, 1, 240)
        cur = L.curva(t, 0.9 * serie(51, 240, 0.93), SENAL, 3.5)
        t1, t2 = 0.3, 0.72
        m1 = Dot(L.p(t1, float(np.interp(t1, t, 0.9 * serie(51, 240, 0.93)))), radius=0.11, color=AMBAR)
        m2 = Dot(L.p(t2, float(np.interp(t2, t, 0.9 * serie(51, 240, 0.93)))), radius=0.11, color=AMBAR)
        y_ad, y_at = 2.45, -0.45

        with self.narrar("b1"):
            # «dos propiedades»
            self.en("dos_prop")
            n1 = caja("1", AMBAR, ancho=0.8, alto=0.7).move_to([-4.0, 3.45, 0])
            n2 = caja("2", AMBAR, ancho=0.8, alto=0.7).move_to([2.6, 3.45, 0])
            self.play(FadeIn(n1), FadeIn(n2), run_time=0.4)

            # «La primera es la simetría»
            self.en("simetria")
            sim = caja("simetría", AZUL, ancho=2.6, alto=0.7).move_to([-2.1, 3.45, 0])
            self.play(FadeIn(sim, shift=RIGHT * 0.2), run_time=0.4)

            # «Erre de tau»
            self.en("r_tau")
            self.play(Create(L.base()), Create(cur), FadeIn(m1), FadeIn(m2), run_time=self.dur(0.8))
            rt = MathTex(r"R(\tau)", color=AMBAR).scale(1.2).move_to([-5.0, -1.4, 0])
            self.pop(rt)

            # «tau segundos después»
            self.en("despues")
            fa = Arrow([float(L.x(t1)), y_ad, 0], [float(L.x(t2)), y_ad, 0], color=AMBAR, buff=0, stroke_width=5)
            la = MathTex(r"\tau", color=AMBAR).scale(0.9).next_to(fa, UP, buff=0.05)
            self.play(Create(fa), FadeIn(la), run_time=self.dur(0.6))

            # «Erre de menos tau»
            self.en("r_menos")
            rm = MathTex(r"R(-\tau)", color=RUIDO).scale(1.2).move_to([5.0, -1.4, 0])
            self.pop(rm)

            # «tau segundos antes»
            self.en("antes")
            fb = Arrow([float(L.x(t2)), y_at, 0], [float(L.x(t1)), y_at, 0], color=RUIDO, buff=0, stroke_width=5)
            lb = MathTex(r"-\tau", color=RUIDO).scale(0.9).next_to(fb, DOWN, buff=0.05)
            self.play(Create(fb), FadeIn(lb), run_time=self.dur(0.6))

            # «la misma pareja de instantes»
            self.en("misma")
            self.resaltar(m1, m2, escala=1.8)

            # «vista desde el otro lado»
            self.en("otro_lado")
            ca, cb = fa.get_center().copy(), fb.get_center().copy()
            self.play(fa.animate.move_to([ca[0], y_at, 0]), la.animate.move_to([la.get_center()[0], y_at - 0.45, 0]),
                      fb.animate.move_to([cb[0], y_ad, 0]), lb.animate.move_to([lb.get_center()[0], y_ad + 0.4, 0]),
                      run_time=self.dur(0.9))

            # «el producto no cambia»
            self.en("no_cambia")
            ec = MathTex(r"R(-\tau) = R(\tau)", color=AMBAR).scale(1.4).move_to([0, -2.6, 0])
            self.pop(ec)
        self.limpiar()

    def parte_b2(self):
        L = Lienzo(ancho=8.0, alto=2.6, t_rango=(-1.5, 1.5), v_max=1.0, centro=(0, 0.3))
        tau = np.linspace(-1.5, 1.5, 240)
        eje_v = Line(L.p(0, -1.0), L.p(0, 1.0), color=INK, stroke_width=2)
        gen = L.curva(tau, np.exp(-2.2 * np.abs(tau)), SENAL, 5)
        ks = list(range(-5, 6))
        pal = Palitos(ks, [0.6 ** abs(k) for k in ks], ancho=8.0, alto=2.6, v_max=1.0, centro=(0, 0.3), rotulo="m")

        with self.narrar("b2"):
            # «es par»
            self.en("par")
            pa = self.palabra("par", AMBAR, 1.4).move_to([0, 3.2, 0])
            self.pop(pa)

            # «vale lo mismo en tau que en menos tau»
            self.en("mismo")
            self.play(Create(L.base()), Create(eje_v), Create(gen), run_time=self.dur(0.8))
            a, b = Dot(L.p(0.7, float(np.exp(-2.2 * 0.7))), radius=0.11, color=AMBAR), Dot(L.p(-0.7, float(np.exp(-2.2 * 0.7))), radius=0.11, color=AMBAR)
            h = DashedLine(a.get_center(), b.get_center(), color=AMBAR, stroke_width=3)
            self.play(FadeIn(a), FadeIn(b), Create(h), run_time=self.dur(0.6))

            # «simétrico respecto del eje vertical»
            self.en("simetrico")
            self.play(eje_v.animate.set_stroke(AMBAR, width=5), run_time=0.3)
            mitad = L.curva(tau[tau >= 0], np.exp(-2.2 * tau[tau >= 0]), AMBAR, 6)
            self.add(mitad)
            self.play(Rotate(mitad, angle=PI, axis=UP, about_point=L.p(0, 0)), run_time=self.dur(1.0))
            self.play(FadeOut(mitad), FadeOut(a), FadeOut(b), FadeOut(h), run_time=0.2)

            # «Con los osciladores»
            self.en("osc")
            fo = MathTex(r"\tfrac12\cos(\omega_0\tau)", color=AMBAR).scale(1.2).move_to([0, 3.2, 0])
            cs = L.curva(tau, np.cos(2 * np.pi * tau), SENAL, 5)
            self.play(ReplacementTransform(pa, fo), ReplacementTransform(gen, cs), run_time=self.dur(0.8))

            # «el coseno es par»
            self.en("coseno")
            self.resaltar(cs, color=AMBAR, escala=1.03)

            # «Con el sensor»
            self.en("sensor")
            self.play(ReplacementTransform(cs, pal), FadeOut(L.base()), FadeOut(eje_v), run_time=self.dur(0.8))

            # «cero coma seis elevado»
            self.en("elevado")
            fe = MathTex(r"0{,}6^{\,|m|}", color=AMBAR).scale(1.4).move_to([0, 3.2, 0])
            self.play(ReplacementTransform(fo, fe), run_time=self.dur(0.5))

            # «número de pasos de separación»
            self.en("pasos")
            y = pal.cy - 0.5
            dd = DoubleArrow([pal.pos(0)[0], y, 0], [pal.pos(3)[0], y, 0], color=AMBAR, buff=0, stroke_width=4,
                             max_tip_length_to_length_ratio=0.15)
            lm = MathTex("|m|", color=AMBAR).scale(0.8).next_to(dd, DOWN, buff=0.08)
            self.play(Create(dd), FadeIn(lm), run_time=self.dur(0.7))

            # «sin signo»
            self.en("sin_signo")
            izq = VGroup(*[pal.tallos[i] for i in range(0, 5)])
            self.play(izq.animate(rate_func=there_and_back).set_color(AMBAR), run_time=self.dur(0.9))
