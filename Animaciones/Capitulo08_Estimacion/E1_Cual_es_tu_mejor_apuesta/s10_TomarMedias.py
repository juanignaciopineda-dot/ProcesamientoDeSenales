"""Escena 10 — Demostración, segunda parte: la media de cada término y el resultado."""
from comun.escena import *


class TomarMedias(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.medias()
        self.resultado()
        self.wait(1.0)
        self.limpiar()

    def cambiar(self, items, i, nuevo, y, quitar=()):
        """Reemplaza `items[i]` por `nuevo` y recoloca la fila. Con `quitar`, saca esos índices."""
        resto = [m for j, m in enumerate(items) if j not in quitar]
        k = resto.index(items[i]) if i not in quitar else None
        lista = [nuevo if m is items[i] else m for m in resto]
        tmp = VGroup(*[m.copy() for m in lista]).arrange(RIGHT, buff=0.3).move_to([0, y, 0])
        anims = []
        for m, t in zip(lista, tmp):
            if m is nuevo:
                nuevo.move_to(t)
            else:
                anims.append(m.animate.move_to(t))
        return anims, lista

    def medias(self):
        top = formula(r"(Y-\mu)^2", "+", r"2(Y-\mu)(\mu-\hat{y})", "+", r"(\mu-\hat{y})^2", escala=1.2,
                      colores={0: SENAL, 2: ERROR, 4: ESTIMACION}).move_to([0, 3.0, 0])
        y = 1.0
        t0 = MathTex(r"E[(Y-\mu)^2]", color=SENAL).scale(1.12)
        p1 = MathTex("+", color=TXT).scale(1.12)
        t1 = MathTex(r"2\,E[(Y-\mu)(\mu-\hat{y})]", color=ERROR).scale(1.12)
        p2 = MathTex("+", color=TXT).scale(1.12)
        t2 = MathTex(r"E[(\mu-\hat{y})^2]", color=ESTIMACION).scale(1.12)
        fila = VGroup(t0, p1, t1, p2, t2).arrange(RIGHT, buff=0.3).move_to([0, y, 0])
        items = [t0, p1, t1, p2, t2]
        lin = Text("Linealidad", color=INK, weight=BOLD).scale(0.9).move_to([-4.6, -0.8, 0])
        ok = tilde(VERDE, 0.7).next_to(lin, RIGHT, buff=0.3)

        sigma = MathTex(r"\sigma^2", color=SENAL).scale(1.6)
        cruzado = MathTex("2", r"(\mu-\hat{y})", r"E[Y-\mu]", color=ERROR).scale(1.3)
        cruzado[1].set_color(ESTIMACION)
        cruzado[2].set_color(SENAL)
        cero = MathTex("= 0", color=VERDE).scale(1.3)

        with self.narrar("b1"):
            # «tomamos la media de cada término»
            self.en("media")
            self.play(FadeIn(top, shift=DOWN * 0.1), run_time=self.dur(0.4))
            self.play(FadeIn(fila, lag_ratio=0.25), run_time=self.dur(1.0))

            # «por linealidad»
            self.en("lineal")
            self.play(FadeIn(lin), FadeIn(ok, scale=0.5), run_time=self.dur(0.5))

            # «La media del primero es la varianza»
            self.en("varianza")
            anims, items = self.cambiar(items, 0, sigma, y)
            self.play(ReplacementTransform(t0, sigma), *anims, run_time=self.dur(0.8))
            t0 = sigma

            # «En el término cruzado»
            self.en("cruzado")
            rojo = SurroundingRectangle(t1, buff=0.1, color=ERROR, stroke_width=4)
            rojo.permitir_encima = True
            self.play(FadeIn(rojo), run_time=self.dur(0.4))

            # «es un número fijo y sale fuera»
            self.en("fijo")
            self.play(FadeOut(rojo), run_time=0.2)
            cruzado.move_to(t1)
            anims, items2 = self.cambiar(items, 2, cruzado, y)
            self.play(ReplacementTransform(t1, cruzado), *anims, run_time=self.dur(0.9))
            items = items2
            marco = SurroundingRectangle(cruzado[2], buff=0.1, color=SENAL, stroke_width=3)
            marco.permitir_encima = True

            # «la media de i griega menos mu»
            self.en("quedadentro")
            self.play(FadeIn(marco), run_time=self.dur(0.4))

            # «que es cero»
            self.en("cero")
            cero.next_to(marco, DOWN, buff=0.3)
            self.pop(cero)

            # «El término cruzado desaparece»
            self.en("desaparece")
            tach = tachar(cruzado, ROJO)
            self.play(Create(tach), run_time=self.dur(0.4))
            self.play(FadeOut(cruzado), FadeOut(tach), FadeOut(marco), FadeOut(cero), FadeOut(p1), run_time=self.dur(0.5))
            quita = VGroup(sigma.copy(), p2.copy(), t2.copy()).arrange(RIGHT, buff=0.4).move_to([0, y, 0])
            self.play(sigma.animate.move_to(quita[0]), p2.animate.move_to(quita[1]), t2.animate.move_to(quita[2]),
                      run_time=self.dur(0.5))

            # «el último es un número fijo»
            self.en("ultimo")
            m2 = SurroundingRectangle(t2, buff=0.12, color=ESTIMACION, stroke_width=4)
            m2.permitir_encima = True
            self.play(FadeIn(m2), run_time=self.dur(0.4))

            # «se queda como está»
            self.en("queda")
            ok2 = tilde(VERDE, 0.7).next_to(m2, RIGHT, buff=0.3)
            self.sfx("exito")
            self.play(FadeIn(ok2, scale=0.5), run_time=self.dur(0.4))
        self.wait(0.3)

    def resultado(self):
        R = formula(r"E[(Y-\hat{y})^2]", "=", r"\sigma^2", "+", r"(\mu-\hat{y})^2", escala=1.6,
                    colores={0: TXT, 2: SENAL, 4: ESTIMACION}).move_to([0, 0.3, 0])
        marco = SurroundingRectangle(R, buff=0.3, color=VERDE, stroke_width=4)
        marco.permitir_encima = True

        with self.narrar("b2"):
            # «Resultado»
            self.en("resultado")
            self.corte()
            self.play(FadeIn(R[0], shift=UP * 0.1), run_time=self.dur(0.5))

            # «la varianza»
            self.en("sigma2")
            self.play(FadeIn(R[1]), FadeIn(R[2], shift=UP * 0.1), run_time=self.dur(0.5))

            # «la distancia entre la apuesta y la media»
            self.en("distancia")
            self.play(FadeIn(R[3]), FadeIn(R[4], shift=UP * 0.1), run_time=self.dur(0.8))

            # «al cuadrado»
            self.en("alcuadrado")
            self.play(Create(marco), run_time=self.dur(0.5))
