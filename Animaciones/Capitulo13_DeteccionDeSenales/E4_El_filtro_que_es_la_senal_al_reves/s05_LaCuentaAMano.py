"""Escena 05 — La cuenta a mano: r = (3, 1, 2) por h = (1, 2, 2) da (3, 7, 10, 6, 4)."""
from comun.escena import *


class LaCuentaAMano(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        s = Tallos(S13, centro=(-4.2, 2.6), paso=0.6, unidad=0.28, color=SENAL)
        h = Tallos(H13, centro=(-4.2, 0.6), paso=0.6, unidad=0.28, color=ESTIMACION)
        r = Tallos(R13, centro=(-4.2, -1.4), paso=0.6, unidad=0.28, color=MEDIDA)
        v_s, v_h, v_r = valores_sobre13(s), valores_sobre13(h), valores_sobre13(r)
        l_s = MathTex("s", color=SENAL).scale(0.8).move_to([-6.4, 2.6, 0])
        l_h = MathTex("h", color=ESTIMACION).scale(0.8).move_to([-6.4, 0.6, 0])
        l_r = MathTex("r", color=MEDIDA).scale(0.8).move_to([-6.4, -1.4, 0])
        cas = CasillasSalida13(5, centro=(2.4, -2.5), lado=0.9)
        marco = SurroundingRectangle(cas.cas[0], color=AMBAR, buff=0.05).set_opacity(0)
        cuentas = [MathTex(r"3\cdot1=3").scale(1.2).move_to([2.4, 0.9, 0]),
                   MathTex(r"3\cdot2+1\cdot1=7").scale(1.2).move_to([2.4, 0.9, 0]),
                   MathTex(r"3\cdot2+1\cdot2+2\cdot1", r"=10").scale(1.2).move_to([2.4, 0.9, 0])]
        cuentas[2][1].set_color(AMBAR)
        pos = [cas.poner(i, str(v), TXT) for i, v in enumerate(SAL13)]
        pos[2].set_color(AMBAR)
        with self.narrar("b1"):
            # «La señal es dos, dos, uno»
            self.en("senal")
            self.play(FadeIn(s), FadeIn(v_s), FadeIn(l_s), run_time=self.dur(0.6))

            # «su inversa, uno, dos, dos»
            self.en("inversa")
            self.sfx("whoosh")
            self.play(FadeIn(h), FadeIn(v_h), FadeIn(l_h), run_time=self.dur(0.6))

            # «Lo recibido es tres, uno, dos»
            self.en("recibido")
            self.play(FadeIn(r), FadeIn(v_r), FadeIn(l_r), run_time=self.dur(0.6))

            # «Salida en el instante cero»
            self.en("i0")
            self.play(FadeIn(cas), run_time=self.dur(0.5))
            marco.move_to(cas.c(0))
            self.play(marco.animate.set_opacity(1), run_time=0.3)

            # «tres por uno, tres»
            self.en("c0")
            self.play(Write(cuentas[0]), run_time=self.dur(0.8))
            self.play(FadeIn(pos[0], scale=1.4), run_time=0.3)

            # «En el uno»
            self.en("i1")
            self.play(marco.animate.move_to(cas.c(1)), FadeOut(cuentas[0]), run_time=self.dur(0.4))

            # «tres por dos, más uno por uno, siete»
            self.en("c1")
            self.play(Write(cuentas[1]), run_time=self.dur(1.0))
            self.play(FadeIn(pos[1], scale=1.4), run_time=0.3)

            # «En el dos»
            self.en("i2")
            self.play(marco.animate.move_to(cas.c(2)), FadeOut(cuentas[1]), run_time=self.dur(0.4))

            # «tres por dos, más uno por dos, más dos por uno»
            self.en("c2")
            self.play(Write(cuentas[2][0]), run_time=self.dur(1.4))

            # «diez»
            self.en("diez")
            self.play(Write(cuentas[2][1]), FadeIn(pos[2], scale=1.6), run_time=self.dur(0.5))
            self.sfx("exito", gain=-18)

            # «Luego seis y cuatro»
            self.en("resto")
            self.play(FadeOut(cuentas[2]), FadeOut(marco), FadeIn(pos[3], scale=1.4), run_time=self.dur(0.4))
            self.play(FadeIn(pos[4], scale=1.4), run_time=self.dur(0.4))
        self.wait(1.0)
        self.limpiar()
