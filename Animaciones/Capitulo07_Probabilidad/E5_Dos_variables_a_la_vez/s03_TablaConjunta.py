"""Escena 03 — La tabla conjunta del canal: cuatro parejas, cuatro casillas, cuatro cuentas."""
from comun.escena import *


class TablaConjunta(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.tabla = Tabla2x2(centro=(-3.0, -0.7), lado=2.0)
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        canal = canal7(centro=(0, 1.0), ancho=8.4, escala=1.1)
        p0 = MathTex(r"0\ \to\ 0{,}7", color=SENAL).scale(0.8).move_to(canal.p_ent() + RIGHT * 1.5 + UP * 0.5)
        p1 = MathTex(r"1\ \to\ 0{,}3", color=SENAL).scale(0.8).move_to(canal.p_ent() + RIGHT * 1.5 + DOWN * 0.5)
        err = MathTex(r"10\,\%", color=ERROR).scale(0.9).next_to(canal.caja, UP, buff=0.2)
        s = MathTex("S", color=SENAL).scale(1.0).move_to(canal.p_ent() + LEFT * 0.4)
        r = MathTex("R", color=MEDIDA).scale(1.0).move_to(canal.p_sal() + RIGHT * 0.4)
        par = MathTex("(", "S", ",", "R", ")", color=TXT).scale(1.4).move_to([0, 2.9, 0])
        par[1].set_color(SENAL)
        par[3].set_color(MEDIDA)
        t = self.tabla
        with self.narrar("b1"):
            # «Volvamos al canal»
            self.en("canal")
            self.play(FadeIn(canal), run_time=self.dur(0.6))

            # «que confunde bits»
            self.en("confunde")
            self.resaltar(canal.caja, color=ERROR, run_time=0.5)

            # «se envía un cero»
            self.en("envia")
            canal.ent.permitir_encima = True
            bit = MathTex("0", color=SENAL).scale(1.1).move_to(canal.p_ent() + RIGHT * 0.3)
            self.play(FadeIn(bit), run_time=0.2)
            self.play(bit.animate.move_to(canal.caja.get_left() + LEFT * 0.25), run_time=self.dur(0.8))
            self.play(FadeOut(bit), run_time=0.15)

            # «cero coma siete»
            self.en("p0")
            self.play(FadeIn(p0, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «un uno con cero coma tres»
            self.en("p1")
            self.play(FadeIn(p1, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «una de cada diez veces»
            self.en("error")
            self.pop(err)
            self.resaltar(canal.caja, color=ERROR, run_time=0.5)

            # «ese a lo que se envió»
            self.en("s")
            self.pop(s)

            # «erre a lo que se recibió»
            self.en("r")
            self.pop(r)

            # «las dos variables a la vez»
            self.en("dos")
            self.pop(par)

            # «qué pareja sale cada vez»
            self.en("cada")
            self.play(Indicate(par, color=AMBAR, scale_factor=1.25), run_time=self.dur(0.7))

            # «cuatro parejas posibles»
            self.en("parejas")
            fila = VGroup(*[MathTex(f"({a},{b})", color=TXT).scale(0.95) for a in (0, 1) for b in (0, 1)])
            fila.arrange(RIGHT, buff=0.9).move_to([0, -2.2, 0])
            self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.2) for p in fila], lag_ratio=0.25), run_time=self.dur(1.4))

            # «sus probabilidades»
            self.en("probs")
            self.play(fila.animate(rate_func=there_and_back).scale(1.15), run_time=self.dur(0.6))

            # «una tabla»
            self.en("tabla")
            todo = VGroup(canal, p0, p1, err, s, r)
            self.play(FadeOut(par), FadeOut(fila),
                      todo.animate.scale(0.6).move_to([0, 3.3, 0]), run_time=self.dur(0.8))
            self.play(Create(VGroup(*[c for f in t.cel for c in f])), run_time=self.dur(0.7))

            # «filas para lo enviado»
            self.en("filas")
            self.play(FadeIn(VGroup(*t.rot_f), shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «columnas para lo recibido»
            self.en("columnas")
            self.play(FadeIn(VGroup(*t.rot_c), shift=DOWN * 0.2), run_time=self.dur(0.5))
        self.todo_canal = todo

    # ---------------------------------------------------------------- b2
    def casilla(self, i, j, cuenta, valor):
        """Muestra la cuenta de la casilla (i, j) y la convierte en su valor."""
        t = self.tabla
        c = MathTex(cuenta, color=TXT).scale(0.8).move_to(t.c(i, j))
        v = t.valor(i, j, valor, VERDE, 1.2)
        return c, v

    def bloque2(self):
        t = self.tabla
        regla = formula("P(A,B)", "=", "P(A)", r"\cdot", r"P(B\mid A)", escala=1.0,
                        colores={0: AMBAR}).move_to([3.6, 1.7, 0])
        cuentas = {(0, 0): (r"0{,}7\cdot0{,}9", r"0{,}63"), (0, 1): (r"0{,}7\cdot0{,}1", r"0{,}07"),
                   (1, 0): (r"0{,}3\cdot0{,}1", r"0{,}03"), (1, 1): (r"0{,}3\cdot0{,}9", r"0{,}27")}
        obj = {k: self.casilla(*k, *v) for k, v in cuentas.items()}
        suma = MathTex(r"0{,}63+0{,}07+0{,}03+0{,}27=1", color=TXT).scale(0.9).move_to([3.2, -1.0, 0])
        with self.narrar("b2"):
            # «la regla del producto»
            self.en("regla")
            self.play(FadeIn(regla[0:2], shift=DOWN * 0.15), run_time=self.dur(0.5))
            self.play(FadeIn(regla[2:], shift=DOWN * 0.15), run_time=self.dur(0.7))

            # «Enviar un cero y recibir un cero»
            self.en("c00")
            m = t.marco(0, 0)
            self.play(Create(m), run_time=self.dur(0.3))

            # «cero coma siete por cero coma nueve»
            self.en("cuenta00")
            self.play(FadeIn(obj[(0, 0)][0]), run_time=self.dur(0.4))

            # «cero coma sesenta y tres»
            self.en("r00")
            self.play(ReplacementTransform(obj[(0, 0)][0], obj[(0, 0)][1]), run_time=self.dur(0.5))

            # «Enviar un cero y recibir un uno»
            self.en("c01")
            self.play(m.animate.move_to(t.c(0, 1)), run_time=self.dur(0.35))

            # «cero coma siete por cero coma uno»
            self.en("cuenta01")
            self.play(FadeIn(obj[(0, 1)][0]), run_time=self.dur(0.4))

            # «cero coma cero siete»
            self.en("r01")
            self.play(ReplacementTransform(obj[(0, 1)][0], obj[(0, 1)][1]), run_time=self.dur(0.5))

            # «Enviar un uno y recibir un cero»
            self.en("c10")
            self.play(m.animate.move_to(t.c(1, 0)), run_time=self.dur(0.35))

            # «cero coma cero tres»
            self.en("r10")
            self.play(FadeIn(obj[(1, 0)][0]), run_time=self.dur(0.35))
            self.play(ReplacementTransform(obj[(1, 0)][0], obj[(1, 0)][1]), run_time=self.dur(0.4))

            # «Y enviar un uno y recibir un uno»
            self.en("c11")
            self.play(m.animate.move_to(t.c(1, 1)), run_time=self.dur(0.35))

            # «cero coma veintisiete»
            self.en("r11")
            self.play(FadeIn(obj[(1, 1)][0]), run_time=self.dur(0.35))
            self.play(ReplacementTransform(obj[(1, 1)][0], obj[(1, 1)][1]), run_time=self.dur(0.4))

            # «suman uno»
            self.en("suman")
            self.play(FadeOut(m), run_time=0.2)
            self.play(FadeIn(suma, shift=LEFT * 0.2), run_time=self.dur(0.7))
