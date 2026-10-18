"""Escena 15 — Combinaciones de variables: Z = αX + βY y su media."""
from comun.escena import *


class MediaDeLaCombinacion(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        t = np.linspace(0, 1, 200)
        ruido = 0.35 * serie(3, 200, 0.0)
        s = np.sin(2 * np.pi * 2 * t)
        Ls = [Lienzo(ancho=2.6, alto=1.1, t_rango=(0, 1), v_max=1.2, centro=(cx, 2.6)) for cx in (-4.8, -0.8, 3.2)]
        c1 = Ls[0].curva(t, s, SENAL, 3)
        c2 = Ls[1].curva(t, ruido * 1.5, RUIDO, 3)
        c3 = Ls[2].curva(t, s + ruido, MEDIDA, 3)
        mas = MathTex("+", color=TXT).scale(1.5).move_to([-2.8, 2.6, 0])
        igual = MathTex("=", color=TXT).scale(1.5).move_to([1.2, 2.6, 0])
        r2 = formula("(", "M_1", "+", "M_2", ")", "/", "2", escala=1.6, colores={1: MEDIDA, 3: MEDIDA}).move_to([-2.0, 0.9, 0])
        r3 = formula("S_1", "-", "S_2", escala=1.6, colores={0: SENAL, 2: SENAL}).move_to([-2.0, -0.6, 0])
        mv = VGroup(formula(r"\mu_Z", "?", escala=1.5, colores={0: AMBAR, 1: ROJO}),
                    formula(r"\sigma_Z^2", "?", escala=1.5, colores={0: AMBAR, 1: ROJO})).arrange(RIGHT, buff=1.4)
        mv.move_to([0, -2.3, 0])
        Z = formula("Z", "=", r"\alpha", "X", "+", r"\beta", "Y", escala=2.0,
                    colores={0: AMBAR, 2: AMBAR, 3: SENAL, 5: AMBAR, 6: MEDIDA}).move_to([0, 1.7, 0])
        M = formula(r"\mu_Z", "=", r"\alpha", r"\mu_X", "+", r"\beta", r"\mu_Y", escala=2.0,
                    colores={0: AMBAR, 2: AMBAR, 3: SENAL, 5: AMBAR, 6: MEDIDA}).move_to([0, -0.7, 0])
        oculta(M)
        self.add(M)
        with self.narrar("b1"):
            # «combinamos variables»
            self.en("combinar")
            self.play(Create(c1), Create(c2), FadeIn(mas), run_time=self.dur(0.9))

            # «la señal más el ruido»
            self.en("sr")
            self.play(FadeIn(igual), Create(c3), run_time=self.dur(0.8))

            # «el promedio de dos medidas»
            self.en("prom")
            self.play(FadeIn(r2, shift=UP * 0.2), run_time=self.dur(0.6))

            # «la diferencia entre dos sensores»
            self.en("dif_s")
            self.play(FadeIn(r3, shift=UP * 0.2), run_time=self.dur(0.6))

            # «Así que conviene saber»
            self.en("conviene")
            self.resaltar(r2, r3, color=AMBAR, escala=1.1)

            # «la media y la varianza»
            self.en("m_v")
            self.play(FadeIn(mv, shift=UP * 0.2), run_time=self.dur(0.7))

            # «zeta igual a alfa por equis más beta por i griega»
            self.en("zeta")
            self.play(*[FadeOut(m) for m in list(self.mobjects) if m not in (M, self.camera.frame)], run_time=0.3)
            oculta(Z)
            self.add(Z)
            self.play(LaggedStart(*revelar(*Z), lag_ratio=0.2), run_time=self.dur(2.4))

            # «La media es fácil»
            self.en("facil")
            self.play(*revelar(M[0], M[1]), run_time=self.dur(0.5))

            # «por linealidad»
            self.en("lineal2")
            lin = Text("Por linealidad", color=INK, slant=ITALIC).scale(0.7).move_to([4.6, -0.7, 0])
            lin.move_to([0, -2.1, 0])
            self.play(FadeIn(lin, shift=UP * 0.2), run_time=self.dur(0.6))

            # «alfa por la media de equis»
            self.en("a_mx")
            self.play(*revelar(M[2], M[3]), run_time=self.dur(0.6))

            # «más beta por la media de i griega»
            self.en("b_my")
            self.play(*revelar(M[4], M[5], M[6]), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
