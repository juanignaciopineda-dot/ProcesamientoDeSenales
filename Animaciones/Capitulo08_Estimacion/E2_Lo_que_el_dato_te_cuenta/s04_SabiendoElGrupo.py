"""Escena 04 — Saber el grupo: apostar la media de cada grupo, con su error, y en promedio 41,2 en vez de 81,76."""
from comun.escena import *

CM = np.linspace(143, 195, 160)


class SabiendoElGrupo(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.grupos()
        self.promedio()
        self.wait(1.0)
        self.limpiar()

    def normalizada(self, al, mu, sd, color):
        """Campana de un solo grupo, estirada hasta ocupar todo el alto del dibujo."""
        d = gaussiana(CM, mu, sd)
        return traza(al.x(CM), al.y(d / d.max() * al.vmax), color, 4)

    def grupos(self):
        al = Alturas7(centro=(0, -1.1), ancho=9.0, alto=3.4)
        self.al = al
        tm = caja("Mujer", MAGENTA, ancho=1.7, alto=0.6, scale=0.5).move_to([-5.6, 3.3, 0])
        th = caja("Hombre", AZUL, ancho=1.7, alto=0.6, scale=0.5).move_to([-5.6, 2.5, 0])
        gente = VGroup(*[persona(MAGENTA if i < 6 else AZUL).scale(0.5) for i in range(10)]).arrange(RIGHT, buff=0.25)
        gente.move_to([1.4, 3.3, 0])
        self.add(al.base, al.h, al.m, tm, th)
        mc = self.normalizada(al, 162, 6, MAGENTA)
        hc = self.normalizada(al, 175, 7, AZUL)
        with self.narrar("b1"):
            # «es una mujer»
            self.en("mujer")
            self.play(FadeIn(gente), al.h.animate.set_stroke(opacity=0.2), run_time=self.dur(0.6))
            self.resaltar(tm)

            # «el mundo se achica»
            self.en("achica")
            self.play(Transform(al.m, mc), run_time=self.dur(0.8))

            # «ya solo cuentan las mujeres»
            self.en("solo_mujeres")
            self.play(*[p.animate.set_opacity(0.15) for p in gente[6:]], run_time=self.dur(0.5))

            # «Dentro de ese grupo»
            self.en("dentro")
            marco = Rectangle(width=float(al.x(176) - al.x(147)), height=3.7, color=AMBAR, stroke_width=3)
            marco.move_to([float(al.x(161.5)), -1.1 - 1.7 + 1.85, 0])
            self.play(Create(marco), run_time=self.dur(0.5))

            # «lo de siempre»
            self.en("lo_siempre")
            sig = Text("Media y varianza", color=AMBAR).scale(0.5).move_to([-1.2, 1.5, 0])
            self.play(FadeIn(sig), run_time=self.dur(0.4))

            # «apuestas su media»
            self.en("su_media")
            marca = al.marca(162, AMBAR, alto=3.4)
            self.play(Create(marca), run_time=self.dur(0.5))

            # «ciento sesenta y dos»
            self.en("n162")
            n162 = MathTex(r"\hat{y}=162", color=AMBAR).scale(0.9).move_to([5.0, 1.8, 0])
            self.pop(n162)

            # «seis al cuadrado»
            self.en("seis2")
            e36 = MathTex(r"\text{Error}=6^2=36", color=ROJO).scale(0.8).move_to([5.0, 0.9, 0])
            b36 = Rectangle(width=36 * 0.05, height=0.4, color=ROJO, stroke_width=2.5).set_fill(ROJO, 0.4)
            b36.move_to([3.6 + 36 * 0.025, 0.3, 0])
            self.play(FadeIn(e36), FadeIn(b36, shift=RIGHT * 0.2), run_time=self.dur(0.6))

            # «es un hombre»
            self.en("hombre")
            self.play(FadeOut(n162), FadeOut(e36), FadeOut(b36), FadeOut(marca), FadeOut(marco), FadeOut(sig),
                      FadeOut(al.m), run_time=self.dur(0.4))
            self.play(FadeIn(hc), *[p.animate.set_opacity(0.15 if i < 6 else 1.0) for i, p in enumerate(gente)],
                      run_time=self.dur(0.7))
            self.resaltar(th)

            # «ciento setenta y cinco»
            self.en("n175")
            m175 = al.marca(175, AMBAR, alto=3.4)
            n175 = MathTex(r"\hat{y}=175", color=AMBAR).scale(0.9).move_to([5.0, 1.8, 0])
            self.play(Create(m175), run_time=self.dur(0.4))
            self.pop(n175)

            # «siete al cuadrado»
            self.en("siete2")
            e49 = MathTex(r"\text{Error}=7^2=49", color=ROJO).scale(0.8).move_to([5.0, 0.9, 0])
            b49 = Rectangle(width=49 * 0.05, height=0.4, color=ROJO, stroke_width=2.5).set_fill(ROJO, 0.4)
            b49.move_to([3.6 + 49 * 0.025, 0.3, 0])
            self.play(FadeIn(e49), FadeIn(b49, shift=RIGHT * 0.2), run_time=self.dur(0.6))

    def promedio(self):
        caja_h = caja("Hombre", AZUL, ancho=2.0, alto=0.7, scale=0.6).move_to([-3.4, 2.6, 0])
        caja_m = caja("Mujer", MAGENTA, ancho=2.0, alto=0.7, scale=0.6).move_to([3.4, 2.6, 0])
        v49 = MathTex(r"49", color=ROJO).scale(2.0).move_to([-3.4, 1.6, 0])
        v36 = MathTex(r"36", color=ROJO).scale(2.0).move_to([3.4, 1.6, 0])
        p04 = MathTex(r"0{,}4", color=AMBAR).scale(1.0).move_to([-3.4, 3.5, 0])
        p06 = MathTex(r"0{,}6", color=AMBAR).scale(1.0).move_to([3.4, 3.5, 0])
        l1 = MathTex(r"0{,}4\cdot 49=19{,}6", color=TXT).scale(1.2).move_to([-0.3, 0.2, 0])
        l2 = MathTex(r"+\ 0{,}6\cdot 36=21{,}6", color=TXT).scale(1.2).move_to([0.0, -0.9, 0])
        l3 = MathTex(r"=\ 41{,}2", color=VERDE).scale(1.8).move_to([-0.3, -2.4, 0])
        with self.narrar("b2"):
            # «sin saber todavía quién entrará»
            self.en("sin_saber")
            self.corte()
            self.play(FadeIn(caja_h), FadeIn(caja_m), FadeIn(v49), FadeIn(v36), run_time=self.dur(0.6))

            # «Cuatro de cada diez veces»
            self.en("cuatro")
            self.pop(p04)

            # «seis de cada diez»
            self.en("seis")
            self.pop(p06)

            # «Cero coma cuatro por cuarenta y nueve»
            self.en("c1")
            self.play(FadeIn(l1, shift=UP * 0.2), run_time=self.dur(0.5))

            # «más cero coma seis por treinta y seis»
            self.en("c2")
            self.play(FadeIn(l2, shift=UP * 0.2), run_time=self.dur(0.5))

            # «cuarenta y uno coma dos»
            self.en("suma")
            self.pop(l3)

            # «reducido el error a la mitad»
            self.en("mitad")
            self.corte()
            b1 = Rectangle(width=81.76 * 0.08, height=1.0, color=ROJO, stroke_width=2.5).set_fill(ROJO, 0.4)
            b1.move_to([-3.3 + 81.76 * 0.04, 0.6, 0])
            b2 = Rectangle(width=41.2 * 0.08, height=1.0, color=ROJO, stroke_width=2.5).set_fill(ROJO, 0.4)
            b2.move_to([-3.3 + 41.2 * 0.04, 0.6, 0])
            t1 = MathTex(r"81{,}76", color=TXT).scale(0.9).next_to(b1, DOWN, buff=0.3).align_to(b1, LEFT)
            t2 = MathTex(r"41{,}2", color=VERDE).scale(0.9).next_to(b2, DOWN, buff=0.3).align_to(b2, LEFT)
            self.play(FadeIn(b1, shift=RIGHT * 0.3), FadeIn(t1), run_time=self.dur(0.4))
            self.play(Transform(b1, b2), Transform(t1, t2), run_time=self.dur(0.8))
