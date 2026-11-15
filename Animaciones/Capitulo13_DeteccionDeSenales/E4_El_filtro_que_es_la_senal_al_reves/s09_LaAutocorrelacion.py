"""Escena 09 — La salida es la autocorrelación: el máximo está sin desplazar."""
from comun.escena import *


class LaAutocorrelacion(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        pal = self.palabra("autocorrelación", AMBAR, 0.9).move_to([0, 3.3, 0])
        c10 = caja("capítulo 10", INK, ancho=2.3, alto=0.6, scale=0.4).move_to([-5.3, 2.4, 0])
        r10 = MathTex(r"R_{XX}(\tau)", color=INK).scale(0.7).next_to(c10, DOWN, buff=0.15)
        esp = MathTex(r"E[\,\cdot\,]", color=INK).scale(1.0).move_to([5.2, 2.4, 0])
        s = Tallos(S13, centro=(0, 1.5), paso=0.9, unidad=0.3, color=SENAL)
        v_s = valores_sobre13(s)
        ok = tilde(VERDE, 0.9).move_to([3.4, 1.5, 0])
        l_con = etiqueta("conocida", VERDE, 0.5).move_to([3.4, 0.9, 0])
        cop = Tallos(S13, centro=(0, -0.3), paso=0.9, unidad=0.3, color=SENAL)
        v_c = valores_sobre13(cop)
        hilos = VGroup(*[Line([s.x(i), 1.25, 0], [s.x(i), 0.95, 0], color=AMBAR, stroke_width=3) for i in range(3)])
        prods = VGroup(*[MathTex(t, color=AMBAR).scale(0.8).move_to([s.x(i), -1.6, 0])
                         for i, t in enumerate(["4", "4", "1"])])
        eq = MathTex("2^2", "+", "2^2", "+", "1^2", "=", "9", "=", "E").scale(1.2).move_to([0, -2.7, 0])
        eq[6].set_color(AMBAR)
        eq[8].set_color(AMBAR)
        eq2 = MathTex(r"2\cdot2+1\cdot2=6").scale(1.2).move_to([0, -2.7, 0])
        x_no = cruz(ROJO, 0.9).move_to([4.2, -0.3, 0])
        with self.narrar("b1"):
            # «una autocorrelación»
            self.en("auto")
            self.pop(pal)

            # «el capítulo diez»
            self.en("cap10")
            self.play(FadeIn(c10), FadeIn(r10), run_time=self.dur(0.5))

            # «sin promedios»
            self.en("sinprom")
            self.play(FadeIn(esp), run_time=0.3)
            self.play(Create(tachar(esp)), run_time=0.3)

            # «la señal es una sola»
            self.en("una")
            self.play(FadeIn(s), FadeIn(v_s), run_time=self.dur(0.6))

            # «la conocemos»
            self.en("conocemos")
            self.play(Create(ok), FadeIn(l_con), run_time=self.dur(0.5))

            # «sin desplazar»
            self.en("sindesp")
            self.play(FadeIn(cop), FadeIn(v_c), run_time=self.dur(0.5))
            self.play(Create(hilos), run_time=self.dur(0.4))

            # «se multiplica por sí misma»
            self.en("misma")
            self.play(LaggedStart(*[FadeIn(p, scale=1.4) for p in prods], lag_ratio=0.3), run_time=self.dur(0.9))

            # «la suma de cuadrados es la energía»
            self.en("cuadrados")
            self.play(Write(eq), run_time=self.dur(1.8))
            self.resaltar(eq[6], color=AMBAR, escala=1.5)

            # «cualquier desplazamiento»
            self.en("desp")
            self.play(FadeOut(prods), FadeOut(hilos), FadeOut(eq), cop.animate.shift(RIGHT * 0.9),
                      FadeOut(v_c), run_time=self.dur(0.7))

            # «dejan de coincidir»
            self.en("coinciden")
            self.play(Create(x_no), run_time=0.3)

            # «la suma baja»
            self.en("baja")
            self.play(Write(eq2), run_time=self.dur(1.0))
        self.wait(1.0)
        self.limpiar()
