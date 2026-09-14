"""Escena 5 - Esperanza condicionada e iterada (propiedad de la torre).

E[X] = E[E[X|Y]]: primero promedio dentro de cada grupo, despues promedio
esos promedios pesando cada uno por lo probable que es el grupo. Se usa el
ejemplo de alturas del apunte.

    manim -pql s05_torre.py EsperanzaIterada
"""
from manim import *
import numpy as np
from comun import *

P_H, MU_H = 0.40, 175.0
P_M, MU_M = 0.60, 162.0
MEDIA = P_H * MU_H + P_M * MU_M          # 167.2


class EsperanzaIterada(Scene):
    def construct(self):
        configurar()

        tit = titulo("La propiedad de la torre")
        self.play(FadeIn(tit, shift=DOWN * 0.2))

        enun = MathTex(r"E[X]\;=\;E\big[\,E[X\mid Y]\,\big]",
                       color=TXT).scale(0.95)
        enun.next_to(tit, DOWN, buff=0.45)
        self.play(Write(enun))
        self.wait(1.0)
        pregunta = nota("se lee de adentro hacia afuera; el ejemplo lo hace obvio",
                        scale=0.47)
        pregunta.next_to(enun, DOWN, buff=0.22)
        self.play(FadeIn(pregunta))
        self.wait(1.6)
        self.play(FadeOut(pregunta), enun.animate.scale(0.68).to_edge(UP, buff=1.1))

        # ============================================ el planteo
        planteo = Text("Altura promedio de una población", color=TXT).scale(0.6)
        planteo.next_to(enun, DOWN, buff=0.4)
        self.play(FadeIn(planteo))
        self.wait(0.8)

        # ---- los dos grupos, como bloques proporcionales
        ANCHO = 8.0
        b_h = Rectangle(width=ANCHO * P_H, height=1.0, stroke_width=2.5,
                        color=AZUL, fill_color=AZUL, fill_opacity=0.28)
        b_m = Rectangle(width=ANCHO * P_M, height=1.0, stroke_width=2.5,
                        color=MAGENTA, fill_color=MAGENTA, fill_opacity=0.28)
        barra_g = VGroup(b_h, b_m).arrange(RIGHT, buff=0)
        barra_g.move_to(ORIGIN).shift(UP * 0.35)

        l_h = VGroup(Text("hombres", color=AZUL).scale(0.5),
                     Text(f"{P_H:.0%}", color=AZUL).scale(0.55)
                     ).arrange(DOWN, buff=0.08).move_to(b_h)
        l_m = VGroup(Text("mujeres", color=MAGENTA).scale(0.5),
                     Text(f"{P_M:.0%}", color=MAGENTA).scale(0.55)
                     ).arrange(DOWN, buff=0.08).move_to(b_m)

        self.play(GrowFromEdge(b_h, LEFT), GrowFromEdge(b_m, RIGHT))
        self.play(FadeIn(l_h), FadeIn(l_m))
        y_lbl = nota("la variable Y es el grupo", scale=0.45)
        y_lbl.next_to(barra_g, UP, buff=0.25)
        self.play(FadeIn(y_lbl))
        self.wait(1.2)

        # ============================================ paso 1: promedio dentro
        paso1 = Text("1.  Promedio DENTRO de cada grupo", color=VERDE).scale(0.58)
        paso1.next_to(barra_g, DOWN, buff=0.75)
        self.play(FadeOut(planteo), FadeIn(paso1, shift=RIGHT * 0.15))

        m_h = MathTex(r"E[X\mid Y=\text{h}]=175", color=AZUL).scale(0.6)
        m_h.next_to(b_h, DOWN, buff=0.2)
        m_m = MathTex(r"E[X\mid Y=\text{m}]=162", color=MAGENTA).scale(0.6)
        m_m.next_to(b_m, DOWN, buff=0.2)
        self.play(paso1.animate.shift(DOWN * 0.55))
        self.play(FadeIn(m_h, shift=UP * 0.1), FadeIn(m_m, shift=UP * 0.1))
        self.wait(0.6)

        gy = nota("esto es g(y) = E[X | Y = y]: una función del grupo",
                  scale=0.45)
        gy.next_to(paso1, DOWN, buff=0.3)
        self.play(FadeIn(gy))
        self.wait(1.8)
        self.play(FadeOut(gy))

        # ============================================ paso 2: promediar los promedios
        paso2 = Text("2.  Promediar esos promedios, pesando por cada grupo",
                     color=AMBAR).scale(0.58)
        paso2.move_to(paso1)
        self.play(Transform(paso1, paso2))
        self.wait(0.5)

        cuenta = MathTex(
            r"E[X]", r"=", r"0{,}4\cdot 175", r"+", r"0{,}6\cdot 162",
            r"=", r"167{,}2\ \text{cm}")
        cuenta.set_color(TXT).scale(0.75)
        cuenta[2].set_color(AZUL)
        cuenta[4].set_color(MAGENTA)
        cuenta[6].set_color(AMBAR)
        cuenta.next_to(paso1, DOWN, buff=0.45)

        self.play(Write(cuenta[0]), Write(cuenta[1]))
        self.play(TransformFromCopy(m_h, cuenta[2]), run_time=1.0)
        self.play(Write(cuenta[3]))
        self.play(TransformFromCopy(m_m, cuenta[4]), run_time=1.0)
        self.play(Write(cuenta[5]), Write(cuenta[6]))
        self.wait(0.6)

        # el resultado, marcado sobre la barra
        marca = Line(UP * 0.55, DOWN * 0.55, color=AMBAR, stroke_width=4)
        pos = interpolate(b_h.get_left()[0], b_m.get_right()[0],
                          (MEDIA - MU_M) / (MU_H - MU_M))
        marca.move_to([pos, barra_g.get_center()[1], 0])
        self.play(Create(marca), Flash(marca.get_top(), color=AMBAR,
                                       line_length=0.15))
        self.wait(1.8)

        # ============================================ el cierre conceptual
        self.play(FadeOut(VGroup(barra_g, l_h, l_m, y_lbl, m_h, m_m, marca,
                                 paso1, cuenta)))

        cierre = VGroup(
            MathTex(r"E[X\mid Y]", color=VERDE).scale(0.95),
            Text("es una variable aleatoria", color=TXT).scale(0.6),
            nota("toma el valor 175 con probabilidad 0,4\n"
                 "y el valor 162 con probabilidad 0,6", scale=0.5),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN).shift(UP * 0.35)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.play(FadeIn(cierre[1]))
        self.wait(0.5)
        self.play(FadeIn(cierre[2]))
        self.wait(1.6)

        final = MathTex(r"E\big[\,E[X\mid Y]\,\big]\;=\;E[X]",
                        color=AMBAR).scale(0.9)
        final.next_to(cierre, DOWN, buff=0.7)
        self.play(Write(final))
        self.wait(0.6)
        remate = nota("tomarle la esperanza a esa variable aleatoria "
                      "devuelve la media original", scale=0.48)
        remate.next_to(final, DOWN, buff=0.28)
        self.play(FadeIn(remate))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, enun, cierre, final, remate)))
        self.wait(0.3)
