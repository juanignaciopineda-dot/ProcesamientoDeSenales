"""Escena 14 — El sensor contra la pila, con números."""
from comun.escena import *


class NumerosDelSensor(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        xs, xp, xn = 1.6, 5.2, -4.2
        ys = [1.4, 0.2, -1.0, -2.2]
        filas = ["N = 20", "N = 100", "N = 500", "N = 2.000"]
        valores = ["0,725", "0,157", "0,032", "0,008"]

        def celda(txt, x, y, color=TXT, escala=0.9):
            return Text(txt, color=color, weight=BOLD).scale(escala).move_to([x, y, 0])

        with self.narrar("b1"):
            # «Con el sensor»
            self.en("sensor")
            h1 = caja("sensor", SENAL, ancho=2.8, alto=0.8).move_to([xs, 2.8, 0])
            self.play(FadeIn(h1), run_time=0.4)

            # «veinte muestras»
            self.en("n20")
            fl = [celda(f, xn, y, INK, 0.85) for f, y in zip(filas, ys)]
            self.play(FadeIn(fl[0]), run_time=0.4)

            # «es cero coma siete dos»
            self.en("v725")
            vv = [celda(v, xs, y, AMBAR, 1.0) for v, y in zip(valores, ys)]
            self.pop(vv[0])

            # «Con cien»
            self.en("n100")
            self.play(FadeIn(fl[1]), run_time=0.4)

            # «cero coma uno seis»
            self.en("v157")
            self.pop(vv[1])

            # «Con quinientas»
            self.en("n500")
            self.play(FadeIn(fl[2]), run_time=0.4)

            # «cero coma cero tres»
            self.en("v032")
            self.pop(vv[2])

            # «Con dos mil»
            self.en("n2000")
            self.play(FadeIn(fl[3]), run_time=0.4)

            # «menos de una centésima»
            self.en("v008")
            self.pop(vv[3])

            # «la pila»
            self.en("pila")
            h2 = caja("pila", AMBAR, ancho=2.8, alto=0.8).move_to([xp, 2.8, 0])
            self.play(FadeIn(h2), run_time=0.4)

            # «en todos los casos»
            self.en("todos")
            cuatro = [celda("4", xp, y, ROJO, 1.0) for y in ys]
            self.play(LaggedStart(*[FadeIn(c, scale=0.5) for c in cuatro], lag_ratio=0.25), run_time=self.dur(1.2))

            # «Una baja sin parar»
            self.en("baja")
            fb = Arrow([xs + 1.5, 1.6, 0], [xs + 1.5, -2.4, 0], color=VERDE, buff=0, stroke_width=6)
            self.play(Create(fb), run_time=self.dur(1.0))

            # «la otra no se mueve»
            self.en("quieta")
            ln = Line([xp + 1.2, 1.4, 0], [xp + 1.2, -2.2, 0], color=ROJO, stroke_width=6)
            self.play(Create(ln), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
