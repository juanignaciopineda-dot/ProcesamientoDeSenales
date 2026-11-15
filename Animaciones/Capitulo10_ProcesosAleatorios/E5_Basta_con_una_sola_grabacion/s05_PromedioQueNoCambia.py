"""Escena 05 — El promedio temporal de una pila es su voltaje: la pila no es ergódica."""
from comun.escena import *


class PromedioQueNoCambia(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        L = Lienzo(ancho=5.8, alto=3.6, t_rango=(0, 1), v_max=3.0, centro=(-3.6, 0.0))
        rectas = rectas_pilas(L, ancho=3.0)
        rec2 = rectas[2]
        base = L.base()
        self.add(rectas, base)
        c_erg = caja("¿ergódico?", AZUL, ancho=3.4, alto=0.9).move_to([4.0, -2.2, 0])

        with self.narrar("b1"):
            # «promedia tu grabación»
            self.en("promedia")
            self.play(rec2.animate.set_color(AMBAR).set_stroke(width=7),
                      *[r.animate.set_stroke(opacity=0.3) for r in rectas if r is not rec2], run_time=0.5)

            # «a lo largo del tiempo»
            self.en("tiempo")
            fl = Arrow(L.p(0.0, 2.6), L.p(1.0, 2.6), color=AMBAR, buff=0, stroke_width=5)
            t_t = MathTex("t", color=INK).scale(0.7).next_to(fl, RIGHT, buff=0.1)
            self.play(Create(fl), FadeIn(t_t), run_time=self.dur(0.9))

            # «el voltaje de tu pila»
            self.en("suvoltaje")
            lab = etiqueta("promedio temporal", AMBAR, 0.65, BOLD).move_to([4.0, 2.4, 0])
            self.play(FadeIn(lab), run_time=0.4)

            # «de dos voltios»
            self.en("dos")
            p = pila("+2").scale(1.1).move_to([6.5, 2.4, 0])
            self.play(FadeIn(p, scale=0.6), run_time=0.4)

            # «el promedio temporal es dos»
            self.en("prom2")
            d2 = MathTex(r"\bar{x}=2", color=AMBAR).scale(1.6).move_to([4.0, 1.2, 0])
            self.pop(d2)

            # «alargues la medida»
            self.en("alarga")
            v0 = L.p(0.0, -2.55)
            ven = Line(v0, L.p(0.3, -2.55), color=VERDE, stroke_width=6)
            self.play(Create(ven), run_time=0.3)
            self.play(ven.animate.put_start_and_end_on(v0, L.p(1.0, -2.55)), run_time=self.dur(1.3))

            # «se acerca a cero»
            self.en("cero")
            fl0 = Arrow(L.p(1.05, 2.0), L.p(1.05, 0.12), color=ROJO, buff=0, stroke_width=5)
            self.play(Create(fl0), run_time=0.6)

            # «la media del cajón»
            self.en("mediacajon")
            mu = MathTex(r"\mu=0", color=TXT).scale(1.1).move_to([4.0, -0.2, 0])
            tx = etiqueta("media del cajón", INK, 0.5).next_to(mu, DOWN, buff=0.15)
            self.pop(mu)
            self.play(FadeIn(tx), run_time=0.3)

            # «No es ergódico»
            self.en("no")
            self.play(FadeIn(c_erg), run_time=0.3)
            x = cruz(ROJO, 0.4).next_to(c_erg, RIGHT, buff=0.2)
            self.sfx("error")
            self.play(FadeIn(x, scale=0.5), c_erg[0].animate.set_stroke(ROJO), run_time=0.4)

            # «una sola pila»
            self.en("una")
            self.resaltar(rec2, escala=1.0)

            # «de las demás»
            self.en("demas")
            self.play(*[r.animate.set_stroke(opacity=0.1) for r in rectas if r is not rec2], run_time=0.5)
            q = self.palabra("¿?", ROJO, 1.2).move_to(L.p(0.5, -1.0))
            self.pop(q)
        self.wait(1.0)
        self.limpiar()
