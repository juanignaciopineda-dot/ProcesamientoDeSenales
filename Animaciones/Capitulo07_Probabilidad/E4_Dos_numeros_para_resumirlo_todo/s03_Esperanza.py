"""Escena 03 — La media del dado: el promedio de las tiradas se estabiliza en 3,5."""
from comun.escena import *


class Esperanza(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        N = 60
        prom = promedios_dado(N, semilla=7)
        tiradas = np.random.default_rng(7).integers(1, 7, N)
        L = Lienzo(ancho=10.4, alto=3.4, t_rango=(0, N), v_max=2.8, centro=(0, -1.1))
        dado = dado_n(5).scale(1.0).move_to([-5.6, 2.9, 0])
        resultados = VGroup(*[Text(str(v), color=TXT, weight=BOLD).scale(0.8) for v in (4, 2, 6, 1, 5)]
                            ).arrange(RIGHT, buff=0.55).move_to([-2.2, 2.9, 0])
        R = Regla7(centro=(0, 2.3), ancho=8.0, rotulos=False)
        caras = caras7(R, escala=0.6, altura=0.9)
        with self.narrar("b1"):
            # «Tira un dado muchas veces»
            self.en("dado")
            self.play(FadeIn(dado, scale=0.4), Rotate(dado, angle=2 * PI), run_time=self.dur(0.7))
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in resultados], lag_ratio=0.25),
                      run_time=self.dur(1.0))

            # «haciendo el promedio»
            self.en("promedio")
            base = L.base()
            et = Text("Promedio", color=INK).scale(0.5).move_to(L.p(0, 0) + LEFT * 0.85)
            self.play(Create(base), FadeIn(et), run_time=self.dur(0.6))

            # «Al principio salta»
            self.en("salta")
            curva = L.curva(np.arange(1, N + 1), prom - 3.5, SENAL, 4)
            self.play(Create(curva), run_time=self.dur(2.1), rate_func=linear)

            # «se estabiliza alrededor de un número»
            self.en("estabiliza")
            linea = DashedLine(L.p(0, 0), L.p(N, 0), color=AMBAR, stroke_width=3)
            self.play(Create(linea), run_time=self.dur(0.6))

            # «tres coma cinco»
            self.en("tres_cinco")
            l35 = Text("3,5", color=AMBAR, weight=BOLD).scale(0.8).move_to(L.p(N, 0) + RIGHT * 0.5)
            self.pop(l35)

            # «el dado nunca saca»
            self.en("nunca")
            self.play(FadeOut(dado), FadeOut(resultados), FadeIn(R), FadeIn(caras), run_time=self.dur(0.6))
            x = cruz(ROJO, 0.55).move_to(R.p(3.5) + UP * 0.9)
            self.play(Create(x), run_time=self.dur(0.4))

            # «alrededor del cual se reparten»
            self.en("reparten")
            puntos = VGroup(*[Dot(L.p(i + 1, tiradas[i] - 3.5), radius=0.055, color=SENAL).set_opacity(0.7)
                              for i in range(0, N, 2)])
            self.play(LaggedStart(*[FadeIn(p) for p in puntos], lag_ratio=0.05), run_time=self.dur(1.5))

            # «Se llama media»
            self.en("media")
            w1 = self.palabra("Media", AMBAR, 0.9).move_to([-2.6, -3.55, 0])
            self.pop(w1)

            # «o esperanza»
            self.en("esperanza")
            w2 = self.palabra("Esperanza", AMBAR, 0.9).move_to([2.6, -3.55, 0])
            self.pop(w2)
        self.wait(1.0)
        self.limpiar()
