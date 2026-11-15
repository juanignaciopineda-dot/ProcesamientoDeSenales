"""Escena 05 — El máximo de la salida, menos el retardo del filtro, es el retardo del eco."""
from comun.escena import *


class ElPicoDaElRetardo(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        sal = Tallos([0, 0, 0, 2, 6, 9, 6, 2, 0, 0], centro=(0.0, -0.5), paso=0.8, unidad=0.27, color=ESTIMACION,
                     indices=True)
        anillo = Circle(radius=0.22, color=AMBAR, stroke_width=4).move_to(sal.pos(5))
        n5 = MathTex("n=5", color=AMBAR).scale(0.8).move_to([sal.x(5), -1.35, 0])
        rf = caja("retardo del filtro", AMBAR, ancho=3.6, alto=0.75, scale=0.5).move_to([-4.6, 2.4, 0])
        dos = MathTex("2", color=AMBAR).scale(0.9).next_to(rf, DOWN, buff=0.2)
        cuenta = formula("5", "-", "2", "=", "3", escala=1.3,
                         colores={4: VERDE, 2: AMBAR, 0: AMBAR}).move_to([2.4, -2.6, 0])
        dtxt = MathTex("D=3", color=AMBAR).scale(1.0).move_to([-3.3, -2.6, 0])
        mini = Tallos([2, 2, 1], centro=(-5.3, -2.6), paso=0.3, unidad=0.2)
        ok = tilde(VERDE, 0.5).move_to([-1.8, -2.6, 0])
        dgen = MathTex("D", color=AMBAR).scale(1.0).move_to(dtxt)
        f = formula(r"\text{salida}", "=", "R_{ss}", "[n-D]", escala=0.95,
                    colores={0: ESTIMACION, 2: AMBAR}).move_to([-3.9, 3.4, 0])
        maxi = Text("máx", color=AMBAR, weight=BOLD).scale(0.55).move_to([sal.x(5), 2.65, 0])
        fm = CurvedArrow([sal.x(5) - 0.5, 2.65, 0], [-3.3, -2.0, 0], color=AMBAR, angle=PI / 3)
        with self.narrar("b1"):
            # «El pico está»
            self.en("pico")
            self.play(FadeIn(sal), run_time=self.dur(0.7))
            self.play(Create(anillo), run_time=0.4)
            # «en el instante cinco»
            self.en("cinco")
            self.pop(n5)
            # «Restamos el retardo del propio filtro»
            self.en("resta")
            self.play(FadeIn(rf), run_time=self.dur(0.5))
            # «dos muestras»
            self.en("dosm")
            self.pop(dos)
            # «y sale tres»
            self.en("tres")
            self.play(FadeIn(cuenta), run_time=self.dur(0.9))
            # «justo el retardo con el que llegó el pulso»
            self.en("justo")
            self.pop(dtxt)
            # «con el que llegó el pulso»
            self.en("llego")
            self.play(FadeIn(mini), FadeIn(ok), run_time=self.dur(0.6))
            # «si el eco llega con cierto retardo»
            self.en("cierto")
            self.play(FadeOut(rf), FadeOut(dos), Transform(dtxt, dgen), run_time=self.dur(0.6))
            # «la salida es la autocorrelación»
            self.en("salidar")
            self.play(FadeIn(f[0]), FadeIn(f[1]), FadeIn(f[2]), run_time=self.dur(0.7))
            # «corrida esas mismas muestras»
            self.en("corrida")
            self.play(FadeIn(f[3]), run_time=0.3)
            self.play(sal.animate(rate_func=there_and_back).shift(RIGHT * 1.0), run_time=self.dur(0.8))
            # «Buscamos el máximo de la salida»
            self.en("maximo")
            self.pop(maxi)
            # «su posición nos dice el retardo»
            self.en("posicion")
            self.play(Create(fm), run_time=self.dur(0.9))
        self.wait(1.0)
        self.limpiar()
