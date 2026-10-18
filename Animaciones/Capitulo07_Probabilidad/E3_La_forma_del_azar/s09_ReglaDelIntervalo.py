"""Escena 09 — La probabilidad de un intervalo: F(b) − F(a)."""
from comun.escena import *


class ReglaDelIntervalo(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        A = AcumDado(centro=(0.5, -0.6))
        A.add(A.peldanos, A.llenos, A.huecos)
        caras = VGroup(*[dado_n(k).scale(0.5).move_to([-6.2 + 0.78 * (k - 1), 3.3, 0]) for k in range(1, 7)])
        self.add(A)

        with self.narrar("b1"):
            self.en("regla")                                  # «una regla práctica»
            pal = self.palabra("Regla práctica", AMBAR, 0.75).move_to([-0.1, 3.45, 0])
            self.pop(pal)
            self.en("caiga")                                  # «que el dado caiga»
            self.play(FadeIn(caras, shift=DOWN * 0.15), run_time=self.dur(0.6))
            self.en("entre")                                  # «entre dos y cinco»
            ca = A.cursor(2.0, AMBAR)
            cb = A.cursor(5.0, VERDE)
            ta = Text("a = 2", color=AMBAR, weight=BOLD).scale(0.45).next_to(ca, UP, buff=0.08)
            tb = Text("b = 5", color=VERDE, weight=BOLD).scale(0.45).next_to(cb, UP, buff=0.08)
            self.play(Create(ca), Create(cb), FadeIn(ta), FadeIn(tb), run_time=self.dur(0.8))
            self.en("sin_dos")                                # «sin incluir el dos»
            ext = Circle(radius=0.11, color=AMBAR, stroke_width=4).set_fill(FONDO, 1).move_to(A.p(2, 0))
            self.play(FadeIn(ext, scale=2), caras[1].cara.animate.set_stroke(ERROR), run_time=self.dur(0.5))
            self.en("hasta_cinco")                            # «acumulado hasta cinco»
            h5 = DashedLine(A.p(5, 5 / 6), A.p(0, 5 / 6), color=VERDE, stroke_width=4)
            self.play(Create(h5), run_time=self.dur(0.6))
            self.en("cinco_sextos")                           # «cinco sextos»
            f5 = Text("F(5) = 5/6", color=VERDE, weight=BOLD).scale(0.62).move_to([4.0, 3.45, 0])
            self.play(Write(f5), run_time=self.dur(0.6))
            self.en("hasta_dos")                              # «acumulado hasta dos»
            h2 = DashedLine(A.p(2, 2 / 6), A.p(0, 2 / 6), color=AMBAR, stroke_width=4)
            self.play(Create(h2), run_time=self.dur(0.6))
            self.en("dos_sextos")                             # «dos sextos»
            f2 = Text("F(2) = 2/6", color=AMBAR, weight=BOLD).scale(0.62).move_to([4.0, 2.85, 0])
            self.play(Write(f2), run_time=self.dur(0.6))
            self.en("tres_sextos")                            # «tres sextos»
            dif = Text("5/6 − 2/6 = 3/6", color=TXT, weight=BOLD).scale(0.62).move_to([4.0, 2.25, 0])
            self.play(Write(dif), run_time=self.dur(0.8))
            self.en("caras")                                  # «Las caras tres, cuatro y cinco»
            self.play(*[caras[i].cara.animate.set_stroke(VERDE if i in (2, 3, 4) else TXT) for i in range(6)],
                      run_time=self.dur(0.8))
            self.en("general")                                # «En general»
            self.play(FadeOut(VGroup(f5, f2, dif, h5, h2, ext, caras, pal)),
                      Transform(ta, Text("a", color=AMBAR, weight=BOLD).scale(0.5).move_to(ta)),
                      Transform(tb, Text("b", color=VERDE, weight=BOLD).scale(0.5).move_to(tb)),
                      run_time=self.dur(0.8))
            self.en("caer")                                   # «la probabilidad de caer entre»
            f = formula("P", "(", "a", "<", "X", r"\le", "b", ")", "=", "F(b)", "-", "F(a)",
                        escala=1.2, colores={2: AMBAR, 6: VERDE, 9: VERDE, 11: AMBAR})
            f.move_to([0.5, 3.4, 0])
            self.play(LaggedStart(*[Write(p) for p in f[:8]], lag_ratio=0.12), run_time=self.dur(1.2))
            self.en("a_b")                                    # «a y b»
            self.play(f[2].animate(rate_func=there_and_back).scale(1.5), f[6].animate(rate_func=there_and_back).scale(1.5),
                      run_time=self.dur(0.7))
            self.en("resta")                                  # «la acumulada en b menos la acumulada en a»
            self.play(LaggedStart(*[Write(p) for p in f[8:]], lag_ratio=0.2), run_time=self.dur(1.6))
        self.wait(1.0)
        self.limpiar()
