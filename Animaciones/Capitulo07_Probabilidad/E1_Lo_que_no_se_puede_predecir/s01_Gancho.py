"""Escena 01 — Gancho: un seno se calcula dentro de un año; el ruido, ni dentro de un segundo."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        L1 = Lienzo(ancho=9.6, alto=1.8, t_rango=(0, 6), v_max=1.2, centro=(-1.0, 2.1))
        L2 = Lienzo(ancho=9.6, alto=1.8, t_rango=(0, 6), v_max=1.2, centro=(-1.0, -0.3))
        tn = np.linspace(0, 3.4, 170)

        with self.narrar("b1"):
            # «Esta señal puedes calcularla»
            self.en("seno")
            b1 = L1.base()
            seno = seno_t(L1, 1.0, 1.0, SENAL, 4.0)
            v1 = eje_v7(L1, -1.2, 1.2)
            self.play(Create(b1), Create(v1), run_time=0.3)
            self.play(Create(seno), run_time=self.dur(1.5), rate_func=linear)

            # «dentro de un año»
            self.en("anio")
            m1 = L1.vertical(6, VERDE, 2.5)
            d1 = Dot(L1.p(6, 0), radius=0.1, color=VERDE)
            t1 = Text("+1 año", color=VERDE, weight=BOLD).scale(0.6).move_to([5.1, 2.1, 0])
            ok = tilde(VERDE, 0.4).move_to([6.3, 2.1, 0])
            self.play(Create(m1), FadeIn(d1), run_time=0.4)
            self.play(FadeIn(t1), FadeIn(ok), run_time=self.dur(0.4))

            # «Esta otra»
            self.en("ruido")
            b2 = L2.base()
            c2 = L2.curva(tn, 0.45 * serie(21, 170, 0.5), RUIDO, 4.0)
            v2 = eje_v7(L2, -1.2, 1.2)
            self.play(Create(b2), Create(v2), run_time=0.3)
            self.play(Create(c2), run_time=self.dur(1.2), rate_func=linear)

            # «ni dentro de un segundo»
            self.en("segundo")
            m2 = L2.vertical(3.4, ROJO, 2.5)
            t2 = Text("+1 s", color=ROJO, weight=BOLD).scale(0.55).move_to([float(L2.x(3.4)) + 0.7, 0.75, 0])
            q = Text("?", color=ROJO, weight=BOLD).scale(1.8).move_to(L2.p(4.9, 0))
            self.play(Create(m2), run_time=0.3)
            self.play(FadeIn(t2), run_time=0.25)
            self.pop(q)

            # «toda una materia»
            self.en("materia")
            mat = Text("Procesamiento de Señales", color=TXT, weight=BOLD).scale(0.85).move_to([0, -2.3, 0])
            self.pop(mat)

            # «señales que no se pueden predecir»
            self.en("impredecible")
            imp = Text("Impredecible", color=RUIDO, weight=BOLD).scale(0.9).move_to([0, -3.2, 0])
            self.pop(imp)
            self.play(c2.animate.set_stroke(width=6), run_time=self.dur(0.4))

            # «pero sí describir»
            self.en("describir")
            pila = pila_de_curvas(L2, 24, semilla=7, a=0.6, color=RUIDO, opacidad=0.4, ancho=2.2, escala=0.45)
            des = Text("Describible", color=VERDE, weight=BOLD).scale(0.9).move_to(imp)
            self.play(FadeOut(q), FadeOut(m2), FadeOut(t2), FadeOut(c2), run_time=0.3)
            self.play(LaggedStart(*[Create(c) for c in pila], lag_ratio=0.03),
                      ReplacementTransform(imp, des), run_time=self.dur(1.0))

        self.wait(1.0)
        self.limpiar()
