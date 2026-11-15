"""Escena 01 — Gancho: mil medidas del sensor valen 250; mil de una pila valen una."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        arriba = fila_puntos(36, 9.0, (0.6, 1.9), SENAL, 0.09)
        abajo = fila_puntos(36, 9.0, (0.6, -1.7), AMBAR, 0.09)
        hilos = hilos_entre(arriba, INK, 2)
        grupos = VGroup(*[RoundedRectangle(corner_radius=0.1, width=1.0, height=0.45, color=VERDE, stroke_width=3)
                          .move_to(VGroup(*arriba[4 * i:4 * i + 4])) for i in range(9)])

        with self.narrar("b1"):
            # «Mil medidas seguidas»
            self.en("mil")
            self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in arriba], lag_ratio=0.03), run_time=self.dur(1.0))

            # «del sensor»
            self.en("sensor")
            et = self.palabra("sensor", SENAL, 0.7).move_to([-5.6, 1.9, 0])
            self.play(Create(hilos), FadeIn(et), run_time=self.dur(0.7))

            # «doscientas cincuenta»
            self.en("n250")
            self.play(Create(grupos), run_time=self.dur(0.8))
            n250 = self.palabra("≈ 250", VERDE, 1.3).move_to([0.6, 3.25, 0])
            self.pop(n250)

            # «mil medidas de una pila»
            self.en("pila")
            p = pila("+2").scale(1.0).move_to([-5.6, -1.7, 0])
            self.play(FadeIn(p), LaggedStart(*[FadeIn(d, scale=0.4) for d in abajo], lag_ratio=0.03),
                      run_time=self.dur(1.0))

            # «como una sola»
            self.en("una")
            uno = Dot([0.6, -1.7, 0], radius=0.14, color=AMBAR)
            self.play(ReplacementTransform(abajo, uno), run_time=self.dur(0.8))
            n1 = self.palabra("1", ROJO, 1.6).move_to([3.0, -1.7, 0])
            self.pop(n1)

            # «¿Por qué?»
            self.en("porque")
            q = self.palabra("¿?", TXT, 2.0).move_to([0.6, 0.1, 0])
            self.pop(q)
        self.wait(0.6)
        self.limpiar()
