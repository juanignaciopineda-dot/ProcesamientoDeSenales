"""Escena 11 — Predecir con todo el pasado: 0,443 z⁻¹ / (1 − 0,157 z⁻¹), error 2,826."""
from comun.escena import *


class TodoElPasado(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        fila = FilaMuestras([r"\cdots", r"x[n{-}3]", r"x[n{-}2]", r"x[n{-}1]"], centro=(0, 3.1), lado=1.35,
                            color=MEDIDA, escala=0.6)
        m_p = fila.marco(0, 3, AMBAR)

        l_h = MathTex(r"H(z)=", color=ESTIMACION).scale(0.9).move_to([-3.0, 1.4, 0])
        fr = fraccion(MathTex(r"0{,}443\,z^{-1}", color=TXT).scale(0.9),
                      MathTex(r"1-0{,}157\,z^{-1}", color=TXT).scale(0.9)).move_to([-0.8, 1.4, 0])
        oculta(fr)
        l_fi = etiqueta("filtrar:", INK, 0.55).move_to([-3.4, -0.1, 0])
        fr2 = fraccion(MathTex(r"0{,}7386", color=INK).scale(0.9),
                       MathTex(r"1-0{,}157\,z^{-1}", color=INK).scale(0.9)).move_to([-0.8, -0.1, 0])
        err = formula(r"\text{error}", "=", r"2{,}826", escala=1.0, colores={0: ERROR, 2: ERROR}).move_to([4.6, 1.4, 0])

        vals = [0, 0.443, 0.0695, 0.0109]
        T = Tallos(vals, centro=(-4.2, -1.9), paso=1.1, unidad=1.5, color=ESTIMACION, extra=0)
        t_v = VGroup(*[MathTex(s, color=TXT).scale(0.55).move_to(T.pos(i) + UP * 0.3)
                       for i, s in enumerate(["0", r"0{,}443", r"0{,}0695", r"0{,}0109"])])
        sus = MathTex(r"\cdots", color=INK).scale(0.8).move_to([T.x(3) + 0.9, -1.8, 0])

        x0 = 1.2
        l_b2 = etiqueta("todo el pasado · 2,826", ERROR, 0.5).move_to([2.6, -2.15, 0])
        b_2 = barra_h(2.826, -2.55, x0, 1.1, ERROR)
        l_b1 = etiqueta("una sola muestra · 2,848", INK, 0.5).move_to([2.8, -0.9, 0])
        b_1 = barra_h(2.848, -1.3, x0, 1.1, INK)

        with self.narrar("b1"):
            # «Con todo el pasado»
            self.en("pasado")
            self.play(FadeIn(fila), Create(m_p), run_time=self.dur(0.8))

            # «cero coma cuatro cuatro tres»
            self.en("num")
            self.add(fr)
            self.play(FadeIn(l_h), *revelar(fr.num), run_time=self.dur(0.8))

            # «entre uno menos»
            self.en("den")
            self.play(*revelar(fr.barra, fr.den), run_time=self.dur(0.7))

            # «cero coma uno cinco siete»
            self.en("n157")
            self.resaltar(fr.den, color=AMBAR)

            # «Se parece al filtro»
            self.en("parece")
            self.play(FadeIn(l_fi), FadeIn(fr2), run_time=self.dur(0.7))

            # «el mismo polo»
            self.en("polo")
            self.resaltar(fr.den, fr2.den, color=AMBAR)

            # «ese retardo de más»
            self.en("ret")
            self.resaltar(fr.num, color=AMBAR)

            # «el primer coeficiente es cero»
            self.en("primero")
            self.play(Create(T.base), run_time=self.dur(0.3))
            self.play(LaggedStart(*[FadeIn(T.palito(i)) for i in range(4)], FadeIn(t_v), FadeIn(sus), lag_ratio=0.2),
                      run_time=self.dur(1.2))
            self.resaltar(T.puntos[0], color=ERROR)

            # «dos coma ocho dos seis»
            self.en("e2826")
            self.play(FadeIn(err), FadeIn(l_b2), GrowFromEdge(b_2, LEFT), run_time=self.dur(0.8))

            # «mejora muy poco»
            self.en("poco")
            self.play(FadeIn(l_b1), GrowFromEdge(b_1, LEFT), run_time=self.dur(0.8))

            # «dos coma ocho cuatro ocho»
            self.en("b2848")
            self.resaltar(b_1, color=AMBAR)

        self.wait(1.0)
        self.limpiar()
