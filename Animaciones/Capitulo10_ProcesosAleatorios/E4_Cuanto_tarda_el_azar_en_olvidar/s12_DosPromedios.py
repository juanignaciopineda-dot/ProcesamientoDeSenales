"""Escena 12 — DosPromedios: promedio vertical (ensemble) contra promedio horizontal (temporal)."""
from comun.escena import *


class DosPromedios(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        L = Lienzo(ancho=9.8, alto=3.4, t_rango=(0, 6), v_max=2.0, centro=(0, 0.4))
        pila = pila_de_curvas(L, 9, semilla=7, a=0.93, puntos=180, opacidad=0.5, ancho=2.4, escala=0.6)
        mas = pila_de_curvas(L, 12, semilla=11, a=0.93, puntos=180, opacidad=0.45, ancho=2.2, escala=0.6)
        base = L.base()
        corte = L.vertical(3.0, AMBAR, 3.5, 1.6)
        flecha_v = DoubleArrow(L.p(3.0, -1.5) + RIGHT * 0.35, L.p(3.0, 1.5) + RIGHT * 0.35, color=AMBAR, buff=0,
                               stroke_width=4, max_tip_length_to_length_ratio=0.1)
        t_vert = etiqueta("promedio del ensemble", AMBAR, 0.55).move_to([-3.4, 2.75, 0])
        lo_que = etiqueta("lo que tienes", AMBAR, 0.6, BOLD).move_to([4.4, 2.75, 0])
        flecha_h = Arrow(L.p(0.0, -1.85), L.p(6.0, -1.85), color=VERDE, buff=0, stroke_width=5)
        suma = etiqueta("suma de todos los valores", VERDE, 0.55).move_to([-3.3, -2.85, 0])
        div = etiqueta("÷ duración", VERDE, 0.55).move_to([0.6, -2.85, 0])
        temp = etiqueta("promedio temporal", VERDE, 0.7, BOLD).move_to([4.2, -2.85, 0])
        self.b1 = VGroup(*pila, *mas, base, corte, flecha_v, t_vert, lo_que, flecha_h, suma, div, temp)

        with self.narrar("b1"):
            # «un promedio vertical»
            self.en("vertical")
            self.play(Create(base), LaggedStart(*[Create(c) for c in pila], lag_ratio=0.06), run_time=self.dur(1.0))
            self.play(Create(corte), run_time=0.4)

            # «en un instante fijo»
            self.en("fijo")
            self.resaltar(corte, color=AMBAR, escala=1.0)

            # «a través de todas las realizaciones»
            self.en("traves")
            self.play(Create(flecha_v), FadeIn(t_vert), run_time=self.dur(0.8))

            # «miles de grabaciones»
            self.en("miles")
            self.play(LaggedStart(*[Create(c) for c in mas], lag_ratio=0.05), run_time=self.dur(2.0))

            # «hechas a la vez»
            self.en("vez")
            self.play(Indicate(corte, color=AMBAR, scale_factor=1.0), run_time=self.dur(0.8))

            # «una sola grabación»
            self.en("sola")
            self.play(*[c.animate.set_stroke(opacity=0.07) for c in list(pila[1:]) + list(mas)],
                      pila[0].animate.set_stroke(opacity=1, width=5),
                      FadeOut(corte), FadeOut(flecha_v), FadeOut(t_vert), run_time=self.dur(0.9))
            self.play(FadeIn(lo_que), run_time=0.4)

            # «un promedio horizontal»
            self.en("horizontal")
            self.play(Create(flecha_h), run_time=self.dur(1.2))

            # «sumar sus valores»
            self.en("suma")
            self.play(FadeIn(suma), run_time=0.4)

            # «dividir entre la duración»
            self.en("divide")
            self.play(FadeIn(div), run_time=0.4)

            # «el promedio temporal»
            self.en("temporal")
            self.pop(temp)

    def parte_b2(self):
        rng = np.random.default_rng(21)
        n = 200
        L = Lienzo(ancho=9.0, alto=3.0, t_rango=(0, n), v_max=1.6, centro=(-0.4, 0.5))
        t = np.arange(1, n + 1)
        corridas = [L.curva(t, np.cumsum(rng.normal(0, 1, n)) / t, SENAL, 2.6, 0.7) for _ in range(6)]
        banda_s = L.curva(t, 1.6 / np.sqrt(t), AMBAR, 2.4)
        banda_i = L.curva(t, -1.6 / np.sqrt(t), AMBAR, 2.4)
        banda_s.set_stroke(opacity=0.8), banda_i.set_stroke(opacity=0.8)
        base = L.base()
        preg = MathTex(r"\text{promedio temporal}\ \overset{?}{=}\ \text{media del ensemble}", color=TXT).scale(1.0)
        preg.move_to([0, 3.5, 0])
        sello7 = sello("capítulo 7", VERDE).scale(0.8).move_to([5.4, 2.2, 0])
        eje_n = MathTex("n", color=INK).scale(0.9).move_to(L.p(n, 0) + RIGHT * 0.85)
        eje_t = Text("tiempo", color=INK).scale(0.5).move_to(eje_n)
        promesa = sello("promesa", AMBAR).scale(0.8).move_to([-5.4, 2.3, 0])
        flecha_h = Arrow(L.p(0, -1.55), L.p(n, -1.55), color=VERDE, buff=0, stroke_width=5)
        pero = etiqueta("¡pero!", ROJO, 0.9, BOLD).move_to([5.6, -0.6, 0])
        puntos = VGroup(*[Dot([x, -3.0, 0], radius=0.11, color=SENAL) for x in np.linspace(-4.2, 4.2, 8)])
        arcos = VGroup(*[ArcBetweenPoints(a.get_center(), b.get_center(), angle=-1.2, color=AMBAR, stroke_width=3)
                         for a, b in zip(puntos[:-1], puntos[1:])])
        memoria = etiqueta("memoria", AMBAR, 0.7, BOLD).move_to([0, -3.7, 0])
        arcos.shift(UP * 0.0)

        with self.narrar("b2"):
            self.play(FadeOut(self.b1), run_time=0.2)
            # «si los dos promedios coinciden»
            self.en("coinciden")
            self.play(Write(preg), run_time=self.dur(1.4))

            # «Ya nos la planteamos»
            self.en("plante")
            self.pop(sello7, sonido="impacto")

            # «ley de los grandes números»
            self.en("grandes")
            self.play(Create(base), LaggedStart(*[Create(c) for c in corridas], lag_ratio=0.15), run_time=self.dur(1.6))

            # «muchas medidas independientes»
            self.en("indep")
            self.play(FadeIn(eje_n), run_time=0.4)

            # «se pega a la media»
            self.en("pega")
            self.play(Create(banda_s), Create(banda_i), run_time=self.dur(1.6))

            # «dijimos que la idea volvería»
            self.en("volveria")
            self.pop(promesa, sonido="impacto")

            # «a lo largo de una sola grabación»
            self.en("largo")
            self.play(Create(flecha_h), run_time=self.dur(1.6))

            # «Aquí está»
            self.en("aqui")
            self.play(ReplacementTransform(eje_n, eje_t), run_time=self.dur(0.6))

            # «La diferencia»
            self.en("difer")
            self.pop(pero, sonido="error")

            # «no son independientes»
            self.en("noindep")
            self.play(FadeIn(puntos), LaggedStart(*[Create(a) for a in arcos], lag_ratio=0.2), run_time=self.dur(1.6))

            # «tienen memoria»
            self.en("memoria")
            self.pop(memoria)
