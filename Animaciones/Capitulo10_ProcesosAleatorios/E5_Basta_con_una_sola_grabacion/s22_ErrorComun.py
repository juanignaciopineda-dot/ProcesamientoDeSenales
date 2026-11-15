"""Escena 22 — El error común con datos con memoria, y las dos caras de la memoria."""
from comun.escena import *


class ErrorComun(EscenaCurso):
    ESCENA = "22"

    def construct(self):
        with self.narrar("b1"):
            # «error de una media»
            self.en("error")
            e = MathTex(r"\text{error}\approx\frac{\sigma}{\sqrt{N}}", color=TXT).scale(1.3).move_to([0, 2.9, 0])
            self.play(Write(e), run_time=self.dur(0.8))

            # «como si los datos fueran independientes»
            self.en("tachada")
            tach = tachar(e)
            nuevo = MathTex(r"\frac{\sigma}{\sqrt{N_{\mathrm{ef}}}}", color=AMBAR).scale(1.3).move_to([4.6, 2.9, 0])
            self.play(Create(tach), run_time=0.4)
            self.play(FadeIn(nuevo, shift=RIGHT * 0.2), run_time=0.4)

            # «cuando tienen memoria»
            self.en("memoria")
            fila = fila_puntos(18, 7.0, (0, 1.3), SENAL, 0.1)
            hilos = hilos_entre(fila, AMBAR, 3)
            self.play(FadeIn(fila), Create(hilos), run_time=self.dur(1.0))

            # «mucho más preciso»
            self.en("preciso")
            falsa = Line([-1.0, -0.2, 0], [1.0, -0.2, 0], color=ROJO, stroke_width=8)
            tf = etiqueta("falso", ROJO, 0.55).next_to(falsa, LEFT, buff=0.3)
            self.play(Create(falsa), FadeIn(tf), run_time=self.dur(0.7))

            # «de lo que es»
            self.en("real")
            real = Line([-2.0, -1.2, 0], [2.0, -1.2, 0], color=VERDE, stroke_width=8)
            tr = etiqueta("real", VERDE, 0.55).next_to(real, LEFT, buff=0.3)
            self.play(Create(real), FadeIn(tr), run_time=self.dur(0.7))

            # «dos caras»
            self.en("caras")
            self.corte()
            c1 = RoundedRectangle(corner_radius=0.2, width=3.8, height=2.4, color=VERDE, stroke_width=3).move_to([-4.3, 0.6, 0])
            c2 = RoundedRectangle(corner_radius=0.2, width=3.8, height=2.4, color=ROJO, stroke_width=3).move_to([0, 0.6, 0])
            self.play(Create(c1), Create(c2), run_time=self.dur(0.8))

            # «se borra»
            self.en("borra")
            t1 = self.palabra("se borra", VERDE, 0.8).move_to(c1.get_center())
            self.pop(t1)

            # «promediar en el tiempo funciona»
            self.en("funciona")
            r1 = self.texto_centrado("promediar", "funciona", color=VERDE, escala=0.5).next_to(c1, DOWN, buff=0.3)
            tl = tilde(VERDE, 0.4).next_to(r1, DOWN, buff=0.15)
            self.play(FadeIn(r1), FadeIn(tl), run_time=0.5)

            # «Pero mientras dura»
            self.en("dura")
            t2 = self.palabra("dura", ROJO, 0.8).move_to(c2.get_center())
            self.pop(t2)

            # «cada muestra cuenta menos»
            self.en("menos")
            r2 = self.texto_centrado("cada muestra", "cuenta menos", color=ROJO, escala=0.5).next_to(c2, DOWN, buff=0.3)
            self.play(FadeIn(r2), run_time=0.5)

            # «una tercera cara»
            self.en("tercera")
            c3 = RoundedRectangle(corner_radius=0.2, width=3.8, height=2.4, color=INK, stroke_width=3).set_fill(INK, 0.25)
            c3.move_to([4.3, 0.6, 0])
            q = self.palabra("¿?", TXT, 1.6).move_to(c3)
            self.play(FadeIn(c3, shift=LEFT * 0.3), run_time=0.4)
            self.pop(q)
        self.wait(1.0)
        self.limpiar()
