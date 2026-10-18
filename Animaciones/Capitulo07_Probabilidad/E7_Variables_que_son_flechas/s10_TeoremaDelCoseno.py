"""Escena 10 — La varianza de una combinación es el teorema del coseno."""
from comun.escena import *

A_ = np.array([-5.4, -2.4, 0.0])   # vértice entre los lados 2X y 3Y
B_ = np.array([-1.3, -1.6, 0.0])   # extremo de 2X
C_ = np.array([-3.5, 1.1, 0.0])    # extremo de 3Y


class TeoremaDelCoseno(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.triangulo()
        self.comparar()
        self.wait(1.0)
        self.limpiar()

    def triangulo(self):
        pago = self.palabra("El pago prometido", AMBAR, 0.7).move_to([3.0, 3.4, 0])
        var = MathTex(r"\mathrm{Var}(2X-3Y)", color=TXT).scale(1.2).move_to([3.0, 2.4, 0])
        largo = MathTex("=", r"|2X-3Y|^2", color=TXT).scale(1.2).move_to([3.0, 1.4, 0])
        l2x = Line(A_, B_, color=COL_U7, stroke_width=6)
        l3y = Line(A_, C_, color=COL_V7, stroke_width=6)
        l3 = Line(B_, C_, color=AMBAR, stroke_width=6)
        t2x = MathTex("2X", color=COL_U7).scale(0.9).move_to((A_ + B_) / 2 + DOWN * 0.4)
        t3y = MathTex("3Y", color=COL_V7).scale(0.9).move_to((A_ + C_) / 2 + LEFT * 0.45)
        t3 = MathTex("2X-3Y", color=AMBAR).scale(0.9).move_to((B_ + C_) / 2 + RIGHT * 0.9)
        teo = self.palabra("Teorema del coseno", AMBAR, 0.65).move_to([3.0, 0.4, 0])
        c2 = MathTex("c^2", "=", "a^2", "+", "b^2", color=TXT).scale(1.2).move_to([3.0, -0.6, 0])
        c2[0].set_color(AMBAR)
        c2[2].set_color(COL_U7)
        c2[4].set_color(COL_V7)
        cruz_ = MathTex("-2ab\\cos\\gamma", color=AMBAR).scale(1.2).move_to([3.0, -1.7, 0])
        gam = arco7(A_, 11.0, 61.5, 0.9, AMBAR)
        tg = MathTex(r"\gamma", color=AMBAR).scale(0.8).move_to(A_ + np.array([1.3, 0.55, 0]))
        with self.narrar("b1"):
            self.en("pago")
            self.pop(pago)
            self.en("varianza")
            self.play(FadeIn(var), run_time=self.dur(0.7))
            self.en("largo")
            self.play(FadeIn(largo), run_time=self.dur(0.7))
            self.en("esa")
            self.resaltar(largo, color=AMBAR, run_time=0.6)
            self.en("tercer")
            self.play(Create(l2x), Create(l3y), Create(l3), FadeIn(t2x), FadeIn(t3y), FadeIn(t3),
                      run_time=self.dur(1.5))
            self.en("teorema")
            self.pop(teo)
            self.en("otros")
            self.play(FadeIn(c2), run_time=self.dur(1.0))
            self.en("cruzado")
            self.play(FadeIn(cruz_), Create(gam), FadeIn(tg), run_time=self.dur(0.8))
        self.partes = [var, largo, pago, teo, t2x, t3y, t3, l2x, l3y, l3, gam, tg]
        self.c2, self.cruz_ = c2, cruz_

    def comparar(self):
        self.play(FadeOut(self.partes[0]), FadeOut(self.partes[1]), FadeOut(self.partes[2]),
                  FadeOut(self.partes[3]), self.c2.animate.move_to([3.0, 3.1, 0]),
                  self.cruz_.animate.move_to([3.0, 2.1, 0]), run_time=0.7)
        head = MathTex(r"\mathrm{Var}(2X-3Y)", color=TXT).scale(1.1).move_to([3.4, 0.9, 0])
        f = MathTex("=", r"4\sigma_X^2", "+", r"9\sigma_Y^2", "-", r"12\sigma_{XY}",
                    color=TXT).scale(1.1).move_to([3.4, -0.1, 0])
        f[1].set_color(COL_U7)
        f[3].set_color(COL_V7)
        f[5].set_color(AMBAR)
        f = oculta(f)
        head = oculta(head)
        self.add(f, head)
        c2, cr = self.c2, self.cruz_
        preg = MathTex(r"\rho", "=", num_tex(1.5), "?", color=TXT).scale(1.5).move_to([3.4, -2.3, 0])
        preg[2].set_color(ROJO)
        tach = Line(preg.get_corner(DL), preg.get_corner(UR), color=ROJO, stroke_width=6)
        ok = tilde(VERDE, 1.0).move_to([6.4, 0.9, 0])
        with self.narrar("b2"):
            self.en("formula")
            self.play(*revelar(f, head), run_time=self.dur(1.0))
            self.en("cuadrados")
            self.resaltar(c2[2], c2[4], f[1], f[3], color=AMBAR, run_time=0.7)
            self.en("cruce")
            self.resaltar(cr, f[5], color=AMBAR, run_time=0.7)
            self.en("geometria")
            self.play(FadeIn(ok), run_time=self.dur(0.4))
            self.sfx("exito")
            self.en("pendiente")
            self.play(FadeOut(ok), FadeIn(preg), run_time=self.dur(0.5))
            self.en("quien")
            self.resaltar(preg, color=AMBAR, run_time=0.5)
            self.en("v15")
            self.play(Create(tach), run_time=self.dur(0.4))
            self.sfx("error")
