"""Escena 15 — Cierre: resumen y anuncio del episodio 2, «Lo que el dato te cuenta»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        resumen = self.palabra("Resumen", AMBAR, 1.5).move_to([0, 3.3, 0])
        P = ParabolaApuestas8(centro=(-0.8, -0.5), ancho=7.0, alto=3.6)
        v = Dot(P.p(3.5), radius=0.13, color=VERDE)
        t35 = Text("3,5", color=VERDE, weight=BOLD).scale(0.7).move_to(P.xy(3.5, 0) + DOWN * 0.3)
        media = Text("Media", color=ESTIMACION, weight=BOLD).scale(0.8).move_to(P.xy(3.5, 0) + DOWN * 0.95)
        suelo = P.suelo(ESTIMACION)
        var = Text("2,92 = Varianza", color=ESTIMACION, weight=BOLD).scale(0.8).move_to([4.8, P.xy(P.A1, P.SUELO)[1], 0])
        cas = [casilla8(-4.6, 0.3, "Cuadrado", "Media", ESTIMACION), casilla8(0.0, 0.3, "Tamaño", "Mediana", VERDE),
               casilla8(4.6, 0.3, "Acierto", "Moda", CIAN)]
        d = dado_n(3).scale(2.0).move_to([-1.8, 0.2, 0])
        q = Text("?", color=ESTIMACION, weight=BOLD).scale(2.0).move_to([-1.8, 2.3, 0])
        ojo_g = ojo(TXT).scale(1.7).move_to([2.6, 0.2, 0])
        tarjeta = caja("Episodio 2", AMBAR, ancho=4.6, alto=1.2, scale=0.95).move_to([0, 2.6, 0])
        titulo = self.palabra("Lo que el dato te cuenta", AMBAR, 1.0).move_to([0, 0.6, 0])

        with self.narrar("b1"):
            # «Resumamos»
            self.en("resumen")
            self.corte()
            self.pop(resumen)

            # «la mejor apuesta es la media»
            self.en("media")
            self.play(FadeIn(P), Create(P.curva), run_time=self.dur(0.9))
            self.play(FadeIn(v, scale=0.5), FadeIn(t35), FadeIn(media), run_time=self.dur(0.5))

            # «el error que queda es la varianza»
            self.en("varianza")
            self.play(Create(suelo), FadeIn(var, shift=LEFT * 0.2), run_time=self.dur(0.7))

            # «cambias la forma de medir el error»
            self.en("cambias")
            self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame and m is not resumen], run_time=0.3)
            self.play(*[FadeIn(c.rect) for c in cas], *[FadeIn(c.forma) for c in cas], run_time=self.dur(0.7))
            self.play(FadeIn(cas[0].resp), run_time=self.dur(0.3))

            # «la mediana, la moda»
            self.en("otras")
            self.play(FadeIn(cas[1].resp, shift=UP * 0.1), FadeIn(cas[2].resp, shift=UP * 0.1), run_time=self.dur(0.7))

            # «antes de apostar»
            self.en("antes")
            self.corte()
            self.play(FadeIn(d, scale=0.6), run_time=self.dur(0.4))
            self.pop(q)

            # «pudieras ver algo»
            self.en("ver")
            self.play(FadeIn(ojo_g, scale=0.6), run_time=self.dur(0.5))

            # «el próximo episodio»
            self.en("proximo")
            self.corte()
            self.play(FadeIn(tarjeta, scale=0.7), run_time=self.dur(0.5))

            # «Lo que el dato te cuenta»
            self.en("titulo")
            self.pop(titulo)
        self.wait(1.0)
        self.limpiar()
