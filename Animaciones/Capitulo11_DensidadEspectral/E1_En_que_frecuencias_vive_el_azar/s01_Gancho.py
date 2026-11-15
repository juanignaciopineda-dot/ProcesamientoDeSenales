"""Escena 01 — Gancho: Fourier no sirve con un ruido, pero el ruido sí tiene una curva de potencia."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        L = Lienzo(ancho=4.6, alto=1.7, t_rango=(0, 4), v_max=1.0, centro=(-4.4, 2.2))
        ruido = ruido_t(L, semilla=7, amp=0.4)
        cf = caja("Fourier", AZUL, ancho=2.1, alto=0.9).move_to([0.2, 2.2, 0])
        a1 = flecha([-1.9, 2.2, 0], [-0.9, 2.2, 0])
        a2 = flecha([1.3, 2.2, 0], [2.3, 2.2, 0])
        caos = espectro_ruidoso(centro=(4.6, 2.2), ancho=3.6, alto=1.6, semilla=9, color=AZUL)
        c = Curva(psd_tele, x_rango=(-6, 6), y_max=1.2, ancho=7.0, alto=2.4, color=AMBAR, x_label=r"\omega") \
            .move_to([-0.6, -1.7, 0])
        with self.narrar("b1"):
            # «Grabas un ruido»
            self.en("ruido")
            self.play(Create(L.base()), Create(ruido), run_time=self.dur(1.2), rate_func=linear)

            # «le aplicas Fourier»
            self.en("fourier")
            self.play(GrowArrow(a1), FadeIn(cf), run_time=self.dur(0.6))

            # «No funciona»
            self.en("nofunciona")
            self.play(GrowArrow(a2), Create(caos), run_time=self.dur(0.7), rate_func=linear)
            x = cruz(ROJO, 1.3).move_to([4.6, 2.2, 0])
            self.play(Create(x), run_time=0.3)
            self.sfx("error")

            # «una curva»
            self.en("curva")
            self.play(Create(c.ejes), FadeIn(c.etiquetas), run_time=self.dur(0.5))
            self.play(Create(c.grafica), run_time=self.dur(1.0))

            # «en qué frecuencias vive su potencia»
            self.en("potencia")
            self.play(FadeIn(c.area(-6, 6, AMBAR, 0.3)), run_time=self.dur(0.6))
            pot = self.palabra("potencia", AMBAR, 0.8).move_to([4.3, -1.3, 0])
            self.pop(pot)

            # «Hoy vemos»
            self.en("hoy")
            fl = Arrow([-4.4, 1.2, 0], [-2.4, -0.7, 0], color=AMBAR, stroke_width=4, buff=0)
            q = self.palabra("¿cómo?", AMBAR, 0.7).move_to([-5.9, 0.4, 0])
            self.play(Create(fl), run_time=0.5)
            self.pop(q)

        self.wait(1.0)
        self.limpiar()
