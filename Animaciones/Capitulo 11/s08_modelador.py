"""Escena 8 - Filtros modeladores y blanqueadores.

La vuelta completa: blanco -> H(z) modelador -> coloreado -> 1/H(z)
blanqueador -> blanco otra vez. Cierra con la ambiguedad del pasa-todo.

    manim -pql s08_modelador.py ModeladorBlanqueador
"""
from manim import *
import numpy as np
from comun import *

A_POLO = 0.62               # H(z) = 1 / (1 - a z^-1)


def D_color(w, a=A_POLO):
    """|H|^2 para el modelador de un polo, con blanco de intensidad 1."""
    return 1.0 / (1 - 2 * a * np.cos(w) + a ** 2)


# el pico de D_color esta en w=0 y vale 1/(1-a)^2; se normaliza a PICO
# para que la curva entre en el cuadro sin tocar el titulo del panel
PICO = 2.45


def D_color_norm(w, a=A_POLO):
    return D_color(w, a) * (1 - a) ** 2 * PICO


class ModeladorBlanqueador(Scene):
    def construct(self):
        configurar()

        tit = titulo("Modelar y blanquear: dos caras de la misma moneda")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # =========================================== la cadena de bloques
        e1 = MathTex(r"w[n]", color=AZUL).scale(0.62)
        b1 = bloque(r"H(z)", color=AMBAR, ancho=1.7, alto=0.8, scale=0.55)
        e2 = MathTex(r"x[n]", color=AMBAR).scale(0.62)
        b2 = bloque(r"1/H(z)", color=VERDE, ancho=1.7, alto=0.8, scale=0.5)
        e3 = MathTex(r"w[n]", color=AZUL).scale(0.62)

        cadena = VGroup(e1, b1, e2, b2, e3).arrange(RIGHT, buff=0.7)
        cadena.next_to(tit, DOWN, buff=0.5)
        fs = VGroup(*[flecha(a.get_right(), b.get_left())
                      for a, b in zip(cadena[:-1], cadena[1:])])

        rot1 = nota("modelador", scale=0.42).next_to(b1, DOWN, buff=0.16)
        rot2 = nota("blanqueador", scale=0.42).next_to(b2, DOWN, buff=0.16)

        self.play(FadeIn(e1))
        self.play(GrowArrow(fs[0]), FadeIn(b1), FadeIn(rot1))
        self.play(GrowArrow(fs[1]), FadeIn(e2))
        self.wait(0.5)
        self.play(GrowArrow(fs[2]), FadeIn(b2), FadeIn(rot2))
        self.play(GrowArrow(fs[3]), FadeIn(e3))
        self.wait(1.0)

        vuelta = nota("uno le da forma al espectro plano; el otro se la saca",
                      scale=0.46)
        vuelta.next_to(cadena, DOWN, buff=0.62)
        self.play(FadeIn(vuelta))
        self.wait(1.6)
        self.play(FadeOut(vuelta))

        # =========================================== los tres espectros
        def panel(shift_x, titulo_txt, color):
            ax, lab = ejes([-PI, PI, PI], [0, 3.4], ancho=3.3, alto=2.0,
                           x_label=r"\Omega")
            ax.shift(shift_x + DOWN * 1.55)
            lab.next_to(ax.x_axis.get_end(), DR, buff=0.08)
            t = subtitulo(titulo_txt, scale=0.44, color=color)
            t.next_to(ax, UP, buff=0.18)
            return ax, lab, t

        axA, labA, titA = panel(LEFT * 4.35, "blanco: plano", AZUL)
        axB, labB, titB = panel(ORIGIN, "coloreado: con forma", AMBAR)
        axC, labC, titC = panel(RIGHT * 4.35, "blanco otra vez", VERDE)

        self.play(Create(axA), FadeIn(labA), FadeIn(titA),
                  Create(axB), FadeIn(labB), FadeIn(titB),
                  Create(axC), FadeIn(labC), FadeIn(titC))

        pA = axA.plot(lambda w: 1.0, x_range=[-PI, PI], color=AZUL, stroke_width=4)
        aA = axA.get_area(pA, x_range=(-PI, PI), color=AZUL, opacity=0.16,
                          stroke_width=0)
        pB = axB.plot(D_color_norm, x_range=[-PI, PI, 0.01], color=AMBAR,
                      stroke_width=4, use_smoothing=False)
        aB = axB.get_area(pB, x_range=(-PI, PI), color=AMBAR, opacity=0.16,
                          stroke_width=0)
        pC = axC.plot(lambda w: 1.0, x_range=[-PI, PI], color=VERDE, stroke_width=4)
        aC = axC.get_area(pC, x_range=(-PI, PI), color=VERDE, opacity=0.16,
                          stroke_width=0)

        self.play(Create(pA), FadeIn(aA))
        self.wait(0.3)
        self.play(Create(pB), FadeIn(aB), Indicate(b1, color=AMBAR))
        self.wait(0.8)
        self.play(Create(pC), FadeIn(aC), Indicate(b2, color=VERDE))
        self.wait(1.2)

        rel = MathTex(r"D_{xx}(e^{j\Omega}) \;=\; \big|H(e^{j\Omega})\big|^2",
                      color=TXT).scale(0.68)
        rel.to_edge(DOWN, buff=0.42)
        self.play(Write(rel))
        self.wait(0.6)
        rel_n = nota("por eso a H se lo llama un factor espectral de la PSD: "
                     "es su “raíz cuadrada”", scale=0.44)
        rel_n.next_to(rel, UP, buff=0.16)
        self.play(FadeIn(rel_n))
        self.wait(2.0)

        # =========================================== la ambiguedad
        self.play(FadeOut(VGroup(axA, labA, titA, pA, aA, axC, labC, titC,
                                 pC, aC, rel, rel_n)))
        self.play(VGroup(axB, labB, titB, pB, aB).animate.shift(RIGHT * 4.3))

        amb_tit = Text("¿Es único ese H?", color=TXT).scale(0.6)
        amb_tit.move_to(LEFT * 3.5 + UP * 0.15)
        amb = VGroup(
            MathTex(r"H_1(z)", color=AMBAR).scale(0.7),
            MathTex(r"H_2(z) = H_1(z)\,A(z)", color=MAGENTA).scale(0.7),
            MathTex(r"|A(e^{j\Omega})| = 1", color=INK).scale(0.6),
        ).arrange(DOWN, buff=0.3)
        amb.next_to(amb_tit, DOWN, buff=0.45)

        self.play(FadeIn(amb_tit))
        self.play(FadeIn(amb[0]))
        self.play(FadeIn(amb[1]), FadeIn(amb[2]))
        self.wait(1.0)

        conc = Text("mismo |H|²  →  mismo espectro", color=INK).scale(0.5)
        conc.next_to(amb, DOWN, buff=0.4)
        self.play(FadeIn(conc), Flash(pB.get_center(), color=MAGENTA,
                                      line_length=0.25, num_lines=14))
        self.wait(1.8)

        clave = nota("la libertad del pasa-todo es lo que en el capítulo 12 "
                     "se usa\npara elegir el factor de FASE MÍNIMA", scale=0.46)
        clave.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(clave))
        self.wait(2.2)

        # =========================================== cierre
        self.play(FadeOut(VGroup(axB, labB, titB, pB, aB, amb_tit, amb, conc,
                                 clave, cadena, fs, rot1, rot2)))
        cierre = VGroup(
            Text("Generar un proceso con un espectro dado:", color=INK).scale(0.52),
            Text("blanco  →  filtro modelador", color=AMBAR).scale(0.62),
            Text("Simplificar un problema con ruido coloreado:",
                 color=INK).scale(0.52),
            Text("coloreado  →  filtro blanqueador", color=VERDE).scale(0.62),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]), FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.5)
        self.play(FadeIn(cierre[2]), FadeIn(cierre[3], shift=UP * 0.12))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
