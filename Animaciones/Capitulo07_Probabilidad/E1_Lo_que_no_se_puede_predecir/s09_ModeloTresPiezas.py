"""Escena 09 — Las tres piezas del modelo: espacio muestral, eventos y probabilidad (con el dado)."""
from comun.escena import *


class ModeloTresPiezas(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.E = EspacioDado(centro=(2.4, -0.7))
        self.fichas = []
        for i, x in enumerate((-5.6, -1.2, 3.2)):
            c = Circle(radius=0.3, color=INK, stroke_width=3).set_fill(FONDO, 1)
            n = Text(str(i + 1), color=INK, weight=BOLD).scale(0.55).move_to(c)
            g = VGroup(c, n).move_to([x, 3.3, 0])
            self.fichas.append(g)
        self.bloque_espacio()
        self.bloque_eventos()
        self.bloque_probabilidad()
        self.wait(1.0)
        self.limpiar()

    def encender(self, i, txt, color):
        """Enciende la ficha `i` y devuelve su rótulo (sin animar)."""
        g = self.fichas[i]
        rot = Text(txt, color=color, weight=BOLD).scale(0.6).next_to(g, RIGHT, buff=0.2)
        self.play(g[0].animate.set_stroke(color).set_fill(color, 0.3), g[1].animate.set_color(color), run_time=0.3)
        return rot

    # ------------------------------------------------------------ b1
    def bloque_espacio(self):
        E = self.E
        with self.narrar("b1"):
            # «hacen falta tres piezas»
            self.en("tres")
            self.play(LaggedStart(*[FadeIn(g) for g in self.fichas], lag_ratio=0.2), run_time=self.dur(0.7))

            # «el espacio muestral»
            self.en("espacio")
            r1 = self.encender(0, "espacio muestral", AMBAR)
            self.pop(r1)

            # «la lista de todo lo que puede pasar»
            self.en("lista")
            self.omega = formula(r"\Omega", "=", r"\{1,2,3,4,5,6\}", colores={0: AMBAR}, escala=1.1).move_to([-3.6, 1.4, 0])
            self.play(LaggedStart(*[FadeIn(self.omega[i]) for i in range(3)], lag_ratio=0.3), run_time=self.dur(1.0))

            # «Si tiras un dado»
            self.en("dado")
            self.d3 = dado_n(3).scale(1.1).move_to([-4.0, -1.0, 0])
            self.pop(self.d3)

            # «son las seis caras»
            self.en("caras")
            self.play(LaggedStart(*[FadeIn(E.caras[n]) for n in (1, 2, 3, 4, 5, 6)], lag_ratio=0.12), run_time=self.dur(0.9))

            # «un rectángulo»
            self.en("rect")
            self.play(Create(E.rect), run_time=self.dur(0.6))

            # «Pase lo que pase»
            self.en("pase")
            self.play(self.d3.animate.move_to(E.p(3) + UP * 0.0).scale(0.8 / 1.1), run_time=self.dur(0.8))

            # «el resultado estará ahí»
            self.en("ahi")
            self.play(FadeOut(self.d3), run_time=0.1)
            self.resaltar(E.caras[3], color=AMBAR, run_time=0.6)

    # ------------------------------------------------------------ b2
    def bloque_eventos(self):
        E = self.E
        with self.narrar("b2"):
            # «La segunda pieza son los eventos»
            self.en("eventos")
            self.play(FadeOut(self.omega), run_time=0.25)
            r2 = self.encender(1, "eventos", AMBAR)
            self.pop(r2)

            # «grupos de resultados»
            self.en("grupos")
            ma, mb = E.marco_par(INK, 0.0), E.marco_mas4(INK, 0.0)
            self.play(Create(ma), Create(mb), run_time=self.dur(0.6))

            # «Que salga un número par»
            self.en("par")
            la = Text("A: sale par", color=AMBAR, weight=BOLD).scale(0.7).move_to([-3.6, 0.8, 0])
            self.play(ma.animate.set_stroke(AMBAR).set_fill(AMBAR, 0.12), run_time=0.3)
            self.pop(la)

            # «es un evento»
            self.en("evento")
            self.play(ma.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.8))

            # «el dos, el cuatro y el seis»
            self.en("246")
            self.resaltar(*[E.caras[n] for n in (2, 4, 6)], color=AMBAR, run_time=0.8)

            # «Que salga más de cuatro»
            self.en("mas4")
            lb = Text("B: más de 4", color=CIAN, weight=BOLD).scale(0.7).move_to([-3.6, -0.4, 0])
            self.play(mb.animate.set_stroke(CIAN).set_fill(CIAN, 0.12), run_time=0.3)
            self.pop(lb)

            # «el cinco y el seis»
            self.en("56")
            self.resaltar(E.caras[5], E.caras[6], color=CIAN, run_time=0.8)

            # «Un evento ocurre»
            self.en("ocurre")
            self.play(ma.animate(rate_func=there_and_back).set_stroke(width=9),
                      mb.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.7))

            # «cae dentro de su grupo»
            self.en("cae")
            d6 = dado_n(6).scale(0.8).move_to([E.p(6)[0], 2.0, 0])
            self.play(FadeIn(d6), run_time=0.2)
            self.play(d6.animate.move_to(E.p(6)), run_time=self.dur(0.5))
            self.play(FadeOut(d6), ma.animate(rate_func=there_and_back).set_stroke(width=9),
                      mb.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.5))
            self.ma, self.mb, self.la, self.lb = ma, mb, la, lb

    # ------------------------------------------------------------ b3
    def bloque_probabilidad(self):
        E = self.E
        with self.narrar("b3"):
            # «La tercera pieza es la probabilidad»
            self.en("tercera")
            r3 = self.encender(2, "probabilidad", AMBAR)
            self.pop(r3)

            # «un número que le asignamos a cada evento»
            self.en("numero")
            self.play(FadeOut(self.la), FadeOut(self.lb), run_time=0.25)
            pa = formula("P", "(", "A", ")", "=", "?", colores={2: AMBAR}, escala=1.1).move_to([-3.6, 1.4, 0])
            self.pop(pa)

            # «un dado bien hecho»
            self.en("bien")
            dd = dado_n(6).scale(1.1).move_to([-4.0, -1.6, 0])
            self.play(FadeIn(dd), Rotate(dd, 2 * PI), run_time=self.dur(0.8))

            # «cada cara vale un sexto»
            self.en("sexto")
            self.frac = E.fracciones("1/6", TXT)
            self.play(FadeOut(dd), LaggedStart(*[FadeIn(f) for f in self.frac.values()], lag_ratio=0.1),
                      run_time=self.dur(0.9))

            # «la probabilidad de un evento»
            self.en("prob_evento")
            self.resaltar(pa, color=AMBAR, run_time=0.7)

            # «la suma de las de sus caras»
            self.en("suma")
            for g in (self.ma, self.mb):
                g.set_stroke(INK).set_fill(opacity=0)
            self.play(self.ma.animate.set_stroke(AMBAR).set_fill(AMBAR, 0.12), run_time=self.dur(0.5))

            # «sale par tiene tres caras»
            self.en("par3")
            f = formula(r"\tfrac{1}{6}", "+", r"\tfrac{1}{6}", "+", r"\tfrac{1}{6}", "=", r"\tfrac{3}{6}", "=",
                        r"\tfrac{1}{2}", escala=0.9).move_to([-3.5, 0.2, 0])
            self.play(FadeOut(pa), LaggedStart(*[FadeIn(f[i]) for i in range(5)], lag_ratio=0.15),
                      run_time=self.dur(1.3))

            # «tres sextos»
            self.en("tres_sextos")
            self.play(FadeIn(f[5]), FadeIn(f[6]), run_time=self.dur(0.5))

            # «un medio»
            self.en("medio")
            self.play(FadeIn(f[7]), FadeIn(f[8]), run_time=self.dur(0.5))
            self.resaltar(f[8], color=AMBAR, run_time=0.5)
