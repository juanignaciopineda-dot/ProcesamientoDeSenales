"""Escena 03 — El radar: cuatro casos, dos aciertos y dos errores distintos (falsa alarma y fallo)."""
from comun.escena import *
from comun.figuras_c9e2 import *


class FalsaAlarmaYFallo(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.cuatro_casos()
        self.nombres()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def cuatro_casos(self):
        self.decide = None
        self.radar = radar13().scale(1.1).move_to([-5.5, -2.3, 0])
        h0 = casilla_h3(0, "Solo ruido", centro=(-3.8, 3.2), ancho=3.6)
        h1 = casilla_h3(1, "Hay avión", centro=(3.8, 3.2), ancho=3.6)
        garab = garabato9(centro=(-3.8, 2.25), ancho=2.2, alto=0.5)
        avion_ = avion_arriba(C1).scale(1.1).move_to([3.8, 2.25, 0])
        eco = Dot([-2.6, -2.0, 0], radius=0.1, color=MEDIDA)
        decide = Text("Decide", color=ESTIMACION, weight=BOLD).scale(0.5).move_to([-5.5, -0.9, 0])
        T = Tabla22_9(("Solo ruido", "Hay avión"), ("Nada", "Avión"), centro=(1.6, -1.0), ancho=1.8, alto=1.7,
                      titulo_f="Realidad", titulo_c="Decisión", escala=0.45)
        self.T = T
        self.decide = decide
        self.marcas = {(i, j): T.marca(i, j) for i in range(2) for j in range(2)}
        neq = MathTex(r"\neq", color=ESTIMACION).scale(1.4).move_to([5.0, -1.0, 0])

        with self.narrar("b1"):
            # «Un radar mira al cielo»
            self.en("radar")
            self.play(FadeIn(self.radar, shift=UP * 0.3), run_time=self.dur(0.5))
            self.play(LaggedStart(*[o.animate(rate_func=there_and_back).set_stroke(width=7)
                                    for o in self.radar.ondas], lag_ratio=0.3), run_time=self.dur(0.9))

            # «La hipótesis cero dice»
            self.en("h0")
            self.play(FadeIn(h0, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «solo hay ruido»
            self.en("garabato")
            self.play(Create(garab), run_time=self.dur(0.8))

            # «hay un avión»
            self.en("h1")
            self.play(FadeIn(h1, shift=DOWN * 0.2), FadeIn(avion_, shift=RIGHT * 0.5), run_time=self.dur(0.6))

            # «mide y decide»
            self.en("decide")
            self.play(FadeIn(eco), run_time=0.15)
            self.play(eco.animate.move_to(self.radar.plato.get_center()), run_time=self.dur(0.5))
            self.play(FadeOut(eco), FadeIn(decide, shift=UP * 0.2), run_time=self.dur(0.4))

            # «cuatro casos posibles»
            self.en("tabla")
            self.play(LaggedStart(*[Create(T.cel[k]) for k in sorted(T.cel)], lag_ratio=0.2),
                      FadeIn(T.rot_f), FadeIn(T.rot_c), FadeIn(T.titulos), run_time=self.dur(1.0))

            # «En dos, acierta»
            self.en("aciertos")
            self.play(Create(self.marcas[(0, 0)]), Create(self.marcas[(1, 1)]), run_time=self.dur(0.5))
            self.sfx("exito", gain=-20)

            # «se equivoca»
            self.en("errores")
            self.play(Create(self.marcas[(0, 1)]), Create(self.marcas[(1, 0)]), run_time=self.dur(0.5))
            self.sfx("error", gain=-20)

            # «no de la misma manera»
            self.en("distintos")
            self.pop(neq)
        self.neq = neq

    # ------------------------------------------------------------ b2
    def nombres(self):
        T = self.T
        fa = T.texto(0, 1, "Falsa alarma", ERROR, dy=-0.15, escala=0.4)
        fallo = T.texto(1, 0, "Fallo", ERROR, dy=-0.15, escala=0.42)
        miss = T.texto(1, 0, "Miss", INK, dy=-0.55, escala=0.36)
        iconos_ = VGroup(radar13().scale(0.45), tira_test07(0.32), canal9(ancho=1.6, escala=0.4))
        iconos_.arrange(DOWN, buff=0.35).move_to([5.9, 0.0, 0])
        canal = canal9(centro=(-5.3, -2.3), ancho=3.0, escala=0.62)
        filas_c = T.nuevas_filas(("Se envió 0", "Se envió 1"))
        cols_c = T.nuevas_cols(("Decir 0", "Decir 1"))
        fa_c = T.texto(0, 1, "0 → 1", ESTIMACION, dy=-0.55, escala=0.4)

        with self.narrar("b2"):
            # «Si dice que hay un avión»
            self.en("dice")
            self.play(FadeOut(self.neq), T.cel[(0, 1)].animate.set_stroke(ERROR, 5), run_time=self.dur(0.4))

            # «es una falsa alarma»
            self.en("fa")
            self.play(Write(fa), run_time=self.dur(0.5))

            # «Si dice que no hay nada»
            self.en("dicenada")
            self.play(T.cel[(0, 1)].animate.set_stroke(INK, 2.5), T.cel[(1, 0)].animate.set_stroke(ERROR, 5),
                      run_time=self.dur(0.4))

            # «es un fallo»
            self.en("fallo")
            self.play(Write(fallo), run_time=self.dur(0.4))

            # «se llama miss»
            self.en("miss")
            self.play(FadeIn(miss, shift=UP * 0.15), T.cel[(1, 0)].animate.set_stroke(INK, 2.5), run_time=self.dur(0.4))

            # «valen para todo»
            self.en("todo")
            self.play(LaggedStart(*[FadeIn(i, shift=LEFT * 0.3) for i in iconos_], lag_ratio=0.3), run_time=self.dur(0.9))

            # «En el canal de bits»
            self.en("canal")
            self.play(FadeOut(self.radar), FadeOut(self.decide), FadeIn(canal), FadeOut(iconos_[0]), FadeOut(iconos_[1]),
                      ReplacementTransform(T.rot_f, filas_c), ReplacementTransform(T.rot_c, cols_c),
                      run_time=self.dur(0.7))

            # «decir uno cuando se envió un cero»
            self.en("fa_canal")
            self.play(FadeIn(fa_c, shift=UP * 0.15), run_time=self.dur(0.4))
            self.resaltar(T.cel[(0, 1)], color=ERROR)
