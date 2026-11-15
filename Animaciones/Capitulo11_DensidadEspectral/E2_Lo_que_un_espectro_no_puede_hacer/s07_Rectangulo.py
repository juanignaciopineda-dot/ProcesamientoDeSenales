"""Escena 07 — El rectángulo no puede ser una autocorrelación: su transformada se hace negativa."""
from comun.escena import *


def opcion(txt, x):
    return caja(txt, INK, ancho=2.6, alto=0.8, scale=0.5).move_to([x, -2.3, 0])


class Rectangulo(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.parte_b3()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        marco_a = RoundedRectangle(corner_radius=0.15, width=6.2, height=3.6, color=INK, stroke_width=2.5).move_to([-3.6, 0.5, 0])
        marco_b = marco_a.copy().move_to([3.6, 0.5, 0])
        A = Lienzo(ancho=5.2, alto=2.6, t_rango=(-3, 3), v_max=2.6, centro=(-3.6, 0.2))
        B = Lienzo(ancho=5.2, alto=2.6, t_rango=(-3, 3), v_max=2.6, centro=(3.6, 0.2))
        ej_a, ej_b = ejes_L(A, -0.2, 2.3), ejes_L(B, -0.2, 2.3)
        rect = A.curva([-3, -1, -1, 1, 1, 3], [0, 0, 1, 1, 0, 0], SENAL, 5)
        tri = B.curva([-3, -2, 0, 2, 3], [0, 0, 2, 0, 0], SENAL, 5)
        q = MathTex(r"R_{xx}(\tau)\;?", color=AMBAR).scale(1.0).move_to([0, 3.3, 0])
        tk_a = VGroup(MathTex("-1", color=INK).scale(0.55).move_to(A.p(-1, -0.4)), MathTex("1", color=INK).scale(0.55).move_to(A.p(1, -0.4)))
        tk_b = VGroup(MathTex("-2", color=INK).scale(0.55).move_to(B.p(-2, -0.4)), MathTex("2", color=INK).scale(0.55).move_to(B.p(2, -0.4)))
        pico = Dot(B.p(0, 2), radius=0.1, color=AMBAR)
        dos_l = MathTex("2", color=AMBAR).scale(0.7).next_to(pico, UP, buff=0.15)
        ops = VGroup(opcion("las dos", -4.2), opcion("ninguna", 0), opcion("solo una", 4.2))
        ra = reloj_arena().scale(0.8).move_to([0, -3.5, 0])
        self.A, self.rect, self.ej_a, self.tk_a = A, rect, ej_a, tk_a
        self.grupo_b1 = VGroup(marco_b, ej_b, tri, tk_b, pico, dos_l, ops, ra)
        self.marco_a, self.q = marco_a, q
        with self.narrar("b1"):
            self.en("dos")
            self.play(FadeIn(marco_a), FadeIn(marco_b), run_time=0.5)
            self.en("autocorr")
            self.pop(q)
            self.en("rect")
            self.play(Create(ej_a), Create(rect), run_time=self.dur(0.8))
            self.en("entre")
            self.play(FadeIn(tk_a), run_time=0.4)
            self.en("tri")
            self.play(Create(ej_b), Create(tri), run_time=self.dur(0.8))
            self.en("dos_origen")
            self.play(FadeIn(pico), FadeIn(dos_l), run_time=0.4)
            self.en("cero2")
            self.play(FadeIn(tk_b), run_time=0.4)
            self.en("encuesta")
            self.play(FadeIn(ops), run_time=0.5)
            self.en("pausa")
            self.play(FadeIn(ra), run_time=0.3)

    def parte_b2(self):
        C = Lienzo(ancho=5.6, alto=3.2, t_rango=(-12, 12), v_max=2.4, centro=(3.7, 0.3))
        ej_c = ejes_L(C, -1.0, 2.3)
        flecha_f = Arrow([-1.0, 0.3, 0], [0.9, 0.3, 0], color=INK, buff=0, stroke_width=4)
        casillas = VGroup(etiqueta("real", VERDE, 0.55), etiqueta("par", VERDE, 0.55))
        k = VGroup(tilde(VERDE, 0.25), tilde(VERDE, 0.25))
        fila = VGroup(casillas[0], k[0], casillas[1], k[1]).arrange(RIGHT, buff=0.25).move_to([-3.6, -2.0, 0])
        tercera = Text("≥ 0 ?", color=AMBAR, weight=BOLD).scale(0.75).move_to([-3.6, -3.0, 0])
        gran_tilde = tilde(VERDE, 0.5).move_to([-3.6, 2.6, 0])
        max_l = DashedLine(self.A.p(0, 1), self.A.p(0, 1.9), color=AMBAR, stroke_width=3)
        f = formula("2", r"\frac{\sin\omega}{\omega}", escala=1.0).move_to([3.7, 2.8, 0])
        sinc_p = self.palabra("sinc", AMBAR, 0.8).move_to([3.7, -2.5, 0])
        sinc = curva_f(C, sinc2x, -12, 12, MEDIDA, 4)
        lob = VGroup(area_f(C, sinc2x, np.pi, 2 * np.pi, ROJO, 0.55), area_f(C, sinc2x, 3 * np.pi, 4 * np.pi, ROJO, 0.55),
                     area_f(C, sinc2x, -2 * np.pi, -np.pi, ROJO, 0.55), area_f(C, sinc2x, -4 * np.pi, -3 * np.pi, ROJO, 0.55))
        self.C, self.sinc, self.tercera, self.fila = C, sinc, tercera, fila
        self.extra_b2 = VGroup(ej_c, sinc, lob, f, sinc_p)
        with self.narrar("b2"):
            self.en("realpar")
            self.play(FadeOut(self.grupo_b1), FadeOut(self.marco_a), FadeOut(self.q), FadeIn(fila), run_time=self.dur(0.6))
            self.en("maximo")
            self.play(Create(max_l), run_time=0.4)
            self.en("todo")
            self.pop(gran_tilde)
            self.en("tercera")
            self.pop(tercera)
            self.en("enfrec")
            self.play(Create(flecha_f), Create(ej_c), run_time=self.dur(0.8))
            self.en("dosseno")
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=self.dur(0.8))
            self.en("sinc")
            self.pop(sinc_p)
            self.play(Create(sinc), run_time=self.dur(1.0))
            self.en("negativa")
            self.play(FadeIn(lob), run_time=0.5)
        self.gran_tilde = gran_tilde

    def parte_b3(self):
        C = self.C
        w47 = 1.5 * np.pi
        pto = Dot(C.p(w47, float(sinc2x(w47))), radius=0.11, color=AMBAR)
        vlin = DashedLine(C.p(w47, 0), C.p(w47, float(sinc2x(w47))), color=AMBAR, stroke_width=2.5)
        sm = MathTex(r"\sin 4{,}7\approx-1", color=TXT).scale(0.85).move_to([-3.6, 2.2, 0])
        val = MathTex(r"\approx-0{,}42", color=ROJO).scale(0.8).next_to(pto, DOWN, buff=0.2)
        nueva = Text("≥ 0 ✗", color=ROJO, weight=BOLD).scale(0.75).move_to(self.tercera)
        nota = MathTex(r"S_{xx}<0", color=ROJO).scale(0.9).move_to([5.5, 1.0, 0])
        sel = sello("potencia negativa", ROJO).scale(0.8).move_to([3.7, -3.5, 0])
        cr = cruz(ROJO, 1.3).move_to([-3.6, 0.5, 0])
        r_lbl = MathTex(r"R_{xx}(\tau)", color=TXT).scale(0.9).move_to([-3.6, 3.2, 0])
        with self.narrar("b3"):
            self.en("w47")
            self.play(FadeOut(self.gran_tilde), FadeIn(pto), Create(vlin), run_time=0.5)
            self.en("senomenos")
            self.play(FadeIn(sm), run_time=0.4)
            self.en("valor")
            self.play(FadeIn(val), run_time=0.4)
            self.en("negativa")
            self.play(ReplacementTransform(self.tercera, nueva), run_time=0.4)
            self.en("enesa")
            self.play(Indicate(pto, color=ROJO, scale_factor=1.6), run_time=0.5)
            self.en("serianeg")
            self.play(FadeIn(nota), run_time=0.4)
            self.en("imposible")
            self.pop(sel)
            self.en("razonable")
            self.play(FadeIn(r_lbl), Create(cr), run_time=0.5)
            self.en("ninguno")
            self.play(Create(tachar(r_lbl)), run_time=0.4)
