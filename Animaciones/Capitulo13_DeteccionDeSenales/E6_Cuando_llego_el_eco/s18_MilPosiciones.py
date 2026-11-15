"""Escena 18 — Buscar el retardo en mil posiciones: cada una es una oportunidad de falsa alarma."""
from comun.escena import *


class MilPosiciones(EscenaCurso):
    ESCENA = "18"

    def construct(self):
        L = Lienzo(ancho=12.0, alto=2.0, t_rango=(0, 1), v_max=1.0, centro=(0.0, 1.4))
        rng = np.random.default_rng(21)
        x = np.linspace(0, 1, 300)
        v = 0.34 * rng.normal(size=300)
        v = np.convolve(v, np.ones(3) / 3, mode="same") * 1.6
        k = int(np.argmax(v))
        rui = L.curva(x, v, RUIDO, 2.6)
        base = L.base()
        dq = formula("D", "=", "?", escala=1.2, colores={0: AMBAR, 2: AMBAR}).move_to([-5.2, 3.4, 0])
        tira = celdas13(40, ancho=12.0, centro=(0.0, -1.0), alto=0.6)
        sel = Rectangle(width=12.0 / 40, height=0.6, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.35)
        sel.move_to(tira[0].get_center())
        mil = Text("1.000 celdas", color=AMBAR, weight=BOLD).scale(0.7).move_to([0, -1.9, 0])
        mx = Dot(L.p(x[k], v[k]), radius=0.12, color=AMBAR)
        mxl = Text("máximo", color=AMBAR).scale(0.45).next_to(mx, UP, buff=0.15)
        ex = Text("!", color=AMBAR, weight=BOLD).scale(2.2).move_to([5.8, 3.0, 0])
        dados = VGroup(*[dado().scale(0.38).move_to(tira[i].get_center() + DOWN * 0.95) for i in range(2, 40, 5)])
        dados2 = VGroup(*[dado().scale(0.38).move_to(tira[i].get_center() + DOWN * 0.95) for i in range(0, 40, 5)])
        solo = Text("solo ruido", color=RUIDO, weight=BOLD).scale(0.55).move_to([-5.2, 2.6, 0])
        umb = DashedLine(L.p(0, 0.55), L.p(1, 0.55), color=ROJO, stroke_width=3)
        kk = [i for i in range(300) if v[i] > 0.55]
        cr = Dot(L.p(x[kk[0]], v[kk[0]]), radius=0.12, color=ROJO) if kk else Dot(L.p(0.2, 0.55), radius=0.12, color=ROJO)
        falsa = Text("falsa alarma", color=ROJO, weight=BOLD).scale(0.6).move_to([5.2, -3.0, 0])
        rojas = [tira[i] for i in (6, 14, 22, 33)]
        with self.narrar("b1"):
            # «Volvamos al ruido»
            self.en("ruido")
            self.play(FadeIn(base), Create(rui), run_time=self.dur(0.8))
            # «no conocemos el retardo»
            self.en("noconocemos")
            self.pop(dq)
            # «probar todas las posiciones posibles»
            self.en("probar")
            self.play(FadeIn(tira), FadeIn(sel), run_time=0.4)
            self.play(sel.animate.move_to(tira[39].get_center()), run_time=self.dur(1.5), rate_func=linear)
            # «digamos mil»
            self.en("mil")
            self.pop(mil)
            # «quedarnos con el máximo de la salida»
            self.en("maximo")
            self.play(FadeIn(mx), FadeIn(mxl), run_time=self.dur(0.6))
            # «Y aquí hay un problema»
            self.en("problema")
            self.play(FadeOut(sel), FadeOut(mil), FadeOut(mx), FadeOut(mxl), run_time=0.3)
            self.pop(ex)
            # «Cada posición es una oportunidad»
            self.en("oportunidad")
            self.play(LaggedStart(*[FadeIn(d) for d in dados], lag_ratio=0.12), run_time=self.dur(1.0))
            # «el ruido, solo»
            self.en("solo")
            self.play(FadeIn(solo), run_time=0.4)
            # «cruce el umbral»
            self.en("cruce")
            self.play(Create(umb), FadeIn(cr), run_time=self.dur(0.7))
            # «una falsa alarma»
            self.en("falsa")
            self.play(tira[6].animate.set_fill(ROJO, 0.7).set_stroke(ROJO), FadeIn(falsa), run_time=self.dur(0.6))
            # «Cuantas más posiciones»
            self.en("mas")
            self.play(LaggedStart(*[FadeIn(d) for d in dados2], lag_ratio=0.1), run_time=self.dur(0.8))
            # «más oportunidades»
            self.en("oportunidades")
            self.play(*[c.animate.set_fill(ROJO, 0.7).set_stroke(ROJO) for c in rojas[1:]], run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
