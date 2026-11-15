"""Escena 09 — Las señales son aleatorias, pero la relación entre sus correlaciones es determinista: R_yy = R_hh * R_xx."""
from comun.escena import *


class Determinista(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        # fila de arriba: los procesos
        bl = BloqueLTI(r"h", centro=(0, 2.9), ancho=1.6, alto=1.0, largo=2.3)
        Lp = Lienzo(ancho=2.6, alto=1.4, t_rango=(0, 1), v_max=1.5, centro=(-4.7, 2.9))
        Lq = Lienzo(ancho=2.6, alto=1.4, t_rango=(0, 1), v_max=1.5, centro=(4.7, 2.9))
        pe = pila_de_curvas(Lp, 6, semilla=3, a=0.9, puntos=120, color=SENAL, opacidad=0.7, ancho=2.4, escala=0.5)
        ps = pila_de_curvas(Lq, 6, semilla=4, a=0.96, puntos=120, color=MEDIDA, opacidad=0.7, ancho=2.4, escala=0.5)
        # fila de en medio: las correlaciones
        bl2 = BloqueLTI(r"h", centro=(0, 0.8), ancho=1.6, alto=1.0, largo=2.3, color=VERDE)
        Lc = Lienzo(ancho=2.6, alto=1.3, t_rango=(-1.5, 1.5), v_max=1.2, centro=(-4.7, 0.8))
        Ld = Lienzo(ancho=2.6, alto=1.3, t_rango=(-1.5, 1.5), v_max=1.2, centro=(4.7, 0.8))
        tau = np.linspace(-1.5, 1.5, 120)
        r_xx = Lc.curva(tau, np.exp(-2.5 * np.abs(tau)), SENAL, 4)
        r_yx = Ld.curva(tau, 0.75 * np.exp(-1.6 * np.abs(tau - 0.3)), MEDIDA, 4)
        lab_rxx = formula(r"R_{xx}", escala=0.8).next_to(Lc.p(0, 0.0), DOWN, buff=0.85)
        lab_ryx = formula(r"R_{yx}", escala=0.8).next_to(Ld.p(0, 0.0), DOWN, buff=0.85)
        limpia = Arrow([-2.6, 1.85, 0], [2.6, 1.85, 0], color=VERDE, buff=0, stroke_width=5)
        siempre = etiqueta("la convolución de siempre", VERDE, 0.68).move_to([0, -0.2, 0])
        hace_de = etiqueta("R_xx hace de «x»", AMBAR, 0.68).move_to([-4.7, -0.7, 0])
        # fila de abajo: se repite el paso
        bl3 = BloqueLTI(r"h(-\tau)", centro=(0, -1.75), ancho=1.9, alto=1.0, largo=2.0, color=VERDE, escala=0.75)
        Le = Lienzo(ancho=2.6, alto=1.2, t_rango=(-1.5, 1.5), v_max=1.2, centro=(-4.7, -1.75))
        Lf = Lienzo(ancho=2.6, alto=1.2, t_rango=(-1.5, 1.5), v_max=1.2, centro=(4.7, -1.75))
        r_yx2 = Le.curva(tau, 0.75 * np.exp(-1.6 * np.abs(tau - 0.3)), MEDIDA, 4)
        r_yy = Lf.curva(tau, 0.6 * np.exp(-1.2 * np.abs(tau)), ESTIMACION, 4)
        lab_ryy = formula(r"R_{yy}", escala=0.8, colores={0: ESTIMACION}).next_to(Lf.p(0, 0), DOWN, buff=0.75)
        mas_h = formula(r"*", r"R_{hh}", escala=0.9).move_to([0, -3.3, 0])
        fusion = formula(r"R_{hh}(\tau)", escala=1.0, colores={0: ESTIMACION}).move_to([0, -1.75, 0])
        final = formula(r"R_{yy}", "=", r"R_{hh}", "*", r"R_{xx}", escala=1.3).move_to([0, -3.3, 0])
        caja_f = SurroundingRectangle(final, color=AMBAR, buff=0.18, stroke_width=3)

        with self.narrar("b1"):
            # «Las señales son aleatorias»
            self.en("aleat")
            self.play(FadeIn(bl), Create(pe), Create(ps), run_time=self.dur(1.0))

            # «pero la relación»
            self.en("relacion")
            self.play(GrowArrow(limpia), run_time=self.dur(0.6))

            # «entre sus correlaciones»
            self.en("correls")
            self.play(Create(r_xx), Create(r_yx), FadeIn(lab_rxx), FadeIn(lab_ryx), run_time=self.dur(0.9))

            # «determinista»
            self.en("determ")
            self.play(FadeIn(bl2), run_time=self.dur(0.6))

            # «la convolución de siempre»
            self.en("siempre")
            self.play(FadeIn(siempre), run_time=self.dur(0.5))

            # «haciendo de señal de entrada»
            self.en("hace_de")
            self.play(FadeIn(hace_de), r_xx.animate.set_stroke(width=7), run_time=self.dur(0.6))

            # «Repitiendo»
            self.en("repite")
            self.play(FadeIn(r_yx2), run_time=self.dur(0.6))

            # «el mismo paso»
            self.en("mismo")
            self.play(FadeIn(bl3), run_time=self.dur(0.5))

            # «la segunda hache»
            self.en("segunda")
            self.resaltar(bl3.caja, color=AMBAR, escala=1.1)

            # «la autocorrelación de la salida»
            self.en("r_yy")
            self.play(Create(r_yy), FadeIn(lab_ryy), run_time=self.dur(0.8))

            # «convolucionada con»
            self.en("conv_con")
            self.play(FadeIn(mas_h), run_time=self.dur(0.5))

            # «erre sub hache hache»
            self.en("r_hh")
            self.play(FadeOut(bl3.rot), FadeIn(fusion), run_time=self.dur(0.6))

            # «determinista de la respuesta»
            self.en("det_h")
            self.play(FadeOut(mas_h), FadeIn(final), Create(caja_f), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
