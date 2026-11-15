"""Escena 11 — La coherencia con números: voz 3 y ruido 1 da 0,75; voz 1 y ruido 3 da 0,25."""
from comun.escena import *

U = 0.6          # alto de una unidad de potencia
BASE = -2.0      # línea de base de las barras


def barra(x, valor, color, y0=BASE, ancho=0.9):
    r = Rectangle(width=ancho, height=valor * U, color=color, stroke_width=2).set_fill(color, 0.55)
    r.move_to([x, y0 + valor * U / 2, 0])
    return r


def numero(x, y, txt, color=TXT):
    return Text(txt, color=color).scale(0.5).move_to([x, y, 0])


class LaCoherenciaConNumeros(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        F = formula("y", "=", r"\text{voz}", "+", r"\text{ruido}", escala=1.0,
                    colores={0: MEDIDA, 2: SENAL, 4: RUIDO}).move_to([-3.6, 3.1, 0])
        indep = etiqueta("independientes", INK, 0.55).move_to([2.2, 3.1, 0])
        bv = barra(-5.2, 3, AZUL)
        br = barra(-3.9, 1, MAGENTA)
        nv, nr = numero(-5.2, BASE + 3 * U + 0.3, "3", AZUL), numero(-3.9, BASE + U + 0.3, "1", MAGENTA)
        lv, lr = numero(-5.2, BASE - 0.35, "voz", INK), numero(-3.9, BASE - 0.35, "ruido", INK)
        base = Line([-6.1, BASE, 0], [-0.4, BASE, 0], color=INK, stroke_width=2.5)
        sv = barra(-1.8, 3, AZUL)
        sr = barra(-1.8, 1, MAGENTA, y0=BASE + 3 * U)
        lm = numero(-1.8, BASE - 0.35, "micrófono", INK)
        n4 = numero(-1.8, BASE + 4 * U + 0.3, "4", MEDIDA)
        r1 = oculta(formula(r"|D_{yx}|", "=", "3", escala=1.0, colores={0: MEDIDA}).move_to([3.9, 1.5, 0]))
        r2 = oculta(formula(r"D_{yy}", "=", "?", escala=1.0, colores={0: MEDIDA}).move_to([3.9, 0.3, 0]))
        r2b = formula(r"D_{yy}", "=", r"3+1", "=", "4", escala=1.0, colores={0: MEDIDA}).move_to([3.9, 0.3, 0])
        cu = oculta(formula(r"|\gamma|^2", "=", r"\frac{3^2}{3\cdot 4}", escala=1.0, colores={0: AMBAR}
                            ).move_to([3.4, -1.2, 0]))
        res = oculta(formula("=", r"0{,}75", escala=1.1, colores={1: AMBAR}).move_to([6.3, -1.2, 0]))
        with self.narrar("b1"):
            # «el micrófono capta la voz más el ruido de la sala»
            self.en("mezcla")
            self.corte()
            self.add(r1, r2, cu, res)
            self.play(FadeIn(F), run_time=self.dur(1.0))

            # «no tiene nada que ver con la voz»
            self.en("indep")
            self.play(FadeIn(indep), run_time=self.dur(0.5))

            # «la voz tiene potencia tres»
            self.en("voz3")
            self.play(Create(base), FadeIn(bv), FadeIn(nv), FadeIn(lv), run_time=self.dur(0.7))

            # «y el ruido, uno»
            self.en("ruido1")
            self.play(FadeIn(br), FadeIn(nr), FadeIn(lr), run_time=self.dur(0.6))

            # «solo recoge la voz: módulo tres»
            self.en("cruz3")
            self.play(*revelar(r1), run_time=self.dur(0.6))
            self.resaltar(bv, color=AMBAR)

            # «El micrófono tiene»
            self.en("mictiene")
            self.play(*revelar(r2), run_time=self.dur(0.6))

            # «tres más uno, cuatro»
            self.en("mic4")
            self.play(FadeIn(sv), FadeIn(sr), FadeIn(lm), FadeIn(n4), run_time=self.dur(0.8))
            self.play(FadeOut(r2), FadeIn(r2b), run_time=self.dur(0.5))

            # «tres al cuadrado entre tres por cuatro»
            self.en("cuenta")
            self.play(*revelar(cu), run_time=self.dur(1.0))

            # «Cero coma siete cinco»
            self.en("res")
            self.play(*revelar(res), run_time=self.dur(0.6))
            self.sfx("exito")

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        base = Line([-6.4, BASE, 0], [-0.2, BASE, 0], color=INK, stroke_width=2.5)
        bv, br = barra(-5.6, 1, AZUL), barra(-4.4, 3, MAGENTA)
        nv, nr = numero(-5.6, BASE + U + 0.3, "1", AZUL), numero(-4.4, BASE + 3 * U + 0.3, "3", MAGENTA)
        lv, lr = numero(-5.6, BASE - 0.35, "voz", INK), numero(-4.4, BASE - 0.35, "ruido", INK)
        # dos micrófonos: B = 1 + 3 (segunda frecuencia), A = 3 + 1 (primera)
        b_v, b_r = barra(-2.7, 1, AZUL), barra(-2.7, 3, MAGENTA, y0=BASE + U)
        a_v, a_r = barra(-0.9, 3, AZUL), barra(-0.9, 1, MAGENTA, y0=BASE + 3 * U)
        l_b, l_a = numero(-2.7, BASE - 0.35, "2.ª", INK), numero(-0.9, BASE - 0.35, "1.ª", INK)
        cu = oculta(formula(r"|\gamma|^2", "=", r"\frac{1^2}{1\cdot 4}", escala=1.0, colores={0: AMBAR}
                            ).move_to([3.2, 1.8, 0]))
        res = oculta(formula("=", r"0{,}25", escala=1.1, colores={1: AMBAR}).move_to([6.2, 1.8, 0]))
        l_fr = etiqueta("fracción de voz", AZUL, 0.5).move_to([3.7, 0.2, 0])
        marco = Rectangle(width=1.1, height=4 * U + 0.15, color=AMBAR, stroke_width=3).move_to(
            [-2.7, BASE + 2 * U, 0])
        r_a = formula(r"0{,}75", escala=0.9, colores={0: AMBAR}).move_to([-0.9, BASE + 4 * U + 0.45, 0])
        r_b = formula(r"0{,}25", escala=0.9, colores={0: AMBAR}).move_to([-2.7, BASE + 4 * U + 0.45, 0])
        t_prim = etiqueta("casi todo voz", AZUL, 0.5).move_to([3.7, -1.2, 0])
        t_seg = etiqueta("casi todo ruido", MAGENTA, 0.5).move_to([3.7, -2.2, 0])
        with self.narrar("b2"):
            # «al revés: voz uno, ruido tres»
            self.en("reves")
            self.corte()
            self.add(cu, res)
            self.play(Create(base), FadeIn(bv), FadeIn(br), FadeIn(nv), FadeIn(nr), FadeIn(lv), FadeIn(lr),
                      FadeIn(b_v), FadeIn(b_r), FadeIn(l_b), run_time=self.dur(1.0))

            # «Uno al cuadrado entre uno por cuatro»
            self.en("cuenta")
            self.play(*revelar(cu), run_time=self.dur(1.0))

            # «cero coma dos cinco»
            self.en("res")
            self.play(*revelar(res), FadeIn(r_b), run_time=self.dur(0.6))

            # «la fracción de lo que capta el micrófono»
            self.en("fraccion")
            self.play(Create(marco), run_time=self.dur(0.6))

            # «que viene de la voz»
            self.en("viene")
            self.resaltar(b_v, color=AMBAR)
            self.play(FadeIn(l_fr), run_time=0.4)

            # «En la primera frecuencia»
            self.en("primera")
            self.play(FadeOut(marco), FadeIn(a_v), FadeIn(a_r), FadeIn(l_a), FadeIn(r_a), run_time=self.dur(0.8))

            # «en la segunda, casi todo ruido»
            self.en("segunda")
            self.play(FadeIn(t_prim), run_time=0.4)
            self.play(FadeIn(t_seg), run_time=0.4)
