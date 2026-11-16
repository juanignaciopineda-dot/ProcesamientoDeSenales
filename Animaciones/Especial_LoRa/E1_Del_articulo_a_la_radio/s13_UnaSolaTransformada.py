"""Escena 13 — Ec. 16, segundo paso: una FFT hace las 128 comparaciones y el pico cae en la casilla 20."""
from comun.escena import *
from comun.figuras_lora import *


class UnaSolaTransformada(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.transformada()
        self.resumen()
        self.wait(1.0)
        self.limpiar()

    def transformada(self):
        paso = VGroup(RoundedRectangle(corner_radius=0.1, width=0.8, height=0.8, color=AMBAR, stroke_width=5),
                      Text("2", color=TXT, weight=BOLD).scale(0.7)).move_to([-6.3, 3.3, 0])
        L = Lienzo(ancho=9.0, alto=1.2, t_rango=(0, 1), v_max=1.0, centro=(1.2, 3.0))
        t = np.linspace(0, 1, 900)
        tono = L.curva(t, np.cos(2 * np.pi * 20 * t), AMBAR, 2.6)
        minis, rots = VGroup(), VGroup()
        for i, y in enumerate((1.4, 0.6, -0.2), 1):
            Lm = Lienzo(ancho=2.4, alto=0.5, t_rango=(0, 1), v_max=1.0, centro=(-5.2, y))
            minis.add(Lm.curva(t[::4], np.cos(2 * np.pi * i * t[::4]), INK, 2.5))
            rots.add(Text(str(i), color=INK, weight=BOLD).scale(0.5).move_to([-6.75, y, 0]))
        mas = MathTex(r"\vdots", color=INK).scale(1.1).move_to([-5.2, -0.95, 0])
        dft = Text("DFT", color=AMBAR, weight=BOLD).scale(0.9).move_to([-5.2, -2.0, 0])
        fft = bloque("FFT", AZUL, ancho=2.4, alto=1.0, escala=0.8).move_to([1.2, 1.1, 0])
        f1 = Arrow([1.2, 2.3, 0], [1.2, 1.65, 0], color=INK, stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.4)
        comp = Text("128 a la vez", color=VERDE, weight=BOLD).scale(0.65).move_to([4.3, 1.1, 0])
        f2 = Arrow([1.2, 0.55, 0], [1.2, -0.1, 0], color=INK, stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.4)
        v = np.zeros(M7)
        v[S_EJEMPLO] = 1.0
        C = CasillasFFT(v, centro=(1.2, -3.2), ancho=9.0, alto=2.2, v_max=1.05, grosor=3.5)
        pico = C.pintar(S_EJEMPLO, AMBAR, 6)
        nada = cota(C.pie(32) + UP * 0.4, C.pie(127) + UP * 0.4, "0", INK, UP, 0.6)
        sh = MathTex(r"\hat{s}", "=", "20", color=AMBAR).scale(1.3).move_to([C.x(S_EJEMPLO) + 1.45, -1.3, 0])
        with self.narrar("b1"):
            # «Segundo paso»
            self.en("paso2")
            self.pop(paso)
            self.play(Create(tono, rate_func=linear), run_time=self.dur(0.8))
            # «ciento veintiocho tonos»
            self.en("tonos")
            self.play(LaggedStart(*[Create(m) for m in minis], lag_ratio=0.3), FadeIn(mas), run_time=self.dur(1.2))
            # «uno, dos, tres»
            self.en("unodos")
            self.play(LaggedStart(*[FadeIn(r, scale=0.5) for r in rots], lag_ratio=0.5), run_time=self.dur(1.3))
            # «la transformada discreta de Fourier»
            self.en("dft")
            self.pop(dft)
            # «la transformada rápida»
            self.en("fft")
            self.play(GrowArrow(f1), FadeIn(fft, shift=UP * 0.2), run_time=self.dur(0.6))
            # «las ciento veintiocho comparaciones»
            self.en("comp")
            self.pop(comp)
            # «de una vez»
            self.en("vez")
            self.play(GrowArrow(f2), FadeIn(C.base), FadeIn(C.rots), run_time=self.dur(0.6))
            # «un pico en la casilla veinte»
            self.en("pico")
            self.sfx("impacto")
            self.play(Create(pico), run_time=self.dur(0.5))
            # «nada en las demás»
            self.en("nada")
            self.play(FadeIn(nada), run_time=self.dur(0.5))
            # «buscar el máximo»
            self.en("max")
            self.pop(sh)

    def resumen(self):
        cajas, fl = fila_bloques(["× Chirp que baja", "FFT", "Máximo"], [CIAN, AZUL, AMBAR], centro=(0, 1.5),
                                 hueco=0.9, alto=1.1, escala=0.7)
        antes = MathTex("16.384", color=INK).scale(1.8).move_to([-3.3, -1.5, 0])
        tac = tachar(antes)
        ahora = Text("1 FFT por símbolo", color=VERDE, weight=BOLD).scale(0.95).move_to([2.6, -1.5, 0])
        with self.narrar("b2"):
            # «Multiplicar por el chirp que baja»
            self.en("m1")
            self.corte()
            self.play(FadeIn(cajas[0], shift=RIGHT * 0.2), run_time=self.dur(0.5))
            # «transformar»
            self.en("m2")
            self.play(GrowArrow(fl[0]), FadeIn(cajas[1]), run_time=self.dur(0.5))
            # «elegir el máximo»
            self.en("m3")
            self.play(GrowArrow(fl[1]), FadeIn(cajas[2]), run_time=self.dur(0.5))
            # «dieciséis mil multiplicaciones»
            self.en("antes")
            self.play(FadeIn(antes), run_time=0.4)
            self.play(Create(tac), run_time=self.dur(0.4))
            # «una transformada rápida por símbolo»
            self.en("ahora")
            self.pop(ahora, sonido="exito")
