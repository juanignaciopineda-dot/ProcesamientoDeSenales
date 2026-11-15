"""Escena 09 — Abrir las muestras: qué monedas contiene cada una."""
from comun.escena import *


class AbrirLasMuestras(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.pregunta()
        self.monedas()
        self.ahora()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def pregunta(self):
        reloj = reloj_arena().scale(0.9).move_to([-5.5, 2.8, 0])
        F = FilaMuestras([r"x[n-1]"], centro=(-3.0, 0.6), lado=2.12, color=MEDIDA, escala=1.17)
        sirve = Text("¿sirve?", color=AMBAR).scale(0.91).next_to(F.cas[0], UP, buff=0.25)
        nada = Text("correlación = 0", color=ERROR).scale(0.78).next_to(F.cas[0], DOWN, buff=0.3)
        truco = MathTex(r"h_1 = -0{,}19", color=AMBAR).scale(1.43).move_to([3.4, 0.6, 0])
        tl = tilde(VERDE, 0.4).next_to(truco, RIGHT, buff=0.35)
        bomb = bombilla(AMBAR).scale(1.0).move_to([0.0, 2.6, 0])
        monedas = VGroup(*[moneda("", RUIDO).scale(0.28) for _ in range(3)]).arrange(RIGHT, buff=0.12)
        monedas.move_to(F.cas[0])

        with self.narrar("b1"):
            # «Piénsalo un momento»
            self.en("pausa")
            self.corte()
            self.play(FadeIn(reloj), run_time=0.4)
            # «¿cómo puede servir un dato»
            self.en("servir")
            self.play(FadeIn(F), FadeIn(sirve), run_time=0.5)
            # «que no se parece en nada»
            self.en("nada")
            self.play(FadeIn(nada), run_time=0.4)
            # «No es un truco de las cuentas ni un error»
            self.en("truco")
            self.play(FadeIn(truco), run_time=0.4)
            self.play(FadeIn(tl), run_time=0.3)
            # «Hay una explicación sencilla»
            self.en("explic")
            self.play(FadeIn(bomb), run_time=0.5)
            # «abrir las muestras»
            self.en("abrir")
            self.play(F.animate.scale(1.5).move_to([-3.0, 0.2, 0]), FadeOut(sirve), FadeOut(nada), run_time=0.5)
            # «qué monedas contiene cada una»
            self.en("monedas")
            monedas.move_to(F.get_center() + DOWN * 0.8)
            self.play(FadeIn(monedas), run_time=0.5)

    # ------------------------------------------------------------------ b2
    def monedas(self):
        nombres = [r"w[n-2]", r"w[n-1]", r"w[n]", r"w[n+1]"]
        self.fila_w = [moneda("", RUIDO).scale(0.55).move_to([-3.45 + 2.3 * i, 2.6, 0]) for i in range(4)]
        self.rot_w = [MathTex(n, color=RUIDO).scale(0.91).next_to(m, DOWN, buff=0.15) for n, m in zip(nombres, self.fila_w)]
        caja_f = caja("(2, 1) / √5", AZUL, ancho=2.2, alto=0.7, scale=0.45).move_to([-5.9, 2.6, 0])
        xn = MathTex(r"x[n]", "=", r"(2\,", r"w[n]", "+", r"w[n-1]", r")\big/\sqrt5", color=TXT).scale(1.23)
        xn.move_to([-2.3, 0.5, 0])
        xn[0].set_color(MEDIDA)
        xn1 = MathTex(r"x[n+1]", "=", r"(2\,", r"w[n+1]", "+", r"w[n]", r")\big/\sqrt5", color=TXT).scale(1.23)
        xn1.move_to([-2.3, -0.6, 0])
        xn1[0].set_color(MEDIDA)
        self.xn, self.xn1 = xn, xn1
        imp = Text("imposible de saber", color=ERROR).scale(0.65).next_to(self.rot_w[3], DOWN, buff=0.15).shift(RIGHT * 0.8)
        ya = Text("ya ocurrió", color=VERDE).scale(0.65).next_to(self.rot_w[2], DOWN, buff=0.15).shift(LEFT * 0.6)

        with self.narrar("b2"):
            # «Abramos las muestras»
            self.en("abramos")
            self.corte()
            self.play(*[FadeIn(m) for m in self.fila_w], *[FadeIn(r) for r in self.rot_w], run_time=self.dur(0.7))
            # «El proceso sale de una moneda, w»
            self.en("sale")
            self.resaltar(*self.fila_w, color=RUIDO, run_time=0.5)
            # «pasada por el filtro de dos coeficientes»
            self.en("filtro")
            self.play(FadeIn(caja_f), run_time=0.5)
            # «equis de ene es dos veces la moneda de ahora»
            self.en("xn")
            self.play(LaggedStart(*[FadeIn(xn[i]) for i in range(4)], lag_ratio=0.3), run_time=self.dur(0.9))
            # «más la anterior,»
            self.en("anterior")
            self.play(FadeIn(xn[4]), FadeIn(xn[5]), run_time=0.4)
            # «entre raíz de cinco»
            self.en("raiz")
            self.play(FadeIn(xn[6]), run_time=0.4)
            # «equis de ene más uno contiene»
            self.en("futuro")
            self.play(FadeIn(xn1[0]), FadeIn(xn1[1]), FadeIn(xn1[2]), run_time=self.dur(0.5))
            # «la moneda nueva, w de ene más uno»
            self.en("nueva")
            xn1[3].set_color(ERROR)
            self.play(FadeIn(xn1[3]), self.fila_w[3].animate.set_stroke(ERROR), run_time=0.5)
            # «imposible de saber»
            self.en("imposible")
            self.play(FadeIn(imp), run_time=0.4)
            # «y también la moneda w de ene»
            self.en("wn")
            xn1[5].set_color(VERDE)
            self.play(FadeIn(xn1[4]), FadeIn(xn1[5]), FadeIn(xn1[6]), self.fila_w[2].animate.set_stroke(VERDE), run_time=0.5)
            # «que sí ocurrió ya»
            self.en("ya")
            self.play(FadeIn(ya), run_time=0.4)
        self.imp, self.ya = imp, ya

    # ------------------------------------------------------------------ b3
    def ahora(self):
        xn, xn1 = self.xn, self.xn1
        nota_fuerza = Text("con más fuerza", color=VERDE).scale(0.65).move_to([5.0, 0.5, 0])
        velo = Underline(xn[5], color=INK, stroke_width=3)
        pred = Text("?", color=AMBAR, weight=BOLD).scale(1.04).next_to(xn1, RIGHT, buff=0.3)
        basura = cruz(ROJO, 0.4).move_to(xn[5])
        sucia = Text("pista sucia", color=RUIDO).scale(0.65).next_to(xn, DOWN, buff=1.2)

        with self.narrar("b3"):
            # «Y equis de ene, la muestra de ahora»
            self.en("ahora")
            self.resaltar(xn, color=AMBAR, escala=1.37, run_time=0.5)
            # «esa misma moneda, w de ene,»
            self.en("fuerza")
            self.play(xn[3].animate.set_color(VERDE), run_time=0.4)
            # «con más fuerza»
            self.en("masfuerza")
            self.play(FadeIn(nota_fuerza), run_time=0.4)
            # «Pero no la trae limpia»
            self.en("limpia")
            self.play(Create(velo), run_time=0.4)
            # «viene mezclada con la moneda anterior»
            self.en("mezclada")
            self.play(xn[5].animate.set_color(RUIDO), run_time=0.4)
            # «w de ene menos uno»
            self.en("wnm1")
            self.resaltar(self.fila_w[1], color=RUIDO, run_time=0.5)
            # «Para predecir equis de ene más uno»
            self.en("predecir")
            self.play(FadeIn(pred), run_time=0.4)
            # «esa moneda anterior es basura»
            self.en("basura")
            self.play(FadeIn(basura), run_time=0.4)
            # «ensucia la única pista que tenemos»
            self.en("ensucia")
            self.play(FadeIn(sucia), run_time=0.4)
