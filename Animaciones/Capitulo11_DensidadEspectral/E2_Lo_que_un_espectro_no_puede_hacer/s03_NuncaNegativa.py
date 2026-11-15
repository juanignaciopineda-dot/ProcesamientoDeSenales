"""Escena 03 — ¿Puede un espectro valer menos cero coma cinco? Cuenta con el colador."""
from comun.escena import *


def hundida(sigma):
    """La densidad imaginaria: positiva, con una hendidura hasta −0,5 en |ω| = 3,5."""
    return lambda w: psd_tele(w) - 0.75 * np.exp(-((np.abs(w) - 3.5) / sigma) ** 2)


class NuncaNegativa(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        S = Lienzo(ancho=9.0, alto=3.4, t_rango=(-6, 6), v_max=1.2, centro=(0.0, -0.9))
        ej = ejes_L(S, -0.8, 1.1)
        self.parte_b1(S, ej)
        self.parte_b2(S)
        self.parte_b3(S)
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self, S, ej):
        q = MathTex(r"S_{xx}(j\omega)=-0{,}5\;?", color=TXT).scale(1.1).move_to([0, 3.3, 0])
        etq = etiqueta("densidad espectral", INK, 0.5).move_to([2.3, 1.2, 0])
        punto = Dot(S.p(3.5, -0.5), radius=0.1, color=ROJO)
        val = MathTex(r"-0{,}5", color=ROJO).scale(0.7).next_to(punto, DOWN, buff=0.15)
        ra = reloj_arena().scale(0.9).move_to([-5.8, 2.6, 0])
        ok = tilde(VERDE, 0.3).move_to([-5.8, 2.6, 0])
        v1 = ventana(S, 3.0, 4.0, -0.5)
        with self.narrar("b1"):
            self.en("pregunta")
            self.play(Create(ej), run_time=self.dur(0.5))
            self.pop(q)
            self.en("puede")
            self.play(FadeIn(etq), run_time=0.3)
            self.en("valor")
            self.play(FadeIn(punto, scale=0.5), FadeIn(val), run_time=0.4)
            self.en("pausa")
            self.play(FadeIn(ra), run_time=0.3)
            self.en("necesario")
            self.play(FadeOut(ra), FadeIn(ok), run_time=0.3)
            self.en("colador")
            self.play(FadeIn(v1), run_time=0.4)
        self.v1 = v1
        self.tmp1 = VGroup(punto, val, etq, ok)
        self.q = q

    def parte_b2(self, S):
        pos = curva_f(S, psd_tele, -6, 6, SENAL, 5)
        neg = curva_f(S, hundida(0.55), -6, 6, SENAL, 5, n=300)
        b1_ = Line(S.p(3, -0.95), S.p(4, -0.95), color=AMBAR, stroke_width=3)
        t1 = etiqueta("3 a 4 rad/s", AMBAR, 0.45).next_to(b1_, DOWN, buff=0.1)
        dash = DashedLine(S.p(-4, -0.95), S.p(-3, -0.95), color=AMBAR, stroke_width=3)
        t2 = etiqueta("−4 a −3", AMBAR, 0.45).next_to(dash, DOWN, buff=0.1)
        vd = ventana(S, -4, -3, -0.5)
        ar = VGroup(area_f(S, hundida(0.55), 3.0, 4.0, ROJO, 0.55), area_f(S, hundida(0.55), -4.0, -3.0, ROJO, 0.55))
        alt = Line(S.p(4.25, 0), S.p(4.25, -0.5), color=AMBAR, stroke_width=4)
        alt_t = etiqueta("altura", AMBAR, 0.42).next_to(alt, RIGHT, buff=0.1)
        anc = Line(S.p(3, 0.12), S.p(4, 0.12), color=AMBAR, stroke_width=4)
        anc_t = etiqueta("ancho", AMBAR, 0.42).next_to(anc, UP, buff=0.08)
        por2 = MathTex(r"\times 2", color=AMBAR).scale(0.8).move_to(S.p(-3.5, 0.0) + UP * 0.45)
        r1 = formula(r"-0{,}5\times1\times2", r"=-1", escala=1.0).move_to([-2.0, 3.3, 0])
        r2 = formula(r"\frac{-1}{2\pi}", r"\approx-0{,}16", escala=1.0).move_to([-2.0, 2.0, 0])
        sel = sello("potencia negativa", ROJO).scale(0.9).move_to([4.8, 2.9, 0])
        self.sel, self.r1, self.r2, self.neg = sel, r1, r2, neg
        with self.narrar("b2"):
            self.en("supongamos")
            self.play(FadeOut(self.tmp1), FadeOut(self.v1), FadeOut(self.q), Create(pos), run_time=self.dur(0.8))
            self.en("curva")
            self.play(ReplacementTransform(pos, neg), run_time=self.dur(1.0))
            self.en("hundir")
            self.play(Create(b1_), FadeIn(t1), run_time=0.5)
            self.en("reflejo")
            self.play(Create(dash), FadeIn(t2), run_time=0.5)
            self.en("poner")
            self.play(FadeIn(ventana(S, 3, 4, -0.5)), FadeIn(vd), run_time=0.5)
            self.en("quedaarea")
            self.play(FadeIn(ar), run_time=0.5)
            self.en("altancho")
            self.play(Create(alt), FadeIn(alt_t), Create(anc), FadeIn(anc_t), FadeIn(por2), run_time=self.dur(0.8))
            self.en("cuenta")
            self.play(FadeIn(r1[0]), run_time=0.5)
            self.en("menos1")
            self.play(FadeIn(r1[1]), run_time=0.4)
            self.en("dospi")
            self.play(FadeIn(r2[0]), run_time=0.5)
            self.en("p016")
            self.play(FadeIn(r2[1]), run_time=0.3)
            self.pop(sel)
        self.v2 = VGroup(b1_, t1, dash, t2, alt, alt_t, anc, anc_t, por2)

    def parte_b3(self, S):
        neg2 = curva_f(S, hundida(0.15), -6, 6, ROJO, 5, n=500)
        f = formula(r"E[y^2]", r"\ge 0", escala=1.1, colores={1: VERDE}).move_to([-2.2, 3.3, 0])
        nadie = etiqueta("densidad de ningún proceso", INK, 0.5).move_to([-1.0, 2.2, 0])
        va = ventana(S, 3.4, 3.6, -0.5)
        vb = ventana(S, -3.6, -3.4, -0.5)
        with self.narrar("b3"):
            self.en("espcuad")
            self.play(FadeOut(self.r1), FadeOut(self.r2), FadeIn(f[0]), run_time=0.4)
            self.en("cuadrado")
            self.pop(f[1])
            self.en("imposible")
            self.play(Create(tachar(self.sel)), run_time=0.4)
            self.en("nopuede")
            self.play(self.neg.animate.set_stroke(ROJO), run_time=0.5)
            self.en("ninguno")
            self.play(FadeIn(nadie), run_time=0.3)
            self.play(Create(tachar(nadie)), run_time=0.3)
            self.en("parteneg")
            self.play(ReplacementTransform(self.neg, neg2), run_time=self.dur(0.8))
            self.en("estrecha")
            self.resaltar(neg2, color=ROJO, escala=1.03)
            self.en("colestrecha")
            self.play(FadeIn(va), FadeIn(vb), run_time=0.5)
            self.en("atrapa")
            self.resaltar(va, vb, color=AMBAR)
