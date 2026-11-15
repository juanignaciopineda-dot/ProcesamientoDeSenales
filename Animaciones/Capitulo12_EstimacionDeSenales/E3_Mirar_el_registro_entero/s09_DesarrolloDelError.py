"""Escena 09 — El error del filtro de Wiener, paso a paso: S_ee = S_yy (1 − |γ|²)."""
from comun.escena import *


def frac_cuad(color=TXT):
    """|S_yx|² / S_xx como fracción de dos piezas."""
    return fraccion(MathTex(r"|S_{yx}|^{2}", color=color), MathTex(r"S_{xx}", color=MEDIDA))


class DesarrolloDelError(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.parte_b3()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        e = formula("e", "=", "y", "-", r"\hat y", escala=1.3,
                    colores={0: ERROR, 2: SENAL, 4: ESTIMACION}).move_to([0, 3.0, 0])
        self.fila1 = f = formula(r"S_{ee}", "=", r"S_{yy}", "-", r"H\,S_{xy}", "-", r"H^{*}S_{yx}", "+",
                                 r"|H|^{2}", r"S_{xx}", escala=1.3,
                                 colores={0: ERROR, 2: SENAL, 9: MEDIDA}).move_to([0, 1.4, 0])
        nota_c = Text("H* es la conjugada de H", color=INK).scale(0.6).next_to(f[6], DOWN, buff=0.3)
        self.e = e
        with self.narrar("b1"):
            self.en("error")                                 # «el error»
            self.pop(e)
            self.en("cuadrado")                              # «Desarrollamos el cuadrado»
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=0.5)
            self.en("t1")                                    # «la densidad de i griega»
            self.play(FadeIn(f[2]), run_time=0.4)
            self.en("t2")                                    # «menos hache por la cruzada de equis con i griega»
            self.play(FadeIn(f[3]), FadeIn(f[4]), run_time=0.5)
            self.en("t3")                                    # «menos hache conjugada por la de i griega con equis»
            self.play(FadeIn(f[5]), FadeIn(f[6]), FadeIn(nota_c), run_time=0.5)
            self.en("t4")                                    # «más el módulo de hache al cuadrado»
            self.play(FadeIn(f[7]), FadeIn(f[8]), run_time=0.5)
            self.en("dxx")                                   # «por la densidad de equis»
            self.play(FadeIn(f[9]), run_time=0.4)
        self.nota_c = nota_c

    def parte_b2(self):
        f = self.fila1
        h_val = MathTex(r"H=\frac{S_{yx}}{S_{xx}}", color=ESTIMACION).scale(0.9).move_to([6.0, 3.3, 0])
        s_ee = MathTex(r"S_{ee}=S_{yy}", color=TXT).scale(1.05)
        s_ee[0][:3].set_color(ERROR)
        m1 = MathTex("-", color=TXT).scale(1.05)
        m2 = MathTex("-", color=TXT).scale(1.05)
        p3 = MathTex("+", color=TXT).scale(1.05)
        f1, f2, f3 = frac_cuad().scale(1.05), frac_cuad().scale(1.05), frac_cuad().scale(1.05)
        fila2 = VGroup(s_ee, m1, f1, m2, f2, p3, f3).arrange(RIGHT, buff=0.22).move_to([0, -0.4, 0])
        cuentas = [MathTex(t, color=AMBAR).scale(0.9).next_to(fr, DOWN, buff=0.35)
                   for t, fr in (("-1", f1), ("-1", f2), ("+1", f3))]
        menos1 = MathTex(r"-1", color=AMBAR).scale(1.4).move_to([0, -2.6, 0])
        res = formula(r"S_{ee}", "=", r"S_{yy}", "-", r"\frac{|S_{yx}|^{2}}{S_{xx}}", escala=1.2,
                      colores={0: ERROR, 2: SENAL}).move_to([0, -2.6, 0])
        with self.narrar("b2"):
            self.en("sustituye")                             # «Sustituimos hache»
            self.play(FadeOut(self.e), FadeOut(self.nota_c), f.animate.move_to([0, 2.5, 0]).scale(0.85),
                      FadeIn(h_val), run_time=0.5)
            self.play(FadeIn(s_ee), run_time=0.4)
            self.en("valor")                                 # «la cruzada entre la densidad de equis»
            self.resaltar(h_val, color=AMBAR, escala=1.15)
            self.en("d2")                                    # «El segundo término da»
            self.play(FadeIn(m1), FadeIn(f1), run_time=0.5)
            self.en("d2b")                                   # «menos el módulo de la cruzada al cuadrado»
            self.resaltar(f1.num, color=AMBAR)
            self.en("dd")                                    # «entre la densidad de equis»
            self.resaltar(f1.den, color=AMBAR)
            self.en("d3")                                    # «El tercero, lo mismo»
            self.play(FadeIn(m2), FadeIn(f2), run_time=0.5)
            self.en("d4")                                    # «el cuarto da más ese mismo cociente»
            self.play(FadeIn(p3), FadeIn(f3), run_time=0.5)
            self.en("cuenta")                                # «Dos veces menos y una vez más»
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cuentas], lag_ratio=0.3), run_time=self.dur(1.2))
            self.en("menos1")                                # «queda menos uno»
            self.play(FadeIn(menos1, scale=1.4), run_time=0.4)
            self.en("resultado")                             # «El error es la densidad de i griega»
            self.play(FadeOut(menos1), FadeIn(res[0:3]), run_time=0.5)
            self.en("menoscoc")                              # «menos ese cociente»
            self.play(FadeIn(res[3]), FadeIn(res[4]), run_time=0.5)
        self.res = res
        self.b2 = VGroup(h_val, s_ee, m1, f1, m2, f2, p3, f3, *cuentas, f)

    def parte_b3(self):
        res = self.res
        r1 = formula(r"S_{ee}", "=", r"S_{yy}", r"\Big(", "1", "-", r"\frac{|S_{yx}|^{2}}{S_{xx}S_{yy}}", r"\Big)",
                     escala=1.2, colores={0: ERROR, 2: SENAL}).move_to([0, 1.5, 0])
        coh = MathTex(r"|\gamma|^{2}", color=AMBAR).scale(1.0).next_to(r1[6], DOWN, buff=0.35)
        final = formula(r"S_{ee}", "=", r"S_{yy}", r"\Big(", "1", "-", r"|\gamma|^{2}", r"\Big)",
                        escala=1.2, colores={0: ERROR, 2: SENAL, 6: AMBAR}).move_to([0, 1.5, 0])
        L = lienzo_omega(ancho=9.0, alto=1.0, v_max=1.0, centro=(-1.4, -1.0))
        sl = rebanadas_omega(L, 5, alto=0.9)
        gam = VGroup(*[MathTex(r"\gamma", color=AMBAR).scale(0.9).move_to(c) for c in sl])
        c11 = Text("Cap. 11", color=INK).scale(0.6).next_to(sl, RIGHT, buff=0.2)
        marco = SurroundingRectangle(final, color=AMBAR, buff=0.2, stroke_width=3)
        c8 = MathTex(r"\sigma^{2}(1-\rho^{2})", color=TXT).scale(1.1).move_to([-3.0, -2.5, 0])
        c8t = Text("Cap. 8", color=INK).scale(0.6).next_to(c8, RIGHT, buff=0.25)
        sl2 = rebanadas_omega(lienzo_omega(ancho=4.6, alto=0.8, v_max=1.0, centro=(3.6, -2.5)), 5, alto=0.8)
        see = VGroup(*[MathTex(r"S_{ee}", color=ERROR).scale(0.7).move_to(c) for c in sl2])
        with self.narrar("b3"):
            self.en("factor")                                # «Sacamos factor común»
            self.play(self.b2.animate.set_opacity(0.0), run_time=0.3)
            self.play(res.animate.move_to([0, 3.0, 0]).scale(0.8), run_time=0.3)
            self.play(FadeIn(r1[0:4]), FadeIn(r1[7]), run_time=0.5)
            self.en("uno_menos")                             # «uno menos el módulo de la cruzada al cuadrado»
            self.play(FadeIn(r1[4]), FadeIn(r1[5]), run_time=0.4)
            self.en("producto")                              # «entre el producto de las dos densidades»
            self.play(FadeIn(r1[6]), run_time=0.6)
            self.en("cociente")                              # «Ese cociente»
            self.resaltar(r1[6], color=AMBAR)
            self.en("coher")                                 # «la coherencia al cuadrado»
            self.pop(coh)
            self.en("rho")                                   # «el rho de cada frecuencia»
            self.play(FadeIn(sl), LaggedStart(*[FadeIn(g) for g in gam], lag_ratio=0.15), run_time=self.dur(1.0))
            self.en("vimos")                                 # «que vimos en el capítulo once»
            self.play(FadeIn(c11), run_time=0.4)
            self.en("ee")                                    # «El error es la densidad de i griega»
            self.resaltar(r1[0], r1[2], color=AMBAR, escala=1.2)
            self.en("final")                                 # «por uno menos la coherencia al cuadrado»
            self.play(FadeOut(r1), FadeOut(coh), FadeIn(final), run_time=0.4)
            self.play(Create(marco), run_time=0.4)
            self.en("cap8")                                  # «la varianza por uno menos rho al cuadrado»
            self.play(FadeIn(c8), run_time=0.6)
            self.en("delocho")                               # «del capítulo ocho»
            self.play(FadeIn(c8t), run_time=0.4)
            self.en("rebanadas")                             # «frecuencia a frecuencia»
            self.play(FadeIn(sl2), LaggedStart(*[FadeIn(s) for s in see], lag_ratio=0.15), run_time=self.dur(1.2))
