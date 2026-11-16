"""Escena 10 — Ec. 10: lo recibido es lo transmitido más ruido blanco gaussiano; qué son −10 dB."""
from comun.escena import *
from comun.figuras_lora import *


class ElCanalConRuido(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        a1 = antena_simple(TXT, 1.3).move_to([-6.5, 2.6, 0])
        a2 = antena_simple(TXT, 1.3).move_to([6.5, 2.6, 0])
        L = Lienzo(ancho=11.2, alto=2.0, t_rango=(0, 1), v_max=6.0, centro=(0, 2.6))
        t = np.linspace(0, 1, 420)
        x = np.cos(2 * np.pi * (1.0 * t + 8.0 * t ** 2))
        g = np.random.default_rng(11)
        w = g.normal(0, np.sqrt(5.0), t.size)          # diez veces la potencia de x (0,5)
        limpio = L.curva(t, 4.5 * x, SENAL, 3.0)       # el chirp solo, ampliado para verlo
        ruido = L.curva(t, 0.6 * w, RUIDO, 2.0, 0.75)
        recib = L.curva(t, x + w, MEDIDA, 2.2)
        f = MathTex("r", "=", "c", "+", "w", color=TXT).scale(2.0).move_to([-3.9, 0.2, 0])
        f[0].set_color(MEDIDA)
        f[2].set_color(SENAL)
        f[4].set_color(RUIDO)
        blanco = Text("Blanco", color=RUIDO, weight=BOLD).scale(0.9).move_to([4.2, 0.75, 0])
        eje = Line([2.3, -0.75, 0], [6.2, -0.75, 0], color=INK, stroke_width=2.5)
        plano = Rectangle(width=3.4, height=0.7, color=RUIDO, stroke_width=3).set_fill(RUIDO, 0.3).move_to([4.2, -0.38, 0])
        rfrec = Text("Frecuencia", color=INK).scale(0.42).move_to([4.2, -1.05, 0])
        snr = MathTex(r"\mathrm{SNR}", "=", r"-10\ \mathrm{dB}", color=TXT).scale(1.5).move_to([-3.9, -2.3, 0])
        snr[2].set_color(AMBAR)
        y0 = -3.45
        bs = Rectangle(width=0.8, height=0.2, color=SENAL, stroke_width=3).set_fill(SENAL, 0.5).move_to([0.4, y0 + 0.1, 0])
        br = Rectangle(width=0.8, height=2.0, color=RUIDO, stroke_width=3).set_fill(RUIDO, 0.5).move_to([1.6, y0 + 1.0, 0])
        ns = Text("1", color=SENAL, weight=BOLD).scale(0.6).next_to(bs, UP, buff=0.12)
        nr = Text("10", color=RUIDO, weight=BOLD).scale(0.6).next_to(br, UP, buff=0.12)
        ls = Text("Señal", color=INK).scale(0.42).next_to(bs, DOWN, buff=0.1)
        lr = Text("Ruido", color=INK).scale(0.42).next_to(br, DOWN, buff=0.1)
        with self.narrar("b1"):
            # «Por el aire»
            self.en("aire")
            self.play(FadeIn(a1), FadeIn(a2), Create(limpio, rate_func=linear), run_time=self.dur(1.1))
            # «se le suma ruido»
            self.en("suma")
            self.play(Create(ruido, rate_func=linear), run_time=self.dur(1.2))
            # «lo recibido»
            self.en("r")
            self.pop(f[0], sonido=None)
            self.play(FadeIn(f[1]), run_time=0.2)
            # «lo transmitido»
            self.en("c")
            self.pop(f[2], sonido=None)
            # «más ruido blanco gaussiano»
            self.en("w")
            self.play(FadeIn(f[3]), run_time=0.2)
            self.pop(f[4], sonido=None)
            # «Blanco»
            self.en("blanco")
            self.pop(blanco)
            # «por igual en todas las frecuencias»
            self.en("plano")
            self.play(Create(eje), FadeIn(rfrec), run_time=0.4)
            self.play(GrowFromEdge(plano, DOWN), run_time=self.dur(0.7))
            # «una relación señal a ruido»
            self.en("snr")
            self.play(Write(snr[:2]), run_time=self.dur(0.7))
            # «menos diez decibelios»
            self.en("db")
            self.pop(snr[2])
            # «diez veces la potencia»
            self.en("diez")
            self.play(GrowFromEdge(bs, DOWN), FadeIn(ns), FadeIn(ls), run_time=0.4)
            self.play(GrowFromEdge(br, DOWN), FadeIn(nr), FadeIn(lr), run_time=self.dur(0.8))
            # «ya no se reconoce»
            self.en("noreco")
            self.play(FadeOut(ruido), Transform(limpio, recib), run_time=self.dur(1.0))
        self.wait(1.0)
        self.limpiar()
