"""Escena 13 — Cierre: resumen del episodio, el cabo suelto (cómo se calcula g) y anuncio del E4."""
import math

from comun.escena import *


def qf(x: float) -> float:
    return 0.5 * math.erfc(x / math.sqrt(2.0))


class Cierre(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.resumen()
        self.cabo_suelto()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def resumen(self):
        L = lienzo_g3(centro=(0.0, -1.4))
        base = eje_g3(L, marcas=())
        cam0 = dens3(L, 0, 3, RUIDO)
        cam1 = dens3(L, 9, 3, SENAL)
        c_rot = MathTex("0", color=RUIDO).scale(0.7).move_to(L.p(0, 0) + DOWN * 0.35)
        e_rot = MathTex("E", color=SENAL).scale(0.7).move_to(L.p(9, 0) + DOWN * 0.35)
        umb = umbral3(L, 4.5, alto=2.0)
        cola_d = cola3(L, 0, 3, 4.5, 17)
        cola_i = cola3(L, 9, 3, -8, 4.5)
        R = Lienzo(ancho=2.2, alto=4.4, t_rango=(0, 1), v_max=1.0, centro=(5.3, 0.6))
        gs = np.linspace(-12, 21, 160)
        roc = traza(R.x(np.array([qf(g / 3) for g in gs])), R.y(np.array([qf(g / 3 - 3) for g in gs])), ESTIMACION, 4)
        marco_r = Rectangle(width=2.2, height=2.2, color=INK, stroke_width=1.5, stroke_opacity=0.5).move_to(R.p(0.5, 0.5))
        roc_t = Text("curva ROC", color=ESTIMACION).scale(0.45).next_to(marco_r, UP, buff=0.1)
        en_t = formula("E", "/", r"\sigma^2", escala=1.8, colores={0: SENAL, 2: RUIDO}).move_to([-4.6, 2.6, 0])
        pa = Barras((2, 2, 1), centro=(-1.4, 2.6), paso=0.6, unidad=0.3, color=SENAL, ancho=0.4)
        pb = Barras((3, 0, 0), centro=(1.0, 2.6), paso=0.6, unidad=0.3, color=SENAL, ancho=0.4)
        igual = MathTex("=", color=AMBAR).scale(1.4).move_to([-0.2, 2.6, 0])

        with self.narrar("b1"):
            # «separar dos campanas»
            self.en("campanas")
            self.corte()
            self.play(FadeIn(base), Create(cam0), Create(cam1), run_time=self.dur(0.8))

            # «una en cero y otra en la energía»
            self.en("centros")
            self.play(FadeIn(c_rot), FadeIn(e_rot), run_time=self.dur(0.5))

            # «el área de dos colas»
            self.en("colas")
            self.play(Create(umb), FadeIn(cola_d), FadeIn(cola_i), run_time=self.dur(0.8))

            # «Con un umbral que usa lo que sabemos»
            self.en("umbral")
            self.play(umb.animate.shift(RIGHT * (L.x(5.886) - L.x(4.5))),
                      Transform(cola_d, cola3(L, 0, 3, 5.886, 17)), Transform(cola_i, cola3(L, 9, 3, -8, 5.886)),
                      run_time=self.dur(1.0))

            # «la curva ROC»
            self.en("roc")
            self.play(Create(marco_r), Create(roc), FadeIn(roc_t), run_time=self.dur(1.0))

            # «solo cuenta la energía entre el ruido»
            self.en("energia")
            self.pop(en_t)

            # «no la forma»
            self.en("forma")
            self.play(FadeIn(pa), FadeIn(pb), FadeIn(igual, scale=0.5), run_time=self.dur(0.7))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def cabo_suelto(self):
        g = formula("g", "=", r"\sum", "r[n]", "s[n]", escala=1.6,
                    colores={0: ESTIMACION, 3: MEDIDA, 4: SENAL}).move_to([0, 2.8, 0])
        hilo = ArcBetweenPoints(g[4].get_bottom() + DOWN * 0.3, g[4].get_bottom() + DOWN * 1.4 + RIGHT * 0.8,
                                angle=-PI / 2, color=AMBAR, stroke_width=5)
        aparato = caja("aparato", ESTIMACION, ancho=2.8, alto=1.2, scale=0.6).move_to([3.0, -0.8, 0])
        rs = VGroup(*[VGroup(Circle(radius=0.32, color=MEDIDA, stroke_width=3).set_fill(MEDIDA, 0.2),
                             Text(str(v), color=MEDIDA, weight=BOLD).scale(0.5)) for v in (3, 1, 2)])
        for r_, x in zip(rs, (-5.6, -4.4, -3.2)):
            r_.move_to([x, -0.8, 0])
        flecha_in = Arrow([-2.2, -0.8, 0], aparato.get_left() + LEFT * 0.1, color=INK, stroke_width=4, buff=0)
        duda = interrogante13(AMBAR, 1.6).move_to(aparato.get_top() + UP * 0.6)
        h = Barras((1, 2, 2), centro=(3.0, -2.9), paso=0.7, unidad=0.3, color=SENAL, ancho=0.5)
        rev = Text("la señal puesta al revés", color=SENAL).scale(0.5).next_to(h, DOWN, buff=0.2)
        filtro_t = Text("filtro", color=ESTIMACION, weight=BOLD).scale(0.6).move_to(aparato[1])
        titulo1 = self.palabra("El filtro que es", TXT, 1.4).move_to([0, 0.7, 0])
        titulo2 = self.palabra("la señal al revés", AMBAR, 1.4).move_to([0, -0.7, 0])
        sig = Text("Capítulo 13 · siguiente episodio", color=INK).scale(0.5).move_to([0, -1.9, 0])

        with self.narrar("b2"):
            # «un cabo suelto»
            self.en("cabo")
            self.corte()
            self.play(Write(g), run_time=self.dur(1.0))
            self.play(Create(hilo), run_time=self.dur(0.5))

            # «multiplicaciones y una suma»
            self.en("suma")
            self.play(g[3].animate(rate_func=there_and_back).scale(1.3), g[4].animate(rate_func=there_and_back).scale(1.3),
                      run_time=self.dur(0.7))
            self.play(g[2].animate(rate_func=there_and_back).scale(1.3).set_color(AMBAR), run_time=self.dur(0.7))

            # «y un aparato real»
            self.en("aparato")
            self.play(FadeIn(aparato, shift=LEFT * 0.3), run_time=self.dur(0.7))

            # «muestra a muestra»
            self.en("muestra")
            self.play(LaggedStart(*[FadeIn(r_, shift=RIGHT * 0.2) for r_ in rs], lag_ratio=0.25), Create(flecha_in),
                      run_time=self.dur(0.9))
            for r_ in rs:
                self.play(r_.animate.move_to(aparato.get_left() + RIGHT * 0.1).scale(0.3).fade(1), run_time=0.35)

            # «¿Cómo lo hace?»
            self.en("como")
            self.pop(duda)

            # «un filtro que es la señal puesta al revés»
            self.en("filtro")
            self.play(FadeOut(duda), ReplacementTransform(aparato[1], filtro_t), run_time=self.dur(0.5))
            self.play(FadeIn(h), FadeIn(rev), run_time=self.dur(0.8))

            # «Es el siguiente episodio»
            self.en("siguiente")
            self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=self.dur(0.4))

            # «El filtro que es la señal al revés»
            self.en("titulo")
            self.pop(titulo1)
            self.pop(titulo2)
            self.play(FadeIn(sig), run_time=0.4)
        self.wait(0.6)
