"""Escena 01 — Gancho: el termómetro marca 23 y la mejor apuesta es 22,4."""
from comun.escena import *
from comun.figuras_cap08_e3 import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        t = termometro(2.4, ROJO, 0.65).move_to([-3.6, 0.3, 0])
        n23 = Text("23 °C", color=MEDIDA, weight=BOLD).scale(1.0).next_to(t, RIGHT, buff=0.45)
        tach = tachar(n23)
        mejor = Text("Mejor apuesta", color=AMBAR, weight=BOLD).scale(0.8).move_to([3.3, 1.7, 0])
        r224 = Text("22,4 °C", color=AMBAR, weight=BOLD).scale(1.3).move_to([3.3, 0.1, 0])
        porque = Text("¿Por qué?", color=TXT, weight=BOLD).scale(1.0).move_to([0, -2.7, 0])
        nube = NubeRhoE3(centro=(0, 0.5), sx=1.8, sy=1.0, n=50, rho=0.89)
        recta = nube.recta(0.89)
        fichas = VGroup(*[caja(txt, AMBAR, ancho=3.0, alto=0.75).move_to([x, -3.3, 0])
                          for txt, x in (("Medias", -4.0), ("Varianzas", 0.0), ("Covarianza", 4.0))])

        with self.narrar("b1"):
            # «Un termómetro marca veintitrés grados»
            self.en("marca")
            self.play(FadeIn(t), run_time=self.dur(0.5))
            self.pop(n23)

            # «la mejor apuesta»
            self.en("apuesta")
            self.pop(mejor)

            # «no es veintitrés»
            self.en("no23")
            self.sfx("error")
            self.play(Create(tach), run_time=self.dur(0.4))

            # «sino veintidós coma cuatro»
            self.en("s224")
            self.pop(r224)

            # «¿Por qué?»
            self.en("porque")
            self.pop(porque)

            # «una recta»
            self.en("recta")
            self.corte()
            self.play(FadeIn(nube), run_time=self.dur(0.5))
            self.play(Create(recta), run_time=self.dur(0.5))

            # «unos pocos números»
            self.en("numeros")
            self.play(LaggedStart(*[FadeIn(f, shift=UP * 0.2) for f in fichas], lag_ratio=0.3),
                      run_time=self.dur(0.9))
        self.wait(1.0)
        self.limpiar()
