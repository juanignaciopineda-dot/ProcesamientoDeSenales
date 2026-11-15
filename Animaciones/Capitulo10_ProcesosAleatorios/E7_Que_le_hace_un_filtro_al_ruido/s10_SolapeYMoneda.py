"""Escena 10 — R_hh: deslizar h sobre sí misma (promediador) y comprobación con la moneda."""
from comun.escena import *


class SolapeYMoneda(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.solape()
        self.moneda()

    # ------------------------------------------------------------------ b1
    def solape(self):
        paso, xc = 1.0, -3.6
        fija = Tallos([0.5, 0.5, 0, 0], centro=(xc, 1.6), paso=paso, unidad=1.6, color=ESTIMACION, extra=0.6)
        movil = Tallos([0.5, 0.5, 0, 0], centro=(xc, -0.1), paso=paso, unidad=1.6, color=AMBAR, extra=0.6)
        # la copia de h dada la vuelta se desliza bajo la fija: columnas 0 y 1 (sin desplazar)
        lab_f = formula("h", escala=0.8, colores={0: ESTIMACION}).move_to([-6.4, 1.8, 0])
        lab_m = formula("h", escala=0.8, colores={0: AMBAR}).move_to([-6.4, 0.0, 0])
        zona0 = Rectangle(width=2 * paso - 0.15, height=3.3, color=VERDE, stroke_width=3).set_fill(VERDE, 0.12)
        zona0.move_to([fija.x(0.5), 0.75, 0])
        zona1 = Rectangle(width=paso - 0.1, height=3.3, color=VERDE, stroke_width=3).set_fill(VERDE, 0.12)
        zona1.move_to([fija.x(1) , 0.75, 0])
        prod0 = formula(r"\tfrac12\cdot\tfrac12", "+", r"\tfrac12\cdot\tfrac12", escala=0.85).move_to([-3.6, -1.6, 0])
        prod1 = formula(r"\tfrac12\cdot\tfrac12", escala=0.85).move_to([-3.6, -1.6, 0])
        cuadrados = formula(r"\tfrac14", "+", r"\tfrac14", escala=0.95).move_to([-3.6, -2.6, 0])
        cuarto_f = formula(r"\tfrac14", escala=0.95).move_to([-3.6, -2.6, 0])
        prom = etiqueta("promediador", AZUL, 0.5).move_to([-3.6, 3.3, 0])
        # R_hh a la derecha
        R = Tallos([0, 0.25, 0.5, 0.25, 0], centro=(3.0, 0.3), paso=0.9, unidad=2.6, color=ESTIMACION, indices=False)
        R.ks = VGroup()
        lab_r = formula(r"R_{hh}", escala=0.9, colores={0: ESTIMACION}).move_to([3.0, 3.0, 0])
        r0 = formula(r"R_{hh}[0]", "=", r"\tfrac12", escala=0.85).move_to([5.5, 1.9, 0])
        r1 = formula(r"R_{hh}[1]", "=", r"\tfrac14", escala=0.85).move_to([5.5, -0.7, 0])
        moneda = tira_pm1([1, -1, -1, 1, -1, 1], lado=0.5).move_to([-4.0, -3.3, 0])
        impulso = Tallos([1.0], centro=(2.0, -3.3), paso=0.6, unidad=0.7, color=AMBAR, extra=2)
        r_xx = formula(r"R_{xx}", "=", r"\text{impulso}", escala=0.75).move_to([5.2, -3.3, 0])
        justo = formula(r"R_{yy}", "=", r"R_{hh}", escala=0.9, colores={0: ESTIMACION}).move_to([2.6, -2.0, 0])

        with self.narrar("b1"):
            # «deslizando hache sobre sí misma»
            self.en("desliza")
            self.play(FadeIn(fija), FadeIn(lab_f), run_time=self.dur(0.5))
            self.play(FadeIn(movil), FadeIn(lab_m), run_time=self.dur(0.5))
            self.play(movil.animate.shift(RIGHT * 2 * paso), run_time=self.dur(0.8))

            # «sumando los productos»
            self.en("productos")
            self.play(movil.animate.shift(LEFT * 2 * paso), run_time=self.dur(0.6))

            # «donde se solapa»
            self.en("solapa")
            self.play(FadeIn(zona0), run_time=self.dur(0.4))

            # «En el promediador»
            self.en("en_prom")
            self.play(FadeIn(prom), run_time=self.dur(0.4))

            # «sin desplazar»
            self.en("cero")
            self.play(FadeIn(prod0), run_time=self.dur(0.6))

            # «un medio al cuadrado más un medio al cuadrado»
            self.en("cuadrados")
            self.play(FadeIn(cuadrados), run_time=self.dur(0.6))

            # «un medio»
            self.en("medio")
            self.play(Create(R.base), FadeIn(R.palito(2)), FadeIn(lab_r), FadeIn(r0), run_time=self.dur(0.6))

            # «Desplazado un paso»
            self.en("paso")
            self.play(movil.animate.shift(RIGHT * paso), FadeOut(zona0), FadeOut(prod0), FadeOut(cuadrados), run_time=self.dur(0.7))

            # «solo se solapa un término»
            self.en("un_termino")
            self.play(FadeIn(zona1), FadeIn(prod1), run_time=self.dur(0.5))

            # «un cuarto»
            self.en("cuarto")
            self.play(FadeIn(cuarto_f), FadeIn(R.palito(1)), FadeIn(R.palito(3)), FadeIn(r1), run_time=self.dur(0.6))

            # «la moneda»
            self.en("moneda")
            self.play(FadeIn(moneda), run_time=self.dur(0.5))

            # «un impulso»
            self.en("impulso")
            self.play(FadeIn(impulso), FadeIn(r_xx), run_time=self.dur(0.6))

            # «justo esa autocorrelación»
            self.en("justo")
            self.play(FadeIn(justo), run_time=self.dur(0.6))
        self.wait(1.0)

    # ------------------------------------------------------------------ b2
    def moneda(self):
        filas = [(1, 1, 1), (1, -1, 0), (-1, 1, 0), (-1, -1, -1)]
        tab = VGroup()
        sig = {1: "+1", -1: "-1", 0: "0"}
        for a, b, y in filas:
            tab.add(VGroup(MathTex(f"({sig[a]},\\;{sig[b]})", color=TXT).scale(0.85),
                           MathTex(r"\to", color=INK).scale(0.85),
                           MathTex(sig[y], color=MEDIDA).scale(0.95)).arrange(RIGHT, buff=0.35))
        tab.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to([-4.3, 0.6, 0])
        marco = SurroundingRectangle(tab, color=INK, buff=0.3, stroke_width=2)
        salidas = VGroup(*[f[2] for f in tab])
        D = Tallos([0.25, 0.5, 0.25], centro=(2.6, 0.8), paso=1.3, unidad=2.6, color=MEDIDA)
        etq = VGroup(*[MathTex(s, color=TXT).scale(0.8).move_to([D.x(i), 0.8 - 0.4, 0]) for i, s in enumerate(["-1", "0", "1"])])
        pr = VGroup(*[MathTex(s, color=AMBAR).scale(0.8).move_to([D.x(i), 0.8 + D.valores[i] * 2.6 + 0.35, 0])
                      for i, s in enumerate([r"\tfrac14", r"\tfrac12", r"\tfrac14"])])
        var = formula(r"\mathrm{Var}", "=", r"E[y^2]", escala=1.1).move_to([-4.3, -2.3, 0])
        cuartos = formula("=", r"\tfrac14", "+", r"\tfrac14", escala=1.1).next_to(var, RIGHT, buff=0.2)
        medio = formula("=", r"\tfrac12", escala=1.1, colores={1: AMBAR}).next_to(cuartos, RIGHT, buff=0.2)
        rhh = formula(r"R_{hh}[0]", "=", r"\tfrac12", escala=1.1).move_to([1.6, -3.4, 0])
        ok = tilde().scale(0.8).next_to(rhh, LEFT, buff=0.3)

        with self.narrar("b2"):
            # «a mano»
            self.en("a_mano")
            self.corte()
            self.play(Create(marco), FadeIn(VGroup(*[VGroup(f[0], f[1]) for f in tab])), run_time=self.dur(0.7))

            # «la media de dos tiradas»
            self.en("media2")
            self.play(LaggedStart(*[FadeIn(s) for s in salidas], lag_ratio=0.25), run_time=self.dur(0.9))

            # «uno, cero o menos uno»
            self.en("valores")
            self.play(Create(D.base), FadeIn(etq), run_time=self.dur(0.5))

            # «un cuarto, un medio y un cuarto»
            self.en("probs")
            self.play(*[GrowFromEdge(VGroup(D.tallos[i], D.puntos[i]), DOWN) for i in range(3)], FadeIn(pr), run_time=self.dur(0.8))

            # «la esperanza del cuadrado»
            self.en("cuadrado")
            self.play(FadeIn(var), run_time=self.dur(0.6))

            # «un cuarto más un cuarto»
            self.en("cuartos")
            self.play(FadeIn(cuartos), run_time=self.dur(0.6))

            # «un medio»
            self.en("var")
            self.play(FadeIn(medio), run_time=self.dur(0.4))

            # «Coincide»
            self.en("coincide")
            self.play(FadeIn(rhh), FadeIn(ok, scale=0.6), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
