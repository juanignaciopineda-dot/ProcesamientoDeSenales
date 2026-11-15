"""Escena 10 — Encuesta: ¿qué espectro tiene un proceso sin memoria?"""
from comun.escena import *


class LaEncuestaDeLaMemoriaCero(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        mini = Espectro(w_max=3, y_max=1.2, ancho=2.6, alto=1.1, centro=(-5.4, 2.6), x_label=None)
        r1, r2 = mini.flecha(-1.8, 1.0, AMBAR, ancho=5), mini.flecha(1.8, 1.0, AMBAR, ancho=5)
        mem = Text("memoria infinita", color=INK).scale(0.45).move_to([-5.4, 1.35, 0])
        tira = tira_pm1([1, -1, -1, 1, -1, 1, 1, -1], lado=0.8, escala_txt=0.5).move_to([1.4, 2.2, 0])
        marcos = VGroup(*[SurroundingRectangle(c, color=AMBAR, buff=0.03, stroke_width=3) for c in tira.celdas])
        for m in marcos:
            m.permitir_encima = True
        hilos = VGroup(*[Line(tira.celdas[i].get_right(), tira.celdas[i + 1].get_left(), color=INK, stroke_width=3)
                         for i in range(7)])
        tachas = VGroup(*[cruz(ROJO, 0.4).move_to(h.get_center() + DOWN * 0.45) for h in hilos])

        def opcion(x, letra, hay):
            cj = RoundedRectangle(corner_radius=0.15, width=3.6, height=2.6, color=INK, stroke_width=3).move_to([x, -1.9, 0])
            e = Espectro(w_max=3, y_max=1.2, ancho=2.8, alto=1.5, centro=(x, -2.6), x_label=None)
            if hay == "raya":
                f = e.flecha(0, 1.1, AMBAR)
            elif hay == "plano":
                f = e.curva(lambda w: 0.7, AMBAR)
            else:
                f = VMobject()
            t = Text(letra, color=AMBAR, weight=BOLD).scale(0.6).move_to([x - 1.5, -0.9, 0])
            return VGroup(cj, e.ejes, f, t)

        a, b, c = opcion(-4.3, "una raya en cero", "raya"), opcion(0.0, "nada", "nada"), opcion(4.3, "plano", "plano")
        # los rótulos de las opciones van debajo de cada caja
        for g, txt in ((a, "una raya en cero"), (b, "no tendría nada"), (c, "sería plano")):
            g[3].become(Text(txt, color=AMBAR, weight=BOLD).scale(0.5).move_to(g[0].get_bottom() + DOWN * 0.35))
        with self.narrar("b1"):
            # «Memoria infinita, dos rayas»
            self.en("resumen")
            self.play(Create(mini.ejes), GrowArrow(r1), GrowArrow(r2), FadeIn(mem), run_time=self.dur(0.8))
            # «un proceso que no recuerda absolutamente nada»
            self.en("nada")
            self.play(FadeIn(tira), run_time=self.dur(0.8))
            # «cada instante»
            self.en("instante")
            self.play(Create(marcos), run_time=self.dur(1.0))
            # «ningún otro»
            self.en("ninguno")
            self.play(FadeOut(marcos), Create(hilos), run_time=self.dur(0.5))
            self.play(Create(tachas), run_time=self.dur(0.8))
            # «una raya en cero»
            self.en("opa")
            self.play(FadeIn(a), run_time=self.dur(0.4))
            # «no tendría nada»
            self.en("opb")
            self.play(FadeIn(b), run_time=self.dur(0.4))
            # «sería plano»
            self.en("opc")
            self.play(FadeIn(c), run_time=self.dur(0.4))
            # «Piénsalo»
            self.en("piensa")
            q = Text("¿?", color=AMBAR, weight=BOLD).scale(1.6).move_to([6.3, 3.2, 0])
            self.pop(q)
            self.play(q.animate(rate_func=there_and_back).scale(1.3), run_time=1.0)
        self.wait(1.0)
        self.limpiar()
