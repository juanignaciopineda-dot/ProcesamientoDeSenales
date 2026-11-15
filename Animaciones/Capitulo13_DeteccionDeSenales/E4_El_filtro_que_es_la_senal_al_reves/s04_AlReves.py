"""Escena 04 — Qué respuesta da ge: la señal invertida en el tiempo."""
from comun.escena import *


class AlReves(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        q = formula("h[n]", "=", "?", escala=1.3, colores={0: ESTIMACION, 2: AMBAR}).move_to([-3.8, 2.8, 0])
        g = formula("g", "=", r"\sum", "r", "s", escala=1.1, colores={3: MEDIDA, 4: SENAL}).move_to([-3.8, 1.3, 0])
        hn = MathTex("h[n]", color=ESTIMACION).scale(1.2).move_to([-3.8, -0.9, 0])
        hmn = MathTex("h[-n]", color=ESTIMACION).scale(1.2).move_to([-3.8, -0.9, 0])
        r = Tallos(R13, centro=(2.6, 1.2), paso=0.8, unidad=0.3, color=MEDIDA)
        s = Tallos(S13, centro=(2.6, -0.9), paso=0.8, unidad=0.3, color=SENAL)
        lab_r = MathTex("r[n]", color=MEDIDA).scale(0.9).move_to([0.3, 1.3, 0])
        lab_s = MathTex("s[n]", color=SENAL).scale(0.9).move_to([0.3, -0.8, 0])
        pares = VGroup(*[Line([r.x(i), 1.05, 0], [r.x(i), -0.2, 0], color=INK, stroke_width=3) for i in range(3)])
        igual = MathTex("=", color=TXT).scale(1.2).move_to([-0.9, -0.9, 0])
        fin = formula("h[n]", "=", "s[2-n]", escala=1.3, colores={0: ESTIMACION, 2: SENAL}).move_to([-3.0, -2.8, 0])
        h_pe = Tallos(H13, centro=(3.6, -2.8), paso=0.7, unidad=0.3, color=ESTIMACION)
        with self.narrar("b1"):
            # «¿qué respuesta hace que»
            self.en("pregunta")
            self.pop(q)

            # «salga justo ge»
            self.en("ge")
            self.play(Write(g), run_time=self.dur(1.0))

            # «da la vuelta a la respuesta»
            self.en("vuelta")
            self.play(FadeIn(hn), run_time=self.dur(0.3))
            self.sfx("whoosh")
            self.play(ReplacementTransform(hn, hmn), run_time=self.dur(0.7))

            # «cada muestra recibida se multiplique por su muestra de señal»
            self.en("parejas")
            self.play(FadeIn(r), FadeIn(lab_r), FadeIn(s), FadeIn(lab_s), run_time=self.dur(0.8))
            self.play(Create(pares), run_time=self.dur(0.6))

            # «su muestra de señal»
            self.en("suya")
            self.play(pares.animate.set_color(AMBAR), run_time=self.dur(0.4))

            # «Para eso, la respuesta»
            self.en("respuesta")
            self.resaltar(hmn, color=AMBAR, escala=1.2)

            # «una vez dada la vuelta»
            self.en("dada")
            self.play(hmn.animate.move_to([-2.3, -0.9, 0]), run_time=self.dur(0.7))

            # «tiene que ser la señal»
            self.en("ser")
            self.play(FadeIn(igual), run_time=self.dur(0.4))
            self.resaltar(s, color=SENAL, escala=1.15)

            # «Es decir»
            self.en("esdecir")
            self.play(FadeOut(pares), FadeOut(r), FadeOut(lab_r), run_time=self.dur(0.4))

            # «la señal invertida en el tiempo»
            self.en("invertida")
            self.pop(fin)
            self.play(FadeIn(h_pe), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
