"""Escena 06 — Tres problemas (uno por grabación) y los dos cambios: potencia y ensemble."""
from comun.escena import *


class TresProblemas(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        ys = [2.4, 1.2, 0.0, -1.2, -2.4]
        Ls = [Lienzo(ancho=4.8, alto=0.9, t_rango=(0, 3), v_max=1.0, centro=(-4.1, y)) for y in ys]
        trazas = [ruido_t(L, semilla=20 + i, amp=0.35, ancho=2.4) for i, L in enumerate(Ls)]
        specs = [espectro_ruidoso(centro=(4.6, y), ancho=4.0, alto=0.85, semilla=30 + i, color=AZUL) for i, y in enumerate(ys)]
        cf = caja("Fourier", AZUL, ancho=1.7, alto=0.8).move_to([0.4, 0.0, 0])
        a1 = flecha([-1.6, 0.0, 0], [-0.5, 0.0, 0])
        a2 = flecha([1.3, 0.0, 0], [2.4, 0.0, 0])
        with self.narrar("b1"):
            # «un problema peor»
            self.en("peor")
            self.corte()
            self.play(Create(Ls[2].base()), Create(trazas[2]), run_time=self.dur(0.9), rate_func=linear)

            # «Aunque pudiéramos transformarla»
            self.en("transformarla")
            self.play(GrowArrow(a1), FadeIn(cf), run_time=self.dur(0.6))

            # «el espectro de esa grabación»
            self.en("espectro")
            self.play(GrowArrow(a2), Create(specs[2]), run_time=self.dur(0.8), rate_func=linear)

            # «el ensemble»
            self.en("ensemble")
            pal = self.palabra("ensemble", AMBAR, 0.8).move_to([-4.1, 3.5, 0])
            self.pop(pal)

            # «mil grabaciones del mismo fenómeno»
            self.en("mil")
            otras = [trazas[i] for i in (0, 1, 3, 4)]
            self.play(LaggedStart(*[Create(t) for t in otras], lag_ratio=0.25), run_time=self.dur(1.6),
                      rate_func=linear)

            # «una encima de otra»
            self.en("encima")
            self.play(*[t.animate.shift(DOWN * ys[i]).set_stroke(opacity=0.55)
                        for i, t in enumerate(trazas) if i != 2], run_time=self.dur(0.9))

            # «su propio espectro»
            self.en("propio")
            self.play(*[t.animate.shift(UP * ys[i]).set_stroke(opacity=1)
                        for i, t in enumerate(trazas) if i != 2], run_time=self.dur(0.6))
            self.play(LaggedStart(*[Create(specs[i]) for i in (0, 1, 3, 4)], lag_ratio=0.2),
                      run_time=self.dur(1.0), rate_func=linear)

            # «distinto en todos los detalles»
            self.en("distinto")
            ne = self.palabra("≠", AMBAR, 1.6).move_to([0.4, 1.9, 0])
            self.pop(ne)

            # «una propiedad del fenómeno»
            self.en("fenomeno")
            marco = Rectangle(width=5.3, height=6.2, color=AMBAR, stroke_width=3).move_to([-4.1, 0, 0])
            marco.permitir_encima = True
            fen = self.palabra("fenómeno", AMBAR, 0.7).move_to([-4.1, -3.55, 0])
            self.play(Create(marco), run_time=self.dur(0.6))
            self.pop(fen)

            # «no de una de sus grabaciones»
            self.en("grab")
            self.play(Create(tachar(trazas[3])), run_time=0.4)
            self.sfx("error")

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        textos = ["no empieza ni termina", "energía infinita", "distinta cada vez"]
        filas = [2.3, 1.3, 0.3]
        ts = [etiqueta(t, TXT, 0.6).move_to([-3.4, y, 0]) for t, y in zip(textos, filas)]
        cr = [cruz(ROJO, 0.9).move_to([-6.2, y, 0]) for y in filas]
        cab = etiqueta("dos cambios", INK, 0.6).move_to([4.0, 3.2, 0])
        vA = etiqueta("energía", TXT, 0.7).move_to([2.5, 1.6, 0])
        nA = self.palabra("potencia", AMBAR, 0.7).move_to([5.6, 1.6, 0])
        aA = flecha([3.3, 1.6, 0], [4.7, 1.6, 0])
        vB = etiqueta("una grabación", TXT, 0.7).move_to([2.6, -0.4, 0])
        nB = self.palabra("ensemble", AMBAR, 0.7).move_to([5.7, -0.4, 0])
        aB = flecha([4.0, -0.4, 0], [4.7, -0.4, 0])
        with self.narrar("b2"):
            # «dura para siempre»
            self.en("p1")
            self.corte()
            self.play(FadeIn(ts[0]), Create(cr[0]), run_time=self.dur(0.6))
            self.sfx("error")

            # «tiene energía infinita»
            self.en("p2")
            self.play(FadeIn(ts[1]), Create(cr[1]), run_time=self.dur(0.6))
            self.sfx("error")

            # «distinta cada vez»
            self.en("p3")
            self.play(FadeIn(ts[2]), Create(cr[2]), run_time=self.dur(0.6))
            self.sfx("error")

            # «cambiando dos palabras»
            self.en("dos")
            self.play(FadeIn(cab), FadeIn(vA), FadeIn(vB), GrowArrow(aA), GrowArrow(aB), run_time=self.dur(0.8))

            # «En lugar de energía»
            self.en("energia")
            self.play(Create(tachar(vA)), run_time=0.4)

            # «vamos a mirar potencia»
            self.en("potencia")
            self.pop(nA)

            # «en lugar de una grabación»
            self.en("grabacion")
            self.play(Create(tachar(vB)), run_time=0.4)

            # «promediar sobre todo el ensemble»
            self.en("ensemble")
            self.pop(nB)
