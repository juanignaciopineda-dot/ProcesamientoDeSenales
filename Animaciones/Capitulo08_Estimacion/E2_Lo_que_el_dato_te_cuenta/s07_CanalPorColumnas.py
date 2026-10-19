"""Escena 07 — El canal, columna por columna: se recibe 1 → apuesta 0,79; se recibe 0 → apuesta 0,045."""
from comun.escena import *


class CanalPorColumnas(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.canal = canal7(centro=(-1.0, 3.0), ancho=6.4, escala=0.7)
        self.T = Tabla2x2(centro=(-2.6, -1.0), lado=1.8)
        self.vals = [[self.T.valor(i, j, CANAL8[i][j], TXT, 0.9) for j in range(2)] for i in range(2)]
        self.col1 = self.marco_col(1)
        self.col0 = self.marco_col(0)
        self.recibido1()
        self.recibido0()
        self.wait(1.0)
        self.limpiar()

    def marco_col(self, j):
        T = self.T
        r = Rectangle(width=T.lado, height=2 * T.lado, color=AMBAR, stroke_width=6)
        return r.move_to((T.c(0, j) + T.c(1, j)) / 2)

    def recibido1(self):
        c, T = self.canal, self.T
        with self.narrar("b1"):
            # «canal que confunde bits»
            self.en("canal")
            self.play(FadeIn(c), run_time=self.dur(0.5))

            # «Se envía un cero»
            self.en("envia")
            cero = MathTex("0", color=SENAL).scale(1.0).move_to(c.p_ent() + UP * 0.6)
            self.play(FadeIn(cero), run_time=0.2)
            self.play(cero.animate.move_to(c.caja.get_left() + LEFT * 0.5 + UP * 0.6), run_time=self.dur(0.7))
            self.play(FadeOut(cero), run_time=0.2)

            # «cero coma siete»
            self.en("p0")
            self.p0 = MathTex(r"0:\ 0{,}7", color=SENAL).scale(0.8).move_to(c.ent.get_center() + UP * 0.5)
            self.pop(self.p0)

            # «un uno con cero coma tres»
            self.en("p1")
            self.p1 = MathTex(r"1:\ 0{,}3", color=SENAL).scale(0.8).move_to(c.ent.get_center() + DOWN * 0.5)
            self.pop(self.p1)

            # «una de cada diez veces»
            self.en("error")
            e = MathTex(r"10\ \%", color=ERROR).scale(0.8).next_to(c.caja, UP, buff=0.15)
            self.pop(e)

            # «Si recibes un uno»
            self.en("recibes")
            self.play(Create(VGroup(*[x for f in T.cel for x in f])), FadeIn(VGroup(*T.rot_f, *T.rot_c)),
                      FadeIn(VGroup(*[v for f in self.vals for v in f])), run_time=self.dur(1.0))
            self.play(Create(self.col1), run_time=self.dur(0.4))

            # «la columna de recibir uno»
            self.en("columna")
            self.resaltar(self.col1, color=AMBAR)

            # «se envió un uno»
            self.en("env1")
            self.play(Create(T.marco(1, 1, VERDE, 4)), run_time=self.dur(0.4))

            # «cero coma setenta y nueve»
            self.en("n79")
            self.frac = MathTex(r"\frac{0{,}27}{0{,}34}\approx 0{,}79", color=VERDE).scale(1.0).move_to([3.9, -0.4, 0])
            self.pop(self.frac)

            # «la media de lo enviado»
            self.en("media_env")
            self.esp = MathTex(r"E[S\mid R=1]", color=AMBAR).scale(0.9).move_to([3.9, 0.9, 0])
            self.pop(self.esp)

            # «esa es la apuesta»
            self.en("apuesta")
            self.ap = MathTex(r"\hat{s}=0{,}79", color=VERDE).scale(1.1).move_to([3.9, -1.9, 0])
            self.rec = SurroundingRectangle(self.ap, color=VERDE, buff=0.2, stroke_width=4)
            self.pop(self.ap)
            self.play(Create(self.rec), run_time=self.dur(0.4))

    def recibido0(self):
        T = self.T
        with self.narrar("b2"):
            # «Si recibes un cero»
            self.en("cero")
            self.play(FadeOut(self.frac), FadeOut(self.esp), FadeOut(self.ap), FadeOut(self.rec),
                      FadeOut(self.col1), run_time=self.dur(0.4))
            self.play(Create(self.col0), run_time=self.dur(0.4))

            # «en la otra columna»
            self.en("otra")
            self.play(Create(T.marco(0, 1, VERDE, 4)), run_time=self.dur(0.4))
            self.play(FadeOut(self.p0), FadeOut(self.p1), run_time=0.2)

            # «cero coma cero cuatro cinco»
            self.en("n045")
            f = MathTex(r"\frac{0{,}03}{0{,}66}\approx 0{,}045", color=VERDE).scale(1.0).move_to([3.9, -0.4, 0])
            self.pop(f)

            # «apuestas eso»
            self.en("apuesta0")
            ap = MathTex(r"\hat{s}=0{,}045", color=VERDE).scale(1.1).move_to([3.9, -1.9, 0])
            rec = SurroundingRectangle(ap, color=VERDE, buff=0.2, stroke_width=4)
            self.pop(ap)
            self.play(Create(rec), run_time=self.dur(0.4))

            # «los errores son las varianzas»
            self.en("errores")
            self.play(FadeOut(f), FadeOut(ap), FadeOut(rec), run_time=0.3)
            et = Text("Error = varianza", color=ERROR, weight=BOLD).scale(0.6).move_to([4.2, 1.9, 0])
            self.pop(et)

            # «Para algo que vale uno»
            self.en("algo")
            bit = MathTex(r"S\in\{0,\,1\}", color=SENAL).scale(0.9).move_to([3.9, 0.9, 0])
            self.pop(bit)

            # «con probabilidad pe»
            self.en("pe")
            p1 = MathTex(r"P(S=1)=p", color=TXT).scale(0.8).move_to([3.9, 0.1, 0])
            self.pop(p1)

            # «y cero si no»
            self.en("cero_si_no")
            p0 = MathTex(r"P(S=0)=1-p", color=TXT).scale(0.8).move_to([3.9, -0.7, 0])
            self.pop(p0)

            # «pe por uno menos pe»
            self.en("pq")
            pq = MathTex("p", "(", "1", "-", "p", ")", color=ERROR).scale(1.3).move_to([3.9, -2.0, 0])
            self.play(LaggedStart(*[FadeIn(pq[i], scale=0.5) for i in range(6)], lag_ratio=0.2), run_time=self.dur(1.3))

            # «Cero coma uno seis»
            self.en("e16")
            r16 = MathTex(r"\approx 0{,}16", color=ERROR).scale(0.9).move_to(T.c(1, 1) + DOWN * (T.lado / 2 + 0.55))
            self.pop(r16)

            # «cero coma cero cuatro»
            self.en("e04")
            r04 = MathTex(r"\approx 0{,}04", color=ERROR).scale(0.9).move_to(T.c(1, 0) + DOWN * (T.lado / 2 + 0.55))
            self.pop(r04)
