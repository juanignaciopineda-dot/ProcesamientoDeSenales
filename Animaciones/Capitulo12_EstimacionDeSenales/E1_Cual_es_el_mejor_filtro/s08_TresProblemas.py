"""Escena 08 — Filtrar, predecir o suavizar: una pregunta con tres tamaños de ventana."""
from comun.escena import *


def _vent(L: Lienzo, k0: float, k1: float, color=AMBAR, opacidad: float = 0.25) -> Rectangle:
    a, b = L.p(k0, 0), L.p(k1, 0)
    r = Rectangle(width=abs(b[0] - a[0]), height=L.alto, stroke_width=2, color=color)
    r.set_fill(color, opacidad).move_to([(a[0] + b[0]) / 2, L.cy, 0])
    return r


class TresProblemas(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.tres_ventanas()
        self.cuantas_condiciones()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def tres_ventanas(self):
        t, y, v, x = sensor12(40)
        ys = [2.3, 0.4, -1.5]
        Ls = [Lienzo(ancho=8.0, alto=1.6, t_rango=(0, 39), v_max=7, centro=(-1.3, c)) for c in ys]
        curvas = [VGroup(L.curva(t, x, MEDIDA, 2.8), L.vertical(26, INK, 2.2, mitad=0.8)) for L in Ls]
        w = [_vent(Ls[0], 14, 26), _vent(Ls[1], 14, 25), _vent(Ls[2], 0, 39)]
        etq = [Text(s, color=AMBAR, weight=BOLD).scale(0.7).move_to([5.2, c, 0])
               for s, c in zip(["filtrar", "predecir", "suavizar"], ys)]
        cinta = triangulo_play().scale(0.5).move_to([6.4, ys[2], 0])
        cap = Text("capítulo 12", color=INK).scale(0.5).move_to([5.2, 3.4, 0])

        with self.narrar("b1"):
            # «qué muestras se usan»
            self.en("usan")
            self.play(FadeIn(curvas[0]), run_time=self.dur(0.7))

            # «tres problemas»
            self.en("tres")
            self.play(FadeIn(curvas[1]), FadeIn(curvas[2]), run_time=self.dur(0.7))

            # «con equis de ene y las anteriores»
            self.en("filtrar_v")
            self.play(FadeIn(w[0]), run_time=self.dur(0.5))

            # «filtrar»
            self.en("filtrar")
            self.pop(etq[0])

            # «solo las anteriores»
            self.en("pred_v")
            self.play(FadeIn(w[1]), run_time=self.dur(0.5))

            # «predecir»
            self.en("predecir")
            self.pop(etq[1])

            # «todo el registro»
            self.en("todo_v")
            self.play(FadeIn(w[2]), run_time=self.dur(0.6))

            # «suavizar»
            self.en("suavizar")
            self.pop(etq[2])

            # «grabaciones que ya están hechas»
            self.en("grab")
            self.pop(cinta)

            # «El capítulo entero»
            self.en("entero")
            self.pop(cap)

            # «tres tamaños de ventana»
            self.en("tamanos")
            self.play(*[m.animate(rate_func=there_and_back).set_stroke(color=ROJO, width=5) for m in w],
                      run_time=self.dur(0.9))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def cuantas_condiciones(self):
        grande = Text("?", color=AMBAR, weight=BOLD).scale(2.4).move_to([0, 0.6, 0])
        hs = [MathTex(f"h_{i} = \\,?", color=ESTIMACION).scale(1.0).move_to([c, 3.0, 0])
              for i, c in enumerate((-4.0, 0.0, 4.0))]
        cuantas = MathTex(r"e \perp \;?", color=ERROR).scale(1.5).move_to([0, 0.6, 0])
        arena = reloj_arena().scale(1.3).move_to([0, -1.5, 0])
        conds = [MathTex(s, color=ERROR).scale(1.0).move_to([-1.2, 1.5 - 0.9 * i, 0])
                 for i, s in enumerate([r"e \perp x[n]", r"e \perp x[n-1]", r"e \perp x[n-2]"])]
        oks = [tilde(VERDE, 0.5).move_to([1.2, 1.5 - 0.9 * i, 0]) for i in range(3)]
        sis = Text("3 ecuaciones · 3 incógnitas", color=TXT, weight=BOLD).scale(0.65).move_to([0, -1.9, 0])
        doc = documento().scale(1.4).move_to([5.2, -1.6, 0])
        lap = lapiz().scale(0.8).move_to([5.9, -2.1, 0])
        ok = tilde(VERDE, 0.7).move_to([5.2, -0.4, 0])

        with self.narrar("b2"):
            # «una pregunta»
            self.en("pregunta")
            self.corte()
            self.pop(grande)

            # «tres coeficientes por encontrar»
            self.en("tres_h")
            self.play(FadeOut(grande), run_time=0.2)
            self.play(*[FadeIn(h, shift=DOWN * 0.2) for h in hs], run_time=self.dur(0.7))

            # «¿cuántas condiciones de perpendicularidad tendremos?»
            self.en("cuantas")
            self.pop(cuantas)

            # «Piénsalo un momento»
            self.en("pausa")
            self.play(FadeIn(arena), run_time=self.dur(0.4))

            # «Tres: una por cada muestra»
            self.en("tres_c")
            self.play(FadeOut(cuantas), FadeOut(arena), run_time=0.25)
            self.play(LaggedStart(*[FadeIn(c) for c in conds], lag_ratio=0.3), run_time=self.dur(0.9))
            self.play(*[Create(o) for o in oks], run_time=self.dur(0.5))

            # «Tres ecuaciones y tres incógnitas»
            self.en("sistema")
            self.pop(sis)

            # «Vamos a escribirlas»
            self.en("escribirlas")
            self.play(FadeIn(doc), FadeIn(lap), run_time=self.dur(0.5))

            # «sin saltarnos ninguna cuenta»
            self.en("sin")
            self.sfx("exito")
            self.play(Create(ok), run_time=self.dur(0.4))
