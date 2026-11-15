"""Escena 10 — La pista limpia: no correlacionado no significa inútil; y el salto al registro entero."""
from comun.escena import *


def _fila(tex_x, piezas, y):
    """Fila `x = (2 w + w') / √5` con las monedas en su color. `piezas` = (w_a, color_a, w_b, color_b)."""
    wa, ca, wb, cb = piezas
    f = MathTex(tex_x, "=", r"(2\,", wa, "+", wb, r")\big/\sqrt5", color=TXT).scale(1.0).move_to([-2.0, y, 0])
    f[0].set_color(MEDIDA)
    f[3].set_color(ca)
    f[5].set_color(cb)
    return f


class LaPistaLimpia(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.pista()
        self.regresion()
        self.resumen()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def pista(self):
        r1 = _fila(r"x[n+1]", (r"w[n+1]", ERROR, r"w[n]", VERDE), 1.6)
        r2 = _fila(r"x[n]", (r"w[n]", VERDE, r"w[n-1]", RUIDO), 0.5)
        r3 = _fila(r"x[n-1]", (r"w[n-1]", RUIDO, r"w[n-2]", INK), -0.6)
        self.add(r1, r2)
        self.r2 = r2
        union = Line(r3[3].get_top(), r2[5].get_bottom(), color=RUIDO, stroke_width=4)
        sin = Text("sin monedas en común", color=ERROR).scale(0.65).move_to([4.6, 0.5, 0])
        cero = Text("correlación = 0", color=ERROR).scale(0.78).move_to([4.6, -0.2, 0])
        cuanta = Text("mide la basura de x[n]", color=RUIDO).scale(0.65).move_to([4.6, -1.0, 0])
        resta = MathTex(r"x[n]", "-", r"0{,}4", r"x[n-1]", color=TXT).scale(1.30).move_to([-2.6, -2.2, 0])
        resta[0].set_color(MEDIDA), resta[3].set_color(MEDIDA)
        limpia = Text("pista limpia", color=VERDE).scale(0.65).next_to(resta, RIGHT, buff=0.4)

        with self.narrar("b1"):
            # «Ahora mira la muestra de hace dos pasos»
            self.en("mira")
            self.play(FadeIn(r3), run_time=self.dur(0.6))
            # «equis de ene menos uno. Contiene»
            self.en("xnm1")
            self.resaltar(r3[0], color=AMBAR, run_time=0.5)
            # «Contiene justo esa moneda anterior»
            self.en("contiene")
            self.play(Create(union), run_time=0.5)
            # «y otra más antigua»
            self.en("antigua")
            self.resaltar(r3[5], color=INK, run_time=0.5)
            # «No tiene ninguna moneda en común»
            self.en("comun")
            self.play(FadeIn(sin), run_time=0.4)
            # «por eso la correlación es cero»
            self.en("cero")
            self.play(FadeIn(cero), run_time=0.4)
            # «cuánta basura lleva equis de ene»
            self.en("cuanta")
            self.play(FadeIn(cuanta), run_time=0.4)
            # «Restándola, limpiamos la pista»
            self.en("resta")
            self.play(FadeIn(resta), run_time=self.dur(0.6))
            self.play(FadeIn(limpia), r2[5].animate.fade(0.8), run_time=0.4)
            # «De ahí el coeficiente negativo»
            self.en("neg")
            self.resaltar(resta[1], color=ERROR, escala=1.80, run_time=0.5)

    # ------------------------------------------------------------------ b2
    def regresion(self):
        c8 = sello("Cap. 8 · regresión", INK).scale(0.9).move_to([0, 3.2, 0])
        nube = nube_puntos(centro=(-3.8, 0.8), n=26, ancho=3.0, semilla=4, color=SENAL)
        ctrl = Text("control", color=AMBAR).scale(0.78).move_to([-3.8, -1.2, 0])
        f_ctrl = Arrow([-3.8, -0.9, 0], [-3.8, -0.3, 0], color=AMBAR, stroke_width=4, buff=0)
        h_ = MathTex(r"h", "=", color=TXT).scale(1.43).move_to([3.0, 2.0, 0])
        h_[0].set_color(ESTIMACION)
        cvec = MathTex(r"c", "=", r"(0{,}4;\ ", r"0", r")", color=TXT).scale(1.30).move_to([3.4, 0.8, 0])
        cvec[0].set_color(AMBAR)
        tch = tachar(cvec[3])
        no_manda = Text("no manda solo", color=ERROR).scale(0.65).next_to(cvec, DOWN, buff=0.25)
        sist = MathTex(r"C\,h = c", color=TXT).scale(1.30).move_to([3.4, -0.9, 0])
        hf = MathTex(r"h", "=", r"C^{-1}", r"c", color=TXT).scale(1.56).move_to([3.0, 2.0, 0])
        hf[0].set_color(ESTIMACION), hf[3].set_color(AMBAR)
        inutil = sello("no correlacionado ≠ inútil", VERDE).scale(0.95).move_to([0, -3.1, 0])

        with self.narrar("b2"):
            # «la regresión»
            self.en("regresion")
            self.corte()
            self.pop(c8)
            # «una variable de control»
            self.en("control")
            self.play(FadeIn(nube), FadeIn(ctrl), Create(f_ctrl), run_time=self.dur(0.7))
            # «ayuda a quitar lo que ensucia a otra variable»
            self.en("quitar")
            self.play(nube.animate.stretch(0.35, 1), run_time=self.dur(0.9))
            # «Lo que decide un coeficiente»
            self.en("decide")
            self.play(FadeIn(h_), run_time=0.4)
            # «no es la correlación de esa muestra con el objetivo»
            self.en("nocorr")
            self.play(FadeIn(cvec), run_time=0.5)
            self.play(Create(tch), FadeIn(no_manda), run_time=0.4)
            # «el resultado de resolver todo el sistema»
            self.en("sistema")
            self.play(FadeIn(sist), run_time=0.5)
            # «la inversa de la matriz»
            self.en("inversa")
            self.play(ReplacementTransform(h_, hf), run_time=0.6)
            # «No correlacionado no significa inútil»
            self.en("inutil")
            self.pop(inutil)

    # ------------------------------------------------------------------ b3
    def resumen(self):
        n = 13
        tira = VGroup(*[Square(side_length=0.56, color=INK, stroke_width=2).set_fill(INK, 0.1) for _ in range(n)])
        tira.arrange(RIGHT, buff=0.06).move_to([0, 1.0, 0])
        centro_i = 7
        tira[centro_i].set_stroke(AMBAR).set_fill(AMBAR, 0.3)
        ahora = MathTex("n", color=AMBAR).scale(0.91).next_to(tira[centro_i], DOWN, buff=0.15)
        ven = SurroundingRectangle(VGroup(*tira[3:centro_i + 1]), color=AMBAR, buff=0.06, stroke_width=5)
        sabemos = VGroup(MathTex("h", color=ESTIMACION).scale(1.17), Text("y", color=INK).scale(0.65),
                         MathTex(r"\text{error}", color=ERROR).scale(1.04), tilde(VERDE, 0.35)).arrange(RIGHT, buff=0.3)
        sabemos.move_to([0, -1.2, 0])
        grab = Text("grabación completa", color=INK).scale(0.65).move_to([0, 2.2, 0])
        ven_total = SurroundingRectangle(tira, color=AMBAR, buff=0.06, stroke_width=5)
        matriz = MathTex(r"\begin{bmatrix}\ddots&&\\&C&\\&&\ddots\end{bmatrix}", r"h", "=", "c", color=TXT).scale(1.17)
        matriz.move_to([0, -1.9, 0])
        inf = MathTex(r"\infty", color=AMBAR).scale(1.30).move_to([4.2, -1.9, 0])
        div = MathTex(r"H", "=", r"\frac{S_{yx}}{S_{xx}}", color=TXT).scale(1.4).move_to([0, -2.4, 0])
        div[0].set_color(ESTIMACION)

        with self.narrar("b3"):
            # «Resumamos»
            self.en("resumen")
            self.corte()
            self.play(FadeIn(tira), FadeIn(ahora), run_time=self.dur(0.6))
            # «una ventana finita hacia atrás»
            self.en("ventana")
            self.play(Create(ven), run_time=0.5)
            # «sabemos calcular sus coeficientes y su error»
            self.en("sabemos")
            self.play(FadeIn(sabemos), run_time=0.5)
            # «si la grabación ya está hecha»
            self.en("grabacion")
            self.play(FadeIn(grab), run_time=0.4)
            # «no hay razón para mirar solo el pasado»
            self.en("pasado")
            self.play(*[tira[i].animate.set_stroke(AMBAR).set_fill(AMBAR, 0.15) for i in range(centro_i + 1, n)],
                      run_time=0.5)
            # «todo el registro»
            self.en("registro")
            self.play(ReplacementTransform(ven, ven_total), FadeOut(sabemos), run_time=0.6)
            # «Entonces el sistema de ecuaciones»
            self.en("entonces")
            self.play(FadeIn(matriz), run_time=0.5)
            # «se hace infinito»
            self.en("infinito")
            self.play(FadeIn(inf), run_time=0.4)
            # «parece magia»
            self.en("magia")
            self.resaltar(matriz, color=AMBAR, escala=1.43, run_time=0.5)
            # «se resuelve con una división»
            self.en("division")
            self.play(FadeOut(matriz), FadeOut(inf), FadeIn(div), run_time=0.6)
