"""Escena 01 — Gancho: tres problemas distintos, una sola operación."""
from comun.escena import *
from comun.figuras_c9e3 import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        Y = 1.0
        with self.narrar("b1"):
            # «El canal»
            self.en("canal")
            canal = canal9(centro=(-4.4, Y), ancho=3.4, escala=0.95)
            b0 = bit9(0, lado=0.5).next_to(canal.ent.get_start(), UP, buff=0.12)
            b1 = bit9(1, lado=0.5).next_to(canal.sal.get_end(), UP, buff=0.12)
            canal_g = VGroup(canal, b0, b1)
            self.play(FadeIn(canal_g, shift=UP * 0.2), run_time=self.dur(0.5))

            # «el radar»
            self.en("radar")
            radar = radar13().scale(1.5).move_to([0, Y, 0])
            self.play(FadeIn(radar, shift=UP * 0.2), run_time=self.dur(0.4))
            self.play(LaggedStart(*[Indicate(o, color=MEDIDA, scale_factor=1.15) for o in radar.ondas],
                                  lag_ratio=0.3), run_time=self.dur(0.8))

            # «el test médico»
            self.en("test")
            test = tira_test07(0.75).move_to([4.7, Y, 0])
            mas = Text("+", color=ERROR, weight=BOLD).scale(0.8).move_to(test.ventana)
            test_g = VGroup(test, mas)
            self.play(FadeIn(test_g, shift=UP * 0.2), run_time=self.dur(0.5))

            # «Parecen problemas distintos»
            self.en("distintos")
            grupos = [canal_g, radar, test_g]
            preg = VGroup(*[Text("?", color=INK, weight=BOLD).scale(0.8).move_to([x, Y + 1.75, 0])
                            for x in (-5.2, 0, 5.2)])
            self.play(canal_g.animate.shift(LEFT * 0.5), test_g.animate.shift(RIGHT * 0.5),
                      FadeIn(preg, shift=DOWN * 0.2), run_time=self.dur(0.6))

            # «con criterios distintos»
            self.en("criterios")
            etqs = VGroup(etiqueta("Error mínimo", TXT, 0.55).move_to([-5.2, -0.65, 0]),
                          etiqueta("Falsa alarma fija", TXT, 0.55).move_to([0, -0.65, 0]),
                          etiqueta("¿Creerle al positivo?", TXT, 0.55).move_to([4.9, -0.65, 0]))
            self.play(LaggedStart(*[FadeIn(e, shift=UP * 0.15) for e in etqs], lag_ratio=0.3),
                      run_time=self.dur(0.9))

            # «Pero la mejor decisión»
            self.en("mejor")
            self.play(canal_g.animate.shift(RIGHT * 0.8), test_g.animate.shift(LEFT * 0.8),
                      etqs[0].animate.shift(RIGHT * 0.8), etqs[2].animate.shift(LEFT * 0.8),
                      preg[0].animate.shift(RIGHT * 0.8), preg[2].animate.shift(LEFT * 0.8),
                      run_time=self.dur(0.6))

            # «la misma operación»
            self.en("misma")
            caja_ = caja_lrt9(escala=1.6).move_to([0, -2.6, 0])
            vacia = caja_.marco.copy()
            arriba = vacia.get_top() + UP * 0.08
            flechas = VGroup(
                flecha(canal_g.get_bottom() + DOWN * 0.15, arriba + LEFT * 0.9, INK, 3),
                flecha(radar.get_bottom() + DOWN * 0.15, arriba, INK, 3),
                flecha(test_g.get_bottom() + DOWN * 0.15, arriba + RIGHT * 0.9, INK, 3))
            self.play(FadeOut(etqs), FadeOut(preg), run_time=self.dur(0.3))
            self.play(LaggedStart(*[GrowArrow(f) for f in flechas], lag_ratio=0.2), Create(vacia),
                      run_time=self.dur(0.8))

            # «calcular un número»
            self.en("numero")
            self.pop(caja_.f[0])

            # «compararlo con un umbral»
            self.en("umbral")
            self.play(FadeIn(caja_.f[1], scale=0.6), run_time=self.dur(0.3))
            self.pop(caja_.f[2])
            self.play(Transform(vacia, caja_.marco), run_time=self.dur(0.3))
        self.wait(1.0)
        self.limpiar()
