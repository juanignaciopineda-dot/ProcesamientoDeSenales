"""Escena 04 — Los cuatro casos de una decisión y la probabilidad de error."""
from comun.escena import *


class CuatroCasos(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.T = TablaDecision(centro=(-2.5, -0.5), lado=2.3)
        self.casos()
        self.error()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def casos(self):
        T = self.T
        tildes = [tilde(VERDE, 0.7).move_to(T.c(0, 0)), tilde(VERDE, 0.7).move_to(T.c(1, 1))]
        self.cruces = [cruz(ROJO, 0.8).move_to(T.c(0, 1) + UP * 0.75), cruz(ROJO, 0.8).move_to(T.c(1, 0) + UP * 0.75)]
        self.rot_fa = Text("falsa alarma", color=ROJO, weight=BOLD).scale(0.52).move_to(T.c(0, 1) + UP * 0.2)
        self.rot_fallo = Text("fallo", color=ROJO, weight=BOLD).scale(0.55).move_to(T.c(1, 0) + UP * 0.2)
        self.rot_miss = Text("miss", color=INK, slant=ITALIC).scale(0.55).move_to(T.c(1, 0) + DOWN * 0.2)
        self.rot_fpos = Text("falso positivo", color=INK).scale(0.46).move_to(T.c(0, 1) + DOWN * 0.25)
        self.rot_fneg = Text("falso negativo", color=INK).scale(0.46).move_to(T.c(1, 0) + DOWN * 0.7)
        av1 = avion(SENAL).scale(1.6).move_to([4.5, 1.4, 0])
        tach = tachar(av1)
        no_habia = etiqueta("no había", INK, 0.7).next_to(av1, DOWN, buff=0.25)
        av2 = avion(SENAL).scale(1.6).move_to([4.5, 1.4, 0])
        habia = etiqueta("sí había", INK, 0.7).next_to(av2, DOWN, buff=0.25)
        self.panel = VGroup(av1, tach, no_habia)
        self.panel2 = VGroup(av2, habia)
        hosp = cruz_hospital(ROJO).scale(1.5).move_to([4.5, -1.5, 0])
        self.hosp = hosp

        with self.narrar("b1"):
            # «cuatro casos posibles»
            self.en("cuatro")
            self.corte()
            self.play(FadeIn(T.cel[(0, 0)]), FadeIn(T.cel[(0, 1)]), FadeIn(T.cel[(1, 0)]), FadeIn(T.cel[(1, 1)]),
                      FadeIn(T.enc), FadeIn(T.titulos), run_time=self.dur(0.9))

            # «Dos son aciertos»
            self.en("aciertos")
            self.play(*[FadeIn(x, scale=0.5) for x in tildes], run_time=self.dur(0.5))

            # «Los otros dos son errores»
            self.en("errores")
            self.play(*[FadeIn(x, scale=0.5) for x in self.cruces], run_time=self.dur(0.5))

            # «nombre propio»
            self.en("nombre")
            self.play(T.cel[(0, 1)].animate.set_stroke(ROJO, 4), T.cel[(1, 0)].animate.set_stroke(ROJO, 4),
                      run_time=self.dur(0.5))

            # «dice que hay avión y no lo había»
            self.en("dicehay")
            self.play(FadeIn(self.panel), run_time=self.dur(0.6))

            # «falsa alarma»
            self.en("fa")
            self.pop(self.rot_fa)

            # «dice que no hay nada y sí lo había»
            self.en("dicenada")
            self.play(FadeOut(self.panel), FadeIn(self.panel2), run_time=self.dur(0.5))

            # «un fallo»
            self.en("fallo")
            self.pop(self.rot_fallo)

            # «miss»
            self.en("miss")
            self.pop(self.rot_miss)

            # «En medicina es igual»
            self.en("medicina")
            self.play(FadeOut(self.panel2), FadeIn(self.hosp, scale=0.6), run_time=self.dur(0.5))

            # «falso positivo»
            self.en("fpos")
            self.play(FadeIn(self.rot_fpos), run_time=self.dur(0.4))

            # «falso negativo»
            self.en("fneg")
            self.play(FadeIn(self.rot_fneg), run_time=self.dur(0.4))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def error(self):
        T = self.T
        pfa = MathTex("P_{FA}", color=ROJO).scale(1.2).move_to(T.c(0, 1) + UP * 0.75)
        pm = MathTex("P_{M}", color=ROJO).scale(1.2).move_to(T.c(1, 0) + UP * 0.75)
        total = Text("probabilidad de error", color=ROJO, weight=BOLD).scale(0.8).move_to([3.9, 1.3, 0])
        f = formula("P_e", "=", "p_0", r"\cdot", "P_{FA}", "+", "p_1", r"\cdot", "P_{M}", escala=1.05,
                    colores={0: ERROR, 2: RUIDO, 4: ERROR, 6: SENAL, 8: ERROR}).move_to([3.7, 3.0, 0])
        diez = casillas(10, rojas=(), centro=(3.7, 1.9), lado=0.46, hueco=0.08)
        diez.cas[2].set_color(SENAL).set_fill(SENAL, 0.7)
        ps = MathTex("p_1=0{,}1", r"\;\cdot\;", "p_0=0{,}9", color=TXT).scale(1.0).move_to([3.7, 1.2, 0])
        ps[0].set_color(SENAL)
        ps[2].set_color(RUIDO)
        n_fa = MathTex(r"P_{FA}=0{,}05", color=ROJO).scale(1.1).move_to([3.7, 0.4, 0])
        n_m = MathTex(r"P_{M}=0{,}2", color=ROJO).scale(1.1).move_to([3.7, -0.4, 0])
        cuenta = MathTex(r"0{,}9\cdot 0{,}05+0{,}1\cdot 0{,}2", color=TXT).scale(1.1).move_to([3.7, -1.5, 0])
        res = MathTex(r"=0{,}065\;(6{,}5\,\%)", color=ROJO).scale(1.3).move_to([3.7, -2.7, 0])

        with self.narrar("b2"):
            # «Cada error tiene su probabilidad»
            self.en("prob")
            self.play(FadeOut(self.hosp), FadeOut(self.rot_fpos), FadeOut(self.rot_fneg),
                      FadeOut(self.cruces[0]), FadeOut(self.cruces[1]), run_time=0.3)
            self.play(FadeIn(pfa, scale=0.5), FadeIn(pm, scale=0.5), run_time=self.dur(0.5))

            # «la de falsa alarma»
            self.en("lafa")
            self.resaltar(pfa, color=AMBAR)

            # «la de miss»
            self.en("lam")
            self.resaltar(pm, color=AMBAR)

            # «la probabilidad total de equivocarnos»
            self.en("total")
            self.play(FadeIn(total), run_time=self.dur(0.5))

            # «la media ponderada»
            self.en("media")
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=self.dur(0.5))

            # «pe cero por la falsa alarma»
            self.en("t1")
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in (2, 3, 4)], run_time=self.dur(0.6))

            # «más pe uno por el miss»
            self.en("t2")
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in (5, 6, 7, 8)], run_time=self.dur(0.6))

            # «Con números redondos»
            self.en("redondos")
            self.play(FadeOut(total), run_time=self.dur(0.3))

            # «una de cada diez veces»
            self.en("diez")
            self.play(FadeIn(diez, lag_ratio=0.1), run_time=self.dur(0.7))
            self.play(FadeIn(ps), run_time=self.dur(0.4))

            # «cinco por ciento de falsas alarmas»
            self.en("cinco")
            self.pop(n_fa)

            # «veinte por ciento de misses»
            self.en("veinte")
            self.pop(n_m)

            # «nos equivocamos»
            self.en("equivocamos")
            self.play(FadeIn(cuenta, shift=UP * 0.1), run_time=self.dur(0.6))

            # «un seis coma cinco por ciento»
            self.en("resultado")
            self.pop(res)
        self.wait(0.3)
