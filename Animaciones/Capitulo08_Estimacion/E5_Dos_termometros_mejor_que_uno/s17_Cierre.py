"""Escena 17 — Cierre: perpendicular a cada medición, lo que trae de nuevo, corregir por la sorpresa;
anuncia el E1 del capítulo 9, «¿Un cero o un uno?»."""
from comun.escena import *
from comun.figuras_c8e5 import *


class Cierre(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        P = PlanoDos8(centro=(-1.0, 0.5), k=1.25)
        lin = formula(r"C_{xx}", r"\,\mathbf{h}", "=", r"\mathbf{c}_{xy}", escala=1.2,
                      colores={1: ESTIMACION, 3: SENAL}).move_to([0.0, -2.75, 0])
        cartas = []
        for x, t, e, c in ((-4.4, r"B_1", "Error 0,8", ERROR), (-0.8, r"B_2", "Error 0,8", ERROR),
                           (2.8, r"B_3", "Error 0", VERDE)):
            g = tarjeta8(t, centro=(x, 0.9), ancho=2.6, alto=2.2)
            g.rot.shift(UP * 0.45)
            txt = Text(e, color=c, weight=BOLD).scale(0.55).move_to([x, 0.45, 0])
            cartas.append(VGroup(g, txt))
        llega = Arrow([5.6, 3.5, 0], [5.6, 1.6, 0], buff=0, color=MEDIDA, stroke_width=6,
                      max_tip_length_to_length_ratio=0.15)
        act = formula(r"\hat{y}_{\text{nueva}}", "=", r"\hat{y}_{\text{vieja}}", "+", "K", r"\cdot",
                      r"\text{sorpresa}", escala=1.05, colores={0: ESTIMACION, 2: ESTIMACION, 4: AMBAR, 6: CIAN})
        act.move_to([0.0, -1.9, 0])
        c9 = Text("Capítulo 9", color=INK).scale(0.6).move_to([0, 1.1, 0])
        tit = Text("¿Un cero o un uno?", color=AMBAR, weight=BOLD).scale(1.2).move_to([0, -0.1, 0])

        with self.narrar("b1"):
            # «con varias mediciones»
            self.en("varias")
            self.play(FadeIn(P.plano), GrowArrow(P.xa), GrowArrow(P.xb), FadeIn(P.rot["xa"]), FadeIn(P.rot["xb"]),
                      GrowArrow(P.y), FadeIn(P.rot["y"]), run_time=self.dur(0.8))

            # «perpendicular a cada una»
            self.en("perp")
            self.play(Create(P.sombra), Create(P.error), FadeIn(P.rot["yh"]), FadeIn(P.rot["e"]), run_time=self.dur(0.5))
            self.play(Create(P.recto_a), Create(P.recto_b), run_time=self.dur(0.4))

            # «las ecuaciones normales»
            self.en("normales")
            self.play(FadeIn(lin, shift=UP * 0.1), run_time=self.dur(0.5))

            # «lo que trae de nuevo»
            self.en("nuevo")
            self.play(FadeOut(P), FadeOut(lin), run_time=0.3)
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cartas], lag_ratio=0.25), run_time=self.dur(0.9))

            # «cuando llega una más»
            self.en("llega")
            self.play(GrowArrow(llega), run_time=self.dur(0.5))

            # «corregir por la sorpresa»
            self.en("sorpresa")
            self.play(FadeIn(act, shift=UP * 0.1), run_time=self.dur(0.6))

            # «En el próximo episodio»
            self.en("proximo")
            todo = [m for m in self.mobjects if m is not self.camera.frame]
            self.play(*[FadeOut(m, shift=UP * 0.5) for m in todo], run_time=self.dur(0.6))

            # «abre el capítulo nueve»
            self.en("cap9")
            self.play(FadeIn(c9, shift=UP * 0.1), run_time=self.dur(0.5))

            # «¿Un cero o un uno?»
            self.en("titulo")
            self.pop(tit)
        self.wait(0.8)
        self.limpiar()
