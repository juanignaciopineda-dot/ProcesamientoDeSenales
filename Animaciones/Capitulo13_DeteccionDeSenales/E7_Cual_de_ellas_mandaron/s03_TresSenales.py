"""Escena 03 — Decidir entre varias señales: tres señales posibles y la derivación con M hipótesis."""
from comun.escena import *

VALS = [(1, 1, 0, 0), (0, 0, 1, 1), (1, -1, 0, 0)]
COLS = [SENAL, AZUL_C7, CIAN]
TXTS = [r"(1,\,1,\,0,\,0)", r"(0,\,0,\,1,\,1)", r"(1,\,-1,\,0,\,0)"]
XS = [-4.4, 0.0, 4.4]


class TresSenales(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.tres()
        self.wait(0.6)
        self.derivacion()
        self.wait(1.0)
        self.limpiar()

    def tres(self):
        mod = modem7(INK).scale(0.9).move_to([-5.6, 2.9, 0])
        c_hay = caja("hay señal", SENAL, ancho=3.2, alto=0.9, scale=0.6).move_to([-2.0, 2.9, 0])
        c_no = caja("no hay", INK, ancho=3.2, alto=0.9, scale=0.6).move_to([1.8, 2.9, 0])
        t1, t2 = tachar(c_hay), tachar(c_no)
        minis = VGroup(*[pulso7(v, centro=(-2.4 + 2.4 * i, 2.9), color=COLS[i], paso=0.4, unidad=0.4)
                         for i, v in enumerate(VALS)])
        letras = VGroup(*[Text(str(i), color=INK).scale(0.5).move_to([-2.4 + 2.4 * i, 2.15, 0]) for i in range(3)])
        cuadros = [RoundedRectangle(corner_radius=0.12, width=3.6, height=2.0, color=COLS[i], stroke_width=2.5)
                   .set_fill(COLS[i], 0.06).move_to([XS[i], 0.0, 0]) for i in range(3)]
        divs = VGroup(*[Line([XS[i] + d, -0.9, 0], [XS[i] + d, 0.9, 0], color=INK, stroke_width=1.5, stroke_opacity=0.6)
                        for i in range(3) for d in (-0.9, 0.0, 0.9)])
        Es = VGroup(*[MathTex("E=2", color=AMBAR).scale(0.8).move_to([XS[i] + 1.1, 1.45, 0]) for i in range(3)])
        tall = [pulso7(VALS[i], centro=(XS[i], 0.0), color=COLS[i], paso=0.9, unidad=0.7) for i in range(3)]
        rot = [MathTex(f"s_{i}", "=", TXTS[i], color=COLS[i]).scale(0.8).move_to([XS[i], -1.5, 0]) for i in range(3)]
        hip = VGroup(*[MathTex(f"H_{i}", color=TXT).scale(0.8).move_to([XS[i] - 1.3, 1.45, 0]) for i in range(3)])
        form = formula("r", "=", "s_i", "+", "v", escala=0.9, colores={0: MEDIDA, 2: SENAL, 4: RUIDO}).move_to([-2.4, -2.8, 0])
        Lr = Lienzo(ancho=2.6, alto=0.7, t_rango=(0, 4), v_max=1.0, centro=(1.6, -2.8))
        ruido = ruido_t(Lr, semilla=4, amp=0.5, color=RUIDO)
        with self.narrar("b1"):
            # «Un módem»
            self.paso("modem", mod, t=0.5)
            # «no decide entre»
            self.en("nodecide")
            self.play(FadeIn(c_hay), FadeIn(c_no), run_time=0.4)
            self.play(Create(t1), Create(t2), run_time=self.dur(0.4))
            # «varias señales posibles»
            self.en("varias")
            self.play(FadeOut(c_hay), FadeOut(c_no), FadeOut(t1), FadeOut(t2), FadeIn(minis), run_time=self.dur(0.6))
            # «una por cada símbolo»
            self.paso("simbolo", letras, t=0.5)
            # «Tomemos tres»
            self.en("tres")
            self.play(FadeOut(minis), FadeOut(letras),
                      *[FadeIn(c) for c in cuadros], run_time=self.dur(0.6))
            # «de cuatro muestras cada una»
            self.paso("cuatro", divs, t=0.5)
            # «energía dos»
            self.paso("energia", Es, t=0.5)
            # «uno, uno, cero, cero»
            self.paso("s0", tall[0], rot[0], t=0.6)
            # «cero, cero, uno, uno»
            self.paso("s1", tall[1], rot[1], t=0.6)
            # «uno, menos uno, cero, cero»
            self.paso("s2", tall[2], rot[2], t=0.6)
            # «Bajo cada hipótesis»
            self.paso("hip", hip, t=0.5)
            # «esa señal más ruido»
            self.en("masruido")
            self.play(FadeIn(form), Create(ruido), run_time=self.dur(0.8))
        self.corte()

    def derivacion(self):
        et = etiqueta("la derivación", INK, 0.55).move_to([-5.0, 3.35, 0])
        ep = caja("episodio 2", AMBAR, ancho=2.2, alto=0.55, scale=0.4).move_to([-2.5, 3.35, 0])
        L1 = formula("p_i", r"\,f(r\mid H_i)", r"\qquad i=0,1,2", escala=1.0,
                     colores={0: AMBAR, 1: MEDIDA}).move_to([-0.8, 2.5, 0])
        L2 = formula(r"\ln p_i", r"-\frac{1}{2\sigma^2}", r"\sum (r-s_i)^2", escala=1.0,
                     colores={0: AMBAR}).move_to([-0.8, 1.2, 0])
        L3 = formula(r"\ln p_i", r"-\frac{1}{2\sigma^2}", r"\Big[", r"\sum r^2", r"-2\sum r\,s_i", "+E_i", r"\Big]",
                     escala=1.0, colores={0: AMBAR, 3: MEDIDA, 4: SENAL}).move_to([-0.8, -0.2, 0])
        caja_r2 = SurroundingRectangle(L3[3], color=AMBAR, buff=0.08, stroke_width=3)
        caja_r2.permitir_encima = True
        llave_c = Brace(L3[3], DOWN, color=INK)
        com = etiqueta("común a las tres", INK, 0.45).next_to(llave_c, DOWN, buff=0.08)
        tach = tachar(L3[3])
        marco = etiqueta("elegir la i que maximice", AMBAR, 0.55, BOLD).move_to([0, -1.6, 0])
        R = formula(r"\sum r\,s_i", r"+\sigma^2\ln p_i", r"-\frac{E_i}{2}", escala=1.3,
                    colores={0: MEDIDA, 1: AMBAR, 2: SENAL}).move_to([0, -2.7, 0])
        with self.narrar("b2"):
            # «Repetimos la derivación»
            self.paso("repetimos", et, t=0.5)
            # «segundo episodio»
            self.paso("segundo", ep, t=0.4)
            # «las densidades escaladas por sus priors»
            self.paso("densidades", L1, t=0.7)
            # «tomamos logaritmos»
            self.paso("logs", L2, t=0.7)
            # «desarrollamos el cuadrado»
            self.paso("cuadrado", L3, t=0.8)
            # «la suma de cuadrados de lo recibido»
            self.en("sumacuad")
            self.play(Create(caja_r2), run_time=self.dur(0.5))
            # «común a todas las hipótesis»
            self.en("comun")
            self.play(FadeIn(llave_c), FadeIn(com), run_time=self.dur(0.6))
            # «se cancela»
            self.en("cancela")
            self.play(Create(tach), run_time=self.dur(0.5))
            # «Queda»
            self.en("queda")
            self.play(FadeOut(llave_c), FadeOut(com), run_time=self.dur(0.4))
            # «elegir la hipótesis que maximice»
            self.paso("maximice", marco, t=0.5)
            # «la suma de recibido por señal»
            self.paso("rs", R[0], t=0.5)
            # «más sigma cuadrado por el logaritmo de su prior»
            self.paso("prior", R[1], t=0.6)
            # «menos su energía entre dos»
            self.paso("mediaenergia", R[2], t=0.6)
