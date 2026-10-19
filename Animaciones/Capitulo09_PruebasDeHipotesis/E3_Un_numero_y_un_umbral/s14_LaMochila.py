"""Escena 14 — Llenar la mochila: lo que más rinde por lo que cuesta es la razón de verosimilitud."""
from comun.escena import *
from comun.figuras_c9e3 import *

X_MOCH, Y_MOCH = -5.0, -2.45


class LaMochila(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        T = self.T = TablaNiveles9()
        # el plano con el que terminó la escena 13
        self.vs, self.vc = T.fila(0, T.SIN, ERROR), T.fila(1, T.CON, VERDE)
        self.rcu, self.rri = T.rot(0, "Cuesta", ERROR), T.rot(1, "Rinde", VERDE)
        tfa = Text("Falsa alarma", color=INK).scale(0.36).next_to(self.rcu, DOWN, buff=0.08).align_to(self.rcu, RIGHT)
        tde = Text("Detección", color=INK).scale(0.36).next_to(self.rri, DOWN, buff=0.08).align_to(self.rri, RIGHT)
        self.mon = monedero9("0,15", escala=0.85).move_to([5.6, -2.55, 0])
        self.add(T, self.vs, self.vc, self.rcu, self.rri, tfa, tde, self.mon)
        self.cocientes()
        self.comprar()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def cocientes(self):
        T = self.T
        with self.narrar("b1"):
            # «llenar una mochila»
            self.en("mochila")
            mo = mochila9(escala=0.75).move_to([X_MOCH, Y_MOCH, 0])
            self.play(FadeIn(mo, shift=UP * 0.2), run_time=self.dur(0.5))

            # «lo que más rinde por lo que cuesta»
            self.en("cociente")
            rq = T.rot(2, "Rinde / Cuesta", ESTIMACION)
            self.play(FadeIn(rq, shift=RIGHT * 0.15), run_time=self.dur(0.5))
            qs = T.fila(2, T.COCIENTE, ESTIMACION)

            # «Para el nivel cinco»
            self.en("n5")
            m5 = T.columna(4)
            self.play(Create(m5), run_time=self.dur(0.4))

            # «ese cociente es ocho»
            self.en("q5")
            self.play(FadeOut(m5), run_time=self.dur(0.2))
            self.pop(qs[4])

            # «Para el cuatro, tres»
            self.en("q4")
            self.pop(qs[3])

            # «Para el tres, uno»
            self.en("q3")
            self.pop(qs[2])

            # «menos de uno»
            self.en("q12")
            self.play(FadeIn(qs[1], scale=0.6), FadeIn(qs[0], scale=0.6), run_time=self.dur(0.4))

            # «lo que rinde con avión»
            self.en("num")
            self.play(Indicate(self.vc, color=VERDE, scale_factor=1.15), run_time=self.dur(0.5))

            # «lo que cuesta sin avión»
            self.en("den")
            self.play(Indicate(self.vs, color=ERROR, scale_factor=1.15), run_time=self.dur(0.5))

            # «la razón de verosimilitud»
            self.en("lambda")
            lam = MathTex(r"= \Lambda", color=MEDIDA).scale(0.8).next_to(rq, DOWN, buff=0.1).align_to(rq, RIGHT)
            self.pop(lam)
        self.mo, self.qs = mo, qs

    # ------------------------------------------------------------------ b2
    def comprar(self):
        T = self.T
        dentro = [self.mo.cuerpo.get_center() + LEFT * 0.35 + UP * 0.1, self.mo.cuerpo.get_center() + RIGHT * 0.35 + UP * 0.1]
        with self.narrar("b2"):
            # «el nivel cinco»
            self.en("m5")
            f5 = ficha9("5").move_to([T.x(4), 3.3, 0])
            self.play(FadeIn(f5, scale=0.6), run_time=self.dur(0.2))
            self.play(f5.animate.move_to(dentro[0]), run_time=self.dur(0.6))

            # «el nivel cuatro»
            self.en("m4")
            f4 = ficha9("4").move_to([T.x(3), 3.3, 0])
            self.play(FadeIn(f4, scale=0.6), run_time=self.dur(0.2))
            self.play(f4.animate.move_to(dentro[1]), run_time=self.dur(0.6))

            # «Cuestan cero coma quince»
            self.en("coste")
            co = Text("Coste: 0,05 + 0,10 = 0,15", color=ERROR, weight=BOLD).scale(0.5).move_to([0.9, -1.45, 0])
            vacio = monedero9("0", escala=0.85).move_to(self.mon)
            self.play(FadeIn(co, shift=UP * 0.1), Transform(self.mon, vacio), run_time=self.dur(0.5))

            # «la detección es cero coma setenta»
            self.en("d70")
            de = Text("Detección: 0,40 + 0,30 = 0,70", color=VERDE, weight=BOLD).scale(0.5).move_to([0.9, -2.15, 0])
            self.pop(de, sonido="exito")

            # «Con el mismo gasto»
            self.en("gasto")
            lleno = monedero9("0,15", escala=0.85).move_to(self.mon)
            self.play(Transform(self.mon, lleno), run_time=self.dur(0.4))

            # «solo el nivel tres»
            self.en("alt")
            alt = Text("Solo el nivel 3: coste 0,15 · detección 0,15", color=INK).scale(0.45).move_to([0.9, -3.0, 0])
            self.play(FadeIn(alt, shift=UP * 0.1), run_time=self.dur(0.4))

            # «detectarías cero coma quince»
            self.en("tacha")
            t = tachar(alt)
            self.play(Create(t), run_time=self.dur(0.4))

            # «Cualquier cambio»
            self.en("cambio")
            f3 = ficha9("3").move_to([T.x(2), 3.3, 0])
            pos4 = f4.get_center()
            self.play(FadeOut(VGroup(alt, t)), FadeIn(f3, scale=0.6), run_time=self.dur(0.3))
            self.play(f4.animate.move_to([T.x(3), 3.3, 0]), f3.animate.move_to(pos4), run_time=self.dur(0.7))

            # «algo que rinde menos»
            self.en("menos")
            de2 = Text("Detección: 0,40 + 0,15 = 0,55", color=ERROR, weight=BOLD).scale(0.5).move_to(de)
            self.play(Transform(de, de2), run_time=self.dur(0.4))
            self.sfx("error")
            de3 = Text("Detección: 0,40 + 0,30 = 0,70", color=VERDE, weight=BOLD).scale(0.5).move_to(de)
            self.play(f3.animate.move_to([T.x(2), 3.3, 0]), f4.animate.move_to(pos4), Transform(de, de3),
                      run_time=self.dur(0.7))
            self.play(FadeOut(f3), run_time=self.dur(0.3))
