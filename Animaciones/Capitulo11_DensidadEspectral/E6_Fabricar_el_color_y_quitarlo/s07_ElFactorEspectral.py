"""Escena 07 — El filtro modelador, el factor espectral y la demostración del teorema de Bochner."""
from comun.escena import *


class ElFactorEspectral(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        blq = BloqueLTI("H", centro=(0, 1.4), ancho=1.9, alto=1.2, largo=1.6, color=CIAN)
        t_mod = self.palabra("modelador", AMBAR, 1.0).move_to([0, 3.4, 0])
        Ei = Lienzo(ancho=2.4, alto=1.3, t_rango=(-3, 3), v_max=1.5, centro=(-5.3, 1.4))
        plano = Ei.curva([-3, 3], [1, 1], AMBAR, 5)
        Eo = Lienzo(ancho=2.4, alto=1.5, t_rango=(-3, 3), v_max=1.5, centro=(5.3, 1.4))
        forma = curva_f(Eo, lambda w: 0.25 + 1.0 * np.exp(-(np.asarray(w) / 1.2) ** 2), -3, 3, AMBAR, 5)
        F = formula("|H|", "=", r"\sqrt{D_{xx}}", escala=1.3, colores={0: AMBAR}).move_to([0, -0.3, 0])
        t_fac = etiqueta("factor espectral", AMBAR, 0.7).move_to([0, -1.4, 0])
        ok = tilde(VERDE, 0.6).move_to([3.0, -1.4, 0])
        E = Lienzo(ancho=4.4, alto=1.4, t_rango=(-6, 6), v_max=1.2, centro=(-3.5, -2.9))
        ej = ejes_L(E, 0, 1.2)
        c = curva_f(E, psd_tele, -6, 6, AMBAR, 4)
        t_pos = MathTex(r"D_{xx}\geq 0", color=AMBAR).scale(0.8).move_to([-3.5, -1.9, 0])
        cr = curva_f(E, lambda w: np.sqrt(psd_tele(w)), -6, 6, CIAN, 4)
        with self.narrar("b1"):
            # «modelador»
            self.en("modelador")
            self.play(FadeIn(blq), run_time=self.dur(0.5))
            self.pop(t_mod)

            # «le da forma al espectro plano del blanco»
            self.en("forma")
            self.play(Create(plano), run_time=0.5)
            self.play(Create(forma), run_time=self.dur(0.8))

            # «una especie de raíz cuadrada de la densidad»
            self.en("raiz")
            self.play(FadeIn(F), run_time=self.dur(1.0))

            # «factor espectral»
            self.en("factor")
            self.pop(t_fac)

            # «Siempre existe»
            self.en("existe")
            self.pop(ok)

            # «la densidad nunca es negativa»
            self.en("nunca")
            self.play(Create(ej), Create(c), FadeIn(t_pos), run_time=self.dur(1.0))

            # «se le puede sacar la raíz»
            self.en("sacar")
            self.play(Create(cr), run_time=self.dur(1.0))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        boch = self.palabra("Bochner", AMBAR, 1.0).move_to([-4.6, 3.3, 0])
        filas = VGroup(*[VGroup(tilde(VERDE, 0.4), etiqueta(s, TXT, 0.65)).arrange(RIGHT, buff=0.3)
                         for s in ("real", "par", "no negativa")]).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([-4.6, 1.5, 0])
        cproc = caja("proceso", RUIDO, ancho=2.4, alto=1.0, scale=0.6).move_to([3.4, 1.5, 0])
        a_proc = flecha([-2.3, 1.5, 0], [2.1, 1.5, 0], INK, 3)
        demo = etiqueta("la demostración", AMBAR, 0.75).move_to([0, 3.3, 0])

        Ea = Lienzo(ancho=2.4, alto=1.3, t_rango=(-6, 6), v_max=1.2, centro=(-5.3, -2.0))
        ca = curva_f(Ea, psd_tele, -6, 6, AMBAR, 4)
        cr = curva_f(Ea, lambda w: np.sqrt(psd_tele(w)), -6, 6, CIAN, 4)
        blq = BloqueLTI("H", centro=(-0.3, -2.0), ancho=1.6, alto=1.0, largo=1.2, color=CIAN)
        a_h = flecha([-3.8, -2.0, 0], [-2.3, -2.0, 0], INK, 3)
        tira = tira_pm1([1, -1, 1, 1, -1], lado=0.5).move_to([-1.5, -0.6, 0])
        a_t = flecha([-1.5, -0.95, 0], [-1.5, -1.6, 0], INK, 3)
        Ls = Lienzo(ancho=3.6, alto=1.3, t_rango=(0, 3), v_max=1.0, centro=(4.6, -2.0))
        sale = traza(Ls.x(np.linspace(0, 3, 150)), Ls.y(0.8 * serie(5, 150, 0.9)), RUIDO, 3.5)
        ok = tilde(VERDE, 0.5).move_to([6.6, -0.9, 0])
        ciclo = VGroup(*[Arrow([-1.2 + i * 1.3, -3.5, 0], [-0.1 + i * 1.3, -3.5, 0], color=INK, buff=0, stroke_width=3,
                               max_tip_length_to_length_ratio=0.25) for i in range(3)])
        with self.narrar("b2"):
            # «teorema de Bochner»
            self.en("bochner")
            self.corte()
            self.pop(boch)

            # «real, par y no negativa»
            self.en("tres")
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in filas], lag_ratio=0.4), run_time=self.dur(1.6))

            # «la densidad de algún proceso»
            self.en("proceso")
            self.play(GrowArrow(a_proc), FadeIn(cproc), run_time=self.dur(0.7))

            # «La demostración es exactamente esto»
            self.en("demo")
            self.pop(demo)

            # «Le sacas la raíz»
            self.en("raiz")
            self.play(Create(ca), run_time=0.5)
            self.play(ReplacementTransform(ca, cr), run_time=self.dur(0.8))

            # «construyes el filtro»
            self.en("filtro")
            self.play(GrowArrow(a_h), FadeIn(blq), run_time=self.dur(0.7))

            # «le metes ruido blanco»
            self.en("blanco")
            self.play(FadeIn(tira), GrowArrow(a_t), run_time=self.dur(0.7))

            # «lo que sale es ese proceso»
            self.en("sale")
            self.play(Create(Ls.base()), Create(sale), run_time=self.dur(1.0), rate_func=linear)
            self.pop(ok)

            # «Cada vez que se colorea un ruido»
            self.en("colorea")
            self.play(LaggedStart(*[GrowArrow(a) for a in ciclo], lag_ratio=0.4), run_time=self.dur(1.2))

            # «ejecutando la demostración»
            self.en("ejecuta")
            self.resaltar(blq, color=AMBAR)
            self.play(demo.animate.set_color(VERDE), run_time=0.4)
