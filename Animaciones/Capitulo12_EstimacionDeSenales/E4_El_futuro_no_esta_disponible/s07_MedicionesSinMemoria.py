"""Escena 07 — El coeficiente de ahora trabaja más; cortar solo sirve si las mediciones no tienen memoria."""
from comun.escena import *


class MedicionesSinMemoria(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.bloque_uno()
        self.bloque_dos()
        self.wait(1.0)
        self.limpiar()

    def bloque_uno(self):
        rel = reloj().scale(1.3).move_to([-5.4, 1.8, 0])
        fl = flecha([-4.5, 1.8, 0], [-3.3, 1.8, 0], INK, 3)
        tach = Line([-4.3, 1.55, 0], [-3.5, 2.05, 0], color=ROJO, stroke_width=7)
        b1 = Tallos([0.686], centro=(-0.8, -1.4), unidad=3.0, color=AMBAR)
        l1 = etiqueta("0,686", AMBAR, 0.55).move_to([-0.8, -1.4 + 0.686 * 3.0 + 0.3, 0])
        b2 = Tallos([0.7386], centro=(-0.8, -1.4), unidad=3.0, color=AMBAR)
        l2 = etiqueta("0,7386", AMBAR, 0.55).move_to([-0.8, -1.4 + 0.7386 * 3.0 + 0.3, 0])
        tj = tijeras().scale(1.1).move_to([3.4, 1.4, 0])
        tj.permitir_encima = True
        cr = cruz(ROJO, 1.4).move_to(tj)
        til = tilde(VERDE, 1.4).move_to(tj)
        ll = llave().scale(1.3).move_to([5.7, -0.2, 0])
        tira = tira_blanca((1, -1, -1, 1, -1, 1), lado=0.5).move_to([3.6, -2.8, 0])
        with self.narrar("b1"):
            # «sin poder ver el futuro»
            self.en("sinfuturo")
            self.play(FadeIn(rel, scale=0.7), GrowArrow(fl), run_time=self.dur(0.5))
            self.play(Create(tach), run_time=0.3)

            # «la muestra de ahora tiene que trabajar más»
            self.en("trabaja")
            self.play(FadeIn(b1), FadeIn(l1), run_time=self.dur(0.5))
            self.play(ReplacementTransform(b1, b2), ReplacementTransform(l1, l2), run_time=self.dur(0.9))

            # «Cortar sin más no sirve»
            self.en("nosirve")
            self.play(FadeIn(tj, scale=0.7), run_time=self.dur(0.4))
            self.play(Create(cr), run_time=0.3)
            self.sfx("error", gain=-18)

            # «un caso en el que cortar sí funciona»
            self.en("funciona")
            self.play(FadeOut(cr), FadeIn(til), run_time=self.dur(0.4))
            self.sfx("exito", gain=-18)

            # «la clave de todo el episodio»
            self.en("clave")
            self.pop(ll)

            # «Ese caso ocurre»
            self.en("ocurre")
            self.resaltar(ll, run_time=self.dur(0.5))

            # «las mediciones no tienen memoria»
            self.en("sinmemoria")
            self.play(FadeIn(tira, shift=UP * 0.2), run_time=self.dur(0.6))

    def bloque_dos(self):
        tira = tira_blanca((1, -1, -1, 1, -1, 1, 1, -1), lado=0.52).move_to([-1.5, 3.0, 0])
        lb = etiqueta("blanca", MEDIDA, 0.55).move_to([-5.3, 3.0, 0])
        mon = moneda("±1").scale(0.8).move_to([2.3, 3.0, 0])
        indep = etiqueta("ninguna depende de las otras", INK, 0.5).move_to([-1.5, 2.2, 0])
        sg = Tallos([0, 0, 1, 0, 0], centro=(-4.0, 0.3), paso=0.7, unidad=1.0, color=MEDIDA, k0=-2)
        lsg = MathTex(r"\sigma^2", color=AMBAR).scale(0.8).move_to([-4.0, 1.7, 0])
        lcxx = MathTex("C_{xx}", color=MEDIDA).scale(0.8).move_to([-6.3, 1.2, 0])
        ceros = [Text("0", color=INK).scale(0.4).move_to([sg.x(i), 0.3 + 0.35, 0]) for i in (0, 1, 3, 4)]
        fs = oculta(formula(r"\sum_k h[k]\,C_{xx}[m-k]", "=", "C_{yx}[m]", escala=0.9,
                            colores={0: ESTIMACION, 2: SENAL})).move_to([2.4, 0.3, 0])
        self.add(fs)
        fx = formula(r"\cdots+0\cdot h[m-1]+", r"\sigma^2 h[m]", r"+0\cdot h[m+1]+\cdots", escala=0.9,
                     colores={1: AMBAR}).move_to([1.0, -1.0, 0])
        fx[0].set_opacity(0.4)
        fx[2].set_opacity(0.4)
        sh = oculta(formula(r"\sigma^2", "h[m]", "=", "C_{yx}[m]", escala=1.3,
                            colores={0: AMBAR, 1: ESTIMACION, 3: SENAL})).move_to([-1.0, -2.3, 0])
        self.add(sh)
        cs = [caja_tex(t, c, ancho=1.5, alto=0.7, escala=0.7) for t, c in
              ((r"h[m-1]", CIAN), (r"h[m]", AMBAR), (r"h[m+1]", VERDE))]
        fila = VGroup(*cs).arrange(RIGHT, buff=0.3).move_to([-1.0, -3.5, 0])
        mat = MathTex(r"\begin{pmatrix}\sigma^2&0&0\\0&\sigma^2&0\\0&0&\sigma^2\end{pmatrix}",
                      color=TXT).scale(0.7).move_to([5.0, -2.5, 0])
        with self.narrar("b2"):
            # «mediciones son blancas»
            self.en("blancas")
            self.corte()
            self.add(fs, sh)
            self.play(FadeIn(tira), FadeIn(lb), run_time=self.dur(0.5))

            # «como la moneda»
            self.en("moneda")
            self.play(FadeIn(mon, scale=0.6), run_time=self.dur(0.4))

            # «sin ninguna memoria»
            self.en("sinmem")
            self.play(FadeIn(indep), run_time=self.dur(0.5))

            # «La autocorrelación vale sigma cuadrado en cero»
            self.en("sigma")
            self.play(FadeIn(sg), FadeIn(lsg), FadeIn(lcxx), run_time=self.dur(0.7))

            # «nada en el resto»
            self.en("resto")
            self.play(*[FadeIn(c) for c in ceros], run_time=self.dur(0.4))

            # «en la suma de la ecuación»
            self.en("suma")
            self.play(*revelar(fs), run_time=self.dur(0.8))

            # «solo sobrevive un término»
            self.en("sobrevive")
            self.play(FadeIn(fx), run_time=self.dur(0.7))

            # «sigma cuadrado por hache de eme»
            self.en("sh")
            self.play(*revelar(sh[0], sh[1]), run_time=self.dur(0.5))

            # «igual a la correlación cruzada en eme»
            self.en("ig")
            self.play(*revelar(sh[2], sh[3]), run_time=self.dur(0.5))

            # «Cada coeficiente»
            self.en("cadacoef")
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in cs], lag_ratio=0.3),
                      run_time=self.dur(0.9))

            # «se despeja por separado»
            self.en("separado")
            self.play(FadeIn(mat), run_time=self.dur(0.6))
