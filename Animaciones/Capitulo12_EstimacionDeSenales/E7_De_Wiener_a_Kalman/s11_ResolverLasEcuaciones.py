"""Escena 11 — Resolver las ecuaciones: invertir cuesta L³, Levinson-Durbin cuesta L²."""
from comun.escena import *


class ResolverLasEcuaciones(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        res = formula("R\\,h", "=", "r", escala=1.2, colores={0: ESTIMACION}).move_to([-3.6, 3.3, 0])
        M = MatrizT([["5", "2,4", "1,44", "0,86"], ["2,4", "5", "2,4", "1,44"],
                     ["1,44", "2,4", "5", "2,4"], ["0,86", "1,44", "2,4", "5"]],
                    centro=(-3.6, 0.9), lado=1.05, escala=0.55)
        cubo = formula("L^3", escala=1.3, colores={0: ERROR}).move_to([3.6, 3.0, 0])
        mil = etiqueta("L = 1.000 → 1.000.000.000", ERROR, 0.5).move_to([3.6, 2.2, 0])
        Lz = Lienzo(ancho=3.6, alto=0.9, t_rango=(0, 1), v_max=1.0, centro=(3.6, 1.0))
        det = Lz.curva(np.linspace(0, 1, 150), 0.8 * np.sin(2 * np.pi * 6 * np.linspace(0, 1, 150)), SENAL, 3.0)
        det_l = etiqueta("casi determinista", INK, 0.42).move_to([3.6, 0.2, 0])
        mal = etiqueta("mal condicionada", ERROR, 0.5).move_to([3.6, -0.55, 0])
        p1 = MathTex("0{,}7386", color=INK).scale(0.8).move_to([3.0, -1.35, 0])
        p2 = MathTex("0{,}7??", color=ERROR).scale(0.8).move_to([3.0, -1.35, 0])
        lev = self.palabra("Levinson-Durbin", AMBAR, 0.6).move_to([3.6, -2.15, 0])
        cuad = formula("L^2", escala=1.3, colores={0: VERDE}).move_to([2.4, -3.0, 0])
        mill = etiqueta("1.000.000", VERDE, 0.5).move_to([4.8, -3.0, 0])
        ords = etiqueta("orden 1 → 2 → 3 → …", AMBAR, 0.5).move_to([-3.6, -2.2, 0])
        tab = VGroup(*[etiqueta(s, TXT, 0.5) for s in ("L = 1: 0,8", "L = 2: 0,7401", "L = 3: 0,7387", "…: 0,7386")]
                     ).arrange(RIGHT, buff=0.5).move_to([-3.0, -3.3, 0])
        with self.narrar("b1"):
            # «resolver las ecuaciones»
            self.en("resolver")
            self.play(FadeIn(res), run_time=self.dur(0.6))
            # «una matriz de ele por ele»
            self.en("matriz")
            self.play(FadeIn(M), run_time=self.dur(0.9))
            # «ele al cubo»
            self.en("cubo")
            self.pop(cubo)
            # «mil millones»
            self.en("mil")
            self.play(FadeIn(mil), run_time=self.dur(0.7))
            # «cerca de ser determinista»
            self.en("determ")
            self.play(Create(Lz.base()), Create(det), FadeIn(det_l), run_time=self.dur(1.0))
            # «mal condicionada»
            self.en("mal")
            self.play(FadeIn(mal), run_time=self.dur(0.5))
            # «se pierde precisión»
            self.en("precision")
            self.play(FadeIn(p1), run_time=0.3)
            self.play(Transform(p1, p2), run_time=self.dur(0.7))
            # «es de Toeplitz»
            self.en("toeplitz")
            self.play(*[M.diag(k).animate.set_color(c) for k, c in ((0, AMBAR), (1, SENAL), (2, MEDIDA), (3, VERDE))],
                      run_time=self.dur(1.0))
            # «Levinson-Durbin»
            self.en("levinson")
            self.pop(lev)
            # «ele al cuadrado»
            self.en("cuad")
            self.pop(cuad)
            # «un millón»
            self.en("millon")
            self.play(FadeIn(mill), run_time=self.dur(0.5))
            # «la solución de todos los órdenes»
            self.en("ordenes")
            self.play(FadeIn(ords), run_time=self.dur(0.6))
            # «la tabla del segundo episodio»
            self.en("tabla")
            self.play(FadeIn(tab), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
