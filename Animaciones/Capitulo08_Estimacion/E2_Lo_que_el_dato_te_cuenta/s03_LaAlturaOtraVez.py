"""Escena 03 — La altura otra vez: la población del Cap. 7 y la apuesta sin datos (167,2 con error 81,76)."""
from comun.escena import *

CM = np.linspace(143, 195, 160)


class LaAlturaOtraVez(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.al = Alturas7(centro=(0, -0.6), ancho=9.0, alto=2.8)
        self.poblacion()
        self.apuesta()
        self.wait(1.0)
        self.limpiar()

    def poblacion(self):
        al = self.al
        dens = 0.4 * gaussiana(CM, 175, 7) + 0.6 * gaussiana(CM, 162, 6)
        self.suma = traza(al.x(CM), al.y(dens), TXT, 5)
        lh = Text("Hombres · 40 %", color=AZUL, weight=BOLD).scale(0.5).move_to([3.1, 1.7, 0])
        lm = Text("Mujeres · 60 %", color=MAGENTA, weight=BOLD).scale(0.5).move_to([-3.9, 1.55, 0])
        cm175 = MathTex(r"175\ \text{cm}", color=AZUL).scale(0.6).move_to([float(al.x(175)), -2.45, 0])
        cm162 = MathTex(r"162\ \text{cm}", color=MAGENTA).scale(0.6).move_to([float(al.x(162)), -2.45, 0])
        per = persona(SENAL).scale(1.5).move_to([6.1, -0.4, 0])
        que = self.que = Text("?", color=AMBAR, weight=BOLD).scale(1.2).move_to([6.1, 1.0, 0])
        with self.narrar("b1"):
            # «el capítulo siete»
            self.en("cap7")
            self.play(Create(al.base), run_time=self.dur(0.3))
            self.play(Create(al.h), Create(al.m), run_time=self.dur(1.0), rate_func=linear)

            # «el cuarenta por ciento son hombres»
            self.en("hombres")
            self.pop(lh)

            # «ciento setenta y cinco centímetros»
            self.en("h175")
            self.play(Create(al.marca(175, AZUL, alto=1.6)), FadeIn(cm175), run_time=self.dur(0.5))

            # «el sesenta por ciento son mujeres»
            self.en("mujeres")
            self.pop(lm)

            # «ciento sesenta y dos»
            self.en("m162")
            self.play(Create(al.marca(162, MAGENTA, alto=2.8)), FadeIn(cm162), run_time=self.dur(0.5))

            # «Entra alguien por la puerta»
            self.en("entra")
            self.play(FadeIn(per, shift=LEFT * 0.4), run_time=self.dur(0.5))

            # «adivinar su altura»
            self.en("adivinar")
            self.pop(que)

            # «Si no sabes nada»
            self.en("nada")
            self.play(al.h.animate.set_stroke(opacity=0.25), al.m.animate.set_stroke(opacity=0.25),
                      Create(self.suma), run_time=self.dur(1.0))

            # «ya sabes qué hacer»
            self.en("sabes")
            self.sabes = Text("Apostar la media", color=AMBAR, weight=BOLD).scale(0.65).move_to([0, 2.7, 0])
            self.pop(self.sabes)

    def apuesta(self):
        al = self.al
        marca = al.marca(167.2, AMBAR, alto=2.2)
        with self.narrar("b2"):
            # «la media de toda la población»
            self.en("media")
            self.play(Create(marca), run_time=self.dur(0.5))

            # «ciento sesenta y siete coma dos»
            self.en("n1672")
            n = MathTex(r"\hat{y}=167{,}2", color=AMBAR).scale(0.9).move_to([-3.6, 2.5, 0])
            self.pop(n)

            # «el error cuadrático medio»
            self.en("ecm")
            self.play(FadeOut(self.sabes), run_time=0.2)
            ecm = Text("Error cuadrático medio", color=TXT).scale(0.55).move_to([-3.3, 3.4, 0])
            self.play(FadeIn(ecm), run_time=self.dur(0.4))

            # «la varianza de la altura»
            self.en("varianza")
            var = MathTex(r"=\ \sigma^2", color=ROJO).scale(0.8).next_to(ecm, RIGHT, buff=0.2)
            self.pop(var)

            # «ochenta y uno coma setenta y seis»
            self.en("n8176")
            barra = Rectangle(width=81.76 * 0.04, height=0.5, color=ROJO, stroke_width=2.5).set_fill(ROJO, 0.4)
            barra.move_to([0.9 + 81.76 * 0.02, 3.4, 0])
            t = MathTex(r"81{,}76", color=TXT).scale(0.8).next_to(barra, RIGHT, buff=0.25)
            self.play(FadeIn(barra, shift=RIGHT * 0.3), FadeIn(t), run_time=self.dur(0.6))

            # «unos nueve centímetros»
            self.en("nueve")
            a, b = [float(al.x(167.2 - 9)), 1.45, 0], [float(al.x(167.2 + 9)), 1.45, 0]
            ll = BraceBetweenPoints(a, b, UP, color=AMBAR)
            tt = Text("≈ 9 cm", color=AMBAR).scale(0.5).next_to(ll, UP, buff=0.1)
            self.play(GrowFromCenter(ll), FadeIn(tt), run_time=self.dur(0.6))

            # «Ahora cambiemos una cosa»
            self.en("cambiemos")
            self.play(FadeOut(ll), FadeOut(tt), FadeOut(marca), run_time=self.dur(0.4))

            # «antes de apostar»
            self.en("antes_apostar")
            self.play(FadeOut(self.que), run_time=0.2)
            tarj = caja("Es mujer", MAGENTA, ancho=1.9, alto=0.7, scale=0.5).move_to([6.0, 0.9, 0])
            self.play(FadeIn(tarj, shift=LEFT * 0.3), run_time=self.dur(0.5))

            # «alguien te dice»
            self.en("dice")
            tarj2 = caja("Es hombre", AZUL, ancho=1.9, alto=0.7, scale=0.5).move_to([6.0, 1.8, 0])
            self.play(FadeIn(tarj2, shift=LEFT * 0.3), run_time=self.dur(0.5))
