"""Escena 13 — La señal con barrido de frecuencia (chirp): comprime sin el tope de Barker."""
from comun.escena import *


def _chirp(t, f0=3.0, f1=15.0):
    return np.cos(2 * np.pi * (f0 * t + (f1 - f0) * t ** 2 / 2))


class ElBarridoDeFrecuencia(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        bk = Tallos(list(BARKER13), centro=(-3.6, 2.8), paso=0.3, unidad=0.5, color=SENAL)
        mu = muro(1.4, 0.35).move_to([-0.9, 2.8, 0])
        t13 = Text("13", color=ERROR, weight=BOLD).scale(0.7).move_to([-0.9, 3.75, 0])
        mas = Text("?", color=AMBAR, weight=BOLD).scale(1.8).move_to([3.0, 2.8, 0])
        bomb = bombilla().scale(0.9).move_to([6.2, 3.1, 0])
        L = Lienzo(ancho=10.0, alto=1.7, t_rango=(0, 1), v_max=1.0, centro=(0.0, 1.5))
        t = np.linspace(0, 1, 700)
        seno = L.curva(t, np.cos(2 * np.pi * 6 * t), SENAL, 3.0)
        chirp = L.curva(t, _chirp(t), SENAL, 3.0)
        base = L.base()
        espe = Rectangle(width=3.6, height=1.9, color=INK, stroke_width=2).move_to([-4.0, -2.3, 0])
        rec = Line(espe.get_corner(DL) + RIGHT * 0.15 + UP * 0.15, espe.get_corner(UR) + LEFT * 0.15 + DOWN * 0.15,
                   color=AMBAR, stroke_width=6)
        ft = Text("tiempo →", color=INK).scale(0.38).next_to(espe, DOWN, buff=0.1)
        ff = Text("frecuencia ↑", color=INK).scale(0.38).next_to(espe, LEFT, buff=0.1).rotate(PI / 2)
        alt = altavoz().scale(0.8).move_to([-0.4, -2.0, 0])
        pal = Text("chirp", color=AMBAR, weight=BOLD).scale(0.9).move_to([1.9, -2.0, 0])
        tr = VGroup(*[L.curva(t[(t >= a) & (t <= b)], _chirp(t[(t >= a) & (t <= b)]), c, 4.5)
                      for (a, b), c in zip([(0, 0.33), (0.33, 0.66), (0.66, 1.0)], [CIAN, AMBAR, VERDE])])
        copia = L.curva(t, _chirp(np.clip(t - 0.08, 0, 1)), INK, 3.0, 0.8).shift(DOWN * 1.9 + RIGHT * 0.0)
        cr = cruz(ROJO, 0.7).move_to([5.8, -0.4, 0])
        fino = Tallos([0.1] * 6 + [4.0] + [0.1] * 6, centro=(4.5, -2.5), paso=0.3, unidad=0.45, color=AMBAR)
        with self.narrar("b1"):
            # «no pasan de trece»
            self.en("tope13")
            self.play(FadeIn(bk), FadeIn(mu), FadeIn(t13), run_time=self.dur(0.8))
            # «Para pulsos más largos»
            self.en("maslargos")
            self.pop(mas)
            # «hay otra idea»
            self.en("idea")
            self.pop(bomb)
            # «una sinusoide»
            self.en("sinus")
            self.play(*[FadeOut(m) for m in (bk, mu, t13, mas, bomb)], FadeIn(base), Create(seno), run_time=self.dur(0.9))
            # «cuya frecuencia va subiendo poco a poco»
            self.en("sube")
            self.play(Transform(seno, chirp), run_time=self.dur(1.6))
            # «Un barrido de frecuencia»
            self.en("barrido")
            self.play(FadeIn(espe), Create(rec), FadeIn(ft), FadeIn(ff), run_time=self.dur(1.0))
            # «un chirrido»
            self.en("chirrido")
            self.play(FadeIn(alt), run_time=self.dur(0.5))
            # «un chirp»
            self.en("chirp")
            self.pop(pal)
            # «cada tramo tiene una frecuencia distinta»
            self.en("tramos")
            self.play(FadeIn(tr), run_time=self.dur(0.8))
            # «ningún tramo se parece a otro desplazado»
            self.en("ninguno")
            self.play(FadeIn(copia), FadeIn(cr), run_time=self.dur(0.8))
            # «la autocorrelación se estrecha»
            self.en("estrecha")
            self.play(FadeIn(fino), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
