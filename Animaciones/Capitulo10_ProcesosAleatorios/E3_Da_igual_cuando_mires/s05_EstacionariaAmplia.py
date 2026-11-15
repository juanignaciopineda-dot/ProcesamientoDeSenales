"""Escena 05 — Estacionariedad en sentido amplio: media constante y R que solo depende del retardo."""
from comun.escena import *


class EstacionariaAmplia(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        cab = caja("amplia · WSS", VERDE, ancho=3.2, alto=0.7).move_to([-4.6, 3.4, 0])
        marco_a = RoundedRectangle(corner_radius=0.15, width=6.2, height=5.8, color=INK, stroke_width=2.5).move_to([-3.5, -0.6, 0])
        marco_b = marco_a.copy().move_to([3.5, -0.6, 0])
        n1 = Text("1", color=AMBAR, weight=BOLD).scale(0.7).move_to([-6.3, 1.9, 0])
        n2 = Text("2", color=AMBAR, weight=BOLD).scale(0.7).move_to([0.7, 1.9, 0])
        La = Lienzo(ancho=5.2, alto=1.6, t_rango=(0, 1), v_max=2.0, centro=(-3.5, -1.0))
        Lb = Lienzo(ancho=5.2, alto=1.6, t_rango=(0, 1), v_max=2.0, centro=(3.5, -0.6))
        t = np.linspace(0, 1, 220)

        with self.narrar("b1"):
            # «La versión débil»
            self.en("debil")
            self.pop(cab)

            # «en sentido amplio»
            self.en("amplio")
            self.play(FadeIn(etiqueta("en sentido amplio", INK, 0.55).move_to([-0.8, 3.4, 0])), run_time=0.3)

            # «usaremos casi siempre»
            self.en("siempre")
            self.resaltar(cab, color=AMBAR, escala=1.08)

            # «dos cosas»
            self.en("dos_cosas")
            self.play(FadeIn(marco_a), FadeIn(marco_b), run_time=0.3)
            self.pop(n1, n2)

            # «la media sea una constante»
            self.en("media_cte")
            f1 = formula(r"\mu_X(t)", "=", r"\mu_X", escala=0.95).move_to([-3.5, 1.6, 0])
            base_a = La.base()
            linea = Line(La.p(0, 0.6), La.p(1, 0.6), color=AMBAR, stroke_width=4)
            self.play(FadeIn(f1), Create(base_a), Create(linea), run_time=self.dur(0.7))

            # «en todos los instantes»
            self.en("todos")
            pts = VGroup(*[Dot(La.p(x, 0.6), radius=0.09, color=AMBAR) for x in (0.1, 0.25, 0.4, 0.55, 0.7, 0.85)])
            self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in pts], lag_ratio=0.15), run_time=self.dur(1.2))

            # «la autocorrelación entre dos instantes»
            self.en("autoc")
            f2 = formula(r"R_{XX}", "(", "t_1", ",", "t_2", ")", escala=0.95).move_to([3.5, 1.6, 0])
            base_b = Lb.base()
            cb = Lb.curva(t, 0.6 * serie(31, 220, 0.9), SENAL, 3)
            v1, v2 = Lb.vertical(0.2, AMBAR, 3.5, mitad=0.85), Lb.vertical(0.55, AMBAR, 3.5, mitad=0.85)
            self.play(FadeIn(f2), Create(base_b), Create(cb), Create(v1), Create(v2), run_time=self.dur(0.9))

            # «dependa solo de la separación»
            self.en("separacion")
            llave = BraceBetweenPoints(Lb.p(0.55, -0.9) + DOWN * 0.05, Lb.p(0.2, -0.9) + DOWN * 0.05, color=AMBAR)
            f3 = MathTex(r"\text{depende solo de } t_1 - t_2", color=TXT).scale(0.8).move_to([3.5, 0.75, 0])
            self.play(FadeIn(f3), Create(llave), run_time=self.dur(0.8))

            # «no de dónde estén»
            self.en("donde")
            grupo = VGroup(v1, v2, llave)
            self.play(grupo.animate.shift(RIGHT * 1.1), run_time=self.dur(1.0))

            # «retardo, o lag»
            self.en("lag")
            rl = etiqueta("retardo (lag)", AMBAR, 0.6, BOLD).move_to([3.5, -2.35, 0])
            self.play(FadeIn(rl, shift=UP * 0.15), run_time=0.4)

            # «tau»
            self.en("tau")
            ft = MathTex(r"\tau = t_1 - t_2", color=AMBAR).scale(0.9).move_to([3.5, -3.05, 0])
            self.pop(ft)
        self.wait(1.0)
        self.limpiar()
