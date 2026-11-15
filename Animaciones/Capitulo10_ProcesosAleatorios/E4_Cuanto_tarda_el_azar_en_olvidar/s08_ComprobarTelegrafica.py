"""Escena 08 — ComprobarTelegrafica: e^(−1) = 0,368 y la onda es estacionaria en sentido amplio."""
from comun.escena import *


class ComprobarTelegrafica(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        f = formula(r"R_{XX}(", r"\tau", ")=", r"e^{-2\lambda|\tau|}", colores={3: AMBAR}, escala=1.8).move_to([0, 2.7, 0])
        f_val = MathTex(r"\lambda = 1,\quad \tau = 0{,}5", color=AMBAR).scale(1.2).move_to([0, 1.0, 0])
        f_em1 = MathTex(r"=\,e^{-1}", color=TXT).scale(1.3).move_to([-3.6, -0.3, 0])
        f_div = MathTex(r"=\,\frac{1}{2{,}718}", color=TXT).scale(1.3).next_to(f_em1, RIGHT, buff=0.4)
        f_res = MathTex(r"\approx\,0{,}368", color=AMBAR).scale(1.4).next_to(f_div, RIGHT, buff=0.4)
        ok = tilde(VERDE, 0.6)
        igual = VGroup(ok, etiqueta("igual que la cuenta a mano: 0,684 − 0,316", VERDE, 0.6)).arrange(RIGHT, buff=0.3)
        igual.move_to([0, -1.6, 0])
        mu = MathTex(r"\mu_X(t)=0", color=AMBAR).scale(1.2).move_to([-3.8, -2.9, 0])
        wss = sello("WSS", VERDE).scale(1.3).move_to([1.2, -2.9, 0])
        libro = documento(INK).scale(1.3).move_to([5.8, -2.9, 0])
        apunte = nota("serie completa: apunte en profundidad, Parte 2.1", 0.42).next_to(libro, UP, buff=0.15)
        apunte.move_to([0, -3.75, 0])

        with self.narrar("b1"):
            # «Comprobémoslo»
            self.en("comprobar")
            self.play(Write(f), run_time=self.dur(1.2))

            # «lambda igual a uno»
            self.en("lam1")
            self.pop(f_val)

            # «e elevado a menos uno»
            self.en("em1")
            self.play(Write(f_em1), run_time=self.dur(0.8))

            # «uno entre dos coma siete uno ocho»
            self.en("div")
            self.play(Write(f_div), run_time=self.dur(1.2))

            # «cero coma tres seis ocho»
            self.en("v368")
            self.pop(f_res)

            # «Lo mismo que la cuenta a mano»
            self.en("igual")
            self.play(FadeIn(igual, shift=UP * 0.2), run_time=self.dur(0.8))

            # «solo depende de la separación»
            self.en("separacion")
            self.play(Indicate(f[1], color=AMBAR, scale_factor=1.6), run_time=self.dur(1.0))

            # «con la media constante»
            self.en("mediacte")
            self.pop(mu)

            # «estacionaria en sentido amplio»
            self.en("wss")
            self.pop(wss, sonido="impacto")

            # «La serie completa»
            self.en("serie_c")
            self.play(FadeIn(libro, shift=UP * 0.2), run_time=self.dur(0.6))

            # «apunte en profundidad»
            self.en("apunte")
            self.play(FadeIn(apunte), run_time=0.5)
        self.wait(1.0)
        self.limpiar()
