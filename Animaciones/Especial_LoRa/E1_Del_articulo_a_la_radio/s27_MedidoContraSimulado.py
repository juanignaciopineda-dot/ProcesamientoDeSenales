"""Escena 27 — Una captura real del Pluto (la trama, 14 dB bajo el ruido) y el FER medido sobre el simulado."""
from comun.escena import *
from comun.figuras_lora import *


class MedidoContraSimulado(EscenaCurso):
    ESCENA = "27"

    def construct(self):
        self.captura()
        self.fer()
        self.wait(1.0)
        self.limpiar()

    def captura(self):
        x, i0 = captura_pluto()
        n, M = x.size, 256
        L = Lienzo(ancho=12.6, alto=2.5, t_rango=(0, n), v_max=43.0, centro=(0, 2.0))
        k = np.arange(0, n, 6)
        tr = L.curva(k, x.real[k], MEDIDA, 1.6)
        radc = Text("Niveles del ADC", color=INK, weight=BOLD).scale(0.45).move_to([-5.2, 3.7, 0])
        ct = cota(L.p(i0, 0) + UP * 1.45, L.p(i0 + 5184, 0) + UP * 1.45, "Trama", AMBAR, UP, 0.5)
        snr = MathTex(r"\mathrm{SNR}", "=", r"-14\ \mathrm{dB}", color=TXT).scale(1.1).move_to([3.6, 0.2, 0])
        snr[2].set_color(ERROR)
        T = correlacion_preambulo(x, M)
        Tm = T[: T.size // 8 * 8].reshape(-1, 8).max(axis=1)
        y0, alto = -3.4, 2.7
        xs = np.array([float(L.x(8 * j)) for j in range(Tm.size)])
        curva = traza(xs, y0 + Tm / Tm.max() * alto, ESTIMACION, 2.6)
        base = Line([L.x(0), y0, 0], [L.x(n), y0, 0], color=INK, stroke_width=2)
        rt = MathTex("T[k]", color=ESTIMACION).scale(0.9).move_to([-5.6, 0.2, 0])
        kp = int(np.argmax(T))
        pico = Dot([float(L.x(kp)), y0 + alto, 0], radius=0.14, color=AMBAR)
        vert = DashedLine(pico.get_center(), L.p(kp, 0) + DOWN * 1.2, color=AMBAR, stroke_width=3, dash_length=0.1)
        with self.narrar("b1"):
            # «una captura real»
            self.en("captura")
            self.play(Create(tr, rate_func=linear), run_time=self.dur(0.9))
            # «del conversor del Pluto»
            self.en("adc")
            self.play(FadeIn(radc), run_time=self.dur(0.4))
            # «hay una trama»
            self.en("trama")
            self.play(FadeIn(ct), run_time=self.dur(0.6))
            # «por debajo del ruido»
            self.en("debajo")
            self.pop(snr)
            # «Se le pasa el detector»
            self.en("detector")
            self.play(FadeIn(base), FadeIn(rt), Create(curva, rate_func=linear), run_time=self.dur(1.2))
            # «el pico aparece»
            self.en("pico")
            self.pop(pico, sonido="impacto")
            # «donde empieza el preámbulo»
            self.en("inicio")
            self.play(Create(vert), run_time=self.dur(0.8))

    def fer(self):
        n200 = Text("200 tramas por punto", color=TXT, weight=BOLD).scale(0.55).move_to([4.6, 2.9, 0])
        E = EjesXY(centro=(-2.0, -0.2), ancho=7.0, alto=5.2, x=(-24, -10), y=(1e-3, 1), log_y=True,
                   x_marcas=(-24, -20, -16, -12), y_marcas=(1, 1e-1, 1e-2, 1e-3), rot_x="SNR (dB)", rot_y="FER",
                   escala=0.45)
        sim = E.curva(FER_SIM_SNR, FER_SIM, SENAL, 4.5)
        pts = E.puntos(TERMICO_SNR, TERMICO_FER, AMBAR, 0.14)
        l1 = Text("Simulado", color=SENAL, weight=BOLD).scale(0.6).move_to([4.6, 1.9, 0])
        l2 = Text("Medido en el Pluto", color=AMBAR, weight=BOLD).scale(0.6).move_to([4.6, 1.2, 0])
        v9 = Text("0,9", color=AMBAR, weight=BOLD).scale(0.55).move_to(E.p(TERMICO_SNR[0], TERMICO_FER[0]) + RIGHT * 0.55 + UP * 0.25)
        v1 = Text("0,01", color=AMBAR, weight=BOLD).scale(0.55).move_to(E.p(TERMICO_SNR[5], TERMICO_FER[5]) + LEFT * 0.75 + DOWN * 0.3)
        m23 = DashedLine(E.p(-23, 1e-3), E.p(-23, 0.93), color=INK, stroke_width=2.5, dash_length=0.1)
        m12 = DashedLine(E.p(-12, 1e-3), E.p(-12, 0.012), color=INK, stroke_width=2.5, dash_length=0.1)
        mod = Text("Medido ≈ Simulado", color=VERDE, weight=BOLD).scale(0.65).move_to([4.6, -0.6, 0])
        with self.narrar("b2"):
            # «doscientas tramas por punto»
            self.en("n200")
            self.corte()
            self.play(FadeIn(n200, shift=UP * 0.15), run_time=self.dur(0.5))
            # «la fracción de tramas perdidas»
            self.en("fer")
            self.play(FadeIn(E.todo), run_time=self.dur(0.7))
            # «cae sobre la curva simulada»
            self.en("sobre")
            self.play(Create(sim, rate_func=linear), FadeIn(l1), run_time=0.8)
            self.play(LaggedStart(*[FadeIn(p, scale=2.0) for p in pts], lag_ratio=0.15), FadeIn(l2),
                      run_time=self.dur(0.9))
            # «nueve de cada diez»
            self.en("nueve")
            self.play(FadeIn(v9), pts[0].animate(rate_func=there_and_back).scale(1.8), run_time=self.dur(0.6))
            # «menos veintitrés decibelios»
            self.en("m23")
            self.play(Create(m23), run_time=self.dur(0.5))
            # «una de cada cien»
            self.en("una")
            self.play(FadeIn(v1), pts[5].animate(rate_func=there_and_back).scale(1.8), run_time=self.dur(0.6))
            # «menos doce»
            self.en("m12")
            self.play(Create(m12), run_time=self.dur(0.5))
            # «como el ruido blanco del modelo»
            self.en("modelo")
            self.pop(mod, sonido="exito")
