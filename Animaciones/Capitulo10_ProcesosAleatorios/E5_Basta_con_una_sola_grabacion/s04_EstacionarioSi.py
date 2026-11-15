"""Escena 04 — ¿Estacionario? ¿Ergódico? La pila es estacionaria."""
from comun.escena import *


class EstacionarioSi(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        L = Lienzo(ancho=5.8, alto=3.6, t_rango=(0, 1), v_max=3.0, centro=(-3.3, 0.2))
        rectas = rectas_pilas(L, ancho=3.0)
        base = L.base()
        c1 = caja("¿estacionario?", AZUL, ancho=3.4, alto=0.9).move_to([3.6, 1.7, 0])
        c2 = caja("¿ergódico?", AZUL, ancho=3.4, alto=0.9).move_to([3.6, -0.3, 0])

        with self.narrar("b1"):
            # «dos preguntas»
            self.en("preguntas")
            self.play(FadeIn(rectas), Create(base), run_time=0.4)
            self.play(FadeIn(c1, shift=LEFT * 0.3), FadeIn(c2, shift=LEFT * 0.3), run_time=self.dur(0.6))

            # «¿este proceso es estacionario?»
            self.en("q1")
            self.resaltar(c1)

            # «¿Y es ergódico?»
            self.en("q2")
            self.resaltar(c2)

            # «Piénsalo un momento»
            self.en("pausa")
            ra = reloj_arena().scale(0.9).move_to([3.6, -2.2, 0])
            self.play(FadeIn(ra), run_time=0.3)
            self.play(Rotate(ra, angle=PI), run_time=self.dur(1.5))

            # «Estacionario lo es»
            self.en("si")
            self.play(FadeOut(ra), run_time=0.2)
            si = self.palabra("sí", VERDE, 0.9).next_to(c1, RIGHT, buff=0.2)
            tl = tilde(VERDE, 0.4).next_to(si, RIGHT, buff=0.1)
            self.sfx("exito")
            self.play(FadeIn(si), FadeIn(tl), c1[0].animate.set_stroke(VERDE), run_time=0.4)

            # «en el sentido más fuerte»
            self.en("fuerte")
            fu = etiqueta("estricto", VERDE, 0.6, BOLD).next_to(c1, DOWN, buff=0.2)
            self.pop(fu)

            # «la estadística no cambia nunca»
            self.en("nocambia")
            cursor = Line(L.p(0.02, -1.9), L.p(0.02, 1.9), color=AMBAR, stroke_width=3.5)
            self.play(Create(cursor), run_time=0.3)
            self.play(cursor.animate.shift(RIGHT * 5.2), run_time=self.dur(1.6), rate_func=linear)

            # «porque nada cambia nunca»
            self.en("nada")
            self.play(rectas.animate.set_stroke(width=6), run_time=0.4)

            # «cuándo hagas el corte»
            self.en("corte")
            c_a = L.vertical(0.25, AMBAR, 3.5, mitad=1.9)
            self.play(FadeOut(cursor), Create(c_a), run_time=0.4)
            c_b = L.vertical(0.75, AMBAR, 3.5, mitad=1.9)
            self.play(Create(c_b), run_time=0.4)

            # «la densidad de los voltajes»
            self.en("densidad")
            ba = campana_en(float(L.x(0.25)), 2.85)
            bb = campana_en(float(L.x(0.75)), 2.85)
            self.play(Create(ba), Create(bb), run_time=self.dur(0.8))

            # «siempre la misma»
            self.en("misma")
            ig = MathTex(r"\mu=0,\ \sigma^2=4", color=AMBAR).scale(0.9).move_to([-3.3, -2.8, 0])
            self.pop(ig)
        self.wait(1.0)
        self.limpiar()
