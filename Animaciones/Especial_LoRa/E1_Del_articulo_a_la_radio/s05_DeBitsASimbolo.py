"""Escena 05 — Ec. 1: el codificador lee siete bits como un número (el símbolo 20)."""
from comun.escena import *
from comun.figuras_lora import *


class DeBitsASimbolo(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        cod = bloque("Codificador", AZUL, ancho=3.4, alto=0.95, escala=0.65).move_to([0, 3.2, 0])
        bits = fila_bits(BITS_EJEMPLO, centro=(0, 1.6), lado=1.0)
        pesos = [1, 2, 4, 8, 16, 32, 64]
        rayas = VGroup(*[Line([bits.x(i) - 0.3, 0.45, 0], [bits.x(i) + 0.3, 0.45, 0], color=INK, stroke_width=2)
                         for i in range(7)])
        nums = VGroup(*[Text(str(p), color=INK, weight=BOLD).scale(0.6).move_to([bits.x(i), 0.78, 0])
                        for i, p in enumerate(pesos)])
        cuenta = MathTex("4", "+", "16", "=", "20", color=TXT).scale(1.6).move_to([0, -0.9, 0])
        cuenta[4].set_color(AMBAR)
        total = Text("128 símbolos", color=TXT, weight=BOLD).scale(0.75).move_to([-2.8, -2.7, 0])
        rango = MathTex(r"0\ \dots\ 127", color=AMBAR).scale(1.3).move_to([2.6, -2.7, 0])
        ec = Text("Ec. 1", color=INK, weight=BOLD).scale(0.6).move_to([-4.6, -2.7, 0])
        f = MathTex("s", "=", r"\sum_{h=0}^{SF-1}", "w_h", r"\cdot\, 2^{h}", color=TXT).scale(1.25).move_to([0.6, -2.7, 0])
        f[0].set_color(AMBAR)
        f[3].set_color(SENAL)
        with self.narrar("b1"):
            # «el codificador»
            self.en("cod")
            self.play(FadeIn(cod, shift=DOWN * 0.2), run_time=self.dur(0.5))
            # «siete bits»
            self.en("bits")
            self.play(LaggedStart(*[Create(c) for c in bits.cas], lag_ratio=0.12), run_time=self.dur(0.9))
            # «un número en binario»
            self.en("bin")
            self.play(LaggedStart(*[FadeIn(n, scale=0.4) for n in bits.nums], lag_ratio=0.12), run_time=self.dur(0.9))
            # «Cada bit tiene un peso»
            self.en("pesos")
            self.play(Create(rayas), run_time=self.dur(0.6))
            # «uno, dos, cuatro, ocho»
            self.en("p1")
            self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.15) for n in nums[:4]], lag_ratio=0.45),
                      run_time=self.dur(1.8))
            # «sesenta y cuatro»
            self.en("p64")
            self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.15) for n in nums[4:]], lag_ratio=0.3),
                      run_time=self.dur(0.9))
            # «el del cuatro y el del dieciséis»
            self.en("enc")
            self.sfx("tick")
            self.play(bits.cas[2].animate.set_stroke(AMBAR, 5).set_fill(AMBAR, 0.25), nums[2].animate.set_color(AMBAR),
                      run_time=0.4)
            self.sfx("tick")
            self.play(bits.cas[4].animate.set_stroke(AMBAR, 5).set_fill(AMBAR, 0.25), nums[4].animate.set_color(AMBAR),
                      run_time=self.dur(0.4))
            # «el símbolo es veinte»
            self.en("veinte")
            self.play(Write(cuenta[:4]), run_time=0.6)
            self.pop(cuenta[4])
            # «ciento veintiocho símbolos posibles»
            self.en("total")
            self.play(FadeIn(total, shift=UP * 0.2), run_time=self.dur(0.5))
            # «del cero al ciento veintisiete»
            self.en("rango")
            self.play(Write(rango), run_time=self.dur(0.8))
        with self.narrar("b2"):
            # «la ecuación uno»
            self.en("ec1")
            self.play(FadeOut(total), FadeOut(rango), FadeIn(ec), run_time=self.dur(0.4))
            # «el símbolo»
            self.en("s")
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=self.dur(0.4))
            # «la suma»
            self.en("suma")
            self.play(FadeIn(f[2]), run_time=self.dur(0.4))
            # «cada bit»
            self.en("bit")
            self.play(FadeIn(f[3]), run_time=self.dur(0.4))
            # «su potencia de dos»
            self.en("pot")
            self.play(FadeIn(f[4]), run_time=self.dur(0.4))
        self.wait(1.0)
        self.limpiar()
