"""Escena 13 — Regla práctica: si en una estimación aparece un pico llamativo, repítela con otro tramo; lo real vuelve a aparecer."""
from comun.escena import *


def estimacion(Lf: Lienzo, semilla: int, espurio: bool) -> VMobject:
    """Estimación de un espectro: una loma con ruido, un pico real en 6 Hz y (si `espurio`) otro pico que es puro temblor en 8,7 Hz."""
    f = np.linspace(0, 10, 140)
    rng = np.random.default_rng(semilla)
    v = 0.22 + 0.2 * np.exp(-((f - 4) / 2.6) ** 2) + 0.06 * rng.random(f.size)
    v += 0.75 * np.exp(-((f - 6) / 0.18) ** 2)
    if espurio:
        v += 0.6 * np.exp(-((f - 8.7) / 0.15) ** 2)
    return Lf.curva(f, v, AMBAR, 3.2)


class RepiteConOtroTramo(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        La = lienzo_f(0, 10, 2.0, ancho=5.8, cx=-3.6, base_y=-1.2)
        Lb = lienzo_f(0, 10, 2.0, ancho=5.8, cx=3.6, base_y=-1.2)
        reg = palabra_regla = self.palabra("regla práctica", AMBAR, 1.2).move_to([0, 3.3, 0])
        rng = np.random.default_rng(4)
        px = rng.normal(0, 1, 40)
        py = 0.8 * px + 0.5 * rng.normal(0, 1, 40)
        nube = VGroup(*[Dot([-3.4 + 0.8 * a, 0.3 + 0.8 * b, 0], radius=0.07, color=SENAL) for a, b in zip(px, py)])
        rho = formula(r"\rho", "=", r"0{,}8", escala=1.6, colores={0: AMBAR}).move_to([3.4, 0.3, 0])
        comillas = etiqueta("mira la nube antes que el número", INK, 0.55).move_to([0, -2.6, 0])
        ejes_a = ejes_L(La, 0, 1.15, x_eje=0.0)
        ejes_b = ejes_L(Lb, 0, 1.15, x_eje=0.0)
        curva_a = estimacion(La, 1, True)
        curva_b = estimacion(Lb, 2, False)
        lab_a = etiqueta("estimación", INK, 0.5).move_to(La.p(5, 1.3))
        lab_b = etiqueta("otro tramo de datos", INK, 0.5).move_to(Lb.p(5, 1.3))
        pico_real = Ellipse(width=0.8, height=1.7, color=AMBAR, stroke_width=4).move_to(La.p(6.0, 0.55))
        ok_b = tilde().scale(1.0).move_to(Lb.p(6.0, 1.6))
        pico_falso = Ellipse(width=0.8, height=1.5, color=ERROR, stroke_width=4).move_to(La.p(8.7, 0.45))
        x_a = cruz().scale(0.9).move_to(La.p(9.4, 1.6))
        lab_temblor = etiqueta("temblor", ERROR, 0.5).move_to(La.p(8.1, 1.65))
        limpio = Espectro(w_max=6, y_max=1.2, ancho=7.0, alto=3.0, centro=(-0.6, -1.6))
        curva_l = limpio.curva(psd_tele, AMBAR, 5.0)
        sig = Arrow([4.0, -0.2, 0], [6.4, -0.2, 0], color=INK, stroke_width=6, buff=0, max_tip_length_to_length_ratio=0.25)

        with self.narrar("b1"):
            # «una regla práctica»
            self.en("regla")
            self.pop(reg)

            # «mira la nube antes que el número»
            self.en("nube")
            self.play(FadeIn(nube, lag_ratio=0.03), FadeIn(rho), FadeIn(comillas), run_time=self.dur(1.5))

            # «Si en una estimación»
            self.en("estimacion")
            self.play(FadeOut(nube), FadeOut(rho), FadeOut(comillas), run_time=0.3)
            self.play(Create(ejes_a), FadeIn(lab_a), run_time=self.dur(0.8))
            self.play(Create(curva_a), run_time=self.dur(1.4), rate_func=linear)

            # «un pico llamativo»
            self.en("llamativo")
            self.play(Create(pico_real), run_time=self.dur(0.7))

            # «repítela con otro tramo de datos»
            self.en("repite")
            self.play(Create(ejes_b), FadeIn(lab_b), run_time=self.dur(0.7))
            self.play(Create(curva_b), run_time=self.dur(1.5), rate_func=linear)

            # «vuelve a aparecer»
            self.en("vuelve")
            self.play(FadeIn(ok_b, scale=0.5), run_time=self.dur(0.5))

            # «el temblor del estimador, no»
            self.en("temblor")
            self.play(Create(pico_falso), FadeIn(x_a, scale=0.5), FadeIn(lab_temblor), run_time=self.dur(0.8))

            # «ya sabemos medir un espectro»
            self.en("medir")
            self.play(*[FadeOut(m) for m in (ejes_a, ejes_b, curva_a, curva_b, lab_a, lab_b, pico_real, ok_b, pico_falso,
                                             x_a, lab_temblor)], run_time=0.4)
            self.play(Create(limpio.ejes), Create(curva_l), run_time=self.dur(1.2))

            # «Lo siguiente es usarlo»
            self.en("usarlo")
            self.play(GrowArrow(sig), run_time=self.dur(0.6))

        self.wait(1.0)
        self.limpiar()
