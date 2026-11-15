"""Escena 08 — Correlación cero no es «sin relación»: el rombo de los osciladores desfasados."""
from comun.escena import *


class TrampaDelRombo(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        cos = CuatroCosenos(ancho=5.4, paso=1.2, amp=0.42, centro=(-3.3, -0.1))
        rombo = Rombo(centro=(3.4, -0.3), radio=1.4)
        with self.narrar("b1"):
            # «una trampa que ya conoces»
            self.en("trampa")
            aviso = VGroup(Triangle(color=AMBAR, stroke_width=5).scale(0.6).set_fill(AMBAR, 0.15),
                           Text("!", color=AMBAR, weight=BOLD).scale(0.8))
            aviso[1].move_to(aviso[0].get_center() + DOWN * 0.05)
            aviso.move_to([-5.6, 3.2, 0])
            self.pop(aviso)

            # «Entre cero y un cuarto de período»
            self.en("entre")
            c1 = cos.corte(0.0, AMBAR)
            c2 = cos.corte(0.25, TXT)
            self.play(Create(VGroup(*cos.bases, *cos.curvas)), FadeIn(cos.rotulos), run_time=self.dur(0.8))
            self.play(Create(c1), Create(c2), run_time=0.4)

            # «la autocorrelación es cero»
            self.en("cero")
            F = formula("R_{XX}", "(", "0", ",", r"\tfrac14", ")", "=", "0", escala=1.1,
                        colores={0: AMBAR, 7: AMBAR}).move_to([3.4, 3.0, 0])
            self.pop(F)

            # «si el primer valor es uno»
            self.en("uno")
            ex = formula("X(0)", escala=0.7, color=INK).move_to(rombo.p(1.5, 0) + RIGHT * 0.3 + DOWN * 0.35)
            ey = formula(r"X(\tfrac14)", escala=0.7, color=INK).move_to(rombo.p(0, 1.6) + RIGHT * 0.55)
            self.play(Create(rombo.ejes), FadeIn(ex), FadeIn(ey), *[FadeIn(d, scale=0.4) for d in rombo.puntos],
                      run_time=self.dur(0.8))
            p0 = rombo.puntos[0]
            self.play(p0.animate.set_color(AMBAR).scale(1.6), run_time=0.4)

            # «el segundo es cero»
            self.en("segundo0")
            lab = MathTex(r"X(\tfrac14)=0", color=AMBAR).scale(0.8).move_to(rombo.p(1, 0) + UP * 0.65 + RIGHT * 0.2)
            self.pop(lab)

            # «Los puntos del rombo»
            self.en("rombo")
            self.play(LaggedStart(*[d.animate.set_color(AMBAR).scale(1.4) for d in rombo.puntos[1:]], lag_ratio=0.25),
                      run_time=self.dur(0.9))

            # «dependen totalmente»
            self.en("depende")
            s = sello("dependen", ROJO).scale(0.8).move_to([3.4, -3.2, 0])
            self.pop(s)

            # «aunque no estén en línea recta»
            self.en("no_recta")
            ajuste = Line(rombo.p(-1.25, 0), rombo.p(1.25, 0), color=ESTIMACION, stroke_width=7)
            al = Text("recta de ajuste: plana", color=ESTIMACION).scale(0.45).move_to([3.4, -2.4, 0])
            self.play(Create(ajuste), FadeIn(al), run_time=self.dur(0.7))

            # «Correlación cero no quiere decir»
            self.en("cero_no")
            a = Text("correlación 0", color=TXT, weight=BOLD).scale(0.6)
            b = Text("≠  no hay relación", color=ROJO, weight=BOLD).scale(0.6)
            fila = VGroup(a, b).arrange(RIGHT, buff=0.4).move_to([-3.3, -3.3, 0])
            self.play(FadeIn(a, shift=UP * 0.15), run_time=0.4)
            self.pop(b)

            # «que no haya relación»
            self.en("sin_rel")
            self.play(b.animate(rate_func=there_and_back).scale(1.15), run_time=0.6)

            # «no hay relación en línea recta»
            self.en("solo_recta")
            solo = Text("solo en línea recta", color=AMBAR, weight=BOLD).scale(0.55).move_to([-3.3, -3.8, 0])
            self.pop(solo)
        self.wait(1.0)
        self.limpiar()
