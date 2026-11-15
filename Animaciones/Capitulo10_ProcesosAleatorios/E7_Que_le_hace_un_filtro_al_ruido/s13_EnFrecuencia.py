"""Escena 13 — Pasar a frecuencia: S_yx = H S_xx y S_yy = |H|² S_xx; por qué el cuadrado."""
from comun.escena import *


def _g(w):
    return 1.0 / np.sqrt(1 + (w / 3.5) ** 2)


class EnFrecuencia(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.pasar()
        self.cuadrado()

    # ------------------------------------------------------------------ b1
    def pasar(self):
        a = formula(r"R_{yx}", "=", "h", "*", r"R_{xx}", escala=1.2).move_to([-2.6, 3.0, 0])
        b = formula(r"R_{yy}", "=", r"R_{hh}", "*", r"R_{xx}", escala=1.2).move_to([-2.6, 1.8, 0])
        flecha_f = Arrow([4.4, 3.4, 0], [4.4, 1.4, 0], color=INK, buff=0, stroke_width=4)
        txt_f = etiqueta("Fourier", AMBAR, 0.65, BOLD).next_to(flecha_f, RIGHT, buff=0.2)
        s_def = formula(r"S_{xx}(j\omega)", "=", r"\mathcal{F}\{R_{xx}(\tau)\}", escala=1.2).move_to([-0.5, 0.35, 0])
        a2 = formula(r"S_{yx}", "=", r"H(j\omega)", r"S_{xx}", escala=1.2).move_to([-2.6, -0.95, 0])
        b2 = formula(r"S_{yy}", "=", r"|H(j\omega)|^2", r"S_{xx}", escala=1.3).move_to([-2.6, -2.25, 0])
        caja_b2 = SurroundingRectangle(b2, color=AMBAR, buff=0.18, stroke_width=3)
        cambio = formula(r"*", r"\;\to\;", r"\cdot", escala=1.6, colores={0: ROJO, 2: VERDE}).move_to([5.2, -1.1, 0])
        incomodas = etiqueta("incómodas", ROJO, 0.6).next_to(a, RIGHT, buff=0.5)

        with self.narrar("b1"):
            # «Las convoluciones son incómodas»
            self.en("incomodas")
            self.play(FadeIn(a), FadeIn(b), run_time=self.dur(0.9))
            self.play(FadeIn(incomodas), run_time=self.dur(0.4))

            # «pasemos a frecuencia»
            self.en("pasar")
            self.play(FadeOut(incomodas), GrowArrow(flecha_f), FadeIn(txt_f), run_time=self.dur(0.7))

            # «ese sub equis equis de jota omega»
            self.en("s_xx")
            self.play(FadeIn(s_def[:2]), run_time=self.dur(0.7))

            # «la transformada de Fourier de la autocorrelación»
            self.en("fourier")
            self.play(FadeIn(s_def[2]), run_time=self.dur(0.8))

            # «Cada convolución se vuelve un producto»
            self.en("producto")
            self.play(FadeIn(cambio), run_time=self.dur(0.6))

            # «la correlación cruzada»
            self.en("cruzada")
            self.play(FadeIn(a2[:2]), run_time=self.dur(0.6))

            # «hache de jota omega por ese sub equis equis»
            self.en("h_s")
            self.play(FadeIn(a2[2:]), run_time=self.dur(0.8))

            # «la autocorrelación de la salida»
            self.en("salida")
            self.play(FadeIn(b2[:2]), run_time=self.dur(0.6))

            # «el módulo de hache al cuadrado»
            self.en("modulo")
            self.play(FadeIn(b2[2]), Create(caja_b2), run_time=self.dur(0.7))

            # «por ese sub equis equis»
            self.en("de_nuevo")
            self.play(FadeIn(b2[3]), run_time=self.dur(0.5))
        self.wait(1.0)

    # ------------------------------------------------------------------ b2
    def cuadrado(self):
        h2 = formula(r"|H|^2", escala=2.2, colores={0: AMBAR}).move_to([0, 3.0, 0])
        # diagrama de fases: H a +φ, su "vuelta" a −φ, y el producto sobre el eje real
        c = np.array([-4.2, -0.3, 0.0])
        ang = np.deg2rad(40)
        eje_re = Line(c + LEFT * 0.4, c + RIGHT * 3.6, color=INK, stroke_width=2)
        eje_im = Line(c + DOWN * 1.9, c + UP * 1.9, color=INK, stroke_width=2)
        a_h = Arrow(c, c + 2.4 * np.array([np.cos(ang), np.sin(ang), 0]), color=ESTIMACION, buff=0, stroke_width=5)
        a_hv = Arrow(c, c + 2.4 * np.array([np.cos(ang), -np.sin(ang), 0]), color=SENAL, buff=0, stroke_width=5)
        l_h = MathTex(r"h", color=ESTIMACION).scale(0.9).move_to(c + 2.9 * np.array([np.cos(ang), np.sin(ang), 0]))
        l_hv = MathTex(r"h(-\tau)", color=SENAL).scale(0.8).move_to(c + 3.1 * np.array([np.cos(ang), -np.sin(ang), 0]))
        ph_p = MathTex(r"+\varphi", color=ESTIMACION).scale(0.8).move_to(c + np.array([1.1, 0.35, 0]))
        ph_m = MathTex(r"-\varphi", color=SENAL).scale(0.8).move_to(c + np.array([1.1, -0.35, 0]))
        a_prod = Arrow(c, c + np.array([3.3, 0, 0]), color=VERDE, buff=0, stroke_width=7)
        l_prod = MathTex(r"|H|^2", color=VERDE).scale(0.9).move_to(c + np.array([3.4, 0.5, 0]))
        # curva de ganancia y su cuadrado
        ax, lab = ejes((0, 10), (0, 1.3), ancho=5.0, alto=2.6, x_label=r"\omega")
        g = VGroup(ax, lab).move_to([3.9, -0.3, 0])
        c_g = ax.plot(_g, x_range=[0, 10], color=ESTIMACION, stroke_width=4)
        c_g2 = ax.plot(lambda w: _g(w) ** 2, x_range=[0, 10], color=AMBAR, stroke_width=5)
        w0 = 2.0
        punto = Dot(ax.c2p(w0, 0), radius=0.1, color=AMBAR)
        mult = etiqueta("× su ganancia al cuadrado", AMBAR, 0.55).move_to([3.9, 1.6, 0])
        fase_txt = etiqueta("fase", INK, 0.6).move_to([-4.2, -3.4, 0])
        fase_x = tachar(fase_txt)
        Ld = ejes((0, 10), (0, 1.3), ancho=5.0, alto=2.6, x_label=r"\Omega")
        pal = Tallos([_g(w) ** 2 for w in np.linspace(0.5, 9.5, 10)], centro=(3.9, -3.1), paso=0.42, unidad=0.7, color=AMBAR)

        with self.narrar("b2"):
            # «¿Por qué al cuadrado?»
            self.en("porque")
            self.corte()
            self.pop(h2, sonido="pop")

            # «aparece dos veces»
            self.en("dos_veces")
            self.play(Create(eje_re), Create(eje_im), GrowArrow(a_h), FadeIn(l_h), run_time=self.dur(0.8))

            # «dada la vuelta»
            self.en("vuelta")
            self.play(GrowArrow(a_hv), FadeIn(l_hv), run_time=self.dur(0.7))

            # «sus desfases se cancelan»
            self.en("cancelan")
            self.play(FadeIn(ph_p), FadeIn(ph_m), run_time=self.dur(0.5))
            self.play(GrowArrow(a_prod), FadeIn(l_prod), run_time=self.dur(0.8))

            # «En cada frecuencia»
            self.en("cada_frec")
            self.play(FadeIn(g), Create(c_g), FadeIn(punto), run_time=self.dur(0.9))

            # «el filtro multiplica»
            self.en("multiplica")
            self.play(FadeIn(mult), run_time=self.dur(0.5))

            # «el cuadrado de su ganancia»
            self.en("cuadrado")
            self.play(Create(c_g2), run_time=self.dur(1.0))

            # «la fase no importa»
            self.en("fase")
            self.play(FadeIn(fase_txt), run_time=0.3)
            self.play(Create(fase_x), run_time=0.4)

            # «En tiempo discreto»
            self.en("discreto")
            self.play(FadeOut(mult), FadeIn(pal), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
