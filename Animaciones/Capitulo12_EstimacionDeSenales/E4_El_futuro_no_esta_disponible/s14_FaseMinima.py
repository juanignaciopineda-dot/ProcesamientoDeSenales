"""Escena 14 — Fase mínima y factorización de la densidad: S_xx = σ² F(z) F(z⁻¹)."""
from comun.escena import *

C = (-4.2, 0.6)
R = 1.3


def en_z(x: float) -> np.ndarray:
    return np.array([C[0] + x * R, C[1], 0.0])


class FaseMinima(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        fm = self.palabra("fase mínima", AMBAR, 1.0).move_to([0, 3.2, 0])
        pl = plano_c(C, R)
        marcas = [MathTex(r"\times", color=AMBAR).scale(1.0).move_to(en_z(0.6)),
                  Circle(radius=0.11, color=VERDE, stroke_width=4).move_to(en_z(-0.4))]
        filas = []
        for txt, y in (("causal", 1.4), ("estable", 0.4), ("su inverso", -0.6)):
            filas.append(VGroup(tilde(VERDE, 0.6).move_to([0.2, y, 0]),
                                etiqueta(txt, TXT, 0.6).move_to([2.0, y, 0])))
        fact = self.palabra("factorización", AMBAR, 0.85).move_to([0, 3.4, 0])
        f = oculta(formula(r"S_{xx}(z)", "=", r"\sigma^2", "F(z)", "F(z^{-1})", escala=1.4,
                           colores={0: MEDIDA, 2: AMBAR, 3: CIAN, 4: ROJO}))
        f.move_to([0, 2.0, 0])
        self.add(f)
        lfm = etiqueta("fase mínima", CIAN, 0.45)
        sec = Tallos([1, 0.6, 0.36, 0.22], centro=(-3.2, -0.7), paso=0.55, unidad=1.0, color=CIAN)
        rev = Tallos([0.22, 0.36, 0.6, 1], centro=(3.2, -0.7), paso=0.55, unidad=1.0, color=ROJO)
        fl = Arrow([-1.5, -0.4, 0], [1.5, -0.4, 0], color=INK, stroke_width=3, buff=0)
        lrev = etiqueta("dado la vuelta", INK, 0.45).move_to([0, 0.05, 0])
        gan = formula(r"S_{xx}(\Omega)=\sigma^2\,|F(e^{j\Omega})|^2", escala=1.0, colores={0: MEDIDA}).move_to([0, -2.2, 0])
        mod = caja("modelador · Cap. 11", INK, ancho=4.2, alto=0.8, scale=0.5).move_to([0, -3.4, 0])
        with self.narrar("b1"):
            # «Fase mínima»
            self.en("fm")
            self.pop(fm)

            # «todos sus polos y ceros dentro del círculo»
            self.en("dentro")
            self.play(FadeIn(pl), *[FadeIn(m) for m in marcas], run_time=self.dur(0.9))

            # «causal y estable»
            self.en("estable")
            self.play(FadeIn(filas[0]), FadeIn(filas[1]), run_time=self.dur(0.8))
            self.sfx("exito", gain=-18)

            # «su inverso también»
            self.en("inversotb")
            self.play(FadeIn(filas[2]), run_time=self.dur(0.5))

            # «la factorización»
            self.en("fact")
            self.corte()
            self.add(f)
            self.pop(fact)

            # «la densidad de lo medido es una constante»
            self.en("dens")
            self.play(*revelar(f[0], f[1], f[2]), run_time=self.dur(0.8))

            # «por F de zeta»
            self.en("fz")
            self.play(*revelar(f[3]), run_time=self.dur(0.5))

            # «el filtro de fase mínima»
            self.en("fmin")
            lfm.next_to(f[3], DOWN, buff=0.3)
            self.play(FadeIn(lfm), run_time=self.dur(0.4))

            # «por F de zeta a la menos uno»
            self.en("fzi")
            self.play(*revelar(f[4]), run_time=self.dur(0.5))

            # «dado la vuelta en el tiempo»
            self.en("vuelta")
            self.play(FadeIn(sec), run_time=self.dur(0.5))
            self.play(GrowArrow(fl), FadeIn(lrev), FadeIn(rev), run_time=self.dur(0.8))

            # «En el círculo es su ganancia al cuadrado»
            self.en("gan")
            self.play(FadeIn(gan, shift=UP * 0.15), run_time=self.dur(0.8))

            # «el modelador del capítulo once»
            self.en("mod")
            self.play(FadeIn(mod, shift=UP * 0.15), run_time=self.dur(0.5))

        self.wait(1.0)
        self.limpiar()
