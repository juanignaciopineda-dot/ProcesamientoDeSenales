"""Escena 11 — El teorema de Bochner: la vuelta del examen, y el filtro con la moneda."""
from comun.escena import *


class Bochner(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        si = self.palabra("sí", VERDE, 3.0).move_to([0, 0.5, 0])
        boch = self.palabra("Bochner", AMBAR, 0.9).move_to([-1.2, 3.1, 0])
        herg = etiqueta("Herglotz · tiempo discreto", INK, 0.55).move_to([-1.2, 2.3, 0])
        izq = RoundedRectangle(corner_radius=0.14, width=3.4, height=1.3, color=SENAL, stroke_width=3).set_fill(SENAL, 0.12).move_to([-4.0, 0.7, 0])
        der = RoundedRectangle(corner_radius=0.14, width=4.6, height=1.3, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.12).move_to([3.6, 0.7, 0])
        t_izq = etiqueta("proceso", TXT, 0.6).move_to(izq)
        t_izq2 = etiqueta("existe un proceso", TXT, 0.55).move_to(izq)
        t_der = etiqueta("real · par · ≥ 0", TXT, 0.6).move_to(der)
        ida = Arrow(izq.get_right() + UP * 0.25, der.get_left() + UP * 0.25, color=INK, buff=0.1, stroke_width=5)
        vuelta = Arrow(der.get_left() + DOWN * 0.25, izq.get_right() + DOWN * 0.25, color=AMBAR, buff=0.1, stroke_width=7)
        estrella = Star(n=5, outer_radius=0.4, color=AMBAR).set_fill(AMBAR, 0.9).move_to([6.2, 2.4, 0])
        mej = etiqueta("lo mejor", AMBAR, 0.5).next_to(estrella, DOWN, buff=0.15)
        bloque = BloqueLTI("?", centro=(0, -2.5), ancho=2.2, alto=1.2)
        r04 = MathTex(r"\rho=0{,}4", color=AMBAR).scale(0.9).move_to([-4.2, -2.5, 0])
        esp = MathTex(r"1+0{,}8\cos\Omega", color=AMBAR).scale(0.9).move_to([4.2, -2.5, 0])
        with self.narrar("b1"):
            self.en("si")
            self.corte()
            self.pop(si)
            self.en("bochner")
            self.play(si.animate.scale(0.35).move_to([-5.9, 3.1, 0]), run_time=0.4)
            self.pop(boch)
            self.en("herglotz")
            self.play(FadeIn(herg), run_time=0.4)
            self.en("vuelta")
            self.play(FadeIn(izq), FadeIn(t_izq), FadeIn(der), Create(ida), run_time=self.dur(0.7))
            self.play(Create(vuelta), run_time=self.dur(0.6))
            self.en("tres")
            self.play(FadeIn(t_der), run_time=0.5)
            self.en("existe")
            self.play(ReplacementTransform(t_izq, t_izq2), run_time=0.4)
            self.en("mejor")
            self.pop(estrella)
            self.play(FadeIn(mej), run_time=0.3)
            self.en("fabricando")
            self.play(FadeIn(bloque), run_time=0.6)
            self.en("rho04")
            self.play(FadeIn(r04), FadeIn(esp), run_time=0.5)

    def parte_b2(self):
        mon = moneda("", AMBAR).scale(1.0).move_to([-6.1, 1.6, 0])
        tira = tira_pm1([1, -1, -1, 1, -1, 1], lado=0.6).move_to([-2.8, 1.6, 0])
        indep = etiqueta("independientes", INK, 0.5).move_to([-2.8, 0.7, 0])
        blq = BloqueLTI("h", centro=(2.6, 1.6), ancho=2.0, alto=1.2, largo=1.0)
        c1 = caja("2", AZUL, ancho=0.7, alto=0.55, scale=0.45).move_to([2.0, 2.75, 0])
        c2 = caja("1", AZUL, ancho=0.7, alto=0.55, scale=0.45).move_to([3.2, 2.75, 0])
        f = formula("y[n]", "=", r"\frac{1}{\sqrt5}", r"\big(", r"2\,w[n]", r"+\,w[n-1]", r"\big)",
                    escala=1.2).move_to([0, -1.6, 0])
        with self.narrar("b2"):
            self.en("moneda")
            self.corte()
            self.pop(mon)
            self.en("pm1")
            self.play(FadeIn(tira), run_time=self.dur(0.8))
            self.en("indep")
            self.play(FadeIn(indep), run_time=0.4)
            self.en("filtro")
            self.play(FadeIn(blq), run_time=0.6)
            self.en("dos")
            self.play(FadeIn(c1), FadeIn(f[0]), FadeIn(f[1]), FadeIn(f[4]), run_time=self.dur(0.7))
            self.en("uno")
            self.play(FadeIn(c2), FadeIn(f[5]), run_time=0.5)
            self.en("raiz5")
            self.play(FadeIn(f[2]), FadeIn(f[3]), FadeIn(f[6]), run_time=0.6)
