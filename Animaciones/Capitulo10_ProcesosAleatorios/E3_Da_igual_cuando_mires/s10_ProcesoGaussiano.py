"""Escena 10 — Con ruido gaussiano, estricta y amplia coinciden."""
from comun.escena import *


class ProcesoGaussiano(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        L = Lienzo(ancho=5.4, alto=2.2, t_rango=(0, 1), v_max=2.2, centro=(3.2, 0.4))
        pila = pila_de_curvas(L, 10, semilla=11, a=0.93, color=SENAL, opacidad=0.5, ancho=2.2, escala=0.5)

        with self.narrar("b1"):
            # «exactamente lo mismo»
            self.en("igual")
            f = MathTex(r"\text{WSS}", r"\Longleftrightarrow", r"\text{SSS}", color=TXT).scale(1.3).move_to([0, 3.0, 0])
            self.pop(f)

            # «el proceso gaussiano»
            self.en("gaussiano")
            camp = campana_mini((-4.3, 0.4), 3.0, 1.8, SENAL, 5)
            base = Line([-5.9, -0.5, 0], [-2.7, -0.5, 0], color=INK, stroke_width=2)
            tag = etiqueta("gaussiano", AMBAR, 0.6, BOLD).move_to([-4.3, 1.9, 0])
            self.play(Create(base), Create(camp), FadeIn(tag), FadeIn(pila), run_time=self.dur(1.0))

            # «la media y la autocovarianza»
            self.en("mu_c")
            cm = caja_tex(r"\mu(t)", AZUL, ancho=1.7, alto=0.9).move_to([-5.4, -2.7, 0])
            cc = caja_tex(r"C_{XX}", VERDE, ancho=1.7, alto=0.9).move_to([-3.4, -2.7, 0])
            self.play(FadeIn(cm, shift=UP * 0.2), FadeIn(cc, shift=UP * 0.2), run_time=self.dur(0.6))

            # «lo determinan entero»
            self.en("determinan")
            marco = RoundedRectangle(corner_radius=0.2, width=5.9, height=2.9, color=AMBAR, stroke_width=4).move_to([3.2, 0.4, 0])
            fl = Arrow([-2.4, -2.7, 0], [1.6, -0.9, 0], color=AMBAR, buff=0, stroke_width=4)
            self.play(Create(marco), Create(fl), run_time=self.dur(0.8))

            # «no cambian al desplazar»
            self.en("no_cambian")
            v1, v2 = L.vertical(0.25, AMBAR, 3.5, mitad=1.0), L.vertical(0.5, AMBAR, 3.5, mitad=1.0)
            self.play(Create(v1), Create(v2), run_time=0.4)
            self.play(v1.animate.shift(RIGHT * 1.0), v2.animate.shift(RIGHT * 1.0), run_time=self.dur(0.8))

            # «no cambia nada»
            self.en("nada")
            t = tilde(VERDE, 0.6).move_to([6.2, 2.4, 0])
            self.pop(t)
            self.play(*[FadeOut(m) for m in (cm, cc, fl)], run_time=0.25)

            # «casi nadie trabaja con la estricta»
            self.en("nadie")
            sss = caja("SSS", AZUL, ancho=2.0, alto=0.8).move_to([-2.4, -2.9, 0])
            wss = caja("WSS", VERDE, ancho=2.0, alto=0.8).move_to([2.4, -2.9, 0])
            self.play(FadeIn(sss), FadeIn(wss), run_time=0.3)
            self.play(sss.animate.fade(0.65), run_time=0.4)

            # «la amplia ya lo dice todo»
            self.en("dice_todo")
            self.resaltar(wss, color=AMBAR, escala=1.12)

            # «más fácil de comprobar»
            self.en("facil")
            ds = etiqueta("infinitas densidades", INK, 0.45).next_to(sss, DOWN, buff=0.15)
            dw = MathTex(r"\mu \text{ y } R", color=AMBAR).scale(0.8).next_to(wss, DOWN, buff=0.12)
            self.play(FadeIn(ds), FadeIn(dw), run_time=0.5)
        self.wait(1.0)
        self.limpiar()
