"""Escena 06 — La onda base: un chirp, de 0 a B a lo largo del símbolo; en el plano, una rampa."""
from comun.escena import *
from comun.figuras_lora import *


def _chirp(t, f0=1.0, f1=17.0):
    return np.cos(2 * np.pi * (f0 * t + (f1 - f0) * t ** 2 / 2))


class ElChirp(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        v20 = Text("20", color=AMBAR, weight=BOLD).scale(1.2).move_to([-6.1, 2.2, 0])
        fl = Arrow([-5.5, 2.2, 0], [-4.5, 2.2, 0], color=INK, stroke_width=4, buff=0)
        L = Lienzo(ancho=10.0, alto=1.9, t_rango=(0, 1), v_max=1.0, centro=(0.9, 2.2))
        t = np.linspace(0, 1, 900)
        base = L.base()
        onda = L.curva(t, _chirp(t), SENAL, 3.0)
        pal = Text("Chirp", color=AMBAR, weight=BOLD).scale(0.9).move_to([0.9, 3.6, 0])
        c0 = Text("0", color=INK, weight=BOLD).scale(0.55).move_to([-4.1, 0.75, 0])
        cb = MathTex("B", color=INK).scale(0.9).move_to([5.9, 0.75, 0])
        ct = cota([-3.7, 0.75, 0], [5.5, 0.75, 0], "T_s", INK, DOWN, 0.5, tex=True)
        P = PlanoTF(centro=(-0.6, -2.0), ancho=6.0, alto=2.6, escala=0.45)
        rad = radar13().scale(1.1).move_to([5.3, -1.7, 0])
        rampa = P.rampa(0, grosor=6)
        with self.narrar("b1"):
            # «convertir ese número en una onda»
            self.en("onda")
            self.pop(v20)
            self.play(GrowArrow(fl), FadeIn(base), run_time=self.dur(0.5))
            # «un chirp»
            self.en("chirp")
            self.pop(pal)
            # «cuya frecuencia sube sin parar»
            self.en("sube")
            self.play(Create(onda, rate_func=linear), run_time=self.dur(1.8))
            # «desde cero»
            self.en("cero")
            self.play(FadeIn(c0), run_time=self.dur(0.3))
            # «hasta el ancho de banda»
            self.en("hastab")
            self.play(FadeIn(cb), run_time=self.dur(0.4))
            # «a lo largo del símbolo»
            self.en("simbolo")
            self.play(FadeIn(ct), run_time=self.dur(0.6))
            # «del radar»
            self.en("radar")
            self.pop(rad)
            # «la frecuencia contra el tiempo»
            self.en("ft")
            self.play(FadeIn(P), run_time=self.dur(0.7))
            # «una rampa»
            self.en("rampa")
            self.play(Create(rampa), run_time=self.dur(0.9))
        self.wait(1.0)
        self.limpiar()
