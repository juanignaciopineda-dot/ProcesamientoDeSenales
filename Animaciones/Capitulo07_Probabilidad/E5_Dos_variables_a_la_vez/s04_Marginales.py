"""Escena 04 — Marginales: sumar filas y columnas de la tabla conjunta."""
from comun.escena import *

# la tabla ya llena, igual que al final de la escena 03
VALORES = [[r"0{,}63", r"0{,}07"], [r"0{,}03", r"0{,}27"]]


class Marginales(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        t = Tabla2x2(centro=(-3.0, 0.6), lado=2.0)
        vals = [[t.valor(i, j, VALORES[i][j], VERDE, 1.2) for j in range(2)] for i in range(2)]
        todos = VGroup(*[v for f in vals for v in f])
        self.add(t, todos)
        # la tabla llega ya armada
        rot = Text("distribución conjunta", color=AMBAR, weight=BOLD).scale(0.7).move_to([4.0, 3.4, 0])
        sum_f = [MathTex(s, color=SENAL).scale(1.0).move_to(t.p_fila(i) + RIGHT * 1.9)
                 for i, s in enumerate((r"0{,}63+0{,}07=0{,}7", r"0{,}03+0{,}27=0{,}3"))]
        sum_c = [MathTex(r"\begin{array}{r}" + a + r"\\+\," + b + r"\\\hline " + c + r"\end{array}", color=MEDIDA)
                 .scale(0.85).move_to(t.p_col(j) + DOWN * 0.7)
                 for j, (a, b, c) in enumerate(((r"0{,}63", r"0{,}03", r"0{,}66"), (r"0{,}07", r"0{,}27", r"0{,}34")))]
        llaves_f = [Brace(VGroup(t.cel[i][0], t.cel[i][1]), RIGHT, color=SENAL, buff=0.1) for i in range(2)]
        llaves_c = [Brace(VGroup(t.cel[0][j], t.cel[1][j]), DOWN, color=MEDIDA, buff=0.1) for j in range(2)]
        with self.narrar("b1"):
            # «distribución conjunta»
            self.en("conjunta")
            self.pop(rot)

            # «contiene todo»
            self.en("todo")
            marco = SurroundingRectangle(VGroup(*[c for f in t.cel for c in f]), color=AMBAR, buff=0.08, stroke_width=4)
            self.play(Create(marco), run_time=self.dur(0.5))

            # «lo que se envió»
            self.en("envio")
            self.play(*[Indicate(m, color=AMBAR, scale_factor=1.3) for m in t.rot_f], run_time=self.dur(0.7))

            # «suma cada fila»
            self.en("filas")
            self.play(FadeOut(marco), *[GrowFromCenter(l) for l in llaves_f], run_time=self.dur(0.5))

            # «cero coma siete y cero coma tres»
            self.en("m_s")
            self.play(FadeIn(sum_f[0], shift=LEFT * 0.2), run_time=self.dur(0.5))
            self.play(FadeIn(sum_f[1], shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «probabilidades de partida»
            self.en("partida")
            partida = Text("las de partida", color=SENAL).scale(0.65).next_to(VGroup(*sum_f), DOWN, buff=0.4)
            self.play(FadeIn(partida), run_time=self.dur(0.4))

            # «lo recibido»
            self.en("recibido")
            self.play(*[Indicate(m, color=AMBAR, scale_factor=1.3) for m in t.rot_c], run_time=self.dur(0.7))

            # «suma cada columna»
            self.en("columnas")
            self.play(*[GrowFromCenter(l) for l in llaves_c], run_time=self.dur(0.5))

            # «cero coma sesenta y seis y cero coma treinta y cuatro»
            self.en("m_r")
            self.play(FadeIn(sum_c[0], shift=UP * 0.2), run_time=self.dur(0.5))
            self.play(FadeIn(sum_c[1], shift=UP * 0.2), run_time=self.dur(0.5))

            # «A estas sumas»
            self.en("sumas")
            self.play(*[Indicate(m, color=AMBAR, scale_factor=1.2) for m in sum_f + sum_c], run_time=self.dur(0.8))

            # «los márgenes de la tabla»
            self.en("margenes")
            self.play(*[l.animate.set_color(AMBAR) for l in llaves_f + llaves_c], run_time=self.dur(0.5))

            # «marginales»
            self.en("marginales")
            marg = self.palabra("marginales", AMBAR, 1.1).move_to([4.2, -2.4, 0])
            self.pop(marg)
        self.wait(1.0)
        self.limpiar()
