"""Escena 04 — El micrófono que llega tarde: la cruzada no es par y la transformada es compleja."""
from comun.escena import *


class ElMicrofonoQueLlegaTarde(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        pers = persona(AZUL).scale(1.0).move_to([-6.3, 3.1, 0])
        mic = microfono(CIAN).scale(1.1).move_to([-4.9, 3.1, 0])
        F = oculta(formula(r"y(t)", "=", r"x(t", "-", r"0{,}5", ")", escala=1.0,
                           colores={0: MEDIDA, 2: SENAL}).move_to([-1.3, 3.1, 0]))
        rel = reloj(INK).scale(0.7).move_to([2.6, 3.1, 0])
        t05 = etiqueta("0,5 s", AMBAR, 0.5).move_to([3.6, 3.1, 0])
        # la correlación cruzada: un pico en τ = 0,5
        L = Lienzo(ancho=6.0, alto=2.2, t_rango=(-2, 2), v_max=1.3, centro=(-3.3, 0.5))
        ej = ejes_L(L, -0.1, 1.25, x_eje=0.0)
        f = lambda u: np.exp(-((np.asarray(u) - 0.5) / 0.28) ** 2)
        cur = curva_f(L, f, -1.9, 1.9, AMBAR, 4.0)
        pico = Dot(L.p(0.5, 1.0), radius=0.09, color=AMBAR)
        rot_pico = formula(r"\tau=0{,}5", escala=0.7, colores={0: AMBAR}).move_to(L.p(0.5, 1.6) + RIGHT * 0.9)
        et_R = formula(r"R_{yx}(\tau)", escala=0.8, colores={0: AMBAR}).move_to([-6.1, 1.9, 0])
        cero = Text("0", color=INK).scale(0.4).move_to(L.p(0, -0.35))
        x_cero = cruz(ROJO, 0.4).move_to(L.p(0, 0.55))
        espejo = cur.copy().flip(UP, about_point=L.p(0, 0)).set_stroke(INK, opacity=0.7)
        etq_nopar = etiqueta("no es par", ROJO, 0.55).move_to([-3.3, -1.4, 0])
        # la transformada
        G = formula(r"e^{-j\omega\tau}", "=", r"\cos\omega\tau", "-", "j", r"\sin\omega\tau", escala=0.85
                    ).move_to([3.7, 0.9, 0])
        Ls = Lienzo(ancho=5.6, alto=1.6, t_rango=(-2, 2), v_max=1.0, centro=(3.9, -1.3))
        g = lambda u: np.exp(-((np.asarray(u) - 0.5) / 0.28) ** 2) * np.sin(3 * np.asarray(u))
        cg = curva_f(Ls, g, -1.9, 1.9, CIAN, 3.5)
        ar = area_f(Ls, g, 0.0, 1.2, AMBAR, 0.5)
        S = oculta(formula(r"S_{yx}(j\omega)", escala=1.0, colores={0: AMBAR}).move_to([-3.4, -2.6, 0]))
        comp = etiqueta("complejo", AMBAR, 0.55).move_to([-3.4, -3.3, 0])
        with self.narrar("b1"):
            # «el micrófono capta la voz»
            self.en("tarde")
            self.add(F)
            self.play(FadeIn(pers), FadeIn(mic), *revelar(F[0], F[1], F[2], F[3], F[5]), run_time=self.dur(0.7))

            # «medio segundo tarde»
            self.en("medio")
            self.play(*revelar(F[4]), FadeIn(rel), FadeIn(t05), run_time=self.dur(0.6))

            # «tiene su pico en tau igual a cero coma cinco»
            self.en("pico")
            self.play(Create(ej), FadeIn(et_R), Create(cur), run_time=self.dur(1.2))
            self.play(FadeIn(pico), FadeIn(rot_pico), run_time=0.3)

            # «no en cero»
            self.en("nocero")
            self.play(FadeIn(cero), Create(x_cero), run_time=self.dur(0.4))

            # «ya no es par»
            self.en("nopar")
            self.play(Create(espejo), FadeIn(etq_nopar), run_time=self.dur(0.8))

            # «la parte con jota»
            self.en("jota")
            self.play(FadeIn(G), run_time=self.dur(1.0))
            self.play(G[4:6].animate.set_color(AMBAR), run_time=0.4)

            # «no se cancela»
            self.en("nocancela")
            self.play(Create(cg), run_time=self.dur(0.7))
            self.play(FadeIn(ar), run_time=self.dur(0.5))

            # «un número complejo en cada frecuencia»
            self.en("complejo")
            self.add(S)
            self.play(*revelar(S), FadeIn(comp), run_time=self.dur(0.7))

        self.wait(1.0)
        self.limpiar()
