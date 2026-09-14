"""Escena 4 - La misma teoria, en tests medicos.

El diccionario radar <-> medicina, y despues el resultado que sorprende a
todo el mundo: con prevalencia baja, un test excelente puede tener un
valor predictivo positivo pesimo.

    manim -pql s04_medico.py TestMedico
"""
from manim import *
import numpy as np
from comun import *

SENS = 0.99          # P_D
ESPEC = 0.99         # 1 - P_FA
POB = 10000


class TestMedico(Scene):
    def construct(self):
        configurar()

        tit = titulo("La misma teoría, en un test médico")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ el diccionario
        pares = [
            (r"P_D", "sensibilidad", VERDE),
            (r"P_{FA}", "probabilidad de falso positivo", ROJO),
            (r"1-P_{FA}", "especificidad", AZUL),
            (r"P_M", "probabilidad de falso negativo", AMBAR),
            (r"P(H_1)", "prevalencia", MAGENTA),
        ]
        dic = VGroup()
        for sim, nom, col in pares:
            dic.add(VGroup(
                MathTex(sim, color=col).scale(0.6),
                MathTex(r"\longleftrightarrow", color=INK).scale(0.5),
                Text(nom, color=col).scale(0.5),
            ).arrange(RIGHT, buff=0.25))
        dic.arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        dic.next_to(tit, DOWN, buff=0.5)
        for f in dic:
            self.play(FadeIn(f, shift=RIGHT * 0.15), run_time=0.4)
        self.wait(1.8)

        self.play(FadeOut(dic))

        # ------------------------------------------------ el planteo
        planteo = VGroup(
            Text("Un test con:", color=TXT).scale(0.6),
            MathTex(r"\text{sensibilidad}=99\%\qquad"
                    r"\text{especificidad}=99\%", color=VERDE).scale(0.68),
            nota("suena excelente, ¿no?", scale=0.5),
        ).arrange(DOWN, buff=0.28)
        planteo.next_to(tit, DOWN, buff=0.7)
        self.play(FadeIn(planteo[0]), FadeIn(planteo[1]))
        self.wait(0.8)
        self.play(FadeIn(planteo[2]))
        self.wait(1.4)

        preg = Text("Te da positivo. ¿Qué probabilidad tenés de estar enfermo?",
                    color=AMBAR).scale(0.6)
        preg.next_to(planteo, DOWN, buff=0.6)
        self.play(FadeIn(preg))
        self.wait(2.2)
        self.play(FadeOut(VGroup(planteo, preg)))

        # ------------------------------------------------ la grilla de 10000
        prev = 0.001
        enfermos = int(POB * prev)                      # 10
        vp = int(round(enfermos * SENS))                # 10
        fp = int(round((POB - enfermos) * (1 - ESPEC)))  # 100

        sub = VGroup(
            Text(f"{POB:,} personas".replace(",", "."), color=TXT).scale(0.55),
            MathTex(r"\text{prevalencia}=0{,}1\%", color=MAGENTA).scale(0.6),
        ).arrange(RIGHT, buff=0.5)
        sub.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(sub))

        # el desglose, en texto: mucho mas claro que una grilla de 10.000 puntos
        desglose = VGroup(
            VGroup(MathTex(r"10", color=MAGENTA).scale(0.85),
                   Text("enfermos", color=MAGENTA).scale(0.5),
                   MathTex(r"\times\ 99\%\ \Rightarrow", color=INK).scale(0.5),
                   MathTex(r"\approx 10", color=MAGENTA).scale(0.6),
                   Text("detectados", color=INK).scale(0.44),
                   ).arrange(RIGHT, buff=0.2),
            VGroup(MathTex(r"9990", color=AZUL).scale(0.85),
                   Text("sanos", color=AZUL).scale(0.5),
                   MathTex(r"\times\ 1\%\ \Rightarrow", color=INK).scale(0.5),
                   MathTex(r"\approx 100", color=ROJO).scale(0.6),
                   Text("falsos positivos", color=ROJO).scale(0.44),
                   ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        desglose.next_to(sub, DOWN, buff=0.55).set_x(0)
        self.play(FadeIn(desglose[0], shift=RIGHT * 0.15))
        self.wait(1.0)
        self.play(FadeIn(desglose[1], shift=RIGHT * 0.15))
        self.wait(1.2)

        exp = nota("el 1% de falsos positivos sobre 9.990 sanos ya son "
                   "10 veces más que los enfermos reales", scale=0.46)
        exp.next_to(desglose, DOWN, buff=0.45).set_x(0)
        self.play(FadeIn(exp))
        self.wait(2.4)

        # ------------------------------------------------ solo los positivos
        self.play(FadeOut(VGroup(desglose, exp)),
                  sub.animate.next_to(tit, DOWN, buff=0.4).set_x(0))

        zoom = Text("De los 110 que dan positivo…", color=TXT).scale(0.6)
        zoom.next_to(sub, DOWN, buff=0.5).set_x(0)
        self.play(FadeIn(zoom))

        # cada punto es UNA persona: 10 enfermos + 100 falsos positivos
        pos = VGroup(*[Dot(radius=0.085,
                           color=MAGENTA if k < enfermos else ROJO,
                           fill_opacity=1.0)
                       for k in range(enfermos + fp)])
        pos.arrange_in_grid(rows=10, cols=11, buff=0.26)
        pos.next_to(zoom, DOWN, buff=0.5).set_x(0)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in pos],
                              lag_ratio=0.012), run_time=2.2)
        self.wait(0.6)

        leyenda = VGroup(
            VGroup(Dot(radius=0.08, color=MAGENTA, fill_opacity=1.0),
                   Text("10 enfermos", color=MAGENTA).scale(0.48),
                   ).arrange(RIGHT, buff=0.16),
            VGroup(Dot(radius=0.08, color=ROJO, fill_opacity=1.0),
                   Text("100 sanos mal clasificados", color=ROJO).scale(0.48),
                   ).arrange(RIGHT, buff=0.16),
        ).arrange(RIGHT, buff=1.0)
        leyenda.next_to(pos, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(leyenda))
        self.wait(2.2)

        # ------------------------------------------------ la cuenta
        self.play(FadeOut(VGroup(pos, leyenda, zoom, sub)))

        cuenta = VGroup(
            Text("De los que dan positivo:", color=TXT).scale(0.58),
            VGroup(
                MathTex(r"10", color=MAGENTA).scale(0.7),
                Text("realmente enfermos", color=MAGENTA).scale(0.5),
            ).arrange(RIGHT, buff=0.22),
            VGroup(
                MathTex(r"100", color=ROJO).scale(0.7),
                Text("sanos mal clasificados", color=ROJO).scale(0.5),
            ).arrange(RIGHT, buff=0.22),
        ).arrange(DOWN, buff=0.26)
        cuenta.next_to(tit, DOWN, buff=0.7)
        self.play(FadeIn(cuenta[0]))
        self.play(FadeIn(cuenta[1], shift=RIGHT * 0.15))
        self.play(FadeIn(cuenta[2], shift=RIGHT * 0.15))
        self.wait(1.2)

        vpp = MathTex(r"\text{VPP} = \frac{10}{10+100} = 9{,}1\%",
                      color=AMBAR).scale(0.9)
        vpp.next_to(cuenta, DOWN, buff=0.6)
        self.play(Write(vpp))
        self.wait(1.6)

        golpe = VGroup(
            Text("Con un test del 99%, un positivo significa", color=ROJO)
            .scale(0.52),
            Text("9% de probabilidad de estar enfermo.", color=ROJO).scale(0.52),
        ).arrange(DOWN, buff=0.12)
        golpe.next_to(vpp, DOWN, buff=0.5)
        self.play(FadeIn(golpe))
        self.wait(2.6)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(cuenta, vpp, golpe)))
        cierre = VGroup(
            Text("La sensibilidad y la especificidad no alcanzan.",
                 color=TXT).scale(0.6),
            Text("Sin la prevalencia, un positivo no dice casi nada.",
                 color=AMBAR).scale(0.6),
            nota("es literalmente el término $P(H_1)$ de la regla MAP "
                 "haciendo su trabajo", scale=0.5),
        ).arrange(DOWN, buff=0.3)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.play(FadeIn(cierre[1], shift=UP * 0.15))
        self.wait(0.5)
        self.play(FadeIn(cierre[2]))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
