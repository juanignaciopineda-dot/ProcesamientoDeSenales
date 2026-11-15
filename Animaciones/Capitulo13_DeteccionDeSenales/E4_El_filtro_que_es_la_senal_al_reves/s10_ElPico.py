"""Escena 10 — Por qué se muestrea en el pico; el filtro adaptado es un detector de parecidos."""
from comun.escena import *


class ElPico(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        aut = Tallos(AUT13, centro=(0, -0.6), paso=1.2, unidad=0.3, color=AMBAR)
        vals = valores_sobre13(aut, color=TXT, escala=0.55)
        cur = Arrow([0, 2.6, 0], aut.pos(2) + UP * 0.6, color=AMBAR, buff=0.05, stroke_width=4,
                    max_tip_length_to_length_ratio=0.25)
        n2 = MathTex("n=2", color=AMBAR).scale(0.8).move_to([0.8, 2.7, 0])
        banda = VGroup(*[Rectangle(width=0.9, height=0.5, stroke_width=0).set_fill(RUIDO, 0.5).move_to([aut.x(i), -1.4, 0])
                         for i in range(1, 4)])
        l_ru = etiqueta("ruido", RUIDO, 0.5).move_to([aut.x(0) - 0.2, -1.4, 0])
        linea = DashedLine([aut.x(1) - 0.6, -1.15, 0], [aut.x(3) + 0.6, -1.15, 0], color=INK, stroke_width=2)
        dif = DoubleArrow([aut.x(2) + 0.55, -0.6, 0], [aut.x(2) + 0.55, aut.pos(2)[1], 0], color=SENAL, buff=0,
                          stroke_width=3, tip_length=0.18)
        # segundo bloque
        pal = self.palabra("detector de parecidos", AMBAR, 0.8).move_to([0, 3.2, 0])
        bl = BloqueLTI("h", centro=(-1.2, 0.2), ancho=1.2, alto=0.9, color=ESTIMACION, largo=0.8, escala=0.7)
        ent_ruido = Tallos([2, -1, -2], centro=(-4.0, 0.2), paso=0.6, unidad=0.25, color=MEDIDA)
        ent_senal = Tallos(S13, centro=(-4.0, 0.2), paso=0.6, unidad=0.25, color=SENAL)
        ent_grande = Tallos([3, 3, 1.5], centro=(-4.0, 0.2), paso=0.6, unidad=0.25, color=SENAL)
        sal_plana = Tallos([0.5, -0.3, 0.4, -0.2, 0.3], centro=(2.6, 0.2), paso=0.6, unidad=0.2, color=AMBAR)
        sal_pico = Tallos(AUT13, centro=(2.6, 0.2), paso=0.6, unidad=0.13, color=AMBAR)
        sal_grande = Tallos([x * 2.0 for x in AUT13], centro=(2.6, 0.2), paso=0.6, unidad=0.13, color=AMBAR)
        al = alarma13().move_to([5.8, 0.4, 0])
        rl = reloj().scale(1.1).move_to([-3.2, -2.4, 0])
        esp = campana_mini(centro=(3.0, -2.4), ancho=1.8, alto=1.1, color=SENAL)
        base = Line([2.0, -2.9, 0], [4.0, -2.9, 0], color=INK, stroke_width=2)

        with self.narrar("b1"):
            # «muestrear en el pico»
            self.en("pico")
            self.play(FadeIn(aut), run_time=self.dur(0.6))
            self.play(Create(cur), FadeIn(n2), run_time=self.dur(0.5))

            # «la contribución de la señal es máxima»
            self.en("maxima")
            self.resaltar(aut.puntos[2], color=SENAL, escala=2.4)

            # «nueve, contra seis o dos en los vecinos»
            self.en("vecinos")
            self.play(FadeIn(vals), run_time=self.dur(0.6))

            # «La contribución del ruido»
            self.en("ruido")
            self.play(FadeIn(banda), FadeIn(l_ru), run_time=self.dur(0.5))

            # «del mismo tamaño»
            self.en("igual")
            self.play(Create(linea), run_time=self.dur(0.5))

            # «Así que en el pico»
            self.en("asique")
            self.resaltar(aut.tallos[2], color=AMBAR, escala=1.0)

            # «la señal destaca»
            self.en("destaca")
            self.play(Create(dif), run_time=self.dur(0.5))
            self.resaltar(dif, color=SENAL, escala=1.15)

        with self.narrar("b2"):
            # «un detector de parecidos»
            self.en("detector")
            self.corte()
            self.pop(pal)
            self.add(bl)

            # «Se queda tranquilo»
            self.en("tranquilo")
            self.play(FadeIn(ent_ruido), run_time=self.dur(0.4))
            self.play(FadeIn(sal_plana), run_time=self.dur(0.5))

            # «no se parece a la señal buscada»
            self.en("noparece")
            self.resaltar(ent_ruido, color=MEDIDA, escala=1.15)

            # «da un pico»
            self.en("pico")
            self.play(FadeOut(ent_ruido), FadeIn(ent_senal), Transform(sal_plana, sal_pico), run_time=self.dur(0.8))
            self.play(FadeIn(al, scale=0.7), run_time=self.dur(0.3))
            self.sfx("alarma", gain=-18)

            # «el pico crece»
            self.en("crece")
            self.play(Transform(ent_senal, ent_grande), Transform(sal_plana, sal_grande), run_time=self.dur(0.9))

            # «Ahora, veamos la misma idea»
            self.en("ahora")
            self.play(FadeIn(rl, scale=0.7), run_time=self.dur(0.5))

            # «en el mundo de las frecuencias»
            self.en("mundo")
            self.play(FadeIn(base), Create(esp), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
