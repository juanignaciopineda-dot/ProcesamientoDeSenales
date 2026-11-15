"""Escena 19 — Cierre de la serie: el mapa del curso y una flecha con su sombra."""
from comun.escena import *

NOMBRES = ["probabilidad", "estimación", "hipótesis", "procesos", "espectros", "Wiener", "detección"]
CAPS = [7, 8, 9, 10, 11, 12, 13]
XS = [-5.4 + 1.8 * i for i in range(7)]
Y = 0.2


class Cierre(EscenaCurso):
    ESCENA = "19"

    def construct(self):
        L = Lienzo(ancho=6.0, alto=1.4, t_rango=(0, 160), v_max=2.2, centro=(0, 2.6))
        senal = L.curva(np.arange(160), serie(4, 160, 0.9) + 0.4 * serie(17, 160, 0.0), RUIDO, 3)
        pregunta = Text("¿predecirla?", color=INK).scale(0.5).move_to([4.3, 2.6, 0])
        linea = Line([XS[0], Y, 0], [XS[-1], Y, 0], color=INK, stroke_width=3)
        est = []
        for i in range(7):
            c = Circle(radius=0.42, color=AMBAR if i == 6 else AZUL, stroke_width=4).set_fill(FONDO, 1).move_to([XS[i], Y, 0])
            n = Text(str(CAPS[i]), color=TXT, weight=BOLD).scale(0.5).move_to(c)
            nom = Text(NOMBRES[i], color=INK).scale(0.4).move_to([XS[i], Y - 0.95, 0])
            est.append(VGroup(c, n, nom))
        detras = Text("¿qué hay detrás?", color=AMBAR, weight=BOLD).scale(0.7).move_to([0, -2.1, 0])
        arcos = VGroup(*[CurvedArrow([XS[i] + 0.1, Y + 0.45, 0], [XS[i + 1] - 0.1, Y + 0.45, 0], angle=-PI / 3,
                                     color=INK, stroke_width=3, tip_length=0.15) for i in range(6)])
        F, R = flechas_xy(origen=(-2.6, -2.2), largo=4.6, angulo=40)
        with self.narrar("b1"):
            # «una señal que no podíamos predecir»
            self.en("impredecible")
            self.play(Create(senal), FadeIn(pregunta), run_time=self.dur(1.2))
            # «Aprendimos a describirla»
            self.paso("aprendimos", Create(linea), t=0.6)
            # «con probabilidad»
            self.paso("prob", est[0], t=0.5)
            # «con proyecciones»
            self.paso("proyecciones", est[1], t=0.5)
            # «con hipótesis»
            self.paso("hipotesis", est[2], t=0.5)
            # «con procesos y espectros»
            self.en("procesos")
            self.play(FadeIn(est[3]), FadeIn(est[4]), run_time=self.dur(0.7))
            # «con Wiener»
            self.paso("wiener", est[5], t=0.5)
            # «ahora, a detectarla»
            self.en("detectar")
            self.play(FadeIn(est[6]), run_time=0.5)
            self.pop(est[6][0])
            # «Detrás de cada capítulo»
            self.paso("detras", detras, t=0.6)
            # «la misma idea»
            self.en("idea")
            self.play(LaggedStart(*[Create(a) for a in arcos], lag_ratio=0.15), run_time=self.dur(1.2))
            # «Una flecha y su sombra»
            self.en("flechasombra")
            mapa = Group(*[m for m in self.mobjects if m is not self.camera.frame])
            self.play(FadeOut(mapa), run_time=0.6)
            self.play(GrowArrow(F.presente), GrowArrow(F.futuro), Create(F.sombra), Create(F.error), Create(F.recto),
                      run_time=self.dur(1.2))
        with self.narrar("b2"):
            # «Y con esto se cierra la serie»
            self.en("serie")
            self.play(F.presente.animate.scale(0.5, about_point=F.o), F.futuro.animate.scale(0.5, about_point=F.o),
                      F.sombra.animate.scale(0.5, about_point=F.o), F.error.animate.scale(0.5, about_point=F.o),
                      F.recto.animate.scale(0.5, about_point=F.o), run_time=self.dur(0.9))
            # «Gracias»
            self.en("gracias")
            g = self.palabra("Gracias", AMBAR, 1.4).move_to([2.6, -0.8, 0])
            self.pop(g)
            # «hasta el final»
            self.en("final")
            self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=self.dur(2.0))
        self.wait(0.5)
