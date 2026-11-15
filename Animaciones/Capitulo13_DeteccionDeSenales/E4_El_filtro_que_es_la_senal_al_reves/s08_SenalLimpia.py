"""Escena 08 — Primera lectura, en el tiempo: la señal limpia por el filtro da (2, 6, 9, 6, 2)."""
from comun.escena import *


class SenalLimpia(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        tit = self.palabra("Primera lectura: el tiempo", AMBAR, 0.7).move_to([0, 3.4, 0])
        L = Lienzo(ancho=2.4, alto=0.8, t_rango=(0, 1), v_max=1, centro=(-4.2, -1.9))
        ruido = ruido_t(L, semilla=5, amp=0.6)
        l_ru = etiqueta("ruido", RUIDO, 0.5).move_to([-4.2, -2.6, 0])
        x_ru = cruz(ROJO, 1.0).move_to([-4.2, -1.9, 0])
        s = Tallos(S13, centro=(-4.2, 2.1), paso=0.6, unidad=0.28, color=SENAL)
        h = Tallos(H13, centro=(-4.2, 0.3), paso=0.6, unidad=0.28, color=ESTIMACION)
        v_s, v_h = valores_sobre13(s), valores_sobre13(h)
        l_s = MathTex("s", color=SENAL).scale(0.8).move_to([-6.4, 2.1, 0])
        l_h = MathTex("h", color=ESTIMACION).scale(0.8).move_to([-6.4, 0.3, 0])
        cas = CasillasSalida13(5, centro=(2.4, -2.5), lado=0.9)
        marco = SurroundingRectangle(cas.cas[0], color=AMBAR, buff=0.05).set_opacity(0)
        cuentas = [MathTex(r"2\cdot1=2").scale(1.2), MathTex(r"2\cdot2+2\cdot1=6").scale(1.2),
                   MathTex(r"2\cdot2+2\cdot2+1\cdot1", r"=9").scale(1.2),
                   MathTex(r"2\cdot2+1\cdot2=6").scale(1.2), MathTex(r"1\cdot2=2").scale(1.2)]
        for c in cuentas:
            c.move_to([2.4, 0.9, 0])
        cuentas[2][1].set_color(AMBAR)
        pos = [cas.poner(i, str(v), TXT) for i, v in enumerate(AUT13)]
        pos[2].set_color(AMBAR)
        aut = Tallos(AUT13, centro=(2.4, -1.0), paso=0.98, unidad=0.25, color=AMBAR)
        s_copia = Tallos(S13, centro=(-3.6, 0.9), paso=0.6, unidad=0.28, color=SENAL)
        l_cop = etiqueta("copia desplazada", INK, 0.45).move_to([-4.2, -0.1, 0])
        l_mul = etiqueta("× y Σ", AMBAR, 0.6).move_to([-4.2, -1.3, 0])
        e9 = MathTex(r"E=9", color=AMBAR).scale(1.0).move_to([5.6, 1.0, 0])
        n9 = Text("9", color=AMBAR, weight=BOLD).scale(0.8).move_to(aut.pos(2) + UP * 0.35)

        with self.narrar("b1"):
            # «Primera lectura, en el tiempo»
            self.en("lectura")
            self.pop(tit)

            # «Imagina que»
            self.en("imagina")
            self.play(FadeIn(ruido), FadeIn(l_ru), run_time=self.dur(0.5))

            # «no hay ruido»
            self.en("sinruido")
            self.play(Create(x_ru), run_time=0.3)
            self.play(FadeOut(ruido), FadeOut(l_ru), FadeOut(x_ru), run_time=self.dur(0.4))

            # «dos, dos, uno, pasando»
            self.en("pasa")
            self.play(FadeIn(s), FadeIn(v_s), FadeIn(l_s), run_time=self.dur(0.5))

            # «el filtro uno, dos, dos»
            self.en("filtro")
            self.play(FadeIn(h), FadeIn(v_h), FadeIn(l_h), run_time=self.dur(0.5))

            # «Calculamos la salida»
            self.en("calculamos")
            self.play(FadeIn(cas), run_time=self.dur(0.5))

            # «igual que antes»
            self.en("antes")
            self.resaltar(h, color=AMBAR, escala=1.1)

            # «Instante cero»
            self.en("i0")
            marco.move_to(cas.c(0))
            self.play(marco.animate.set_opacity(1), run_time=0.3)

            # «dos por uno, dos»
            self.en("c0")
            self.play(Write(cuentas[0]), run_time=self.dur(0.7))
            self.play(FadeIn(pos[0], scale=1.4), run_time=0.3)

            # «Instante uno»
            self.en("i1")
            self.play(marco.animate.move_to(cas.c(1)), FadeOut(cuentas[0]), run_time=self.dur(0.4))

            # «dos por dos, más dos por uno, seis»
            self.en("c1")
            self.play(Write(cuentas[1]), run_time=self.dur(1.0))
            self.play(FadeIn(pos[1], scale=1.4), run_time=0.3)

            # «Instante dos»
            self.en("i2")
            self.play(marco.animate.move_to(cas.c(2)), FadeOut(cuentas[1]), run_time=self.dur(0.4))

            # «más uno por uno, nueve»
            self.en("c2")
            self.play(Write(cuentas[2][0]), run_time=self.dur(1.2))
            self.play(Write(cuentas[2][1]), FadeIn(pos[2], scale=1.6), run_time=self.dur(0.4))
            self.sfx("exito", gain=-18)

        with self.narrar("b2"):
            # «Y los dos últimos»
            self.en("ultimos")
            self.play(FadeOut(cuentas[2]), marco.animate.move_to(cas.c(3)), run_time=self.dur(0.4))

            # «más uno por dos, seis»
            self.en("c3")
            self.play(Write(cuentas[3]), run_time=self.dur(0.9))
            self.play(FadeIn(pos[3], scale=1.4), run_time=0.3)

            # «uno por dos, dos»
            self.en("c4")
            self.play(FadeOut(cuentas[3]), marco.animate.move_to(cas.c(4)), run_time=self.dur(0.3))
            self.play(Write(cuentas[4]), run_time=self.dur(0.6))
            self.play(FadeIn(pos[4], scale=1.4), run_time=0.3)

            # «dos, seis, nueve, seis, dos»
            self.en("salida")
            self.play(FadeOut(cuentas[4]), FadeOut(marco), FadeIn(aut, shift=UP * 0.3), run_time=self.dur(0.7))

            # «un pico en el medio»
            self.en("pico")
            self.resaltar(aut.puntos[2], color=AMBAR, escala=2.2)

            # «vale nueve»
            self.en("nueve")
            self.pop(n9)

            # «la energía»
            self.en("energia")
            self.pop(e9)

            # «una copia suya desplazada»
            self.en("copia")
            self.play(FadeOut(h), FadeOut(v_h), FadeOut(l_h), FadeIn(s_copia), FadeIn(l_cop), run_time=self.dur(0.7))

            # «se multiplican y se suman»
            self.en("suman")
            self.pop(l_mul)
        self.wait(1.0)
        self.limpiar()
