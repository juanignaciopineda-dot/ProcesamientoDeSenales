"""Escena 09 — Tres segundos termómetros; el primero, una copia exacta de A: no aporta y la matriz no tiene inversa."""
from comun.escena import *
from comun.figuras_c8e5 import *

ESQ = [(5.0, 3.3), (6.1, 3.3)]       # dónde esperan las tarjetas que todavía no se dieron vuelta


class LaCopiaExacta(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.encuesta()
        self.sin_inversa()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def encuesta(self):
        A0 = Termo8("A", centro=(-4.5, 0.6), alto=2.8, escala_letra=1.0)
        mas = Text("+ ?", color=AMBAR, weight=BOLD).scale(1.6).move_to([-1.6, 0.8, 0])
        r = ruido8(centro=(-1.6, -0.9), ancho=2.4, amp=0.22, semilla=6, grosor=4)
        cartas = [tarjeta8(t, centro=(x, -0.3)) for t, x in ((r"B_1", -4.0), (r"B_2", 0.0), (r"B_3", 4.0))]
        reloj = reloj_arena().scale(0.9).move_to([0, 2.6, 0])
        A = Termo8("A", centro=(-4.2, 0.2), alto=2.8, escala_letra=1.0)
        B1 = Termo8("B_1", centro=(-0.6, 0.2), alto=2.8, escala_letra=1.0)
        cable = ArcBetweenPoints(A.t.bulbo.get_bottom() + DOWN * 0.05, B1.t.bulbo.get_bottom() + DOWN * 0.05,
                                 angle=TAU / 5, color=INK, stroke_width=5)
        na = Text("23", color=MEDIDA, weight=BOLD).scale(0.8).next_to(A.t.tubo, RIGHT, buff=0.25)
        nb = Text("23", color=MEDIDA, weight=BOLD).scale(0.8).next_to(B1.t.tubo, RIGHT, buff=0.25)
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.6).move_to([1.4, 2.0, 0])

        with self.narrar("b1"):
            # «¿Añadir un termómetro siempre ayuda?»
            self.en("ayuda")
            self.play(FadeIn(A0), run_time=0.4)
            self.pop(mas)

            # «Depende de cómo sea su ruido»
            self.en("ruido")
            self.play(Create(r), run_time=self.dur(0.8))

            # «tres segundos termómetros distintos»
            self.en("tres")
            self.play(FadeOut(A0), FadeOut(mas), FadeOut(r), run_time=0.3)
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.3) for c in cartas], lag_ratio=0.25), run_time=self.dur(0.9))

            # «piensa cada respuesta»
            self.en("piensa")
            self.play(FadeIn(reloj, scale=0.6), run_time=0.3)
            self.play(Rotate(reloj, PI), run_time=self.dur(0.8))

            # «El primero es un cable»
            self.en("b1")
            self.play(FadeOut(reloj), cartas[0].animate.stretch(0.03, 0),
                      *[c.animate.scale(0.3).move_to([x, y, 0]) for c, (x, y) in zip(cartas[1:], ESQ)],
                      run_time=self.dur(0.5))
            self.remove(cartas[0])
            self.play(FadeIn(A), FadeIn(B1), run_time=self.dur(0.4))
            self.play(Create(cable), run_time=self.dur(0.6))

            # «marca exactamente lo mismo»
            self.en("igual")
            self.play(A.nivel(0.7), B1.nivel(0.7), run_time=self.dur(0.5))
            self.play(FadeIn(na), FadeIn(nb), run_time=0.3)

            # «¿Cuánto aporta?»
            self.en("cuanto")
            self.pop(q)
        self.q, self.cartas = q, cartas[1:]

    # ------------------------------------------------------------ b2
    def sin_inversa(self):
        cero = Text("0", color=AMBAR, weight=BOLD).scale(1.6).move_to(self.q)
        lin = formula(r"C_{xx}", r"\,\mathbf{h}", "=", r"\mathbf{c}_{xy}", escala=1.1,
                      colores={1: ESTIMACION, 3: SENAL}).move_to([-3.8, 3.0, 0])
        M = Matriz8([["5", "5"], ["5", "5"]], centro=(-3.8, 1.0), dx=1.3, dy=1.0, escala=1.3)
        det = MathTex(r"\det=5\cdot 5-5\cdot 5", color=TXT).scale(1.0).move_to([-4.3, -1.0, 0])
        d0 = MathTex("=0", color=ERROR).scale(1.0).next_to(det, RIGHT, buff=0.15)
        inv = MathTex(r"C_{xx}^{-1}", color=TXT).scale(1.2).move_to([-3.8, -2.5, 0])
        tache = tachar(inv)
        pares = VGroup(*[MathTex(t, color=ESTIMACION).scale(0.95).move_to([2.2, y, 0])
                         for t, y in ((r"(0{,}8\,;\,0)", 2.0), (r"(0{,}4\,;\,0{,}4)", 1.0), (r"(0\,;\,0{,}8)", 0.0))])
        meta = MathTex(r"\hat{y}=22{,}4", color=ESTIMACION).scale(1.0).move_to([5.6, 1.0, 0])
        flechas = VGroup(*[Arrow(p.get_right() + RIGHT * 0.1, meta.get_left() + LEFT * 0.1, buff=0, color=INK,
                                 stroke_width=3, max_tip_length_to_length_ratio=0.12) for p in pares])
        A = Termo8("A", centro=(1.4, -2.2), alto=1.3, escala_letra=0.7)
        B1 = Termo8("B_1", centro=(3.6, -2.2), alto=1.3, escala_letra=0.7)
        n1 = Text("23", color=MEDIDA, weight=BOLD).scale(0.55).next_to(A.t.tubo, RIGHT, buff=0.2)
        n2 = Text("23", color=MEDIDA, weight=BOLD).scale(0.55).next_to(B1.t.tubo, RIGHT, buff=0.2)
        par = VGroup(A, B1, n1, n2)
        nueva = Text("Repetida = nada nuevo", color=AMBAR, weight=BOLD).scale(0.65).move_to([2.6, -2.3, 0])

        with self.narrar("b2"):
            # «Nada, claro»
            self.en("nada")
            self.play(ReplacementTransform(self.q, cero), run_time=self.dur(0.5))

            # «Y las ecuaciones lo notan»
            self.en("notan")
            self.corte(*self.cartas)
            self.play(FadeIn(lin, shift=DOWN * 0.1), run_time=self.dur(0.5))

            # «La matriz de covarianzas»
            self.en("mat")
            self.play(FadeIn(M), run_time=self.dur(0.5))

            # «todas sus casillas iguales»
            self.en("iguales")
            self.resaltar(M.todas(), color=AMBAR, escala=1.3, run_time=0.7)

            # «El determinante»
            self.en("det")
            self.play(FadeIn(det, shift=UP * 0.1), run_time=self.dur(0.6))

            # «es cero»
            self.en("cero")
            self.pop(d0, sonido="error")

            # «no tiene inversa»
            self.en("noinv")
            self.play(FadeIn(inv), run_time=0.3)
            self.play(Create(tache), run_time=self.dur(0.4))

            # «infinitos pares de pesos»
            self.en("pares")
            self.play(LaggedStart(*[FadeIn(p, shift=LEFT * 0.2) for p in pares], lag_ratio=0.3), run_time=self.dur(0.9))

            # «dan la misma estimación»
            self.en("misma")
            self.play(*[GrowArrow(f) for f in flechas], FadeIn(meta), run_time=self.dur(0.6))

            # «da igual cómo repartas»
            self.en("reparte")
            self.resaltar(*pares, color=AMBAR, escala=1.12, run_time=0.6)

            # «dos lecturas idénticas»
            self.en("identicas")
            self.play(FadeIn(par), run_time=self.dur(0.6))

            # «Una medición repetida no es información nueva»
            self.en("nueva")
            self.play(FadeOut(par), run_time=0.3)
            self.pop(nueva)
