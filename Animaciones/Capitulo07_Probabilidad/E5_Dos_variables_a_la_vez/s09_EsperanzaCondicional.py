"""Escena 09 — Esperanza condicional con la tabla: dos respuestas según lo que se reciba, luego es una variable aleatoria."""
from comun.escena import *

VALORES = [[r"0{,}63", r"0{,}07"], [r"0{,}03", r"0{,}27"]]


class EsperanzaCondicional(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.t = Tabla2x2(centro=(-3.4, 0.2), lado=2.0)
        self.vals = [[self.t.valor(i, j, VALORES[i][j], VERDE, 1.2) for j in range(2)] for i in range(2)]
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def columna(self, j, color=AMBAR):
        t = self.t
        return Rectangle(width=t.lado, height=2 * t.lado, color=color, stroke_width=5).move_to(
            (t.c(0, j) + t.c(1, j)) / 2)

    def vela(self, j):
        t = self.t
        return Rectangle(width=t.lado, height=2 * t.lado, stroke_width=0).set_fill(FONDO, 0.72).move_to(
            (t.c(0, j) + t.c(1, j)) / 2)

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        t = self.t
        vela0, vela1 = self.vela(0), self.vela(1)
        marco = self.columna(1)
        p1 = MathTex(r"S=1:\ 0{,}79", color=VERDE).scale(0.95).move_to([3.2, 1.4, 0])
        p0 = MathTex(r"S=0:\ 0{,}21", color=INK).scale(0.95).move_to([3.2, 0.5, 0])
        cuenta = MathTex(r"0\cdot0{,}21+1\cdot0{,}79=0{,}79", color=TXT).scale(0.95).move_to([3.6, -0.7, 0])
        esp = formula(r"E[S\mid R=1]", "=", r"0{,}79", escala=1.2, colores={0: AMBAR, 2: VERDE}).move_to([3.4, 2.9, 0])
        with self.narrar("b1"):
            # «En la tabla del canal»
            self.en("tabla")
            self.play(Create(VGroup(*[c for f in t.cel for c in f])), FadeIn(VGroup(*t.rot_f, *t.rot_c)),
                      FadeIn(VGroup(*[v for f in self.vals for v in f])), run_time=self.dur(0.8))

            # «la columna de recibir un uno»
            self.en("columna")
            self.play(FadeIn(vela0), Create(marco), run_time=self.dur(0.6))

            # «Dentro de esa columna»
            self.en("dentro")
            self.resaltar(marco, color=AMBAR, escala=1.06, run_time=0.6)

            # «vale uno con probabilidad»
            self.en("vale")
            self.play(FadeIn(p1, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «cero coma setenta y nueve»
            self.en("p79")
            self.play(FadeIn(p0, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «sabiendo que se recibió un uno»
            self.en("sabiendo")
            self.play(Indicate(t.rot_c[1], color=AMBAR, scale_factor=1.3), Indicate(p1, color=AMBAR, scale_factor=1.2), run_time=self.dur(0.8))

            # «la media de lo enviado»
            self.en("cuenta")
            self.play(FadeIn(cuenta, shift=UP * 0.15), run_time=self.dur(1.0))

            # «es cero coma setenta y nueve»
            self.en("igual")
            self.play(Indicate(cuenta, color=VERDE, scale_factor=1.15), run_time=self.dur(0.8))

            # «esperanza condicional»
            self.en("esperanza")
            self.play(FadeIn(esp[0:2], shift=DOWN * 0.15), run_time=self.dur(0.5))
            self.play(FadeIn(esp[2], shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «mundo achicado»
            self.en("achicado")
            self.resaltar(marco, color=VERDE, escala=1.06, run_time=0.7)
        self.estado = VGroup(vela0, marco, p1, p0, cuenta)
        self.esp = esp
        self.vela1 = vela1
        self.vela0 = vela0

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        t = self.t
        marco0 = self.columna(0)
        frac = MathTex(r"\dfrac{0{,}03}{0{,}66}", color=TXT).scale(1.2).move_to([3.4, 0.6, 0])
        esp0 = formula(r"E[S\mid R=0]", r"\approx", r"0{,}045", escala=1.2, colores={0: AMBAR, 2: VERDE}).move_to([3.4, 1.8, 0])
        self.esp.generate_target()
        self.esp.target.move_to([3.4, 3.0, 0]).scale(0.85)
        mon = moneda("R", MEDIDA).scale(1.0).move_to([-3.4, -2.8, 0])
        var = formula(r"E[S\mid R]", escala=1.5, color=ESTIMACION).move_to([3.4, -1.6, 0])
        dep = Text("depende de R", color=MEDIDA).scale(0.6).next_to(var, DOWN, buff=0.35)
        with self.narrar("b2"):
            # «Si se recibió un cero»
            self.en("cero")
            self.play(Indicate(t.rot_c[0], color=AMBAR, scale_factor=1.3), run_time=self.dur(0.6))

            # «la columna es otra»
            self.en("otra")
            self.play(FadeOut(self.estado), FadeOut(self.vela0), FadeIn(self.vela1), Create(marco0),
                      MoveToTarget(self.esp), run_time=self.dur(0.7))

            # «mucho más pequeña»
            self.en("pequena")
            self.play(FadeIn(frac, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «cero coma cero cuatro cinco»
            self.en("r045")
            self.play(FadeIn(esp0[0:2], shift=DOWN * 0.15), run_time=self.dur(0.4))
            self.play(FadeIn(esp0[2], shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «Dos respuestas distintas»
            self.en("dos")
            self.resaltar(self.esp, esp0, color=AMBAR, escala=1.12, run_time=0.7)

            # «según lo que se reciba»
            self.en("segun")
            self.pop(mon)

            # «es aleatorio»
            self.en("aleatorio")
            self.play(Rotate(mon, angle=2 * PI, axis=UP), run_time=self.dur(1.0))

            # «una variable aleatoria»
            self.en("variable")
            self.pop(var)

            # «depende de lo que salga»
            self.en("depende")
            self.play(FadeIn(dep), Rotate(mon, angle=2 * PI, axis=UP), run_time=self.dur(1.0))
