"""Escena 12 — Llega un dato nuevo: ya había una estimación con A; llega B, se predice y se mide la sorpresa."""
from comun.escena import *
from comun.figuras_c8e5 import *


class LlegaUnDatoNuevo(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.situacion()
        self.sorpresa()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def situacion(self):
        eje = Arrow([-6.4, -0.6, 0], [6.6, -0.6, 0], buff=0, color=INK, stroke_width=3,
                    max_tip_length_to_length_ratio=0.02)
        p1 = Dot([-3.0, -0.6, 0], radius=0.13, color=ESTIMACION)
        p2 = Dot([2.8, -0.6, 0], radius=0.13, color=MEDIDA)
        llega = Arrow([2.8, 2.4, 0], [2.8, -0.4, 0], buff=0, color=MEDIDA, stroke_width=5,
                      max_tip_length_to_length_ratio=0.12)
        A = Termo8("A", centro=(-3.0, 1.3), alto=1.8, escala_letra=0.8)
        B = Termo8("B", centro=(2.8, 1.3), alto=1.8, escala_letra=0.8)
        xa = MathTex("x_A=23", color=MEDIDA).scale(0.95).move_to([-1.3, 1.4, 0])
        ap = MathTex(r"\hat{y}=22{,}4", color=ESTIMACION).scale(1.0).move_to([-3.0, -1.45, 0])
        e08 = MathTex(r"\text{Error}=0{,}8", color=ERROR).scale(0.9).move_to([-3.0, -2.3, 0])
        xb = MathTex("x_B=22", color=MEDIDA).scale(0.95).move_to([4.5, 0.9, 0])
        M, H, igual, C, sis = sistema8([["5", "4"], ["4", "8"]], centro=(2.4, -2.6), escala=0.7)
        sis.fade(0.5)
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.3).move_to([5.6, -2.6, 0])

        with self.narrar("b1"):
            # «Una situación muy habitual»
            self.en("hab")
            self.play(GrowArrow(eje), run_time=self.dur(0.7))

            # «Ya tenías una estimación»
            self.en("tenias")
            self.play(FadeIn(p1, scale=0.4), run_time=self.dur(0.4))

            # «llega una medición nueva»
            self.en("nueva")
            self.play(GrowArrow(llega), FadeIn(p2), run_time=self.dur(0.6))

            # «Primero leíste A»
            self.en("a")
            self.play(FadeIn(A, shift=DOWN * 0.2), run_time=self.dur(0.4))
            self.play(A.nivel(0.7), FadeIn(xa, shift=LEFT * 0.1), run_time=self.dur(0.5))

            # «apostaste veintidós coma cuatro»
            self.en("ap")
            self.play(FadeIn(ap, shift=UP * 0.1), run_time=self.dur(0.5))

            # «con error cero coma ocho»
            self.en("e08")
            self.play(FadeIn(e08, shift=UP * 0.1), run_time=self.dur(0.5))

            # «Ahora llega B»
            self.en("b")
            self.play(FadeOut(llega), FadeIn(B, shift=DOWN * 0.3), run_time=self.dur(0.6))

            # «y marca veintidós»
            self.en("b22")
            self.play(B.nivel(0.6), FadeIn(xb, shift=LEFT * 0.1), run_time=self.dur(0.5))

            # «¿Hay que rehacer todas las cuentas»
            self.en("rehacer")
            self.play(FadeIn(sis), run_time=self.dur(0.5))
            self.pop(q)
        self.B, self.xb, self.sis, self.q = B, xb, sis, q

    # ------------------------------------------------------------ b2
    def sorpresa(self):
        globo = RoundedRectangle(corner_radius=0.3, width=2.3, height=0.95, color=TXT, stroke_width=3)
        globo.set_fill(FONDO, 1).move_to([5.3, 2.7, 0])
        pico = Line(globo.get_corner(DL) + RIGHT * 0.4, [3.6, 2.2, 0], color=TXT, stroke_width=3)
        g_q = MathTex(r"x_B=\;?", color=TXT).scale(0.9).move_to(globo)
        g_v = MathTex(r"22{,}4", color=ESTIMACION).scale(0.95).move_to(globo)
        bym = formula("x_B", "=", "y", "+", "v_B", escala=1.0, colores={0: MEDIDA, 2: SENAL, 4: RUIDO})
        bym.move_to([2.6, -1.5, 0])
        m0 = MathTex(r"E[v_B]=0", color=RUIDO).scale(0.9).move_to([2.6, -2.35, 0])
        apy = formula(r"\hat{x}_B", "=", r"\hat{y}", escala=1.0, colores={0: ESTIMACION, 2: ESTIMACION})
        apy.move_to([2.2, -3.2, 0])
        e224 = MathTex(r"=22{,}4", color=ESTIMACION).scale(1.0).next_to(apy, RIGHT, buff=0.15)
        sor = Text("Sorpresa", color=AMBAR, weight=BOLD).scale(0.8).move_to([2.6, -1.6, 0])
        s04 = MathTex(r"=22-22{,}4=-0{,}4", color=AMBAR).scale(1.0).move_to([2.6, -2.5, 0])

        with self.narrar("b2"):
            # «No hace falta»
            self.en("no")
            tache = tachar(self.sis)
            self.play(Create(tache), run_time=0.4)
            self.play(FadeOut(self.sis), FadeOut(tache), FadeOut(self.q), run_time=self.dur(0.4))

            # «¿qué esperabas que marcara?»
            self.en("esperabas")
            self.play(FadeIn(globo), Create(pico), FadeIn(g_q), run_time=self.dur(0.6))

            # «B es la temperatura»
            self.en("bym")
            self.play(FadeIn(bym, shift=UP * 0.1), run_time=self.dur(0.5))

            # «un ruido de media cero»
            self.en("media0")
            self.play(FadeIn(m0, shift=UP * 0.1), run_time=self.dur(0.5))

            # «tu mejor apuesta para B»
            self.en("apy")
            self.play(FadeIn(apy, shift=UP * 0.1), run_time=self.dur(0.5))

            # «veintidós coma cuatro»
            self.en("e224")
            self.play(FadeIn(e224, shift=LEFT * 0.1), ReplacementTransform(g_q, g_v), run_time=self.dur(0.5))

            # «Pero marca veintidós»
            self.en("m22")
            self.resaltar(self.xb, color=AMBAR, escala=1.3)

            # «La sorpresa»
            self.en("sorpresa")
            self.play(FadeOut(bym), FadeOut(m0), FadeOut(apy), FadeOut(e224), run_time=0.3)
            self.pop(sor)

            # «menos cero coma cuatro»
            self.en("s04")
            self.play(FadeIn(s04, shift=UP * 0.1), run_time=self.dur(0.6))
