"""Escena 08 — El triángulo sí aprueba: un rectángulo deslizado sobre sí mismo (convolución)."""
from comun.escena import *


class Triangulo(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        U = Lienzo(ancho=7.2, alto=1.5, t_rango=(-4.5, 4.5), v_max=1.4, centro=(-1.0, 2.0))
        V = Lienzo(ancho=6.4, alto=2.6, t_rango=(-3, 3), v_max=2.4, centro=(-1.0, -1.5))
        d = ValueTracker(-3.2)

        def rect_fijo():
            a, b = U.p(-1, 0), U.p(1, 1)
            return Rectangle(width=b[0] - a[0], height=b[1] - a[1], color=SENAL, stroke_width=3).set_fill(SENAL, 0.25).move_to(
                [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0])

        def rect_mov():
            x = d.get_value()
            a, b = U.p(x - 1, 0), U.p(x + 1, 1)
            return Rectangle(width=b[0] - a[0], height=b[1] - a[1], color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.25).move_to(
                [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0])

        def comun_():
            x = d.get_value()
            w = max(0.0, 2 - abs(x))
            if w < 0.02:
                return VMobject()
            c = (max(-1, x - 1) + min(1, x + 1)) / 2
            a, b = U.p(c - w / 2, 0), U.p(c + w / 2, 1)
            return Rectangle(width=b[0] - a[0], height=b[1] - a[1], color=VERDE, stroke_width=0).set_fill(VERDE, 0.7).move_to(
                [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0])

        fijo = rect_fijo()
        mov = always_redraw(rect_mov)
        com = always_redraw(comun_)
        ej_v = ejes_L(V, -0.2, 2.3)
        ghost = V.curva([-3, -2, 0, 2, 3], [0, 0, 2, 0, 0], INK, 3, 0.07)
        interr = MathTex("?", color=AMBAR).scale(1.3).move_to(V.p(1.0, 2.4))
        conv = self.palabra("convolución", AMBAR, 0.75).move_to([-5.0, 3.5, 0])
        cap = lambda txt, y, col=TXT: etiqueta(txt, col, 0.55).move_to([5.0, y, 0])
        col_d = [cap("desplazamiento 0", 0.8), cap("desplazamiento 1", 0.8), cap("desplazamiento 2", 0.8)]
        col_a = [cap("área común 2", -0.1, VERDE), cap("área común 1", -0.1, VERDE), cap("área común 0", -0.1, VERDE)]
        area_l = cap("área común", -0.1, VERDE)
        pts = [Dot(V.p(x, y), radius=0.11, color=AMBAR) for x, y in ((0, 2), (1, 1), (2, 0))]
        quebrada = V.curva([0, 1, 2], [2, 1, 0], AMBAR, 4)
        espejo_q = V.curva([-2, -1, 0], [0, 1, 2], AMBAR, 4)
        tri = V.curva([-2, 0, 2], [0, 2, 0], AMBAR, 5)
        with self.narrar("b1"):
            self.en("truco")
            self.play(Create(ej_v), FadeIn(ghost), FadeIn(interr), run_time=self.dur(0.6))
            self.en("convo")
            self.pop(conv)
            self.en("deslizas")
            self.play(FadeIn(fijo), FadeIn(mov), Create(U.base()), run_time=self.dur(0.6))
            self.add(com)
            self.en("comun")
            self.play(d.animate.set_value(-1.2), FadeIn(area_l), run_time=self.dur(0.8))
            self.en("desliza")
            self.play(d.animate.set_value(-0.5), run_time=self.dur(0.8))
            self.en("d0")
            self.play(d.animate.set_value(0), FadeIn(col_d[0]), FadeOut(area_l), FadeIn(col_a[0]), run_time=0.5)
            self.play(FadeIn(pts[0]), run_time=0.2)
            self.en("d1")
            self.play(d.animate.set_value(1), FadeOut(col_d[0]), FadeOut(col_a[0]),
                      FadeIn(col_d[1]), FadeIn(col_a[1]), run_time=self.dur(0.6))
            self.play(FadeIn(pts[1]), run_time=0.2)
            self.en("d2")
            self.play(d.animate.set_value(2), FadeOut(col_d[1]), FadeOut(col_a[1]),
                      FadeIn(col_d[2]), FadeIn(col_a[2]), run_time=self.dur(0.6))
            self.play(FadeIn(pts[2]), run_time=0.2)
            self.en("sube")
            self.play(Create(quebrada), Create(espejo_q), run_time=self.dur(0.8))
            self.en("triangulo")
            self.play(FadeOut(interr), ReplacementTransform(VGroup(quebrada, espejo_q), tri), FadeOut(ghost), run_time=self.dur(0.8))
        com.clear_updaters()
        mov.clear_updaters()

    def parte_b2(self):
        f1 = formula(r"\mathcal{F}\{a*b\}", "=", r"\mathcal{F}\{a\}", r"\cdot", r"\mathcal{F}\{b\}",
                     escala=1.1).move_to([-3.0, 3.2, 0])
        f2 = formula(r"\mathrm{sinc}", r"\cdot", r"\mathrm{sinc}", "=", r"\mathrm{sinc}^2", escala=1.1).move_to([-3.0, 1.7, 0])
        P = Lienzo(ancho=5.6, alto=2.8, t_rango=(-12, 12), v_max=4.6, centro=(3.7, 0.4))
        ej = ejes_L(P, -0.4, 4.4)
        curva = curva_f(P, lambda w: sinc2x(w) ** 2, -12, 12, AMBAR, 5, n=300)
        ge0 = MathTex(r"\ge 0", color=VERDE).scale(1.2).move_to([-3.0, 0.4, 0])
        ok = tilde(VERDE, 0.6).move_to([-3.0, -0.9, 0])
        # el dibujo guardado: dos rectángulos y un candado
        r1 = Rectangle(width=0.9, height=0.45, color=SENAL, stroke_width=3).set_fill(SENAL, 0.25).move_to([-5.9, -3.2, 0])
        r2 = Rectangle(width=0.9, height=0.45, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.25).move_to([-5.45, -3.2, 0])
        cand = candado(AMBAR).scale(0.6).move_to([-4.6, -3.2, 0])
        # la grabación corta y su periodograma
        Lg = Lienzo(ancho=2.6, alto=0.9, t_rango=(0, 1), v_max=2.4, centro=(-0.9, -3.0))
        t = np.linspace(0, 1, 120)
        graba = Lg.curva(t, 0.8 * serie(77, 120, 0.7), RUIDO, 3)
        fl = Arrow([0.6, -3.0, 0], [1.4, -3.0, 0], color=INK, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.3)
        Lp = Lienzo(ancho=2.6, alto=0.9, t_rango=(0, 1), v_max=2.4, centro=(2.8, -3.0))
        pg = Lp.curva(t, 0.8 * np.abs(serie(78, 120, 0.2)) , MEDIDA, 3)
        interr = MathTex("?", color=ROJO).scale(1.4).move_to([5.9, -3.0, 0])
        with self.narrar("b2"):
            self.en("transfconv")
            self.corte()
            self.play(FadeIn(f1[0]), run_time=0.5)
            self.en("producto")
            self.play(FadeIn(f1[1]), FadeIn(f1[2]), FadeIn(f1[3]), FadeIn(f1[4]), run_time=self.dur(0.9))
            self.en("sinc2")
            self.play(FadeIn(f2), Create(ej), Create(curva), run_time=self.dur(1.0))
            self.en("cuadrado")
            self.pop(ge0)
            self.en("aprueba")
            self.pop(ok)
            self.en("guarda")
            self.play(FadeIn(r1), FadeIn(r2), FadeIn(cand), run_time=0.5)
            self.en("volvera")
            self.resaltar(cand, color=AMBAR, escala=1.3)
            self.en("datos")
            self.play(Create(Lg.base()), Create(graba), Create(fl), Create(Lp.base()), Create(pg), run_time=self.dur(1.0))
            self.en("causa")
            self.pop(interr)
