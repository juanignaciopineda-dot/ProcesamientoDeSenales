"""Escena 13 — El empate en la frontera y las tres hipótesis."""
from comun.escena import *
from comun.figuras_c9e1 import *


class LaFrontera(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        C = Campanas9(centro=(0.0, -2.6), alto=8.0, v_max=0.3)
        self.C = C
        eje = C.eje((0, 1, 2))
        c0, c1 = C.campana(0, P0, C0), C.campana(2, P1, C1)
        r0, r1 = C.region(-3, CRUCE9, C0), C.region(CRUCE9, 5, C1)
        self.add(eje, c0, c1, r0, r1)
        self.empate()
        self.tres()
        self.wait(1.0)
        self.limpiar()

    def empate(self):
        C = self.C
        h = C.f(0, CRUCE9, P0)
        foco = C.p(CRUCE9) + UP * 1.15          # el cruce, con el eje y sus números dentro del cuadro
        cx = C.p(CRUCE9)[0]
        with self.narrar("b1"):
            # «justo en el cruce»
            self.en("zoom")
            self.zoom(foco, 6.0, run_time=self.dur(0.9))

            # «Ahí hay empate»
            self.en("empate")
            s0 = Line(C.p(CRUCE9) + LEFT * 0.09, C.p(CRUCE9, h) + LEFT * 0.09, color=C0, stroke_width=7)
            s1 = Line(C.p(CRUCE9) + RIGHT * 0.09, C.p(CRUCE9, h) + RIGHT * 0.09, color=C1, stroke_width=7)
            emp = Text("Empate", color=ESTIMACION, weight=BOLD).scale(0.45).move_to([cx - 1.6, -0.2, 0])
            self.play(Create(s0), Create(s1), run_time=self.dur(0.4))
            self.pop(emp)

            # «falla lo mismo»
            self.en("igual")
            ig = MathTex("=", color=ESTIMACION).scale(0.55).move_to(C.p(CRUCE9, h / 2) + RIGHT * 0.42)
            self.play(FadeIn(ig), run_time=self.dur(0.3))

            # «exactamente ese valor»
            self.en("linea")
            fina = Line(C.p(CRUCE9), C.p(CRUCE9) + UP * 2.3, color=TXT, stroke_width=1.2)
            self.play(FadeOut(s0), FadeOut(s1), FadeOut(ig), Create(fina), run_time=self.dur(0.5))

            # «es»
            self.en("cero")
            p0 = Text("Probabilidad 0", color=TXT).scale(0.38).move_to([cx + 1.75, -2.0, 0])
            self.play(FadeIn(p0), run_time=self.dur(0.4))

            # «en la frontera»
            self.en("frontera")
            self.play(fina.animate.set_stroke(ESTIMACION, 3), run_time=self.dur(0.4))

            # «lo que quieras»
            self.en("moneda")
            mon = moneda("").scale(0.45).move_to([cx + 1.3, -0.2, 0])
            self.play(FadeIn(mon), run_time=self.dur(0.2))
            self.play(mon.animate(rate_func=there_and_back).stretch(0.05, 0), run_time=self.dur(0.35))
            self.play(mon.animate(rate_func=there_and_back).stretch(0.05, 0), run_time=self.dur(0.35))

            # «sigue»
            self.en("mejor")
            self.play(FadeOut(VGroup(emp, p0, mon, fina)), run_time=self.dur(0.2))
            self.zoom_reset(run_time=self.dur(0.8))
            mp = VGroup(Text("MAP", color=ESTIMACION, weight=BOLD).scale(0.7), tilde(VERDE, 0.55))
            mp.arrange(RIGHT, buff=0.3).move_to([0, 2.7, 0])
            self.pop(mp)

    def tres(self):
        C = Campanas9(centro=(0.0, -2.3), ancho=12.0, r_rango=(-2.4, 6.4))
        with self.narrar("b2"):
            # «más de dos hipótesis»
            self.en("mas")
            self.corte()
            base = Line(C.p(C.r0), C.p(C.r1), color=INK, stroke_width=2.4)
            fantasmas = [C.campana(m, 1, INK).set_stroke(opacity=0.3) for m in (0, 2, 4)]
            self.play(Create(base), *[Create(f) for f in fantasmas], run_time=self.dur(0.9))

            # «no cambia nada»
            self.en("nada")
            mr = Text("Misma regla", color=ESTIMACION, weight=BOLD).scale(0.65).move_to([0, 3.3, 0])
            self.pop(mr)

            # «cero, dos o»
            self.en("niveles")
            nv = VGroup(*[Text(f"{v} V", color=INK).scale(0.5).move_to(C.p(v) + DOWN * 0.35) for v in (0, 2, 4)])
            self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.15) for n in nv], lag_ratio=0.3), run_time=self.dur(0.6))

            # «tres campanas»
            self.en("tres")
            cols = (C0, C1, VERDE)
            cs = [C.campana(m, 1, c) for m, c in zip((0, 2, 4), cols)]
            self.play(LaggedStart(*[ReplacementTransform(f, c) for f, c in zip(fantasmas, cs)], lag_ratio=0.25),
                      run_time=self.dur(0.9))

            # «escalada por su probabilidad a»
            self.en("escala")
            ks = VGroup(*[MathTex(rf"\times\, p_{i}", color=c).scale(0.75).move_to(C.p(m, 0.4) + UP * 0.45)
                          for i, (m, c) in enumerate(zip((0, 2, 4), cols))])
            self.play(FadeIn(ks), run_time=self.dur(0.3))
            fs = (0.75, 1.25, 0.9)
            self.play(*[Transform(c, C.campana(m, f, col)) for c, m, f, col in zip(cs, (0, 2, 4), fs, cols)],
                      run_time=self.dur(0.6))

            # «ganaría la más alta»
            self.en("alta")
            t = np.linspace(C.r0, C.r1, 240)
            env = C.L.curva(t, np.max([C.f(m, t, f) for m, f in zip((0, 2, 4), fs)], axis=0), ESTIMACION, 7,
                            opacidad=0.85)
            cur = Line(C.p(C.r0), C.p(C.r0) + UP * 3.3, color=MEDIDA, stroke_width=3)
            self.add(cur)
            self.play(Create(env), cur.animate.shift(C.p(C.r1) - C.p(C.r0)), run_time=self.dur(2.0), rate_func=linear)
            self.play(FadeOut(cur), FadeOut(env), run_time=self.dur(0.3))

            # «igual de probables»
            self.en("iguales")
            self.play(*[Transform(c, C.campana(m, 1, col)) for c, m, col in zip(cs, (0, 2, 4), cols)],
                      run_time=self.dur(0.6))

            # «en uno y en tres»
            self.en("umbrales")
            us = VGroup(*[Line(C.p(u) + DOWN * 0.12, C.p(u) + UP * 2.4, color=ESTIMACION, stroke_width=4) for u in (1, 3)])
            regs = VGroup(C.region(C.r0, 1, C0), C.region(1, 3, C1), C.region(3, C.r1, VERDE))
            self.play(Create(us), FadeIn(regs), run_time=self.dur(0.6))
