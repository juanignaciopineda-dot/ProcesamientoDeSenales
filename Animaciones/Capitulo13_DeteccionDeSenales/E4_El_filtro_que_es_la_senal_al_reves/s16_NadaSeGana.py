"""Escena 16 — Ningún filtro supera al adaptado: la igualdad y las dos justificaciones."""
from comun.escena import *


class NadaSeGana(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        f_le = MathTex(r"\mathrm{SNR}", r"\leq", r"E/\sigma^2", color=TXT).scale(1.3).move_to([-3.5, 2.8, 0])
        f_le[2].set_color(AMBAR)
        f_eq = MathTex(r"=", color=AMBAR).scale(1.5).move_to(f_le[1])
        par = parabola_l(centro=(-3.0, -0.7), ancho=4.2, alto=2.6, fondo=0.0, color=AMBAR)
        s = Tallos(S13, centro=(3.8, 1.2), paso=0.8, unidad=0.28, color=SENAL)
        h = Tallos([4, 4, 2], centro=(3.8, -0.7), paso=0.8, unidad=0.14, color=ESTIMACION)
        l_h = MathTex(r"h=c\,s", color=ESTIMACION).scale(1.0).move_to([3.8, -2.0, 0])
        pal = self.palabra("adaptado", ESTIMACION, 0.7).move_to([0.5, -0.7, 0])
        cor = corona().scale(0.8).move_to([-0.7, 2.9, 0])
        f_ent = MathTex(r"\mathrm{SNR}_{\mathrm{ent}}=E/\sigma^2", color=TXT).scale(1.0).move_to([4.0, 2.9, 0])
        ok = tilde(VERDE, 0.9).move_to([1.1, 2.9, 0])
        r_izq = RoundedRectangle(corner_radius=0.12, width=5.8, height=0.8, color=SENAL, stroke_width=2.5).set_fill(SENAL, 0.1).move_to([-3.3, -3.4, 0])
        r_der = RoundedRectangle(corner_radius=0.12, width=6.4, height=0.8, color=ESTIMACION, stroke_width=2.5).set_fill(ESTIMACION, 0.1).move_to([3.6, -3.4, 0])
        t_izq = etiqueta("ruido gaussiano → mínimo error", TXT, 0.45).move_to(r_izq)
        t_der = etiqueta("solo ruido blanco → máxima relación señal-ruido", TXT, 0.45).move_to(r_der)

        with self.narrar("b1"):
            # «La igualdad se da»
            self.en("igualdad")
            self.play(Write(f_le), run_time=self.dur(0.8))
            self.play(ReplacementTransform(f_le[1], f_eq), run_time=self.dur(0.5))

            # «la parábola toca el eje»
            self.en("toca")
            self.play(Create(par.eje), Create(par.curva), run_time=self.dur(1.0))

            # «un múltiplo de la señal»
            self.en("multiplo")
            self.play(FadeIn(s), FadeIn(h), run_time=self.dur(0.6))
            self.play(FadeIn(l_h), run_time=self.dur(0.4))

            # «el filtro adaptado»
            self.en("adaptado")
            self.pop(pal)

            # «ese máximo»
            self.en("maximo")
            self.play(FadeIn(cor, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «la relación señal-ruido que ya había a la entrada»
            self.en("entrada")
            self.play(Write(f_ent), run_time=self.dur(1.2))

            # «no se pierde nada»
            self.en("nada")
            self.play(Create(ok), run_time=self.dur(0.4))
            self.sfx("exito", gain=-18)

            # «Dos justificaciones independientes»
            self.en("dos")
            self.play(FadeIn(r_izq), FadeIn(r_der), run_time=self.dur(0.6))

            # «con ruido gaussiano, minimiza el error»
            self.en("gauss")
            self.play(FadeIn(t_izq), run_time=self.dur(0.5))

            # «solo con ruido blanco, maximiza»
            self.en("blanco")
            self.play(FadeIn(t_der), run_time=self.dur(0.5))

            # «maximiza la relación señal-ruido»
            self.en("maxsnr")
            self.resaltar(r_der, color=AMBAR, escala=1.04)
        self.wait(1.0)
        self.limpiar()
