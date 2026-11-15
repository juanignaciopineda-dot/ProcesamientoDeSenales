"""Escena 06 — MediaYSigno: media cero y producto ±1 (mismo signo si el número de cambios es par)."""
from comun.escena import *


class MediaYSigno(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.L = Lienzo(ancho=9.6, alto=2.0, t_rango=(0, 6), v_max=1.3, centro=(0, 2.3))
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        L = self.L
        T1, T2 = 1.6, 3.9
        base = L.base()
        onda = onda_tel(L, CAMBIOS, 1, SENAL, 3.5)
        f_mu = MathTex(r"\mu_X(t)", color=AMBAR).scale(1.3).move_to([-5.0, 0.0, 0])
        f_mu0 = MathTex(r"\mu_X(t) = 0", color=AMBAR).scale(1.3).move_to([-4.6, 0.0, 0])
        b_p = Rectangle(width=0.9, height=1.2, color=SENAL, stroke_width=2).set_fill(SENAL, 0.4)
        b_m = Rectangle(width=0.9, height=1.2, color=RUIDO, stroke_width=2).set_fill(RUIDO, 0.4)
        barras = VGroup(b_p, b_m).arrange(RIGHT, buff=0.7).move_to([3.4, -0.3, 0])
        r_p = etiqueta("+1 · 50 %", TXT, 0.5).next_to(b_p, DOWN, buff=0.1)
        r_m = etiqueta("−1 · 50 %", TXT, 0.5).next_to(b_m, DOWN, buff=0.1)
        f_R = MathTex(r"R_{XX}(\tau)", color=AMBAR).scale(1.3).move_to([-5.0, -1.6, 0])
        c1, c2 = L.vertical(T1, AMBAR, 3, 0.8), L.vertical(T2, AMBAR, 3, 0.8)
        llave = BraceBetweenPoints(L.p(T2, -0.8), L.p(T1, -0.8), color=AMBAR)
        tau = MathTex(r"\tau", color=AMBAR).scale(0.9).next_to(llave, DOWN, buff=0.05)
        p1 = Dot(L.p(T1, nivel_en(T1)), radius=0.13, color=AMBAR)
        p2 = Dot(L.p(T2, nivel_en(T2)), radius=0.13, color=AMBAR)
        f_prod = MathTex(r"x(t)\cdot x(t+\tau)", color=TXT).scale(1.2).move_to([0, -1.0, 0])
        ok = VGroup(MathTex(r"(+1)\cdot(+1)=+1", color=TXT).scale(0.95), tilde(VERDE, 0.45)).arrange(RIGHT, buff=0.3)
        ko = VGroup(MathTex(r"(+1)\cdot(-1)=-1", color=TXT).scale(0.95), cruz(ROJO, 0.45)).arrange(RIGHT, buff=0.3)
        VGroup(ok, ko).arrange(DOWN, buff=0.35).move_to([0, -2.6, 0])
        self.b1 = VGroup(f_mu0, barras, r_p, r_m, f_R, f_prod, ok, ko, llave, tau, c1, c2, p1, p2)

        with self.narrar("b1"):
            # «la media»
            self.en("media")
            self.play(Create(base), Create(onda), run_time=self.dur(0.8))
            self.pop(f_mu)

            # «más uno y menos uno»
            self.en("igual")
            self.play(FadeIn(barras), FadeIn(r_p), FadeIn(r_m), run_time=self.dur(0.6))

            # «no prefieren ningún signo»
            self.en("prefieren")
            self.resaltar(b_p, b_m, color=AMBAR, escala=1.1)

            # «La media es cero»
            self.en("cero")
            self.play(ReplacementTransform(f_mu, f_mu0), run_time=self.dur(0.7))

            # «la autocorrelación»
            self.en("autoc")
            self.pop(f_R)

            # «dos instantes separados tau»
            self.en("dos_inst")
            self.play(Create(c1), Create(c2), run_time=self.dur(0.6))
            self.play(FadeIn(llave), FadeIn(tau), run_time=0.4)

            # «Las dos muestras valen»
            self.en("muestras")
            self.play(FadeIn(p1, scale=0.4), FadeIn(p2, scale=0.4), run_time=0.4)
            self.resaltar(p1, p2, color=AMBAR, escala=1.8)

            # «su producto»
            self.en("producto")
            self.pop(f_prod)

            # «el mismo signo»
            self.en("mismo")
            self.play(FadeIn(ok[0]), FadeIn(ok[1], scale=0.4), run_time=self.dur(0.6))

            # «signos distintos»
            self.en("distintos")
            self.play(FadeIn(ko[0]), FadeIn(ko[1], scale=0.4), run_time=self.dur(0.6))

    def parte_b2(self):
        L = self.L
        # tres casos: 1, 2 y 3 cambios entre dos cortes (minionda en cada columna)
        casos = []
        for x, tiempos in ((-4.6, [0.5]), (0.0, [0.35, 0.65]), (4.6, [0.25, 0.5, 0.75])):
            Lc = Lienzo(ancho=3.4, alto=1.3, t_rango=(0, 1), v_max=1.3, centro=(x, -0.7))
            w = onda_tel(Lc, tiempos, 1, SENAL, 3.5)
            a, b = Lc.vertical(0.05, AMBAR, 2.5, 0.7), Lc.vertical(0.95, AMBAR, 2.5, 0.7)
            nb = len(tiempos) % 2 == 0
            pa = Dot(Lc.p(0.05, 1), radius=0.1, color=AMBAR)
            pb = Dot(Lc.p(0.95, 1 if nb else -1), radius=0.1, color=AMBAR)
            marcas = marcas_cambio(Lc, tiempos, AMBAR, 0.18)
            casos.append((VGroup(Lc.base(), w, a, b, pa, pb, marcas), nb, Lc))
        pregunta = etiqueta("¿mismo signo?", AMBAR, 0.8, BOLD).move_to([0, 1.0, 0])
        verdes = [VGroup(etiqueta(f"{n} cambio" + ("s" if n > 1 else ""), INK, 0.5),
                         ) for n in (1, 2, 3)]
        for g, (caso, nb, Lc) in zip(verdes, casos):
            g.next_to(caso, DOWN, buff=0.5)
        marcos = [SurroundingRectangle(caso, color=VERDE if nb else ROJO, buff=0.2, stroke_width=3)
                  for caso, nb, _ in casos]
        t_par = etiqueta("par: mismo signo", VERDE, 0.6, BOLD).move_to([0, -3.3, 0])
        t_imp = etiqueta("impar: signos distintos", ROJO, 0.6, BOLD).move_to([0.0, -3.7, 0])
        t_par.move_to([0, -3.3, 0])
        t_imp.move_to([0, -3.75, 0])
        coin = BraceBetweenPoints(L.p(3.9, 1.05), L.p(1.6, 1.05), color=VERDE)
        coin.shift(UP * 0.05)

        with self.narrar("b2"):
            self.play(FadeOut(self.b1), run_time=0.2)
            # «¿Cuándo tienen el mismo signo?»
            self.en("cuando")
            self.pop(pregunta)

            # «le da la vuelta»
            self.en("vuelta")
            self.resaltar(casos[0][0][1], color=AMBAR, escala=1.0)

            # «Con un cambio»
            self.en("uno")
            self.play(FadeIn(casos[0][0]), FadeIn(verdes[0]), run_time=self.dur(0.7))
            self.play(FadeIn(cruz(ROJO, 0.45).next_to(casos[0][0], UP, buff=0.1)), run_time=0.3)

            # «Con dos»
            self.en("dos")
            self.play(FadeIn(casos[1][0]), FadeIn(verdes[1]), run_time=self.dur(0.7))
            self.play(FadeIn(tilde(VERDE, 0.45).next_to(casos[1][0], UP, buff=0.1)), run_time=0.3)

            # «Con tres»
            self.en("tres")
            self.play(FadeIn(casos[2][0]), FadeIn(verdes[2]), run_time=self.dur(0.7))
            self.play(FadeIn(cruz(ROJO, 0.45).next_to(casos[2][0], UP, buff=0.1)), run_time=0.3)

            # «al revés otra vez»
            self.en("otra_vez")
            self.resaltar(casos[2][0][1], color=ROJO, escala=1.0)

            # «las dos muestras coinciden»
            self.en("coin")
            self.play(FadeIn(coin), run_time=self.dur(0.5))

            # «un número par»
            self.en("par")
            self.play(Create(marcos[1]), FadeIn(t_par), run_time=self.dur(0.6))

            # «un número impar»
            self.en("impar")
            self.play(Create(marcos[0]), Create(marcos[2]), FadeIn(t_imp), run_time=self.dur(0.6))
