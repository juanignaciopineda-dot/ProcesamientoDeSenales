"""Escena 08 — La letra pequeña de la Ec. 2: la fase crece con k², la frecuencia barre 2B y se repliega."""
from comun.escena import *
from comun.figuras_lora import *


class LaLetraPequena(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        lup = lupa().scale(1.5).move_to([-6.0, 2.9, 0])
        cua = cuaderno_lora().scale(0.95).move_to([-3.9, 2.9, 0])
        f = MathTex(r"2\pi", "(s+k)", r"\cdot", r"\frac{k}{2^{SF}}", color=TXT).scale(1.3).move_to([1.2, 2.9, 0])
        f[1].set_color(AMBAR)
        f[3].set_color(CIAN)
        sube = Arrow(f.get_right() + RIGHT * 0.35 + DOWN * 0.45, f.get_right() + RIGHT * 0.35 + UP * 0.45, color=CIAN,
                     stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.3)
        fase = Text("Fase", color=TXT, weight=BOLD).scale(0.8).move_to([-0.2, 1.3, 0])
        k2 = MathTex(r"\propto\ k^{2}", color=AMBAR).scale(1.4).next_to(fase, RIGHT, buff=0.3)
        # plano que llega hasta 2B (símbolo 0)
        P2 = PlanoTF(centro=(-3.2, -1.5), ancho=4.8, alto=3.6, f_max=2.0, rotulos=False)
        c0 = Text("0", color=INK).scale(0.5).next_to(P2.p(0, 0), LEFT, buff=0.12)
        cb = Text("B", color=INK).scale(0.5).next_to(P2.p(0, 1), LEFT, buff=0.12)
        c2b = Text("2B", color=AMBAR, weight=BOLD).scale(0.5).next_to(P2.p(0, 2), LEFT, buff=0.12)
        bajo = Line(P2.p(0, 0), P2.p(0.5, 1), color=AMBAR, stroke_width=6)
        alto_ = Line(P2.p(0.5, 1), P2.p(1, 2), color=AMBAR, stroke_width=6)
        nivel = P2.nivel(1.0, ROJO)
        alias = Text("Aliasing", color=ROJO, weight=BOLD).scale(0.8).move_to([-3.2, 0.75, 0])
        r2 = Text("Ec. 2: dos pasadas", color=TXT, weight=BOLD).scale(0.5).move_to([-3.2, -3.65, 0])
        P1 = PlanoTF(centro=(3.4, -2.4), ancho=4.8, alto=1.8, rotulos=False)
        una = P1.rampa(0, grosor=6)
        r1 = Text("Descripción: una pasada", color=TXT, weight=BOLD).scale(0.5).move_to([3.4, -3.65, 0])
        neq = MathTex(r"\neq", color=ROJO).scale(2.0).move_to([0.1, -2.4, 0])
        doc = documento(TXT).scale(1.3).move_to([-1.3, 2.8, 0])
        ok = tilde(VERDE, 0.7).move_to([-0.3, 2.8, 0])
        sig = Text("Ortogonalidad · Receptor · BER", color=VERDE, weight=BOLD).scale(0.55).move_to([3.5, 2.8, 0])
        with self.narrar("b1"):
            # «letra pequeña»
            self.en("letra")
            self.pop(lup)
            # «el cuaderno del trabajo»
            self.en("cuaderno")
            self.play(FadeIn(cua, shift=UP * 0.2), run_time=self.dur(0.5))
            # «esa frecuencia que crece»
            self.en("frec")
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=self.dur(0.6))
            # «multiplicada por el tiempo»
            self.en("tiempo")
            self.play(FadeIn(f[2]), FadeIn(f[3]), run_time=self.dur(0.6))
            # «que también crece»
            self.en("crece")
            self.play(GrowArrow(sube), run_time=self.dur(0.5))
            # «La fase avanza»
            self.en("fase")
            self.pop(fase)
            # «el cuadrado del índice»
            self.en("cuad")
            self.play(Write(k2), run_time=self.dur(0.7))
            # «el doble de rápido»
            self.en("doble")
            self.play(FadeIn(P2), FadeIn(c0), FadeIn(cb), run_time=0.4)
            self.play(Create(bajo), run_time=0.5)
            self.play(Create(alto_), run_time=self.dur(0.5))
            # «dos veces el ancho de banda»
            self.en("dosb")
            self.pop(c2b)
        with self.narrar("b2"):
            # «muestreamos al ritmo»
            self.en("muest")
            self.play(Create(nivel), *[FadeOut(m) for m in (lup, f, sube, fase, k2)], run_time=self.dur(0.7))
            # «se repliega»
            self.en("replieg")
            self.sfx("whoosh")
            self.play(alto_.animate.shift(DOWN * 1.8), run_time=self.dur(0.9))
            # «aliasing»
            self.en("alias")
            self.pop(alias)
            # «dos pasadas por símbolo»
            self.en("dospas")
            self.play(FadeIn(r2, shift=UP * 0.15), run_time=self.dur(0.5))
            # «en lugar de una»
            self.en("una")
            self.play(FadeIn(P1), FadeIn(r1), run_time=0.4)
            self.play(Create(una), run_time=self.dur(0.6))
            # «compara las dos versiones»
            self.en("compara")
            self.pop(neq)
            # «se queda con la ecuación dos»
            self.en("queda")
            self.sfx("exito")
            self.play(P2.marco.animate.set_stroke(VERDE, 6), r2.animate.set_color(VERDE), run_time=self.dur(0.6))
            # «tal cual»
            self.en("talcual")
            self.play(VGroup(P1, una, r1).animate.fade(0.65), FadeOut(neq), run_time=self.dur(0.5))
            # «el artículo demuestra»
            self.en("demuestra")
            self.play(FadeIn(doc, shift=UP * 0.2), run_time=0.4)
            self.play(Create(ok), run_time=self.dur(0.4))
            # «todo lo que sigue»
            self.en("sigue")
            self.play(FadeIn(sig, shift=LEFT * 0.3), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
