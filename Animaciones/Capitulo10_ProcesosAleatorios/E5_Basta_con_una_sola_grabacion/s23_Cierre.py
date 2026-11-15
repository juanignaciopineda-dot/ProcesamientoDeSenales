"""Escena 23 — Cierre: anuncia el E6, «Adivinar el futuro, limpiar el presente»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "23"

    def construct(self):
        L = Lienzo(ancho=6.0, alto=2.0, t_rango=(0, 1), v_max=3.0, centro=(-3.5, 0.5))
        t = np.linspace(0, 1, 300)
        s = 1.0 * serie(77, 300, 0.6)
        acum = np.cumsum(s) / np.arange(1, 301)

        with self.narrar("b1"):
            # «se borra»
            self.en("borra")
            c1 = caja("se borra", VERDE, ancho=3.0, alto=0.8).move_to([-3.5, 3.2, 0])
            tl = tilde(VERDE, 0.4).next_to(c1, RIGHT, buff=0.15)
            self.play(FadeIn(c1), FadeIn(tl), run_time=0.4)

            # «una sola grabación basta»
            self.en("basta")
            gr = L.curva(t, s, SENAL, 2.5, 0.6)
            mu = DashedLine(L.p(0, 0), L.p(1, 0), color=INK, stroke_width=2)
            pr = L.curva(t, acum, AMBAR, 5)
            self.play(Create(L.base()), Create(gr), Create(mu), run_time=self.dur(1.0))
            self.play(Create(pr), run_time=self.dur(1.6), rate_func=linear)

            # «aunque cada dato cuente menos»
            self.en("menos")
            self.play(gr.animate.set_stroke(opacity=0.2), run_time=0.5)

            # «Si no se borra»
            self.en("noborra")
            c2 = caja("no se borra", ROJO, ancho=3.4, alto=0.8).move_to([3.5, 3.2, 0])
            p = pila("+2").scale(0.9).move_to([3.5, 1.4, 0])
            x = cruz(ROJO, 0.4).next_to(c2, RIGHT, buff=0.15)
            self.play(FadeIn(c2), FadeIn(p), FadeIn(x), run_time=0.5)

            # «Pero esa memoria que estorba»
            self.en("estorba")
            fila = fila_puntos(10, 6.0, (-3.0, -1.4), SENAL, 0.12)
            hilos = hilos_entre(fila, AMBAR, 4)
            self.play(FadeIn(fila), Create(hilos), run_time=self.dur(0.9))

            # «tercera cara»
            self.en("tercera")
            c3 = caja("predecir", AMBAR, ancho=3.0, alto=0.9).move_to([3.5, -1.4, 0])
            self.pop(c3)

            # «si una muestra recuerda a la anterior»
            self.en("recuerda")
            self.resaltar(fila[-2], fila[-1], color=AMBAR, escala=1.5)

            # «adivinar la siguiente»
            self.en("adivinar")
            sig = Dot([0.6, -1.4, 0], radius=0.14, color=ROJO)
            q = self.palabra("?", ROJO, 0.9).next_to(sig, UP, buff=0.15)
            self.play(FadeIn(sig, scale=0.5), FadeIn(q), run_time=0.5)

            # «en el próximo episodio»
            self.en("proximo")
            self.corte()
            sl = etiqueta("próximo episodio", INK, 0.7).move_to([0, 1.6, 0])
            self.play(FadeIn(sl), run_time=0.3)

            # «Adivinar el futuro, limpiar el presente»
            self.en("titulo")
            a = self.palabra("Adivinar el futuro,", TXT, 1.3).move_to([0, 0.2, 0])
            b = self.palabra("limpiar el presente", AMBAR, 1.3).move_to([0, -1.2, 0])
            self.pop(a)
            self.pop(b)
        self.wait(1.0)
        self.limpiar()
