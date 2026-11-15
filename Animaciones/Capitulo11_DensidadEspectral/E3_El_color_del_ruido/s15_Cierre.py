"""Escena 15 — Cierre: resumen del episodio y la pregunta del siguiente."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        mon = moneda("", AMBAR).scale(1.5).move_to([-5.2, 2.2, 0])
        lista = VGroup(*[Text(t, color=c, weight=BOLD).scale(0.75) for t, c in
                         (("sin memoria", SENAL), ("espectro plano", AMBAR), ("media cero", VERDE))])
        lista.arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([-3.9, -0.6, 0])
        resumen = Text("resumen", color=INK, weight=BOLD).scale(0.6).move_to([-3.9, 1.0, 0])
        formulas = MathTex(r"R_{xx}(\tau)", "=", r"e^{-2|\tau|}", color=TXT).scale(1.1).move_to([3.4, 2.4, 0])
        nadie = MathTex(r"R_{xx}(\tau)", "=", "?", color=AMBAR).scale(1.2).move_to([3.4, 0.6, 0])
        archivo = documento(INK).scale(2.0).move_to([3.4, -1.4, 0])
        nums = VGroup(*[Text(t, color=INK).scale(0.28) for t in ("0,3  1,2  −0,8", "0,9  −1,1  0,2", "−0,4  0,7  1,5")])
        nums.arrange(DOWN, buff=0.12).move_to(archivo)
        titulo_e4 = Text("Un espectro a partir de datos", color=AMBAR, weight=BOLD).scale(0.85).move_to([0, -3.4, 0])
        with self.narrar("b1"):
            # «el blanco existe de verdad»
            self.en("existe")
            ok = tilde().scale(1.0).next_to(mon, RIGHT, buff=0.3)
            self.play(FadeIn(mon), FadeIn(ok), run_time=self.dur(0.6))
            # «Resumen del episodio»
            self.en("resumen")
            self.play(FadeIn(resumen), run_time=self.dur(0.4))
            # «sin memoria»
            self.en("sinmem")
            self.play(FadeIn(lista[0]), run_time=self.dur(0.4))
            # «espectro plano»
            self.en("plano")
            self.play(FadeIn(lista[1]), run_time=self.dur(0.4))
            # «media cero»
            self.en("mu0")
            self.play(FadeIn(lista[2]), run_time=self.dur(0.4))
            # «autocorrelaciones conocidas»
            self.en("conocidas")
            self.play(FadeIn(formulas), run_time=self.dur(0.6))
            # «nadie te da la autocorrelación»
            self.en("nadie")
            self.play(FadeIn(nadie), FadeIn(cruz(ROJO, 1.0).move_to([4.9, 0.6, 0])), run_time=self.dur(0.6))
            # «un archivo con datos»
            self.en("archivo")
            self.play(FadeIn(archivo), FadeIn(nums), run_time=self.dur(0.6))
            # «un espectro a partir de datos»
            self.en("titulo_e4")
            self.sfx("pop")
            self.play(FadeIn(titulo_e4, shift=UP * 0.3), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
