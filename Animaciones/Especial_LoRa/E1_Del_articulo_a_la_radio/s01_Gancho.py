"""Escena 01 — Gancho: un símbolo enterrado en ruido y el pico que aparece al deshacer el chirp."""
from comun.escena import *
from comun.figuras_lora import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        L = Lienzo(ancho=11.0, alto=2.6, t_rango=(0, 1), v_max=0.6, centro=(-0.5, 2.4))
        tr = traza_ruidosa(L, 5)
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.8).move_to([6.1, 2.4, 0])
        rx10 = Text("Ruido × 10", color=RUIDO, weight=BOLD).scale(0.85).move_to([0, 0.55, 0])
        cajas, fl = fila_bloques(["× Chirp que baja", "FFT"], [CIAN, AZUL], centro=(0, -0.55), hueco=1.0,
                                 escala=0.62, alto=0.95)
        C = CasillasFFT(casillas_fft(recibido())[0], centro=(0, -3.4), ancho=11.0, alto=1.9, v_max=1.1, grosor=3.5)
        pico = C.pintar(S_EJEMPLO)
        r20 = Text("20", color=AMBAR, weight=BOLD).scale(0.8).next_to(C.cima(S_EJEMPLO), UP, buff=0.12)
        lora = self.palabra("LoRa", AMBAR, 2.0).move_to([0, 1.6, 0])
        doc = documento(TXT).scale(1.6).move_to([-2.6, -1.3, 0])
        fle = Arrow([-1.5, -1.3, 0], [1.1, -1.3, 0], color=INK, stroke_width=4, buff=0)
        pl = pluto().scale(1.1).move_to([2.9, -1.5, 0])
        with self.narrar("b1"):
            # «Aquí dentro hay un mensaje»
            self.en("senal")
            self.play(Create(tr), run_time=self.dur(1.2))
            # «No lo ves»
            self.en("nolo")
            self.pop(q)
            # «diez veces más potencia»
            self.en("diez")
            self.pop(rx10)
            # «Dos operaciones después»
            self.en("dos")
            self.play(FadeIn(cajas[0]), run_time=0.4)
            self.play(GrowArrow(fl[0]), FadeIn(cajas[1]), run_time=self.dur(0.5))
            # «un pico limpio»
            self.en("pico")
            self.play(FadeIn(C.base), FadeIn(C.rots), Create(C.barras, lag_ratio=0.02), run_time=self.dur(0.9))
            # «la posición que dice el dato»
            self.en("dato")
            self.pop(r20)
            self.resaltar(pico, color=AMBAR, escala=1.15, run_time=self.dur(0.5))
            # «Así funciona LoRa»
            self.en("lora")
            self.corte()
            self.pop(lora)
            # «del artículo»
            self.en("articulo")
            self.play(FadeIn(doc, shift=UP * 0.2), run_time=self.dur(0.5))
            # «a una radio de verdad»
            self.en("radio")
            self.play(GrowArrow(fle), FadeIn(pl, shift=UP * 0.2), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
