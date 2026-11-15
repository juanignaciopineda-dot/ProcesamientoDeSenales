"""Escena 06 — No se puede transformar y dividir, y cortar el no causal del sensor da 0,686 en vez de 0,7386."""
from comun.escena import *


class CortarNoSirve(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        mneg = formula(r"m<0", escala=1.1, colores={0: AMBAR}).move_to([-5.7, 2.9, 0])
        f = formula("(", "h", r"\ast", "C_{xx}", ")[m]", r"\neq", "C_{yx}[m]", escala=1.1,
                    colores={1: ESTIMACION, 3: MEDIDA, 5: ROJO, 6: SENAL}).move_to([-0.8, 2.9, 0])
        interr = Text("?", color=ROJO, weight=BOLD).scale(0.8).next_to(f[1], UP, buff=0.12)
        fr = formula(r"\frac{S_{yx}}{S_{xx}}", escala=0.9).move_to([5.2, 2.9, 0])
        tach = tachar(fr)
        hb = Tallos(H_NO_CAUSAL, centro=(-3.2, -1.0), paso=0.9, unidad=3.0, color=AMBAR, k0=-2, indices=True)
        lnc = etiqueta("no causal", INK, 0.5).move_to([-3.2, -2.1, 0])
        tj = tijeras().scale(0.8).move_to([-6.2, 0.8, 0])
        tj.permitir_encima = True
        v0 = etiqueta("0,686", AMBAR, 0.5).move_to([hb.x(2), -1.0 + 0.686 * 3.0 + 0.3, 0])
        v1 = [etiqueta("0,108", AMBAR, 0.45).move_to([hb.x(i), -1.0 + 0.108 * 3.0 + 0.3, 0]) for i in (1, 3)]
        hc = Tallos(H_CAUSAL, centro=(3.6, -1.0), paso=0.9, unidad=3.0, color=AMBAR, k0=0, indices=True)
        lc = etiqueta("causal", AMBAR, 0.5).move_to([3.6, -2.1, 0])
        vc = etiqueta("0,7386", AMBAR, 0.5).move_to([hc.x(0), -1.0 + 0.7386 * 3.0 + 0.3, 0])
        dist = formula(r"0{,}686", r"\neq", r"0{,}7386", escala=1.1, colores={1: ROJO}).move_to([0, -3.3, 0])
        with self.narrar("b1"):
            # «para eme negativo»
            self.en("neg")
            self.pop(mneg)

            # «los dos lados no coinciden»
            self.en("nocoin")
            self.play(FadeIn(f, shift=UP * 0.2), run_time=self.dur(0.7))
            self.sfx("error", gain=-18)

            # «un hache que aún no conocemos»
            self.en("noconocemos")
            self.play(FadeIn(interr, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «no podemos transformar y dividir»
            self.en("nodividir")
            self.play(FadeIn(fr), run_time=self.dur(0.4))
            self.play(Create(tach), run_time=0.3)
            self.sfx("error", gain=-18)

            # «el filtro no causal del sensor»
            self.en("sensor")
            self.play(FadeIn(hb), FadeIn(lnc), run_time=self.dur(0.9))

            # «le cortamos los coeficientes»
            self.en("corta")
            self.play(FadeIn(tj, scale=0.7), run_time=self.dur(0.4))

            # «de eme negativo»
            self.en("negc")
            self.play(tj.animate.move_to([-3.65, 0.9, 0]), run_time=self.dur(0.5))
            self.play(hb.palito(0).animate.fade(0.8), hb.palito(1).animate.fade(0.8), FadeOut(tj),
                      run_time=self.dur(0.6))

            # «cero coma seis ocho seis en el cero»
            self.en("c0")
            self.play(FadeIn(v0, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «cero coma uno cero ocho a cada lado»
            self.en("lados")
            self.play(*[FadeIn(v, shift=DOWN * 0.1) for v in v1], run_time=self.dur(0.4))

            # «el óptimo causal empieza en cero coma siete tres ocho seis»
            self.en("optimo")
            self.play(FadeIn(hc), FadeIn(lc), FadeIn(vc), run_time=self.dur(0.9))

            # «distinto»
            self.en("distinto")
            self.pop(dist, sonido="error")

        self.wait(1.0)
        self.limpiar()
