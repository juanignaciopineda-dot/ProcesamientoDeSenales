"""Escena 01 — Gancho: infinitos coeficientes, dos multiplicaciones, y un error que se clava en 0,7386."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        # izquierda: la fila de barras que decae sin fin
        vals = [2.4 * 0.62 ** i for i in range(8)]
        fila = Tallos(vals, centro=(-3.7, 1.5), paso=0.6, unidad=0.7, color=ESTIMACION)
        puntos = Text("…", color=INK).scale(0.9).move_to([-1.0, 0.9, 0])
        c1 = caja("× 0,157", ESTIMACION, ancho=2.0, alto=0.9, scale=0.55).move_to([-5.0, -1.3, 0])
        c2 = caja("× 0,7386", ESTIMACION, ancho=2.2, alto=0.9, scale=0.55).move_to([-2.3, -1.3, 0])
        # derecha: las barras de error
        be = barras_error([4, 0.8, 0.7401, 0.7387, 0.7386], ["0", "1", "2", "3", "∞"],
                          centro=(3.9, -0.3), ancho=5.4, alto=3.6, v_max=4.0)
        titulo_e = etiqueta("error", ERROR, 0.55).move_to([3.9, 2.2, 0])
        val = etiqueta("0,7386", ERROR, 0.6, BOLD).next_to(be.barras[-1], UP, buff=0.15)
        interrogante = MathTex("?", color=AMBAR).scale(1.6).move_to([3.9, 1.0, 0])
        with self.narrar("b1"):
            # «infinitos coeficientes»
            self.en("infinitos")
            self.play(Create(fila.base), LaggedStart(*[GrowFromEdge(t, DOWN) for t in fila.tallos], lag_ratio=0.12),
                      *[FadeIn(p, scale=0.3) for p in fila.puntos], FadeIn(puntos), run_time=self.dur(1.5))

            # «dos multiplicaciones»
            self.en("dos")
            self.play(FadeIn(c1, shift=UP * 0.2), FadeIn(c2, shift=UP * 0.2), run_time=self.dur(0.6))
            self.sfx("tick")

            # «Y un error que baja»
            self.en("baja")
            self.play(Create(be.base), FadeIn(titulo_e), *[FadeIn(e) for e in be.etiquetas], run_time=0.3)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in be.barras], lag_ratio=0.3),
                      run_time=self.dur(1.6))

            # «se clava en cero coma siete tres ocho seis»
            self.en("clava")
            self.play(be.barras[-1].animate.set_fill(ROJO, 1), run_time=0.3)
            self.pop(val, sonido="impacto")

            # «Hoy sabemos por qué»
            self.en("porque")
            lp = lupa(TXT).scale(1.5).move_to([6.3, 2.4, 0])
            lp.permitir_encima = True
            self.play(FadeIn(interrogante, scale=0.5), FadeIn(lp, scale=0.6), run_time=self.dur(0.5))
            self.play(lp.animate.move_to([4.6, -0.1, 0]), run_time=self.dur(1.0))

        self.wait(1.0)
        self.limpiar()
