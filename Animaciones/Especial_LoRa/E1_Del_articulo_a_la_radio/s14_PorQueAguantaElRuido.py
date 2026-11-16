"""Escena 14 — La señal se concentra en una casilla y el ruido blanco se reparte: 21 dB de ganancia."""
from comun.escena import *
from comun.figuras_lora import *


class PorQueAguantaElRuido(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        L = Lienzo(ancho=11.0, alto=1.7, t_rango=(0, 1), v_max=0.6, centro=(0, 2.8))
        tr = traza_ruidosa(L, 5)
        v = casillas_fft(recibido())[0]
        C = self.C = CasillasFFT(v, centro=(0, -3.2), ancho=11.0, alto=2.5, v_max=1.1, color=RUIDO, grosor=3.2)
        pico = self.pico = C.pintar(S_EJEMPLO, AMBAR, 6)
        resto = VGroup(*[b for q, b in enumerate(C.barras) if q != S_EJEMPLO])
        bl = Text("Ruido blanco", color=RUIDO, weight=BOLD).scale(0.7).move_to([-4.0, 1.2, 0])
        mu = Text("× Chirp", color=CIAN, weight=BOLD).scale(0.7).move_to([0.2, 1.2, 0])
        nc = Text("Sigue blanco", color=RUIDO, weight=BOLD).scale(0.7).move_to([4.0, 1.2, 0])
        n128 = cota([C.x(0), 0.1, 0], [C.x(127), 0.1, 0], "128 casillas", INK, UP, 0.5)
        ruido_medio = float(np.delete(v, S_EJEMPLO).mean())
        media = DashedLine([C.x(0), C.y(ruido_medio), 0], [C.x(127), C.y(ruido_medio), 0], color=TXT, stroke_width=3,
                           dash_length=0.12)
        with self.narrar("b1"):
            # «el principio del vídeo»
            self.en("principio")
            self.play(Create(tr, rate_func=linear), run_time=self.dur(1.2))
            # «toda la energía del símbolo»
            self.en("energia")
            self.play(FadeIn(C.base), FadeIn(C.rots), run_time=self.dur(0.5))
            # «en una sola casilla»
            self.en("casilla")
            self.sfx("impacto")
            self.play(Create(pico), run_time=self.dur(0.5))
            # «El ruido, en cambio, es blanco»
            self.en("blanco")
            self.pop(bl)
            # «multiplicarlo por el chirp»
            self.en("multi")
            self.pop(mu)
            # «no lo cambia»
            self.en("nocambia")
            self.pop(nc)
            # «lo reparte por igual»
            self.en("reparte")
            self.play(Create(resto, lag_ratio=0.02), run_time=self.dur(1.3))
            # «ciento veintiocho casillas»
            self.en("n128")
            self.play(FadeIn(n128), run_time=self.dur(0.5))
            # «La señal se concentra»
            self.en("concentra")
            self.resaltar(pico, color=AMBAR, escala=1.12, run_time=self.dur(0.6))
            # «el ruido se diluye»
            self.en("diluye")
            self.play(Create(media), run_time=self.dur(0.8))
        g = MathTex(r"\text{Ganancia}", "=", "2^{SF}", "=", "128", "=", r"21\ \mathrm{dB}", color=TXT).scale(1.25)
        g.move_to([0, 3.1, 0])
        g[6].set_color(VERDE)
        s = MathTex(r"-10\ \mathrm{dB}", r"+\ 21\ \mathrm{dB}", "=", r"+11\ \mathrm{dB}", color=TXT).scale(1.25)
        s.move_to([0, 1.9, 0])
        s[0].set_color(ROJO)
        s[3].set_color(VERDE)
        du = MathTex(r"SF\ 7 \to 8:\quad 128 \to 256", color=TXT).scale(1.0).move_to([-3.4, 0.6, 0])
        d3 = MathTex(r"+3\ \mathrm{dB}", color=VERDE).scale(1.2).move_to([1.8, 0.6, 0])
        t2 = MathTex(r"T_s \times 2", color=ROJO).scale(1.2).move_to([4.8, 0.6, 0])
        with self.narrar("b2"):
            # «el número de casillas»
            self.en("num")
            self.play(*[FadeOut(m) for m in (tr, bl, mu, nc, n128)], run_time=0.3)
            self.play(Write(g[:3]), run_time=self.dur(0.8))
            # «ciento veintiocho veces»
            self.en("veces")
            self.play(FadeIn(g[3]), FadeIn(g[4]), run_time=self.dur(0.4))
            # «veintiún decibelios»
            self.en("db21")
            self.play(FadeIn(g[5]), run_time=0.2)
            self.pop(g[6], sonido=None)
            # «menos diez decibelios por muestra»
            self.en("m10")
            self.play(Write(s[0]), run_time=self.dur(0.6))
            # «once decibelios por encima»
            self.en("db11")
            self.play(FadeIn(s[1]), FadeIn(s[2]), run_time=0.4)
            self.pop(s[3])
            # «Por eso se ve»
            self.en("seve")
            self.resaltar(pico, color=AMBAR, escala=1.12, run_time=self.dur(0.6))
            # «duplica las casillas»
            self.en("duplica")
            self.play(Write(du), run_time=self.dur(0.9))
            # «tres decibelios más»
            self.en("db3")
            self.pop(d3)
            # «tardar el doble»
            self.en("doble")
            self.pop(t2)
        self.wait(1.0)
        self.limpiar()
