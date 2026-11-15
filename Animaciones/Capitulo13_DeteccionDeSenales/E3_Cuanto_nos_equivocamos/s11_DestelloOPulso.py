"""Escena 11 — El pulso (2, 2, 1) y un destello (3, 0, 0), ambos de energía 9: mismo error."""
from comun.escena import *


class DestelloOPulso(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.pregunta()
        self.cuenta_del_destello()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def pregunta(self):
        f1 = formula("P_{FA}", "=", "Q", "(", r"\frac{\gamma}{\sigma\sqrt{E}}", ")", escala=1.0,
                     colores={0: ERROR}).move_to([-2.4, 3.0, 0])
        f2 = formula("P_M", "=", "Q", "(", r"\frac{E-\gamma}{\sigma\sqrt{E}}", ")", escala=1.0,
                     colores={0: ERROR}).move_to([-2.4, 1.6, 0])
        f3 = formula("P_D", "=", "Q", "(", "Q^{-1}", "(", "P_{FA}", ")", "-", "d", ")", escala=0.95,
                     colores={0: VERDE, 6: ERROR}).move_to([-2.0, 0.3, 0])
        e_sol = MathTex("E", color=SENAL).scale(1.8).move_to([4.2, 2.6, 0])
        s_sol = MathTex(r"\sigma^2", color=RUIDO).scale(1.8).move_to([6.0, 2.6, 0])
        muestras = formula("s[0],\\ s[1],\\ s[2]", escala=0.9, colores={0: SENAL}).move_to([5.3, 0.8, 0])
        tacha = Line(muestras.get_corner(DL) + DL * 0.05, muestras.get_corner(UR) + UR * 0.05, color=ERROR, stroke_width=6)
        rel = reloj(TXT).scale(1.2).move_to([5.3, -0.9, 0])
        pa = Barras((2, 2, 1), centro=(-3.2, -1.6), paso=1.2, unidad=0.5, color=SENAL, nums=True)
        pb = Barras((3, 0, 0), centro=(3.2, -1.6), paso=1.2, unidad=0.5, color=SENAL, nums=True)
        nueve1 = formula("E", "=", "9", escala=1.0, colores={0: SENAL, 2: AMBAR}).move_to([-3.2, -3.1, 0])
        nueve2 = formula("E", "=", "9", escala=1.0, colores={0: SENAL, 2: AMBAR}).move_to([3.2, -3.1, 0])
        cual = self.palabra("¿cuál?", AMBAR, 1.4).move_to([0, -1.2, 0])

        with self.narrar("b1"):
            # «en todas las fórmulas»
            self.en("formulas")
            self.play(*[FadeIn(f, shift=RIGHT * 0.2) for f in (f1, f2, f3)], run_time=self.dur(1.0))

            # «la energía y la varianza del ruido»
            self.en("solo")
            self.pop(e_sol, s_sol)

            # «Ninguna muestra concreta de la señal»
            self.en("ninguna")
            self.play(FadeIn(muestras), run_time=self.dur(0.5))
            self.play(Create(tacha), run_time=self.dur(0.4))

            # «Pregunta, y piénsala un momento»
            self.en("piensa")
            self.play(*[m.animate.fade(0.7) for m in (f1, f2, f3, e_sol, s_sol, muestras, tacha)], FadeIn(rel),
                      run_time=self.dur(0.6))

            # «el pulso dos, dos, uno»
            self.en("pulso1")
            self.play(FadeOut(rel), run_time=self.dur(0.3))
            self.play(FadeIn(pa.base), *[GrowFromEdge(b, DOWN) for b in pa.barras], FadeIn(pa.nums), run_time=self.dur(0.9))

            # «un solo destello de tres en una muestra»
            self.en("destello")
            self.play(FadeIn(pb.base), GrowFromEdge(pb.barras[0], DOWN), FadeIn(pb.nums[0]), run_time=self.dur(0.8))

            # «y ceros en las demás»
            self.en("ceros")
            self.play(FadeIn(pb.nums[1]), FadeIn(pb.nums[2]), run_time=self.dur(0.5))

            # «energía nueve»
            self.en("nueve")
            self.play(FadeIn(nueve1, shift=UP * 0.1), FadeIn(nueve2, shift=UP * 0.1), run_time=self.dur(0.6))

            # «¿Cuál se detecta mejor?»
            self.en("cual")
            self.pop(cual)
        self.wait(0.3)
        self.pa, self.pb = pa, pb

    # ------------------------------------------------------------ b2
    def cuenta_del_destello(self):
        L = lienzo_g3(centro=(0.0, -1.7))
        base = eje_g3(L, marcas=(0, 9))
        cuenta = formula("g", "=", "3", "r[0]", "+", "0", "r[1]", "+", "0", "r[2]", escala=1.2,
                         colores={0: ESTIMACION, 2: SENAL, 3: MEDIDA, 5: INK, 6: MEDIDA, 8: INK, 9: MEDIDA}).move_to([0, 3.3, 0])
        ge = formula("g", "=", "3", "r[0]", escala=1.4, colores={0: ESTIMACION, 2: SENAL, 3: MEDIDA}).move_to([0, 3.3, 0])
        cam0 = dens3(L, 0, 3, RUIDO)
        cam1 = dens3(L, 9, 3, SENAL)
        f0 = DashedVMobject(dens3(L, 0, 3, TXT, ancho=2.5))
        f1 = DashedVMobject(dens3(L, 9, 3, TXT, ancho=2.5))
        c0 = casilla_h3(0, "solo ruido", centro=(-4.0, 1.1), ancho=3.4)
        c1 = casilla_h3(1, "señal + ruido", centro=(4.0, 1.1), ancho=3.4)
        umb = umbral3(L, 4.5, alto=2.0)
        err = formula("P_e", "=", "0{,}0668", escala=1.1, colores={0: ESTIMACION, 2: VERDE}).move_to([0, -3.5, 0])
        mini_b = Barras((3, 0, 0), centro=(-5.4, 2.7), paso=0.6, unidad=0.25, color=SENAL, ancho=0.4)
        mini_a = Barras((2, 2, 1), centro=(5.4, 2.7), paso=0.6, unidad=0.25, color=SENAL, ancho=0.4)
        igual = MathTex("=", color=AMBAR).scale(1.6).move_to([0, 2.0, 0])
        e_b = formula("P_e", "=", "0{,}0668", escala=0.8, colores={2: VERDE}).move_to([-5.2, 1.9, 0])
        e_a = formula("P_e", "=", "0{,}0668", escala=0.8, colores={2: VERDE}).move_to([5.2, 1.9, 0])
        ok = tilde(VERDE, 0.6).move_to([2.4, -3.5, 0])

        with self.narrar("b2"):
            # «la cuenta del destello»
            self.en("cuenta")
            self.corte()
            self.play(Write(cuenta), run_time=self.dur(1.5))

            # «Ge es tres por»
            self.en("ge")
            self.play(ReplacementTransform(cuenta, ge), run_time=self.dur(0.7))

            # «lo recibido en la primera muestra»
            self.en("primera")
            self.play(ge[3].animate(rate_func=there_and_back).scale(1.5), run_time=self.dur(0.7))

            # «Bajo la hipótesis cero»
            self.en("bajoh0")
            self.play(FadeIn(c0), FadeIn(base), run_time=self.dur(0.5))

            # «media cero y desvío tres»
            self.en("h0")
            self.play(Create(cam0), run_time=self.dur(0.8))

            # «Bajo la hipótesis uno»
            self.en("bajoh1")
            self.play(FadeIn(c1), run_time=self.dur(0.5))

            # «media nueve y desvío tres»
            self.en("h1")
            self.play(Create(cam1), run_time=self.dur(0.8))

            # «las mismas dos campanas»
            self.en("mismas")
            self.play(Create(f0), Create(f1), run_time=self.dur(0.9))

            # «el mismo umbral»
            self.en("umbral")
            self.play(Create(umb), run_time=self.dur(0.6))

            # «el mismo error: cero coma cero seis seis ocho»
            self.en("error")
            self.play(FadeIn(err, shift=UP * 0.1), run_time=self.dur(1.0))

            # «Da igual»
            self.en("daigual")
            self.play(FadeIn(mini_b), FadeIn(mini_a), FadeIn(igual, scale=0.5), run_time=self.dur(0.7))

            # «Un pulso extendido y un destello»
            self.en("extend")
            self.play(FadeIn(e_b), FadeIn(e_a), run_time=self.dur(0.7))

            # «dan el mismo error»
            self.en("final")
            self.play(FadeIn(ok, scale=0.5), run_time=self.dur(0.4))
        self.wait(0.3)
