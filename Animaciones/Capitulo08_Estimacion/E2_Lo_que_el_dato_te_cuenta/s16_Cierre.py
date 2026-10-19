"""Escena 16 — Cierre: la media de la rebanada y el error sin patrón; falta conocer la distribución entera (anuncia E3)."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        n = Nube8(centro=(-3.0, 0.0), ancho=6.4, alto=6.0, n=80, semilla=11)
        with self.narrar("b1"):
            # «Resumiendo»
            self.en("resumen")
            self.play(Create(n.ax), FadeIn(n.etq), run_time=self.dur(0.4))
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in n.pts], lag_ratio=0.01), run_time=self.dur(1.2))

            # «la media de la rebanada»
            self.en("rebanada")
            reb = n.rebanada(0.8, 0.6)
            dot = Dot(n.p(0.8, 0.8), radius=0.14, color=AMBAR)
            e = MathTex(r"E[Y\mid X=x]", color=AMBAR).scale(1.4).move_to([3.7, 1.9, 0])
            self.play(FadeIn(reb), FadeIn(dot), run_time=self.dur(0.5))
            self.pop(e)

            # «ningún patrón»
            self.en("patron")
            ok = tilde(VERDE, 0.7).move_to([1.5, 0.4, 0])
            sp = Text("Error sin patrón", color=VERDE, weight=BOLD).scale(0.85).next_to(ok, RIGHT, buff=0.25)
            self.play(Create(ok), FadeIn(sp), run_time=self.dur(0.6))

            # «una pega»
            self.en("pega")
            self.corte()
            pe = Text("!", color=AMBAR, weight=BOLD).scale(5.0).move_to([0, 0.3, 0])
            self.pop(pe)

            # «la distribución entera»
            self.en("entera")
            self.corte()
            col = Colina(centro=(0, -0.2), rho=0.82, ancho=8.0, prof=3.6, alto=3.6, n=15)
            td = Text("Toda la distribución", color=TXT, weight=BOLD).scale(1.0).move_to([0, 3.3, 0])
            self.play(FadeIn(col.base), LaggedStart(*[AnimationGroup(FadeIn(r[0]), FadeIn(r[1])) for r in col.filas],
                                                    lag_ratio=0.04), FadeIn(td), run_time=self.dur(1.2))

            # «casi nunca la tenemos»
            self.en("nunca")
            x = cruz(ROJO, 4.5).move_to([0, -0.2, 0])
            self.play(Create(x), run_time=self.dur(0.5))

            # «medias, varianzas y covarianzas»
            self.en("numeros")
            self.corte()
            cs = VGroup(*[caja(" ", c, ancho=3.4, alto=2.4) for c in (SENAL, RUIDO, AMBAR)]).arrange(RIGHT, buff=0.7)
            cs.move_to([0, 0.4, 0])
            fs = [MathTex(t, color=TXT).scale(2.2).move_to(c) for t, c in
                  zip((r"\mu", r"\sigma^2", r"\sigma_{XY}"), cs)]
            self.play(LaggedStart(*[AnimationGroup(FadeIn(c), FadeIn(f, scale=0.5)) for c, f in zip(cs, fs)],
                                  lag_ratio=0.4), run_time=self.dur(1.5))

            # «solo podemos usar una recta»
            self.en("recta")
            self.corte()
            n2 = Nube8(centro=(0, 0.0), ancho=9.0, alto=6.4, n=80, semilla=11)
            lin = Line(n2.p(-2.6, -2.6), n2.p(2.6, 2.6), color=AMBAR, stroke_width=6)
            self.play(FadeIn(n2.ax), FadeIn(n2.etq), *[FadeIn(p) for p in n2.pts], run_time=self.dur(0.5))
            self.play(Create(lin), run_time=self.dur(0.9))

            # «En el próximo episodio»
            self.en("proximo")
            self.corte()
            prox = etiqueta("Próximo episodio", INK, 0.8).move_to([0, 2.0, 0])
            a = self.palabra("¿Y si solo", TXT, 1.5).move_to([0, 0.5, 0])
            b = self.palabra("vale una recta?", AMBAR, 1.5).move_to([0, -0.9, 0])
            self.play(FadeIn(prox), run_time=0.3)

            # «¿Y si»
            self.en("t1")
            self.pop(a)

            # «vale una recta»
            self.en("t2")
            self.pop(b)
        self.wait(1.0)
        self.limpiar()
