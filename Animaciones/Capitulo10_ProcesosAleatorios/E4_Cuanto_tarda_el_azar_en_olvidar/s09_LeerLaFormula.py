"""Escena 09 — LeerLaFormula: los valores de e^(−2|τ|) y la memoria que se borra."""
from comun.escena import *


class LeerLaFormula(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.tau = np.linspace(-2.6, 2.6, 260)
        self.L = Lienzo(ancho=9.0, alto=2.8, t_rango=(-2.6, 2.6), v_max=1.1, centro=(0.4, -0.9))
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        L, tau = self.L, self.tau
        self.eje = Line(L.p(0, -0.05), L.p(0, 1.1), color=INK, stroke_width=2)
        self.base = L.base()
        self.curva = L.curva(tau, np.exp(-2 * np.abs(tau)), SENAL, 5)
        f = MathTex(r"R_{XX}(\tau)=", r"e^{-2\,", r"|\tau|", r"}", color=TXT).scale(1.6).move_to([0, 2.9, 0])
        f[1].set_color(AMBAR), f[2].set_color(AMBAR), f[3].set_color(AMBAR)
        espejo = L.curva(tau[tau >= 0], np.exp(-2 * tau[tau >= 0]), AMBAR, 6)
        div = MathTex(r"\div\,2{,}718", color=RUIDO).scale(0.9).move_to([-4.6, 1.4, 0])
        div_txt = etiqueta("cada unidad del exponente", INK, 0.45).next_to(div, DOWN, buff=0.1)
        lam = MathTex(r"\lambda = 1", color=AMBAR).scale(1.0).move_to([4.8, 1.4, 0])
        vals = [(0.0, "1"), (0.5, "0,37"), (1.0, "0,14"), (2.0, "0,02")]
        dots = [Dot(L.p(t, float(np.exp(-2 * t))), radius=0.11, color=AMBAR) for t, _ in vals]
        rots = [etiqueta(txt, AMBAR, 0.6, BOLD) for _, txt in vals]
        rots[0].next_to(dots[0], UR, buff=0.12)
        rots[1].next_to(dots[1], UR, buff=0.15)
        rots[2].next_to(dots[2], UR, buff=0.15)
        rots[3].next_to(dots[3], UP, buff=0.35)
        pasos = VGroup(*[DashedLine(L.p(t, 0), L.p(t, float(np.exp(-2 * t))), color=AMBAR, stroke_width=2.5)
                         for t, _ in vals])
        self.f = f
        self.b1_obj = VGroup(div, div_txt, lam, *dots, *rots, pasos, espejo)

        with self.narrar("b1"):
            # «Leamos la fórmula»
            self.en("leer")
            self.play(Write(f), Create(self.base), Create(self.eje), Create(self.curva), run_time=self.dur(1.6))

            # «El valor absoluto»
            self.en("abs")
            self.play(Indicate(f[2], color=AMBAR, scale_factor=1.3), run_time=self.dur(0.9))

            # «hacia delante o hacia atrás»
            self.en("ambos")
            self.add(espejo)
            self.play(Rotate(espejo, angle=PI, axis=UP, about_point=L.p(0, 0)), run_time=self.dur(1.3))
            self.play(FadeOut(espejo), run_time=0.2)

            # «una exponencial negativa»
            self.en("expneg")
            self.play(Indicate(f[1], color=AMBAR, scale_factor=1.15), run_time=self.dur(0.9))

            # «entre dos coma siete uno ocho»
            self.en("divide")
            self.pop(div)
            self.play(FadeIn(div_txt), run_time=0.4)

            # «avanza una unidad»
            self.en("unidad")
            self.play(Indicate(div, color=RUIDO, scale_factor=1.15), run_time=self.dur(1.2))

            # «Con lambda uno»
            self.en("lam1")
            self.pop(lam)

            # «vale uno en cero»
            self.en("v1")
            self.play(Create(pasos[0]), FadeIn(dots[0], scale=0.5), FadeIn(rots[0]), run_time=0.5)

            # «cero coma tres siete»
            self.en("v037")
            self.play(Create(pasos[1]), FadeIn(dots[1], scale=0.5), FadeIn(rots[1]), run_time=0.5)

            # «cero coma uno cuatro»
            self.en("v014")
            self.play(Create(pasos[2]), FadeIn(dots[2], scale=0.5), FadeIn(rots[2]), run_time=0.5)

            # «cero coma cero dos»
            self.en("v002")
            self.play(Create(pasos[3]), FadeIn(dots[3], scale=0.5), FadeIn(rots[3]), run_time=0.5)

    def parte_b2(self):
        L, tau = self.L, self.tau
        # minionda con dos marcas (arriba a la izquierda)
        Lo = Lienzo(ancho=7.0, alto=1.2, t_rango=(0, 6), v_max=1.3, centro=(-2.3, 0.85))
        onda = onda_tel(Lo, CAMBIOS, 1, SENAL, 3.0)
        marcas_a, marcas_b = Lo.vertical(1.0, AMBAR, 3, 0.55), Lo.vertical(1.3, AMBAR, 3, 0.55)
        marcas_c = Lo.vertical(3.6, AMBAR, 3, 0.55)
        lejos_c = Lo.vertical(1.0, AMBAR, 3, 0.55)
        memoria = etiqueta("memoria", AMBAR, 0.8, BOLD).move_to([2.6, 0.9, 0])
        cursor = Dot(L.p(0.15, float(np.exp(-0.3))), radius=0.13, color=AMBAR)
        cambios_ent = marcas_cambio(Lo, [1.7, 2.6, 3.1], AMBAR, 0.2)
        ninguno = etiqueta("sin cambios entre medias", INK, 0.45).move_to([-2.3, 0.0, 0])

        with self.narrar("b2"):
            self.play(FadeOut(self.b1_obj), FadeOut(self.f), run_time=0.2)
            # «La curva cuenta una historia»
            self.en("historia")
            self.resaltar(self.curva, color=AMBAR, escala=1.03)

            # «tau muy pequeño»
            self.en("pequeno")
            self.play(Create(Lo.base()), Create(onda), Create(marcas_a), Create(marcas_b), run_time=self.dur(1.2))

            # «ningún cambio»
            self.en("ninguno")
            self.play(FadeIn(ninguno), run_time=0.4)

            # «se acuerda perfectamente»
            self.en("acuerda")
            self.play(FadeIn(cursor, scale=0.5), run_time=0.4)

            # «más cambios caben»
            self.en("caben")
            self.play(FadeOut(ninguno), FadeOut(marcas_b), run_time=0.3)
            self.play(Create(marcas_c), FadeIn(cambios_ent), run_time=self.dur(0.8))
            self.play(cursor.animate.move_to(L.p(1.3, float(np.exp(-2.6)))), run_time=self.dur(1.0))

            # «dice cada vez menos»
            self.en("menos")
            self.play(cursor.animate.move_to(L.p(1.9, float(np.exp(-3.8)))), run_time=self.dur(1.6))

            # «la memoria del interruptor»
            self.en("memoria")
            self.pop(memoria)

            # «borrándose»
            self.en("borrando")
            self.play(self.curva.animate.set_stroke(opacity=0.45), memoria.animate.set_opacity(0.45),
                      run_time=self.dur(1.4))

            # «A dos segundos»
            self.en("dos_s")
            self.play(cursor.animate.move_to(L.p(2.0, float(np.exp(-4.0)))), run_time=self.dur(1.0))

            # «no queda nada»
            self.en("nada")
            self.resaltar(cursor, color=ROJO, escala=2.2)
