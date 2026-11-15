"""Escena 19 — Dos comprobaciones de la fórmula: con mediciones blancas sale el corte; sin cortar sale el no causal."""
from comun.escena import *


def fh_formula(escala: float = 1.0):
    return formula("H(z)", "=", r"\frac{1}{\sigma^2 F(z)}", r"\bigg[", r"\frac{S_{yx}(z)}{F(z^{-1})}",
                   r"\bigg]_{+}", escala=escala,
                   colores={0: ESTIMACION, 2: COLOR_PASO[3], 3: COLOR_PASO[2], 4: COLOR_PASO[1], 5: COLOR_PASO[2]})


class DosComprobaciones(EscenaCurso):
    ESCENA = "19"

    def construct(self):
        self.bloque_uno()
        self.bloque_dos()
        self.wait(1.0)
        self.limpiar()

    def bloque_uno(self):
        fh = fh_formula(1.0).move_to([0, 2.5, 0])
        self.add(fh)
        n1 = VGroup(Circle(radius=0.3, color=CIAN, stroke_width=4), Text("1", color=TXT).scale(0.5)).move_to([-3.5, 1.2, 0])
        n2 = VGroup(Circle(radius=0.3, color=AMBAR, stroke_width=4), Text("2", color=TXT).scale(0.5)).move_to([3.5, 1.2, 0])
        tira = tira_blanca((1, -1, -1, 1, -1, 1), lado=0.5).move_to([-3.5, 0.3, 0])
        f1 = formula("F=1", escala=1.0, colores={0: CIAN}).move_to([-3.5, -0.8, 0])
        h = formula(r"h=\frac{C_{yx}}{\sigma^2},\ m\geq 0", escala=0.85, colores={0: ESTIMACION}).move_to([-3.5, -2.1, 0])
        til1 = tilde(VERDE, 0.9).move_to([-3.5, -3.3, 0])
        tj = tijeras().scale(0.9).move_to([3.5, 0.3, 0])
        tj.permitir_encima = True
        br = formula(r"\bigg[\ \bigg]_{+}", escala=1.0, colores={0: AMBAR}).move_to([3.5, -0.8, 0])
        tbr = tachar(br)
        res = formula(r"\frac{S_{yx}}{\sigma^2 F\,F^{*}}", escala=0.9).move_to([3.5, -1.1, 0])
        dens = formula(r"=\frac{S_{yx}}{S_{xx}}", escala=0.9).move_to([3.5, -2.4, 0])
        til2 = tilde(VERDE, 0.9).move_to([6.0, -2.4, 0])
        noc = etiqueta("el no causal", VERDE, 0.5).move_to([3.5, -3.5, 0])
        with self.narrar("b1"):
            # «Dos comprobaciones»
            self.en("dos")
            self.pop(n1, n2, sonido=None)

            # «Si lo medido ya fuera blanco»
            self.en("blanco")
            self.play(FadeIn(tira, shift=UP * 0.15), run_time=self.dur(0.5))

            # «F sería uno»
            self.en("f1")
            self.play(FadeIn(f1), run_time=self.dur(0.4))

            # «la cruzada dividida entre sigma cuadrado, cortada»
            self.en("h")
            self.play(FadeIn(h, shift=UP * 0.15), run_time=self.dur(0.8))

            # «es el caso de las mediciones blancas»
            self.en("caso")
            self.play(FadeIn(til1, scale=0.6), run_time=self.dur(0.4))
            self.sfx("exito", gain=-18)

            # «si no cortásemos nada»
            self.en("nocort")
            self.play(FadeIn(tj, scale=0.7), run_time=self.dur(0.4))
            self.play(tj.animate.shift(RIGHT * 2.8).set_opacity(0), run_time=self.dur(0.6))

            # «el corchete desaparecería»
            self.en("desap")
            self.play(FadeIn(br), run_time=self.dur(0.3))
            self.play(Create(tbr), run_time=0.3)
            self.play(FadeOut(br), FadeOut(tbr), run_time=self.dur(0.4))

            # «la cruzada entre sigma cuadrado por F por F al revés»
            self.en("res")
            self.play(FadeIn(res, shift=UP * 0.15), run_time=self.dur(0.8))

            # «la densidad de lo medido»
            self.en("dens")
            self.play(FadeIn(dens, shift=UP * 0.15), run_time=self.dur(0.6))

            # «el filtro no causal de siempre»
            self.en("noc")
            self.play(FadeIn(til2, scale=0.6), FadeIn(noc), run_time=self.dur(0.5))
            self.sfx("exito", gain=-18)

    def bloque_dos(self):
        fh = fh_formula(1.0).move_to([0, 2.5, 0])
        fn = formula(r"H(z)=\frac{S_{yx}}{S_{xx}}", escala=1.0, colores={0: ESTIMACION}).move_to([0, 1.2, 0])
        lc = etiqueta("causal", AMBAR, 0.5).move_to([-6.0, 2.5, 0])
        lnc = etiqueta("no causal", INK, 0.5).move_to([-5.8, 1.2, 0])
        barras = Tallos([0.686, 0.7386], centro=(-4.5, -3.0), paso=1.0, unidad=2.0, color=AMBAR)
        v = [etiqueta(s, AMBAR, 0.45).move_to([barras.x(i), -3.0 + (0.686, 0.7386)[i] * 2.0 + 0.3, 0])
             for i, s in enumerate(["0,686", "0,7386"])]
        pr = etiqueta("¿cuánto se pierde?", AMBAR, 0.6).move_to([-0.2, -1.9, 0])
        lp = lupa(TXT).scale(1.2).move_to([-1.0, 3.8, 0])
        lp.permitir_encima = True
        tr = etiqueta("¿truco?", ROJO, 0.6).move_to([5.6, 0.3, 0])
        cu = etiqueta("con el sensor", AMBAR, 0.6).move_to([4.6, -3.2, 0])
        with self.narrar("b2"):
            # «el filtro no causal con una diferencia»
            self.en("dif")
            self.corte()
            self.play(FadeIn(fh), FadeIn(fn), FadeIn(lc), FadeIn(lnc), run_time=self.dur(0.8))

            # «el corchete»
            self.en("corchete")
            self.play(fh[3].animate(rate_func=there_and_back).scale(1.6), fh[5].animate(rate_func=there_and_back).scale(1.6),
                      run_time=self.dur(0.8))

            # «Lo que se pierde por ser causal»
            self.en("pierde")
            self.play(FadeIn(barras), *[FadeIn(x) for x in v], FadeIn(pr), run_time=self.dur(0.9))

            # «está escondido ahí»
            self.en("escondido")
            self.play(FadeIn(lp, scale=0.6), run_time=self.dur(0.3))
            self.play(lp.animate.move_to([fh[4].get_center()[0] + 0.0, 3.3, 0]), run_time=self.dur(0.9))

            # «parece un truco»
            self.en("truco")
            self.pop(tr, sonido=None)

            # «solo se ve al hacer las cuentas»
            self.en("cuentas")
            self.play(FadeIn(cu), run_time=self.dur(0.5))
