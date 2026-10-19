"""Escena 12 — Por qué la apuesta (22,4) tira hacia la media: la lectura (23) mezcla calor y ruido."""
from comun.escena import *


class TiraHaciaLaMedia(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        R = RectaNum(18, 24, centro=(0.0, -0.2), ancho=11.0, marcas=[])

        def dato(x, palabra, numero, color):
            d = Dot(R.p(x), radius=0.12, color=color)
            rot = VGroup(Text(palabra, color=color).scale(0.45),
                         MathTex(numero, color=color).scale(0.8)).arrange(DOWN, buff=0.08)
            rot.next_to(d, DOWN, buff=0.25)
            return d, rot

        d20, l20 = dato(20, "Media", "20", SENAL)
        d224, l224 = dato(22.4, "Apuesta", r"22{,}4", ESTIMACION)
        d23, l23 = dato(23, "Lectura", "23", MEDIDA)
        l224.shift(LEFT * 0.3)      # las dos etiquetas están a 1,1 de distancia: se separan para que no se toquen
        l23.shift(RIGHT * 0.3)

        def salto(x0, x1, y, color, txt):
            a = Arrow(R.p(x0) + UP * y, R.p(x1) + UP * y, buff=0, color=color, stroke_width=5,
                      max_tip_length_to_length_ratio=0.2)
            t = MathTex(txt, color=color).scale(0.8).move_to((a.get_start() + a.get_end()) / 2 + UP * 0.38)
            return a, t

        a3, t3 = salto(20, 23, 0.6, MEDIDA, "+3")
        a24, t24 = salto(20, 22.4, 1.5, ESTIMACION, r"+2{,}4")
        a06, t06 = salto(22.4, 23, 2.5, TXT, r"0{,}6")
        fiar = Text("¿Fiarse del todo?", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, 3.5, 0])
        s = sol(SENAL).scale(0.8).move_to([-4.8, -3.3, 0])
        t_sol = Text("Calor de verdad", color=SENAL).scale(0.55).next_to(s, RIGHT, buff=0.25)
        f_r = Arrow([1.2, -3.8, 0], [1.2, -2.9, 0], buff=0, color=RUIDO, stroke_width=6,
                    max_tip_length_to_length_ratio=0.35)
        t_r = Text("Ruido hacia arriba", color=RUIDO).scale(0.55).next_to(f_r, RIGHT, buff=0.25)
        x23, x20 = R.p(23)[0], R.p(20)[0]
        tira = Arrow([x23, -2.0, 0], [x20, -2.0, 0], buff=0, color=ESTIMACION, stroke_width=5,
                     max_tip_length_to_length_ratio=0.1)
        t_tira = Text("Hacia la media", color=ESTIMACION, weight=BOLD).scale(0.5).move_to([(x23 + x20) / 2, -2.5, 0])

        with self.narrar("b1"):
            # «Fíjate en el veintidós coma cuatro»
            self.en("a224")
            self.play(Create(R.base), FadeIn(d20), FadeIn(l20), run_time=self.dur(0.6))
            self.play(FadeIn(d224), FadeIn(l224), run_time=self.dur(0.6))

            # «El termómetro marcaba veintitrés»
            self.en("m23")
            self.play(FadeIn(d23), FadeIn(l23), run_time=self.dur(0.6))

            # «tres por encima de la media»
            self.en("tres")
            self.play(GrowArrow(a3), FadeIn(t3), run_time=self.dur(0.6))

            # «la apuesta solo sube dos coma cuatro»
            self.en("sube")
            self.play(GrowArrow(a24), FadeIn(t24), run_time=self.dur(0.6))

            # «¿Por qué no fiarse del todo?»
            self.en("fiar")
            self.pop(fiar)

            # «Porque una lectura alta»
            self.en("alta")
            self.play(Indicate(l23, color=AMBAR), run_time=self.dur(0.8))

            # «calor de verdad»
            self.en("calor")
            self.pop(s)
            self.play(FadeIn(t_sol), run_time=self.dur(0.4))

            # «ruido hacia arriba»
            self.en("ruidoar")
            self.play(GrowArrow(f_r), FadeIn(t_r), run_time=self.dur(0.6))

            # «reparte la diferencia»
            self.en("reparte")
            self.play(GrowArrow(a06), FadeIn(t06), run_time=self.dur(0.6))

            # «tira un poco hacia la media»
            self.en("tira")
            self.play(GrowArrow(tira), FadeIn(t_tira), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
