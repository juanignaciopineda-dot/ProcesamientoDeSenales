"""Escena 04 — La densidad espectral nunca baja de cero (y las otras dos propiedades del examen)."""
from comun.escena import *


def tarjeta(titulo, sub, color, centro, vacia=False):
    r = RoundedRectangle(corner_radius=0.14, width=3.7, height=1.6, color=color, stroke_width=3)
    r.set_fill(color, 0.12).move_to([centro[0], centro[1], 0])
    if vacia:
        r.set_fill(color, 0.04)
        t = Text("?", color=color, weight=BOLD).scale(0.9).move_to(r)
        return VGroup(r, t)
    t1 = Text(titulo, color=TXT, weight=BOLD).scale(0.6)
    t2 = Text(sub, color=INK).scale(0.4)
    VGroup(t1, t2).arrange(DOWN, buff=0.15).move_to(r)
    return VGroup(r, t1, t2)


class LaFormula(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        S = Lienzo(ancho=8.0, alto=3.0, t_rango=(-6, 6), v_max=1.2, centro=(-0.6, -1.0))
        ej = ejes_L(S, -0.4, 1.15)
        f = formula(r"S_{xx}(j\omega)", r"\ge", "0", r"\forall\,\omega", escala=1.3).move_to([0, 3.0, 0])
        f[1].set_color(AMBAR), f[2].set_color(AMBAR)
        banda_v = Line(S.p(-6, 0), S.p(6, 0), color=VERDE, stroke_width=9)
        curva = curva_f(S, psd_tele, -6, 6, AMBAR, 5)
        num = MathTex("4", color=TXT).scale(1.0)
        den = MathTex(r"4+\omega^2", color=TXT).scale(1.0)
        fr = fraccion(num, den).move_to([5.4, 0.6, 0])
        pos = MathTex(r"\omega^2\ge0", color=VERDE).scale(0.8).move_to([5.4, -0.9, 0])
        t_num = tilde(VERDE, 0.28).next_to(fr, UP, buff=0.15)
        t_den = tilde(VERDE, 0.28).next_to(pos, DOWN, buff=0.15)
        t_fin = tilde(VERDE, 0.5).move_to([-5.6, 0.4, 0])
        with self.narrar("b1"):
            self.en("conclusion")
            self.play(FadeIn(f[0]), run_time=0.5)
            self.en("mayor")
            self.pop(f[1], f[2])
            self.en("todas")
            self.play(FadeIn(f[3]), Create(banda_v), run_time=self.dur(0.7))
            self.en("tele")
            self.play(FadeOut(banda_v), Create(ej), Create(curva), run_time=self.dur(1.0))
            self.en("formula")
            self.play(FadeIn(fr), run_time=0.5)
            self.en("numerador")
            self.play(FadeIn(t_num), run_time=0.3)
            self.en("denominador")
            self.play(FadeIn(pos), run_time=0.4)
            self.en("tambien")
            self.play(FadeIn(t_den), run_time=0.3)
            self.en("nunca")
            self.pop(t_fin)

    def parte_b2(self):
        q = etiqueta("examen de tres preguntas", INK, 0.6).move_to([0, 3.2, 0])
        c1 = tarjeta("S ≥ 0", "sale de la potencia", AMBAR, (-4.1, -1.3))
        c2 = tarjeta("", "", INK, (0, -1.3), vacia=True)
        c3 = tarjeta("", "", INK, (4.1, -1.3), vacia=True)
        L = Lienzo(ancho=4.0, alto=1.6, t_rango=(-3, 3), v_max=1.0, centro=(-1.3, 1.5))
        rara = curva_f(L, lambda x: 0.5 + 0.4 * np.sin(1.7 * x) * np.exp(-0.15 * x * x), -3, 3, MEDIDA, 4)
        interr = MathTex(r"R_{xx}(\tau)\;?", color=AMBAR).scale(1.0).move_to([2.2, 1.5, 0])
        with self.narrar("b2"):
            self.en("primera")
            self.corte()
            self.play(FadeIn(c1), run_time=0.5)
            self.en("otras")
            self.play(FadeIn(c2), FadeIn(c3), run_time=0.5)
            self.en("juntas")
            self.play(FadeIn(q), run_time=0.4)
            self.en("decidir")
            self.play(Create(L.base()), Create(rara), run_time=self.dur(0.9))
            self.en("autocorr")
            self.pop(interr)
