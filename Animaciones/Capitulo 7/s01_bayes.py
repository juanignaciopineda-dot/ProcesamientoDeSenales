"""Escena 1 - Probabilidad condicional y regla de Bayes.

Condicionar es achicar el universo y volver a normalizar. Bayes da vuelta
el condicionamiento. El cierre es el ejemplo del test medico, que es
contraintuitivo y reaparece en el capitulo 9.

    manim -pql s01_bayes.py Bayes
"""
from manim import *
import numpy as np
from comun import *

# ---- parametros del ejemplo medico
PREVALENCIA = 0.01     # P(enfermo)
SENSIBILIDAD = 0.99    # P(+ | enfermo)
ESPECIFICIDAD = 0.95   # P(- | sano)


class Bayes(Scene):
    def construct(self):
        configurar()

        tit = titulo("Condicionar es achicar el universo")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ============================================ el universo
        uni = Rectangle(width=6.4, height=3.8, color=INK, stroke_width=2.5,
                        fill_color=INK, fill_opacity=0.05)
        uni.shift(LEFT * 2.9 + DOWN * 0.5)
        uni_lbl = MathTex(r"\psi", color=INK).scale(0.75)
        uni_lbl.next_to(uni, UP, buff=0.12).align_to(uni, LEFT)

        A = Circle(radius=1.45, color=AZUL, stroke_width=3,
                   fill_color=AZUL, fill_opacity=0.22)
        A.move_to(uni.get_center() + LEFT * 0.95)
        B = Circle(radius=1.45, color=AMBAR, stroke_width=3,
                   fill_color=AMBAR, fill_opacity=0.22)
        B.move_to(uni.get_center() + RIGHT * 0.95)
        A_lbl = MathTex("A", color=AZUL).scale(0.75).move_to(
            A.get_center() + LEFT * 0.85)
        B_lbl = MathTex("B", color=AMBAR).scale(0.75).move_to(
            B.get_center() + RIGHT * 0.85)

        self.play(Create(uni), FadeIn(uni_lbl))
        self.play(Create(A), FadeIn(A_lbl), Create(B), FadeIn(B_lbl))
        self.wait(0.6)

        # ---- llega el dato: ocurrio B  (arriba, para no pisar la etiqueta
        #      de la interseccion que va debajo del diagrama)
        dato = Text("dato: ocurrió B", color=AMBAR).scale(0.58)
        dato.next_to(uni, UP, buff=0.3).align_to(uni, RIGHT)
        self.play(FadeIn(dato, shift=DOWN * 0.15))
        self.wait(0.5)

        # todo lo que esta fuera de B deja de importar
        self.play(uni.animate.set_stroke(opacity=0.25).set_fill(opacity=0.02),
                  A.animate.set_stroke(opacity=0.3).set_fill(opacity=0.05),
                  A_lbl.animate.set_opacity(0.3),
                  uni_lbl.animate.set_opacity(0.25),
                  B.animate.set_fill(opacity=0.30),
                  run_time=1.2)

        inter = Intersection(A, B, color=VERDE, fill_color=VERDE,
                             fill_opacity=0.75, stroke_width=3)
        self.play(FadeIn(inter))
        inter_lbl = MathTex(r"A\cap B", color=VERDE).scale(0.55)
        inter_lbl.next_to(inter, DOWN, buff=0.9).shift(RIGHT * 0.1)
        fl_i = Arrow(inter_lbl.get_top(), inter.get_bottom(), color=VERDE,
                     stroke_width=2.5, buff=0.08,
                     max_tip_length_to_length_ratio=0.22)
        self.play(FadeIn(inter_lbl), GrowArrow(fl_i))
        self.wait(0.8)

        # ---- la formula
        form = MathTex(r"P(A\mid B)", r"=", r"\frac{P(A\cap B)}{P(B)}")
        form[0].set_color(VERDE); form[2].set_color(TXT)
        form.scale(0.9).to_edge(RIGHT, buff=1.0).shift(UP * 0.3)
        self.play(Write(form))
        self.wait(0.5)
        expl = nota("el nuevo universo es B:\nse renormaliza dividiendo por P(B)",
                    scale=0.46)
        expl.next_to(form, DOWN, buff=0.45)
        self.play(FadeIn(expl))
        self.wait(2.0)

        # ============================================ Bayes
        self.play(FadeOut(VGroup(dato, inter_lbl, fl_i, expl)))
        nuevo_tit = titulo("Bayes: dar vuelta el condicionamiento")
        self.play(Transform(tit, nuevo_tit))

        bayes = MathTex(r"P(A\mid B)", r"=",
                        r"\frac{P(B\mid A)\;P(A)}{P(B)}")
        bayes[0].set_color(VERDE)
        bayes.scale(0.9).move_to(form)
        self.play(TransformMatchingTex(form, bayes))
        self.wait(0.6)

        idea = nota("sirve cuando sabés medir P(B|A)\npero lo que querés es P(A|B)",
                    scale=0.46)
        idea.next_to(bayes, DOWN, buff=0.45)
        self.play(FadeIn(idea))
        self.wait(2.0)

        self.play(FadeOut(VGroup(uni, uni_lbl, A, A_lbl, B, B_lbl, inter,
                                 bayes, idea)))

        # ============================================ el test medico
        tit2 = titulo("Un test buenísimo que igual te confunde")
        self.play(Transform(tit, tit2))

        planteo = VGroup(
            Text(f"prevalencia de la enfermedad:  {PREVALENCIA:.0%}",
                 color=INK).scale(0.55),
            Text(f"sensibilidad  P(+ | enfermo):  {SENSIBILIDAD:.0%}",
                 color=VERDE).scale(0.55),
            Text(f"especificidad  P(− | sano):  {ESPECIFICIDAD:.0%}",
                 color=AZUL).scale(0.55),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        planteo.next_to(tit, DOWN, buff=0.45).to_edge(LEFT, buff=0.9)
        for l in planteo:
            self.play(FadeIn(l, shift=RIGHT * 0.15), run_time=0.5)
        self.wait(0.8)

        preg = Text("Te da positivo. ¿Qué probabilidad tenés de estar enfermo?",
                    color=TXT).scale(0.6)
        preg.next_to(planteo, DOWN, buff=0.5)
        self.play(FadeIn(preg))
        self.wait(1.6)
        intuicion = nota("la intuición dice ~99 %", scale=0.5)
        intuicion.next_to(preg, DOWN, buff=0.25)
        self.play(FadeIn(intuicion))
        self.wait(1.6)
        self.play(FadeOut(VGroup(planteo, preg, intuicion)))

        # ---- la grilla de 10 000 personas
        FIL, COL = 20, 50           # 1000 celdas -> cada una son 10 personas
        celdas = VGroup()
        for i in range(FIL):
            for j in range(COL):
                c = Square(side_length=0.19, stroke_width=0.7,
                           stroke_color="#2c3140", fill_color=AZUL,
                           fill_opacity=0.22)
                c.move_to(RIGHT * (j * 0.20) + DOWN * (i * 0.20))
                celdas.add(c)
        celdas.move_to(ORIGIN).shift(DOWN * 0.35)
        # alineado a la derecha: la etiqueta de los enfermos va arriba a la
        # izquierda y si las dos se centran, se pisan
        pie_g = nota("10 000 personas · cada cuadrito son 10", scale=0.44)
        pie_g.next_to(celdas, UP, buff=0.3).align_to(celdas, RIGHT)
        self.play(FadeIn(celdas, lag_ratio=0.0005, run_time=1.6), FadeIn(pie_g))
        self.wait(0.5)

        n_total = FIL * COL
        n_enf = int(round(PREVALENCIA * n_total))                    # 10
        n_vp = int(round(n_enf * SENSIBILIDAD))                      # 10
        n_fp = int(round((n_total - n_enf) * (1 - ESPECIFICIDAD)))   # 50

        # los enfermos arriba a la izquierda y los falsos positivos al final
        # de la grilla: pegados no se distinguen, y ese contraste es el punto
        enfermos = VGroup(*celdas[:n_enf])
        falsos = VGroup(*celdas[-n_fp:])

        self.play(enfermos.animate.set_fill(ROJO, opacity=1.0)
                  .set_stroke(ROJO, width=1.4), run_time=1.0)
        marco_e = SurroundingRectangle(enfermos, color=ROJO, buff=0.03,
                                       stroke_width=2.5)
        lab_e = VGroup(
            Text(f"{n_enf*10} enfermos", color=ROJO).scale(0.48),
            nota("el 1 %", scale=0.40),
        ).arrange(RIGHT, buff=0.18)
        lab_e.next_to(marco_e, UP, buff=0.18).align_to(marco_e, LEFT)
        self.play(Create(marco_e), FadeIn(lab_e))
        self.wait(1.4)

        # ---- los falsos positivos
        self.play(falsos.animate.set_fill(AMBAR, opacity=1.0)
                  .set_stroke(AMBAR, width=1.4), run_time=1.2)
        marco_f = SurroundingRectangle(falsos, color=AMBAR, buff=0.03,
                                       stroke_width=2.5)
        lab_f = VGroup(
            Text(f"{n_fp*10} falsos positivos", color=AMBAR).scale(0.48),
            nota("el 5 % de los sanos", scale=0.40),
        ).arrange(RIGHT, buff=0.18)
        lab_f.next_to(marco_f, DOWN, buff=0.18).align_to(marco_f, RIGHT)
        self.play(Create(marco_f), FadeIn(lab_f))
        self.wait(1.8)

        # ---- comparar los dos grupos de positivos, lado a lado
        self.play(FadeOut(VGroup(celdas, marco_e, marco_f, lab_e, lab_f, pie_g)))

        ESC = 0.0052        # alto por persona
        b_vp = Rectangle(width=1.5, height=n_vp * 10 * ESC, stroke_width=0,
                         fill_color=ROJO, fill_opacity=0.95)
        b_fp = Rectangle(width=1.5, height=n_fp * 10 * ESC, stroke_width=0,
                         fill_color=AMBAR, fill_opacity=0.95)
        barras = VGroup(b_vp, b_fp).arrange(RIGHT, buff=1.3, aligned_edge=DOWN)
        barras.move_to(ORIGIN).shift(UP * 0.55)
        t_vp = VGroup(Text(f"{n_vp*10}", color=ROJO).scale(0.62),
                      nota("enfermos", scale=0.42)).arrange(DOWN, buff=0.1)
        t_vp.next_to(b_vp, DOWN, buff=0.22)
        t_fp = VGroup(Text(f"{n_fp*10}", color=AMBAR).scale(0.62),
                      nota("sanos", scale=0.42)).arrange(DOWN, buff=0.1)
        t_fp.next_to(b_fp, DOWN, buff=0.22)
        rot = Text("de cada 600 positivos…", color=INK).scale(0.55)
        rot.next_to(barras, UP, buff=0.45)

        self.play(FadeIn(rot))
        self.play(GrowFromEdge(b_vp, DOWN), FadeIn(t_vp), run_time=0.8)
        self.play(GrowFromEdge(b_fp, DOWN), FadeIn(t_fp), run_time=0.8)
        self.wait(1.4)

        vpp = n_vp / (n_vp + n_fp)
        cuenta = MathTex(
            r"P(\text{enfermo}\mid +)=\frac{"
            + f"{n_vp*10}" + r"}{" + f"{n_vp*10}" + r"+" + f"{n_fp*10}" + r"}"
            + r"\approx" + f"{vpp:.0%}".replace("%", r"\,\%"),
            color=TXT).scale(0.78)
        cuenta.next_to(VGroup(t_vp, t_fp), DOWN, buff=0.5)
        self.play(Write(cuenta))
        self.wait(2.2)

        moraleja = Text("con una enfermedad rara, la mayoría de los positivos "
                        "son sanos", color=AMBAR).scale(0.52)
        moraleja.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(moraleja))
        self.wait(2.4)

        # ============================================ cierre
        self.play(FadeOut(VGroup(barras, t_vp, t_fp, rot, cuenta, moraleja)))
        cierre = VGroup(
            Text("La probabilidad a priori pesa tanto como el dato.",
                 color=TXT).scale(0.6),
            nota("Esta misma cuenta vuelve en el capítulo 9, con otro nombre:\n"
                 "es el valor predictivo positivo de un detector.", scale=0.5),
        ).arrange(DOWN, buff=0.4)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.wait(0.5)
        self.play(FadeIn(cierre[1]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
