"""Escena 17 — Ejemplo con números: varianzas 6 y 4, covarianza 3, Z = 2X − 3Y."""
from comun.escena import *


class EjemploSeisCuatroTres(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def bloque1(self):
        G = formula(r"\sigma_Z^2", "=", r"\alpha^2\sigma_X^2", "+", r"\beta^2\sigma_Y^2", "+", r"2\alpha\beta\,\sigma_{XY}",
                    escala=1.2, colores={0: AMBAR, 2: SENAL, 4: MEDIDA, 6: AMBAR}).move_to([0, 3.2, 0])
        self.gen = G
        v6 = formula(r"\sigma_X^2", "=", "6", escala=1.4, colores={0: SENAL}).move_to([-5.0, 1.7, 0])
        v4 = formula(r"\sigma_Y^2", "=", "4", escala=1.4, colores={0: MEDIDA}).move_to([-5.0, 0.5, 0])
        c3 = formula(r"\sigma_{XY}", "=", "3", escala=1.4, colores={0: AMBAR}).move_to([-5.0, -0.7, 0])
        z = formula("Z", "=", "2", "X", "-", "3", "Y", escala=1.4,
                    colores={2: AMBAR, 3: SENAL, 5: AMBAR, 6: MEDIDA}).move_to([-4.9, -2.1, 0])
        p1 = formula(r"2^2\cdot 6", "=", "24", escala=1.4, colores={2: VERDE}).move_to([1.6, 1.7, 0])
        p2 = formula(r"(-3)^2\cdot 4", "=", "36", escala=1.4, colores={2: VERDE}).move_to([1.6, 0.5, 0])
        p3 = formula(r"2\cdot 2\cdot(-3)\cdot 3", "=", "-36", escala=1.4, colores={2: ROJO}).move_to([1.6, -0.7, 0])
        tot = formula("24", "+", "36", "-", "36", "=", "24", escala=1.7, colores={6: AMBAR}).move_to([1.6, -2.3, 0])
        for p in (p1, p2, p3):
            p.align_to([-1.0, 0, 0], LEFT)
        for m in (p1, p2, p3, tot):
            oculta(m)
            self.add(m)
        self.p3, self.datos = p3, VGroup(v6, v4, c3, z, p1, p2, tot)
        with self.narrar("b1"):
            # «Un ejemplo con números»
            self.en("ejemplo")
            self.play(FadeIn(G, shift=DOWN * 0.2), run_time=self.dur(0.7))

            # «la varianza de equis es seis»
            self.en("v6")
            self.play(FadeIn(v6, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «la de i griega es cuatro»
            self.en("v4")
            self.play(FadeIn(v4, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «su covarianza es tres»
            self.en("c3")
            self.play(FadeIn(c3, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «dos equis menos tres i griega»
            self.en("z")
            self.play(FadeIn(z, shift=RIGHT * 0.2), run_time=self.dur(0.7))

            # «Primer término»
            self.en("p1")
            self.resaltar(G[2], escala=1.15)
            self.play(*revelar(p1[0]), run_time=self.dur(0.6))

            # «veinticuatro»
            self.en("r24a")
            self.play(*revelar(p1[1], p1[2]), run_time=self.dur(0.4))

            # «Segundo»
            self.en("p2")
            self.resaltar(G[4], escala=1.15)
            self.play(*revelar(p2[0]), run_time=self.dur(0.6))

            # «treinta y seis»
            self.en("r36")
            self.play(*revelar(p2[1], p2[2]), run_time=self.dur(0.4))

            # «Término cruzado»
            self.en("p3")
            self.resaltar(G[6], escala=1.15)
            self.play(*revelar(p3[0]), run_time=self.dur(0.8))

            # «menos treinta y seis»
            self.en("rm36")
            self.play(*revelar(p3[1], p3[2]), run_time=self.dur(0.4))

            # «En total, veinticuatro»
            self.en("total")
            self.play(LaggedStart(*revelar(*tot), lag_ratio=0.15), run_time=self.dur(1.2))
            self.caja_tot = SurroundingRectangle(tot, color=AMBAR, buff=0.2, stroke_width=3)
            self.play(Create(self.caja_tot), run_time=self.dur(0.4))

    def bloque2(self):
        t = np.linspace(0, 1, 200)
        u1 = np.sin(2 * np.pi * 1.5 * t) + 0.25 * np.sin(2 * np.pi * 5 * t)
        u2 = 0.9 * u1 + 0.12 * serie(7, 200, 0.0)
        L1 = Lienzo(ancho=3.6, alto=1.5, t_rango=(0, 1), v_max=1.6, centro=(-4.4, -2.6))
        L2 = Lienzo(ancho=3.6, alto=1.5, t_rango=(0, 1), v_max=1.6, centro=(0.3, -2.6))
        cx, cy = L1.curva(t, u1, SENAL, 3), L1.curva(t, u2, MEDIDA, 3)
        cd = L2.curva(t, u1 - u2, ESTIMACION, 3)
        with self.narrar("b2"):
            # «Fíjate en el signo»
            self.en("signo")
            self.play(FadeOut(self.datos), FadeOut(self.caja_tot), self.p3.animate.move_to([0, 1.2, 0]).scale(1.2), run_time=self.dur(0.6))

            # «La covarianza es positiva»
            self.en("pos")
            pos = formula(r"\sigma_{XY}", "=", "+3", escala=1.6, colores={0: AMBAR, 2: VERDE}).move_to([-4.4, -0.5, 0])
            self.play(FadeIn(pos), run_time=self.dur(0.5))

            # «suelen subir juntas»
            self.en("juntas")
            self.play(Create(L1.base()), Create(cx), Create(cy), run_time=self.dur(1.0))

            # «al restarlas»
            self.en("restarlas")
            rs = formula("X", "-", "Y", escala=1.6, colores={0: SENAL, 2: MEDIDA}).move_to([0.3, -0.5, 0])
            self.play(FadeIn(rs), run_time=self.dur(0.5))

            # «sus movimientos se compensan»
            self.en("compensa")
            self.play(Create(L2.base()), Create(cd), run_time=self.dur(0.9))

            # «el término cruzado resta»
            self.en("resta")
            self.resaltar(self.p3, color=ROJO, escala=1.1, run_time=0.6)

            # «Y otra cosa»
            self.en("otra")
            self.resaltar(self.gen, color=AMBAR, escala=1.05)

            # «dos cuadrados y un término cruzado»
            self.en("tres_t")
            tt = formula("a^2", "+", "b^2", "+", "2ab", escala=1.6, colores={0: SENAL, 2: MEDIDA, 4: AMBAR}).move_to([4.6, -0.5, 0])
            self.play(FadeIn(tt, shift=UP * 0.2), run_time=self.dur(0.7))

            # «te suena de otro sitio»
            self.en("suena")
            q = Text("?", color=AMBAR, weight=BOLD).scale(3.0).move_to([4.6, -2.6, 0])
            self.pop(q)

            # «No es casualidad»
            self.en("casualidad2")
            self.play(Create(SurroundingRectangle(self.gen, color=AMBAR, buff=0.2, stroke_width=3)), run_time=self.dur(0.6))
