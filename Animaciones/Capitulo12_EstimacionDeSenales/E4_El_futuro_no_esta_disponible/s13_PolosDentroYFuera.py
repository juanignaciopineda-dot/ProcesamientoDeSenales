"""Escena 13 — Un polo dentro del círculo unidad decae y uno fuera explota; (2, 1) y (1, 2) del Cap. 11."""
from comun.escena import *

C = (-3.9, 1.0)      # centro del plano z
R = 1.1              # radio del círculo unidad


def en_z(x: float) -> np.ndarray:
    return np.array([C[0] + x * R, C[1], 0.0])


class PolosDentroYFuera(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        pl = plano_c(C, R)
        polo = MathTex(r"\times", color=AMBAR).scale(1.1).move_to(en_z(0.6))
        l06 = MathTex("0{,}6", color=AMBAR).scale(0.6).move_to(en_z(0.6) + DOWN * 0.4)
        b1 = Tallos([1, 0.6, 0.36, 0.22, 0.13], centro=(3.0, -0.6), paso=0.8, unidad=1.6, color=AMBAR)
        polo2 = MathTex(r"\times", color=ERROR).scale(1.1).move_to(en_z(2.0))
        l2 = MathTex("2", color=ERROR).scale(0.6).move_to(en_z(2.0) + DOWN * 0.4)
        b2 = Tallos([1, 2, 4, 8], centro=(3.0, -0.6), paso=0.9, unidad=0.28, color=ERROR)
        cap = caja("Cap. 11", INK, ancho=1.8, alto=0.6, scale=0.45).move_to([6.0, 3.4, 0])
        f1 = formula(r"\frac{2+z^{-1}}{\sqrt5}", escala=0.9, colores={0: AMBAR}).move_to([-3.2, -2.9, 0])
        f2 = formula(r"\frac{1+2z^{-1}}{\sqrt5}", escala=0.9, colores={0: ROJO}).move_to([3.2, -2.9, 0])
        cero1 = Circle(radius=0.12, color=VERDE, stroke_width=4).move_to(en_z(-0.5))
        cero2 = Circle(radius=0.12, color=ROJO, stroke_width=4).move_to(en_z(-2.0))
        l_c1 = MathTex("-0{,}5", color=VERDE).scale(0.55).move_to(en_z(-0.5) + DOWN * 0.4)
        l_c2 = MathTex("-2", color=ROJO).scale(0.55).move_to(en_z(-2.0) + DOWN * 0.4)
        i1 = Tallos([0.5, -0.25, 0.125], centro=(3.0, 0.6), paso=0.9, unidad=1.6, color=VERDE)
        i2 = Tallos([1, -2, 4, -8], centro=(3.0, 0.6), paso=0.9, unidad=0.2, color=ERROR)
        with self.narrar("b1"):
            # «El polo es la base de la caída»
            self.en("base")
            self.play(FadeIn(pl), FadeIn(polo), FadeIn(l06), run_time=self.dur(0.8))

            # «menor que uno»
            self.en("menor")
            self.resaltar(polo, run_time=self.dur(0.5))

            # «dentro del círculo unidad»
            self.en("circulo")
            self.play(pl.circ.animate.set_stroke(AMBAR, opacity=1.0, width=5), run_time=self.dur(0.6))

            # «los coeficientes se apagan»
            self.en("apagan")
            self.play(FadeIn(b1.base), LaggedStart(*[GrowFromEdge(t, DOWN) for t in b1.tallos], lag_ratio=0.2),
                      *[FadeIn(p) for p in b1.puntos], run_time=self.dur(1.0))

            # «si fuera dos»
            self.en("dos")
            self.play(FadeIn(polo2), FadeIn(l2), run_time=self.dur(0.5))
            self.sfx("tick")

            # «uno, dos, cuatro, ocho»
            self.en("explotan")
            self.play(FadeOut(b1), run_time=0.3)
            self.play(FadeIn(b2.base), LaggedStart(*[GrowFromEdge(t, DOWN) for t in b2.tallos], lag_ratio=0.25),
                      *[FadeIn(p) for p in b2.puntos], run_time=self.dur(1.2))

            # «Así se entiende el capítulo once»
            self.en("cap11")
            self.play(FadeOut(b2), FadeOut(polo), FadeOut(polo2), FadeOut(l06), FadeOut(l2), FadeIn(cap),
                      run_time=self.dur(0.5))

            # «Dos más zeta a la menos uno»
            self.en("f1")
            self.play(FadeIn(f1, shift=UP * 0.15), run_time=self.dur(0.6))

            # «su cero en menos un medio»
            self.en("cero1")
            self.play(FadeIn(cero1), FadeIn(l_c1), run_time=self.dur(0.5))

            # «su inverso se apaga»
            self.en("inv1")
            self.play(FadeIn(i1), run_time=self.dur(0.8))

            # «Uno más dos zeta a la menos uno»
            self.en("f2")
            self.play(FadeOut(i1), FadeIn(f2, shift=UP * 0.15), FadeIn(cero2), FadeIn(l_c2), run_time=self.dur(0.7))

            # «su inverso explota»
            self.en("inv2")
            self.play(FadeIn(i2), run_time=self.dur(0.9))

        self.wait(1.0)
        self.limpiar()
