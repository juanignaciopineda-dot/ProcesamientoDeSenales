"""Escena 11 — Cierre: el lenguaje del episodio y la pregunta del siguiente."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        E = EspacioDado(centro=(-3.6, 0.3))
        fr = E.fracciones("1/6", TXT)

        with self.narrar("b1"):
            # «un espacio de resultados»
            self.en("espacio")
            self.play(FadeIn(E), run_time=self.dur(0.5))

            # «eventos»
            self.en("eventos")
            ma = E.marco_par(AMBAR, 0.12)
            mb = E.marco_mas4(CIAN, 0.12)
            self.play(Create(ma), Create(mb), run_time=self.dur(0.4))

            # «probabilidades que cumplen tres reglas»
            self.en("reglas")
            reglas = VGroup(*[caja(t, AMBAR, ancho=3.8, alto=0.7, scale=0.5) for t in
                              ("Entre 0 y 1", "El total vale 1", "Si no se solapan, se suman")])
            reglas.arrange(DOWN, buff=0.25).move_to([3.4, 2.4, 0])
            self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in reglas], lag_ratio=0.25), run_time=self.dur(0.9))

            # «Con él se puede hablar»
            self.en("con_el")
            self.resaltar(E.rect, color=AMBAR, run_time=0.6)

            # «señales que no se pueden predecir»
            self.en("senales")
            Lr = Lienzo(ancho=5.0, alto=1.5, t_rango=(0, 1), v_max=1.5, centro=(3.4, -1.0))
            cr = Lr.curva(np.linspace(0, 1, 160), serie(19, 160, 0.5), RUIDO, 3.5)
            self.play(Create(cr), run_time=self.dur(0.9), rate_func=linear)

            # «pero sí describir»
            self.en("describir")
            pila = pila_de_curvas(Lr, 22, semilla=5, a=0.6, color=RUIDO, opacidad=0.4, ancho=2.2, escala=0.45)
            self.play(LaggedStart(*[Create(c) for c in pila], lag_ratio=0.03), run_time=self.dur(0.9))

            # «Falta una pregunta»
            self.en("falta")
            gq = Text("?", color=AMBAR, weight=BOLD).scale(2.2).move_to([-4.6, -3.0, 0])
            self.pop(gq)

            # «qué le pasa a una probabilidad»
            self.en("pasa")
            pq = formula("P", "=", "?", colores={0: AMBAR}, escala=1.1).next_to(gq, RIGHT, buff=0.3)
            self.play(LaggedStart(*[FadeIn(pq[i]) for i in range(3)], lag_ratio=0.2), run_time=self.dur(0.7))

            # «información nueva»
            self.en("nueva")
            sob = sobre().scale(1.1).move_to([3.4, -3.0, 0])
            nue = Text("¡nuevo!", color=AMBAR, weight=BOLD).scale(0.55).next_to(sob, RIGHT, buff=0.25)
            self.pop(VGroup(sob, nue))

            # «el dado salió par»
            self.en("par")
            self.play(*[E.caras[n].animate.fade(0.7) for n in (1, 3, 5)], FadeOut(mb), run_time=self.dur(0.5))
            self.resaltar(ma, color=AMBAR, run_time=0.5)

            # «ya no vale un sexto»
            self.en("tercio")
            p6 = Text("1/6", color=TXT).scale(0.55).move_to(E.p(6) + DOWN * 0.62)
            q = Text("?", color=AMBAR, weight=BOLD).scale(0.6).next_to(p6, RIGHT, buff=0.2)
            self.play(FadeIn(p6), run_time=0.2)
            self.play(FadeIn(tachar(p6)), FadeIn(q), run_time=self.dur(0.4))

            # «Cuando sabes algo más»
            self.en("titulo")
            self.corte()
            sig = etiqueta("Siguiente episodio", INK, 0.6).move_to([0, 1.6, 0])
            ti = self.palabra("Cuando sabes", TXT, 1.3).move_to([0, 0.4, 0])
            tj = self.palabra("algo más", AMBAR, 1.3).move_to([0, -0.9, 0])
            self.play(FadeIn(sig), run_time=0.2)
            self.pop(ti)
            self.pop(tj)

        self.wait(1.0)
        self.limpiar()
