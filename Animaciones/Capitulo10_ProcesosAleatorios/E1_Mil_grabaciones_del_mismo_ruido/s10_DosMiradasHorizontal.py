"""Escena 10 — Congelar el resultado da una señal determinista; el proceso tiene dos caras."""
from comun.escena import *


class DosMiradasHorizontal(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        cos = CuatroCosenos()
        with self.narrar("b1"):
            self.play(FadeIn(cos), run_time=0.6)
            b1 = VGroup(Circle(0.27, color=INK, stroke_width=3), Text("1", color=INK, weight=BOLD).scale(0.4))
            b2 = VGroup(Circle(0.27, color=INK, stroke_width=3), Text("2", color=INK, weight=BOLD).scale(0.4))
            b1.move_to([-6.5, 3.55, 0])
            b2.move_to([-5.8, 3.55, 0])
            self.play(FadeIn(b1), FadeIn(b2), run_time=0.3)

            # «congela el resultado»
            self.en("resultado")
            self.play(b2.animate.set_stroke(AMBAR), b2[1].animate.set_color(AMBAR), run_time=self.dur(0.5))

            # «un solo oscilador»
            self.en("uno")
            otras = [0, 2, 3]
            self.play(*[cos.curvas[i].animate.set_stroke(opacity=0.14) for i in otras],
                      *[cos.rotulos[i].animate.set_opacity(0.14) for i in otras],
                      *[cos.bases[i].animate.set_stroke(opacity=0.14) for i in otras],
                      cos.curvas[1].animate.set_stroke(AMBAR, width=6), run_time=self.dur(0.8))

            # «recórrelo de izquierda a derecha»
            self.en("recorre")
            tr = ValueTracker(cos.t0)
            punto = always_redraw(lambda: Dot(cos.punto(1, tr.get_value()), radius=0.14, color=TXT))
            self.add(punto)
            self.play(tr.animate.set_value(cos.t1), run_time=self.dur(3.2), rate_func=linear)
            punto.clear_updaters()

            # «nada de aleatorio»
            self.en("sin_azar")
            sa = Text("sin azar", color=TXT, weight=BOLD).scale(0.8).move_to([-2.5, 3.55, 0])
            self.pop(sa)

            # «un coseno desplazado»
            self.en("desplazado")
            fo = formula(r"\cos(\omega_0 t+90^\circ)", color=AMBAR, escala=1.1).move_to([3.0, 3.55, 0])
            self.pop(fo)

            # «señal determinista»
            self.en("determinista")
            det = Text("señal determinista", color=AMBAR, weight=BOLD).scale(0.8).move_to([1.1, -3.55, 0])
            self.pop(det)

        with self.narrar("b2"):
            self.play(FadeOut(punto), FadeOut(sa), FadeOut(fo), FadeOut(det), FadeOut(b1), FadeOut(b2),
                      *[cos.curvas[i].animate.set_stroke(opacity=1.0) for i in otras],
                      *[cos.bases[i].animate.set_stroke(opacity=1.0) for i in otras],
                      cos.curvas[1].animate.set_stroke(SENAL, width=3.2),
                      FadeOut(cos.rotulos), run_time=0.4)
            corte0, corte1 = cos.corte(0.0), cos.corte(0.25)
            corte1.set_stroke(opacity=0)
            grupo = VGroup(cos, corte0)
            self.add(corte0, corte1)
            grupo.add(corte1)

            # «dos caras»
            self.en("caras")
            self.play(grupo.animate.scale(0.62).move_to([-3.6, 0, 0]), run_time=0.7)
            vertical = Arrow([3.6, -2.5, 0], [3.6, 2.6, 0], color=AMBAR, stroke_width=6, buff=0)
            horizontal = Arrow([0.4, 0.0, 0], [6.8, 0.0, 0], color=SENAL, stroke_width=6, buff=0)
            self.play(GrowArrow(vertical), GrowArrow(horizontal), run_time=self.dur(0.8))

            # «En vertical»
            self.en("vert")
            l_v = Text("variable aleatoria", color=AMBAR, weight=BOLD).scale(0.6).rotate(PI / 2).move_to([4.15, 1.3, 0])
            self.play(FadeIn(l_v, shift=UP * 0.2), vertical.animate(rate_func=there_and_back).set_stroke(width=11),
                      run_time=self.dur(0.9))

            # «En horizontal»
            self.en("horiz")
            l_h = Text("señal", color=SENAL, weight=BOLD).scale(0.7).move_to([6.0, 0.45, 0])
            self.play(FadeIn(l_h, shift=LEFT * 0.2), horizontal.animate(rate_func=there_and_back).set_stroke(width=11),
                      run_time=self.dur(0.9))

            # «todo lo que viene en este capítulo»
            self.en("todo")
            for _ in range(2):
                self.play(vertical.animate(rate_func=there_and_back).set_stroke(width=11), run_time=0.55)
                self.play(horizontal.animate(rate_func=there_and_back).set_stroke(width=11), run_time=0.55)

            # «pasar de una lectura a la otra»
            self.en("pasar")
            self.play(vertical.animate.set_stroke(width=9), horizontal.animate.set_stroke(width=3), run_time=0.5)
            self.play(vertical.animate.set_stroke(width=3), horizontal.animate.set_stroke(width=9), run_time=0.5)
            self.play(vertical.animate.set_stroke(width=6), horizontal.animate.set_stroke(width=6), run_time=self.dur(0.5))

            # «más de un corte»
            self.en("cortes")
            self.play(corte1.animate.set_stroke(opacity=1.0), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
