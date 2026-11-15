"""Escena 14 — Cómo medir lo bueno que es un filtro: la relación señal-ruido de la salida."""
from comun.escena import *


def _campana_rara(centro, ancho=2.4, alto=1.4, color=RUIDO):
    x = np.linspace(-2.6, 2.6, 80)
    y = np.exp(-(x - 0.3) ** 2 / 1.2) * (1 + 0.35 * np.sin(3.0 * x)) * 0.8 + 0.25 * np.exp(-(x + 1.6) ** 2 / 0.3)
    return traza(centro[0] + x / 2.6 * ancho / 2, centro[1] - alto / 2 + y * alto, color, 3.0)


class MedirFiltros(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        h = Tallos(H13, centro=(-4.6, 1.2), paso=0.6, unidad=0.3, color=ESTIMACION)
        cor = corona().scale(0.8).move_to([-4.6, 2.5, 0])
        q = interrogante13(AMBAR, 1.2).move_to([-3.2, 2.4, 0])
        c1 = campana_mini(centro=(2.0, 1.7), ancho=2.4, alto=1.4, color=RUIDO)
        c2 = _campana_rara((2.0, 1.7))
        l_gauss = etiqueta("¿gaussiano?", RUIDO, 0.55).move_to([2.0, 2.9, 0])
        regla = caja("regla de error mínimo", ERROR, ancho=3.8, alto=0.7, scale=0.42).move_to([-3.4, -0.5, 0])
        ca = campana_mini(centro=(-4.4, -2.5), ancho=2.2, alto=1.2, color=SENAL)
        cb = campana_mini(centro=(-1.4, -2.5), ancho=2.2, alto=1.2, color=SENAL)
        sep = DoubleArrow([-4.4, -1.95, 0], [-1.4, -1.95, 0], color=AMBAR, buff=0, stroke_width=3, tip_length=0.15)
        snr = self.palabra("relación señal-ruido", AMBAR, 0.5).move_to([4.8, -0.2, 0])
        num = MathTex(r"(\mu_1-\mu_0)^2", color=TXT).scale(0.9).move_to([4.8, -1.1, 0])
        raya = Line([3.4, -1.65, 0], [6.2, -1.65, 0], color=TXT, stroke_width=3)
        den = MathTex(r"\sigma^2", color=RUIDO).scale(0.9).move_to([4.8, -2.2, 0])
        # segundo bloque
        f_m = formula(r"\mu_1", "=", r"\sum", "s", "h", escala=1.2, colores={3: SENAL, 4: ESTIMACION}).move_to([-3.8, 2.9, 0])
        m5 = MathTex(r"2+2+1=5").scale(1.0).move_to([-3.8, 1.75, 0])
        v25 = MathTex(r"5^2=25").scale(1.0).move_to([-3.8, 0.75, 0])
        f_v = formula(r"\mathrm{Var}", "=", r"\sigma^2", r"\sum h^2", escala=1.2, colores={2: RUIDO}).move_to([-3.8, -0.7, 0])
        v3 = MathTex(r"1+1+1=3").scale(1.0).move_to([-3.8, -1.85, 0])
        r833 = MathTex(r"25/3=8{,}33", color=AMBAR).scale(1.2).move_to([-3.8, -3.1, 0])
        s_row = Tallos(S13, centro=(4.2, 2.0), paso=0.7, unidad=0.3, color=SENAL)
        l_s = MathTex("s", color=SENAL).scale(0.8).move_to([2.2, 2.0, 0])
        h_gen = Tallos([1.4, 0.6, 1.9], centro=(4.2, 0.2), paso=0.7, unidad=0.3, color=INK)
        h_prom = Tallos([1, 1, 1], centro=(4.2, 0.2), paso=0.7, unidad=0.3, color=ESTIMACION)
        l_h = MathTex("h", color=ESTIMACION).scale(0.8).move_to([2.2, 0.2, 0])
        pares = VGroup(*[Line([s_row.x(i), 1.85, 0], [s_row.x(i), 0.8, 0], color=INK, stroke_width=3) for i in range(3)])
        ad81 = MathTex(r"\text{adaptado: }", r"\tfrac{81}{9}=9", color=TXT).scale(1.1).move_to([4.2, -2.4, 0])
        ad81[1].set_color(AMBAR)

        with self.narrar("b1"):
            # «el mejor filtro que existe»
            self.en("mejor")
            self.play(FadeIn(h), run_time=self.dur(0.5))
            self.play(FadeIn(cor, shift=DOWN * 0.2), FadeIn(q), run_time=self.dur(0.5))

            # «una segunda pregunta»
            self.en("segunda")
            self.play(Create(c1), FadeIn(l_gauss), run_time=self.dur(0.8))

            # «no sabemos que sea gaussiano»
            self.en("nogauss")
            self.play(Transform(c1, c2), run_time=self.dur(1.0))

            # «Entonces no podemos calcular»
            self.en("entonces")
            self.play(FadeIn(regla), run_time=self.dur(0.6))

            # «la regla de error mínimo»
            self.en("regla")
            self.play(Create(tachar(regla)), run_time=self.dur(0.5))
            self.sfx("error", gain=-18)

            # «cuánto separa un filtro las dos hipótesis»
            self.en("separa")
            self.play(Create(ca), Create(cb), run_time=self.dur(0.7))
            self.play(Create(sep), run_time=self.dur(0.5))

            # «la relación señal-ruido de su salida»
            self.en("snr")
            self.pop(snr)

            # «la diferencia de medias al cuadrado»
            self.en("medias")
            self.play(Write(num), run_time=self.dur(0.9))

            # «dividida entre la varianza»
            self.en("varianza")
            self.play(Create(raya), run_time=0.3)
            self.play(Write(den), run_time=self.dur(0.5))

        with self.narrar("b2"):
            # «la media con señal»
            self.en("media")
            self.corte()
            self.play(Write(f_m), run_time=self.dur(1.0))

            # «la suma de señal por filtro»
            self.en("sumasf")
            self.play(FadeIn(s_row), FadeIn(l_s), FadeIn(h_gen), FadeIn(l_h), run_time=self.dur(0.7))
            self.play(Create(pares), run_time=self.dur(0.4))

            # «la varianza del ruido»
            self.en("varruido")
            self.play(Write(f_v), run_time=self.dur(1.0))

            # «sigma cuadrado por la suma de los cuadrados»
            self.en("sigma")
            self.resaltar(f_v[2], f_v[3], color=AMBAR, escala=1.2)

            # «Prueba con»
            self.en("prueba")
            self.resaltar(s_row, color=SENAL, escala=1.1)

            # «el promediador, uno, uno, uno»
            self.en("prom")
            self.play(Transform(h_gen, h_prom), run_time=self.dur(0.7))

            # «media cinco»
            self.en("m5")
            self.play(Write(m5), run_time=self.dur(0.7))

            # «veinticinco»
            self.en("v25")
            self.play(Write(v25), run_time=self.dur(0.6))

            # «varianza tres»
            self.en("v3")
            self.play(Write(v3), run_time=self.dur(0.6))

            # «ocho coma tres tres»
            self.en("r833")
            self.play(Write(r833), run_time=self.dur(0.8))

            # «ochenta y uno entre nueve»
            self.en("ad81")
            self.play(Write(ad81), run_time=self.dur(1.0))
            self.sfx("exito", gain=-18)
        self.wait(1.0)
        self.limpiar()
