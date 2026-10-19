"""Escena 14 — Cierre: resumen y anuncio del episodio 4, «La sombra de una flecha»."""
from comun.escena import *
from comun.figuras_cap08_e3 import *


class Cierre(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        resumen = self.palabra("Resumen", AMBAR, 0.9).move_to([0, 3.3, 0])
        fichas = VGroup(*[caja(txt, AMBAR, ancho=3.0, alto=0.7, scale=0.5).move_to([x, 2.2, 0])
                          for txt, x in (("Medias", -4.2), ("Varianzas", 0.0), ("Covarianza", 4.2))])
        f = formula(r"\hat{y}", "=", r"\mu_y", "+", r"\rho", r"\frac{\sigma_y}{\sigma_x}", "(", "x", "-", r"\mu_x",
                    ")", escala=1.2, colores={0: ESTIMACION, 2: SENAL, 4: AMBAR, 7: MEDIDA, 9: MEDIDA})
        f.move_to([0, 0.8, 0])
        error = Text("Error", color=ERROR, weight=BOLD).scale(0.7).move_to([-3.2, -0.6, 0])
        var1r = MathTex(r"J=\sigma_y^2\,(1-\rho^2)", color=ERROR).scale(1.2).move_to([0.9, -0.6, 0])
        pregunta = Text("Una pregunta", color=AMBAR, weight=BOLD).scale(0.8).move_to([-3.0, -1.9, 0])
        porque = Text("¿Por qué?", color=TXT, weight=BOLD).scale(0.8).move_to([2.0, -1.9, 0])
        mejor = Text("Otra recta mejor", color=INK).scale(0.6).move_to([-1.0, -3.1, 0])
        cruz_m = cruz(ROJO, 0.8).move_to([1.9, -3.1, 0])
        F, r = flechas_xy(origen=(-3.0, -1.8), largo=5.0, angulo=50)
        tarjeta = caja("Episodio 4", AMBAR, ancho=3.4, alto=0.9, scale=0.6).move_to([0, 2.4, 0])
        titulo_p = self.palabra("La sombra de una flecha", TXT, 1.2).move_to([0, 0.2, 0])

        with self.narrar("b1"):
            # «Resumimos»
            self.en("resumen")
            self.corte()
            self.pop(resumen)

            # «medias, varianzas y la covarianza»
            self.en("datos")
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in fichas], lag_ratio=0.3),
                      run_time=self.dur(1.2))

            # «arranca en la media y corrige con rho»
            self.en("recta")
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in range(11)], run_time=self.dur(1.3))

            # «el error que deja»
            self.en("error")
            self.pop(error)

            # «la varianza por uno menos rho al cuadrado»
            self.en("var1r")
            self.play(FadeIn(var1r, shift=UP * 0.1), run_time=self.dur(1.0))

            # «Pero queda una pregunta»
            self.en("pregunta")
            self.pop(pregunta)

            # «¿por qué esa fórmula»
            self.en("porque")
            self.pop(porque)

            # «por qué no hay una recta mejor»
            self.en("mejor")
            self.play(FadeIn(mejor), run_time=self.dur(0.5))
            self.pop(cruz_m, sonido="error")

            # «un dibujo con flechas»
            self.en("flechas")
            self.corte()
            self.play(Create(F.presente), Create(F.futuro), FadeIn(r["x"]), FadeIn(r["y"]), run_time=self.dur(0.6))
            self.play(Create(F.sombra), FadeIn(r["yh"]), Create(F.error), FadeIn(r["e"]), run_time=self.dur(0.6))
            self.play(Create(F.recto), run_time=self.dur(0.3))

            # «el próximo episodio»
            self.en("proximo")
            self.corte()
            self.pop(tarjeta)

            # «la sombra de una flecha»
            self.en("titulo")
            self.pop(titulo_p)
        self.wait(1.0)
        self.limpiar()
