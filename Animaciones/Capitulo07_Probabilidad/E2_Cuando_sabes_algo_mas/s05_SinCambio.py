"""Escena 05 — Sin cambio: eventos independientes (dado y moneda)."""
from comun.escena import *


class SinCambio(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.moneda_()
        self.regla_()
        self.contar()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def moneda_(self):
        sob = sobre(AMBAR).scale_to_fit_height(1.0).move_to([-2.4, 2.9, 0])
        nada = Text("Nada", color=AMBAR, weight=BOLD).scale(0.9).next_to(sob, RIGHT, buff=0.4)
        d = dado_n(6).scale(1.6).move_to([-3.0, 0.4, 0])
        m = moneda("").scale(1.6).move_to([3.0, 0.4, 0])
        alg = persona(INK).scale_to_fit_height(1.2).move_to([0, -2.4, 0])
        cara_m = moneda("Cara").scale(1.6).move_to(m)
        cara_t = Text("¡Cara!", color=AMBAR, weight=BOLD).scale(0.8).move_to([3.0, 1.9, 0])
        preg = MathTex(r"P(6)=\,?", color=AMBAR).scale(1.5).move_to([-3.0, -1.3, 0])
        no = Text("No", color=ERROR, weight=BOLD).scale(1.5).move_to([0, 1.7, 0])
        hilo = DashedLine([-1.9, 0.4, 0], [1.9, 0.4, 0], color=INK, stroke_width=3)
        tij = tijeras().scale_to_fit_height(0.8).move_to([0, 0.4, 0])
        sexto = MathTex(r"P(6\mid \text{cara})=\tfrac16", color=VERDE).scale(1.3).move_to([-2.0, -1.4, 0])

        with self.narrar("b1"):
            # «no cambia nada»
            self.en("nada")
            self.play(FadeIn(sob), FadeIn(nada), run_time=self.dur(0.6))

            # «Tiras un dado y lanzas una moneda»
            self.en("dado_moneda")
            self.play(FadeIn(d, shift=DOWN * 0.3), FadeIn(m, shift=DOWN * 0.3), run_time=self.dur(0.6))

            # «Alguien te dice»
            self.en("alguien")
            self.play(FadeIn(alg), run_time=self.dur(0.4))

            # «la moneda ha salido cara»
            self.en("cara")
            self.play(FadeOut(m), FadeIn(cara_m), run_time=self.dur(0.3))
            self.pop(cara_t)

            # «¿Cambia en algo la probabilidad»
            self.en("pregunta")
            self.play(FadeOut(alg), FadeIn(preg), run_time=self.dur(0.5))

            # «No:»
            self.en("no")
            self.pop(no, sonido="error")

            # «el dado no sabe qué hizo la moneda»
            self.en("no_sabe")
            self.play(Create(hilo), run_time=self.dur(0.4))
            self.play(FadeIn(tij), run_time=self.dur(0.3))
            self.play(FadeOut(hilo), run_time=self.dur(0.3))

            # «Sigue siendo un sexto»
            self.en("sexto")
            self.play(FadeOut(preg), FadeOut(tij), FadeIn(sexto), run_time=self.dur(0.5))
            self.play(FadeIn(tilde(VERDE, 0.5).next_to(sexto, RIGHT, buff=0.3)), run_time=self.dur(0.3))

    # ------------------------------------------------------------ b2
    def regla_(self):
        f_ind = formula(r"P(A\mid B)", "=", "P(A)", escala=1.7, colores={2: AMBAR}).move_to([0, 2.6, 0])
        indep = Text("Independientes", color=AMBAR, weight=BOLD).scale(1.2).move_to([0, 1.2, 0])
        comodo = Text("Cuentas más fáciles", color=INK).scale(0.7).move_to([0, 0.3, 0])
        f = formula(r"P(A\cap B)", "=", "P(B)", r"\cdot", r"P(A\mid B)", escala=1.5).move_to([0, -0.9, 0])
        nuevo = MathTex("P(A)", color=AMBAR).scale(1.5)
        final = formula(r"P(A\cap B)", "=", "P(A)", r"\cdot", "P(B)", escala=1.7).move_to([0, -2.7, 0])
        caja_f = SurroundingRectangle(final, color=VERDE, buff=0.2, stroke_width=4)

        with self.narrar("b2"):
            # «saber B no cambia la probabilidad de A»
            self.en("no_cambia")
            self.corte()
            self.play(LaggedStart(*[FadeIn(p) for p in f_ind], lag_ratio=0.3), run_time=self.dur(1.0))

            # «independientes»
            self.en("indep")
            self.pop(indep)

            # «algo cómodo»
            self.en("comodo")
            self.play(FadeIn(comodo), run_time=self.dur(0.4))

            # «La regla que acabamos de ver»
            self.en("regla")
            self.play(FadeIn(f), run_time=self.dur(0.8))

            # «la de B por la de A dado B»
            self.en("rb")
            self.resaltar(f[2], f[4], color=AMBAR)

            # «Si son independientes»
            self.en("si_indep")
            self.play(f[4].animate.set_color(AMBAR), run_time=self.dur(0.4))

            # «es simplemente la de A»
            self.en("solo_a")
            nuevo.move_to(f[4])
            self.play(ReplacementTransform(f[4], nuevo), run_time=self.dur(0.7))

            # «ocurran las dos cosas»
            self.en("dos_cosas")
            self.resaltar(f[0], color=AMBAR)

            # «el producto de sus probabilidades»
            self.en("producto")
            self.play(FadeIn(final), Create(caja_f), run_time=self.dur(0.8))

    # ------------------------------------------------------------ b3
    def contar(self):
        celdas, contenido = {}, VGroup()
        grupo_celdas = VGroup()
        for fila, lado in enumerate(("cara", "cruz")):
            for i in range(6):
                c = Square(side_length=1.05, color=INK, stroke_width=2.5).move_to([-3.15 + i * 1.26, 0.9 - fila * 1.2, 0])
                celdas[(i + 1, lado)] = c
                grupo_celdas.add(c)
                contenido.add(VGroup(dado_n(i + 1).scale(0.36).move_to(c.get_center() + UP * 0.2),
                                     Text(lado.capitalize(), color=TXT).scale(0.4).move_to(c.get_center() + DOWN * 0.3)))
        igual = MathTex(r"\text{Cada una: }\tfrac1{12}", color=INK).scale(1.2).move_to([0, 2.7, 0])
        elegida = celdas[(6, "cara")]
        doce = MathTex(r"\tfrac1{12}", color=AMBAR).scale(1.5).move_to([5.7, 0.9, 0])
        cuenta = MathTex(r"\tfrac16", r"\cdot", r"\tfrac12", "=", r"\tfrac1{12}", color=TXT).scale(1.6).move_to([0, -2.1, 0])
        ok = tilde(VERDE, 0.6).move_to([4.2, -2.1, 0])

        with self.narrar("b3"):
            # «Comprobémoslo contando»
            self.en("contar")
            self.corte()
            self.play(LaggedStart(*[Create(c) for c in grupo_celdas], lag_ratio=0.05), run_time=self.dur(1.2))

            # «doce combinaciones»
            self.en("doce")
            self.play(LaggedStart(*[FadeIn(c) for c in contenido], lag_ratio=0.05), run_time=self.dur(1.2))

            # «todas igual de probables»
            self.en("igual")
            self.play(FadeIn(igual), run_time=self.dur(0.5))

            # «Seis con cara»
            self.en("seis_cara")
            self.play(elegida.animate.set_fill(AMBAR, 0.5).set_stroke(AMBAR, 5), run_time=self.dur(0.4))

            # «un doceavo»
            self.en("doceavo")
            self.pop(doce)

            # «un sexto por un medio»
            self.en("cuenta")
            self.play(LaggedStart(*[FadeIn(p) for p in cuenta], lag_ratio=0.25), run_time=self.dur(1.2))

            # «Encaja»
            self.en("encaja")
            self.play(FadeIn(ok), run_time=self.dur(0.3))
            self.sfx("exito")
