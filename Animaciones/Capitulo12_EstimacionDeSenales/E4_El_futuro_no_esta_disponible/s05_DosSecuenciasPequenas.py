"""Escena 05 — Dos secuencias iguales en media recta tienen transformadas distintas."""
from comun.escena import *


class DosSecuenciasPequenas(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        p = oculta(Tallos([0, 0, 1, 0, 0, 0], centro=(-1.8, 1.7), paso=0.9, unidad=0.9, color=SENAL, k0=-2))
        q = oculta(Tallos([0, 3, 1, 0, 0, 0], centro=(-1.8, -0.3), paso=0.9, unidad=0.5, color=RUIDO, k0=-2,
                          indices=True))
        self.add(p, q)
        q.tallos[1].set_color(ROJO)
        q.puntos[1].set_color(ROJO)
        lp = MathTex("p", color=SENAL).scale(0.9).move_to([-6.0, 1.7, 0])
        lq = MathTex("q", color=RUIDO).scale(0.9).move_to([-6.0, -0.3, 0])
        uno_p = Text("1", color=TXT).scale(0.5).move_to([p.x(2), 1.7 + 0.9 + 0.3, 0])
        uno_q = Text("1", color=TXT).scale(0.5).move_to([q.x(2), -0.3 + 0.5 + 0.3, 0])
        tres_q = Text("3", color=ROJO).scale(0.5).move_to([q.x(1), -0.3 + 1.5 + 0.3, 0])
        ceros = [Text("0", color=INK).scale(0.4).move_to([p.x(i), 1.7 + 0.3, 0]) for i in (0, 1, 3, 4, 5)]
        marco = Rectangle(width=3.3, height=4.5, color=VERDE, stroke_width=4).set_fill(VERDE, 0.06)
        marco.move_to([-0.9, 1.05, 0])
        pb = caja_tex("P", AZUL, ancho=3.4, alto=0.9).move_to([4.9, 1.7, 0])
        qb = caja_tex("Q", RUIDO, ancho=3.4, alto=0.9).move_to([4.9, -0.3, 0])
        ne = MathTex(r"\neq", color=ROJO).scale(0.9).move_to([4.9, 0.7, 0])
        p_eq = MathTex(r"P=1", color=TXT).scale(0.9).move_to(pb.tex)
        q_eq = MathTex(r"Q=1+3e^{j\Omega}", color=TXT).scale(0.85).move_to(qb.tex)
        t1 = etiqueta("iguales en media recta", TXT, 0.6).move_to([-2.6, -2.9, 0])
        t2 = etiqueta("en general", AMBAR, 0.5).move_to([3.2, -2.35, 0])
        t3 = etiqueta("≠ misma transformada", ROJO, 0.6).move_to([3.2, -2.9, 0])
        with self.narrar("b1"):
            # «La primera vale uno en cero»
            self.en("p")
            self.play(*revelar(p.base, p.tallos[2], p.puntos[2]), FadeIn(lp), FadeIn(uno_p), run_time=self.dur(0.7))

            # «y nada más»
            self.en("nada")
            self.play(*revelar(*[p.puntos[i] for i in (0, 1, 3, 4, 5)]), *[FadeIn(c) for c in ceros],
                      run_time=self.dur(0.6))

            # «La segunda vale uno en cero»
            self.en("q")
            self.play(*revelar(q.base, q.ks, q.tallos[2], *[q.puntos[i] for i in (0, 2, 3, 4, 5)]),
                      FadeIn(lq), FadeIn(uno_q), run_time=self.dur(0.7))

            # «tres en la posición menos uno»
            self.en("tres")
            self.play(*revelar(q.tallos[1], q.puntos[1]), FadeIn(tres_q), run_time=self.dur(0.6))
            self.sfx("tick")

            # «Coinciden para todo eme mayor o igual que cero»
            self.en("coinciden")
            self.play(Create(marco), run_time=self.dur(0.8))
            self.sfx("exito", gain=-18)

            # «sus transformadas son distintas»
            self.en("distintas")
            self.play(FadeIn(pb), FadeIn(qb), run_time=self.dur(0.5))
            self.pop(ne, sonido="error")

            # «la primera es uno»
            self.en("pp")
            self.play(ReplacementTransform(pb.tex, p_eq), run_time=self.dur(0.6))

            # «uno más tres e elevado a jota omega»
            self.en("qq")
            self.play(ReplacementTransform(qb.tex, q_eq), run_time=self.dur(0.9))

            # «Dos secuencias»
            self.en("dossec")
            self.resaltar(p.base, q.base, run_time=self.dur(0.5))

            # «iguales solo en la mitad del eje»
            self.en("mitad")
            self.play(FadeIn(t1), run_time=self.dur(0.5))

            # «en general»
            self.en("engeneral")
            self.play(FadeIn(t2), run_time=self.dur(0.4))

            # «la misma transformada»
            self.en("misma")
            self.play(FadeIn(t3), run_time=self.dur(0.5))

        self.wait(1.0)
        self.limpiar()
