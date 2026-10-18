"""Escena 01 — Gancho: el dado nunca saca 3,5, pero el promedio sí."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        R = Regla7(centro=(0, -1.8), ancho=9.6, rotulos=False)
        caras = caras7(R, escala=0.9, altura=1.2)
        d = dado_n(5).scale(1.7).move_to([0, 0.2, 0])
        L = Lienzo(ancho=9.8, alto=3.2, t_rango=(0, 1000), v_max=2.6, centro=(0, -0.6))
        t = np.arange(1, 1001)
        curva = L.curva(t, promedios_dado(1000) - 3.5, SENAL, 3)
        mu = MathTex(r"\mu", color=AMBAR).scale(2.0).move_to([-2.8, 2.9, 0])
        s2 = MathTex(r"\sigma^2", color=AMBAR).scale(2.0).move_to([2.8, 2.9, 0])
        with self.narrar("b1"):
            # «Un dado nunca saca»
            self.en("dado")
            self.play(FadeIn(d, scale=0.4), Rotate(d, angle=2 * PI), run_time=self.dur(0.9))

            # «tres coma cinco»
            self.en("valor")
            self.play(FadeOut(d), FadeIn(R), FadeIn(caras), run_time=self.dur(0.6))
            x = cruz(ROJO, 0.7).move_to(R.p(3.5) + UP * 1.2)
            lab = Text("3,5", color=AMBAR, weight=BOLD).scale(0.7).move_to(R.p(3.5) + UP * 2.2)
            self.play(Create(x), FadeIn(lab), run_time=self.dur(0.6))

            # «lo tiras mil veces»
            self.en("mil")
            self.corte()
            self.play(Create(L.base()), run_time=0.3)
            self.play(Create(curva), run_time=self.dur(1.9), rate_func=linear)

            # «clavado en tres coma cinco»
            self.en("clavado")
            linea = DashedLine(L.p(0, 0), L.p(1000, 0), color=AMBAR, stroke_width=3)
            l35 = Text("3,5", color=AMBAR, weight=BOLD).scale(0.6).move_to(L.p(1000, 0) + RIGHT * 0.55)
            self.play(Create(linea), run_time=0.4)
            self.pop(l35)

            # «dos números»
            self.en("dos")
            self.play(curva.animate.set_stroke(opacity=0.35), FadeOut(linea), FadeOut(l35), run_time=0.3)
            self.pop(mu, s2)

            # «la media y la varianza»
            self.en("nombres")
            self.play(FadeIn(Text("Media", color=TXT).scale(0.6).next_to(mu, DOWN, buff=0.2)),
                      FadeIn(Text("Varianza", color=TXT).scale(0.6).next_to(s2, DOWN, buff=0.2)),
                      run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
