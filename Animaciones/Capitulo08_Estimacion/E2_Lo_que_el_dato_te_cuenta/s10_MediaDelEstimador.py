"""Escena 10 — El estimador no se desvía: su media es la media de lo enviado (la torre del capítulo 7)."""
from comun.escena import *


class MediaDelEstimador(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        y0 = -1.2
        h = 4.0
        x45, x79 = -5.2, -0.9
        base = Line([-6.4, y0, 0], [0.6, y0, 0], color=INK, stroke_width=3)
        b45 = Rectangle(width=1.0, height=0.66 * h, color=VERDE, stroke_width=2.5).set_fill(VERDE, 0.5)
        b45.move_to([x45, y0 + 0.66 * h / 2, 0])
        b79 = Rectangle(width=1.0, height=0.34 * h, color=VERDE, stroke_width=2.5).set_fill(VERDE, 0.5)
        b79.move_to([x79, y0 + 0.34 * h / 2, 0])
        e45 = MathTex(r"0{,}045", color=INK).scale(1.0).move_to([x45, y0 - 0.5, 0])
        e79 = MathTex(r"0{,}79", color=INK).scale(1.0).move_to([x79, y0 - 0.5, 0])
        p66 = MathTex(r"0{,}66", color=VERDE).scale(1.1).next_to(b45, UP, buff=0.12)
        p34 = MathTex(r"0{,}34", color=VERDE).scale(1.1).next_to(b79, UP, buff=0.12)
        xm = x45 + (x79 - x45) * (0.3 - 0.045) / (0.79 - 0.045)
        fiel = Triangle(color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.6).scale(0.35).move_to([-3.3, y0 - 1.2, 0])
        t1 = MathTex(r"0{,}34\cdot 0{,}79=0{,}27", color=TXT).scale(1.1).move_to([3.3, 3.1, 0])
        t2 = MathTex(r"+\ 0{,}66\cdot 0{,}045=0{,}03", color=TXT).scale(1.1).move_to([3.3, 2.0, 0])
        r03 = MathTex(r"=\ 0{,}3", color=VERDE).scale(2.0).move_to([2.7, 0.7, 0])
        env = MathTex(r"E[S]=0{,}3", color=SENAL).scale(1.4).move_to([3.3, -0.7, 0])
        torre = MathTex(r"E\big[\,E[S\mid R]\,\big]=E[S]", color=AMBAR).scale(1.2).move_to([3.0, -2.1, 0])
        with self.narrar("b1"):
            # «tiene media»
            self.en("media")
            self.play(Create(base), FadeIn(b45), FadeIn(b79), FadeIn(e45), FadeIn(e79), FadeIn(p66), FadeIn(p34),
                      run_time=self.dur(0.8))
            self.play(FadeIn(fiel), run_time=self.dur(0.3))

            # «Cero coma treinta y cuatro por cero coma setenta y nueve»
            self.en("t1")
            self.play(FadeIn(t1, shift=UP * 0.2), run_time=self.dur(0.5))

            # «más cero coma sesenta y seis por cero coma cero cuatro cinco»
            self.en("t2")
            self.play(FadeIn(t2, shift=UP * 0.2), run_time=self.dur(0.5))

            # «cero coma tres»
            self.en("r03")
            self.pop(r03)
            self.play(fiel.animate.move_to([xm, y0 - 1.2, 0]), run_time=self.dur(0.6))

            # «la media de lo enviado»
            self.en("enviado")
            self.pop(env)

            # «la propiedad de la torre»
            self.en("torre")
            self.pop(torre)

            # «del capítulo siete»
            self.en("cap7")
            c7 = etiqueta("Capítulo 7", INK, 0.65).move_to([5.6, -3.2, 0])
            self.play(FadeIn(c7), run_time=self.dur(0.3))

            # «Quiere decir»
            self.en("quiere")
            self.resaltar(fiel, color=VERDE)

            # «en promedio, no se desvía»
            self.en("no_desvia")
            ok = tilde(VERDE, 0.6).move_to([-4.0, y0 - 2.4, 0])
            sin = Text("Sin sesgo", color=VERDE, weight=BOLD).scale(0.8).next_to(ok, RIGHT, buff=0.25)
            self.sfx("exito")
            self.play(Create(ok), FadeIn(sin), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
