"""Escena 07 — Estacionario no es lo mismo que ergódico."""
from comun.escena import *


class DosPropiedades(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        a = self.palabra("estacionario", AZUL, 0.9).move_to([-3.6, 2.9, 0])
        b = self.palabra("ergódico", AMBAR, 0.9).move_to([3.6, 2.9, 0])
        ne = MathTex(r"\neq", color=TXT).scale(1.6).move_to([0, 2.9, 0])
        Lizq = Lienzo(ancho=5.0, alto=2.2, t_rango=(0, 1), v_max=3.0, centro=(-3.6, 0.5))
        rectas = rectas_pilas(Lizq, ancho=2.5)
        t = np.linspace(0, 1, 200)
        Lder = Lienzo(ancho=5.0, alto=2.2, t_rango=(0, 1), v_max=3.0, centro=(3.6, 0.5))
        s = 1.1 * serie(17, 200, 0.97)
        una = Lder.curva(t, s, SENAL, 4)

        with self.narrar("b1"):
            # «estacionario y ergódico»
            self.en("dos")
            self.pop(a)
            self.pop(b)
            self.play(FadeIn(ne), run_time=0.3)

            # «cosas distintas»
            self.en("distintas")
            self.resaltar(ne, escala=1.4)

            # «Estacionario dice»
            self.en("estacp")
            self.resaltar(a, escala=1.15)

            # «no cambia con el tiempo»
            self.en("estac")
            cursor = Line(Lizq.p(0.1, -1.6), Lizq.p(0.1, 1.6), color=AMBAR, stroke_width=3.5)
            cam = campana_en(float(Lizq.x(0.5)), -2.5)
            self.play(FadeIn(rectas), Create(cursor), run_time=0.4)
            self.play(cursor.animate.shift(RIGHT * 3.0), run_time=self.dur(1.2), rate_func=linear)
            self.play(Create(cam), run_time=0.4)

            # «Ergódico dice»
            self.en("ergop")
            self.resaltar(b, escala=1.15)

            # «una sola realización»
            self.en("una")
            self.play(Create(Lder.base()), Create(una), run_time=self.dur(1.2))

            # «recorre todo lo que el ensemble puede hacer»
            self.en("ergo")
            banda = Rectangle(width=5.0, height=2.0, color=AMBAR, stroke_width=0).set_fill(AMBAR, 0.12).move_to(Lder.p(0.5, 0))
            self.play(FadeIn(banda), run_time=0.5)

            # «La pila es estacionaria»
            self.en("pila")
            tl = tilde(VERDE, 0.45).next_to(a, RIGHT, buff=0.2)
            self.play(FadeIn(tl, scale=0.5), run_time=0.4)

            # «encerrada en su valor»
            self.en("encerrada")
            fr = VGroup(*[Rectangle(width=2.5, height=0.42, color=ROJO, stroke_width=3).move_to(Lizq.p(0.5, v))
                          for v in (1, -2, 2, 0)])
            self.play(Create(fr), run_time=self.dur(0.8))

            # «¿Qué tiene que pasar»
            self.en("pregunta")
            q = self.palabra("¿?", ROJO, 1.6).move_to([0, -1.6, 0])
            self.pop(q)

            # «el promedio temporal sí funcione»
            self.en("funcione")
            prom = Line(Lder.p(0.0, 0.0), Lder.p(1.0, 0.0), color=VERDE, stroke_width=5)
            self.play(Create(prom), run_time=self.dur(1.0))
        self.wait(1.0)
        self.limpiar()
