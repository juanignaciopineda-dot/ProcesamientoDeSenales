"""Escena 05 — El ángulo recto es la regla de ortogonalidad recortada: el error es ortogonal al uno y al dato."""
from comun.escena import *
from comun.figuras_c8e4 import *


class ElErrorEsPerpendicular(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.recortada()
        self.dos_condiciones()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def recortada(self):
        F, r = flechas8()
        self.add(F.presente, F.futuro, F.sombra, F.error, F.recto, r["x"], r["y"], r["yh"], r["e"])
        perp = formula("e", r"\perp", "X", escala=1.3, colores={0: ERROR, 2: MEDIDA}).move_to([3.7, 2.9, 0])
        prod = formula("E[", "e", r"\cdot", r"\tilde{x}", "]", "=", "0", escala=1.2,
                       colores={1: ERROR, 3: MEDIDA}).move_to([3.7, 1.8, 0])
        # tarjeta con la regla del episodio 2
        titulo_t = Text("Regla del episodio 2", color=INK).scale(0.5)
        regla_f = formula("E[", "e", r"\cdot", "g(X)", "]", "=", "0", escala=1.1, colores={1: ERROR})
        toda = Text("Para toda función g", color=TXT).scale(0.55)
        contenido = VGroup(titulo_t, regla_f, toda).arrange(DOWN, buff=0.22).move_to([3.7, -0.5, 0])
        tarjeta = RoundedRectangle(corner_radius=0.15, width=5.4, height=contenido.height + 0.5, color=INK,
                                   stroke_width=2.5).set_fill(INK, 0.1).move_to(contenido)
        solo = Text("Solo la lectura", color=MEDIDA).scale(0.55).move_to(toda)
        gx_nuevo = MathTex(r"\tilde{x}", color=MEDIDA).scale(1.1 * 0.9).move_to(regla_f[3])
        tij = tijeras().scale(0.7).move_to(tarjeta.get_right() + RIGHT * 0.5 + UP * 0.1)
        interr = Text("?", color=AMBAR, weight=BOLD).scale(2.0).move_to([3.7, -2.9, 0])

        with self.narrar("b1"):
            # «Mira el ángulo recto»
            self.en("recto")
            self.resaltar(F.recto, color=AMBAR, escala=1.8)

            # «El error es perpendicular»
            self.en("perp")
            self.resaltar(F.error, color=ERROR, escala=1.06)

            # «a la flecha de la lectura»
            self.en("lect")
            self.resaltar(F.presente, color=MEDIDA, escala=1.04)

            # «para variables»
            self.en("variables")
            self.play(FadeIn(perp, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «la media de su producto es cero»
            self.en("prod")
            self.play(*[FadeIn(prod[i]) for i in range(len(prod))], run_time=self.dur(0.9))

            # «la regla de ortogonalidad»
            self.en("regla")
            self.play(FadeIn(tarjeta), FadeIn(contenido), run_time=self.dur(0.7))

            # «pero recortada»
            self.en("recorta")
            self.play(FadeIn(tij), run_time=self.dur(0.25))
            self.play(tij.animate.shift(LEFT * 5.0), run_time=self.dur(1.0))
            self.play(FadeOut(tij), run_time=0.2)

            # «cualquier función del dato»
            self.en("cualq")
            self.resaltar(regla_f[3], toda, color=AMBAR, escala=1.15)

            # «solo a la lectura»
            self.en("sola")
            self.play(ReplacementTransform(regla_f[3], gx_nuevo), ReplacementTransform(toda, solo),
                      run_time=self.dur(0.7))

            # «¿Por qué solo a ella?»
            self.en("porque")
            self.pop(interr)

    # ------------------------------------------------------------ b2
    def dos_condiciones(self):
        f = formula(r"\hat{y}", "=", "h", r"\cdot", "X", "+", "b", r"\cdot", "1", escala=1.7,
                    colores={0: ESTIMACION, 4: MEDIDA, 8: INK}).move_to([0, 2.3, 0])
        c_e = Circle(radius=0.95, color=ERROR, stroke_width=4).set_fill(ERROR, 0.15).move_to([-4.6, -1.3, 0])
        c_x = Circle(radius=0.95, color=MEDIDA, stroke_width=4).set_fill(MEDIDA, 0.15).move_to([-3.4, -1.3, 0])
        l_e = MathTex("e", color=ERROR).scale(0.9).move_to([-4.9, -0.0, 0])
        l_x = MathTex("X", color=MEDIDA).scale(0.9).move_to([-3.1, 0.0, 0])
        flecha_a = CurvedArrow([-4.0, -0.6, 0], f[0].get_center() + DOWN * 0.5 + LEFT * 0.2, color=ESTIMACION,
                               stroke_width=4)
        num1 = Text("1", color=AMBAR, weight=BOLD).scale(0.9).move_to([-5.4, 0.2, 0])
        num2 = Text("2", color=AMBAR, weight=BOLD).scale(0.9).move_to([-5.4, -1.5, 0])
        r1a = formula("e", r"\perp", "1", escala=1.3, colores={0: ERROR}).move_to([-3.4, 0.2, 0])
        r1b = formula(r"\Rightarrow", "E[e]", "=", "0", escala=1.3, colores={1: ERROR}).move_to([1.2, 0.2, 0])
        r2a = formula("e", r"\perp", "X", escala=1.3, colores={0: ERROR, 2: MEDIDA}).move_to([-3.4, -1.5, 0])
        r2b = formula(r"\Rightarrow", "E[", "e", r"\cdot", r"\tilde{x}", "]", "=", "0", escala=1.3,
                      colores={2: ERROR, 4: MEDIDA}).move_to([2.0, -1.5, 0])

        with self.narrar("b2"):
            # «solo sabe usar dos cosas»
            self.en("dos")
            self.corte()
            self.play(LaggedStart(*[FadeIn(f[i]) for i in range(len(f))], lag_ratio=0.12), run_time=self.dur(1.2))

            # «la lectura»
            self.en("lec")
            self.resaltar(f[4], color=MEDIDA, escala=1.4)

            # «el uno que multiplica a be»
            self.en("uno")
            self.resaltar(f[8], color=AMBAR, escala=1.4)

            # «algo en común»
            self.en("comun")
            self.play(FadeIn(c_e), FadeIn(c_x), FadeIn(l_e), FadeIn(l_x), run_time=self.dur(0.7))

            # «la recta podría aprovecharlo»
            self.en("aprov")
            self.play(Create(flecha_a), run_time=self.dur(0.8))

            # «Así que pedimos dos condiciones»
            self.en("cond")
            self.play(*[FadeOut(m) for m in (c_e, c_x, l_e, l_x, flecha_a)], FadeIn(num1), FadeIn(num2),
                      run_time=self.dur(0.5))

            # «ortogonal al uno»
            self.en("ort1")
            self.play(FadeIn(r1a), run_time=self.dur(0.5))

            # «su media sea cero»
            self.en("media0")
            self.play(FadeIn(r1b), run_time=self.dur(0.6))

            # «ortogonal a la lectura»
            self.en("ortx")
            self.play(FadeIn(r2a), run_time=self.dur(0.5))
            self.play(FadeIn(r2b), run_time=self.dur(0.7))
