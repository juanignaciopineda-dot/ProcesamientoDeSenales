"""Escena 03 — Dado par: saber algo achica el mundo."""
from comun.escena import *


class DadoPar(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.esp = EspacioDado07(centro=(0, 0.5), lado=1.0)
        self.pregunta()
        self.achicar()
        self.wait(1.0)
        self.limpiar()

    def pregunta(self):
        e = self.esp
        sexto = MathTex(r"P(6)=\tfrac16", color=TXT).scale(1.3).move_to([0, -2.6, 0])
        unos = VGroup(*[MathTex(r"\frac16", color=INK).scale(0.85).next_to(c, DOWN, buff=0.75)
                        for c in e.caras])
        ojo_ = ojo().scale_to_fit_height(0.9).move_to([0, 2.9, 0])
        par = Text("¡Par!", color=AMBAR, weight=BOLD).scale(0.8).move_to([3.2, 2.9, 0])
        otra = MathTex(r"P(6)=\,?", color=AMBAR).scale(1.3).move_to([0, -2.6, 0])
        reloj = reloj_arena().scale_to_fit_height(1.1).move_to([5.8, 0.5, 0])

        with self.narrar("b1"):
            # «Tiras un dado»
            self.en("dado")
            self.play(FadeIn(e.marco), LaggedStart(*[FadeIn(c, shift=DOWN * 0.3) for c in e.caras],
                                                   lag_ratio=0.12), run_time=self.dur(1.0))

            # «un seis»
            self.en("seis")
            self.aro6 = e.aros([6], AMBAR)
            self.play(Create(self.aro6), run_time=self.dur(0.4))

            # «Un sexto»
            self.en("sexto")
            self.pop(sexto)

            # «todas pesan lo mismo»
            self.en("pesan")
            self.play(LaggedStart(*[FadeIn(u) for u in unos], lag_ratio=0.1), run_time=self.dur(0.8))

            # «alguien mira el dado antes que tú»
            self.en("mira")
            self.play(FadeIn(ojo_, scale=0.5), run_time=self.dur(0.5))

            # «ha salido un número par»
            self.en("par")
            self.aros_par = e.aros([2, 4], VERDE, 0.1)
            self.pop(par)
            self.play(Create(self.aros_par), run_time=self.dur(0.4))

            # «Te hago la misma pregunta»
            self.en("misma")
            self.play(FadeOut(unos), ReplacementTransform(sexto, otra), run_time=self.dur(0.6))

            # «¿Qué probabilidad hay de que sea un seis?»
            self.en("otra_vez")
            self.resaltar(otra, color=AMBAR)

            # «Piénsalo un momento»
            self.en("piensalo")
            self.play(FadeIn(reloj), run_time=self.dur(0.4))
            self.flotar(reloj, amp=0.1)
        self.otra, self.ojo_, self.par, self.reloj = otra, ojo_, par, reloj

    def achicar(self):
        e, otra = self.esp, self.otra
        tercio = MathTex(r"P(6\mid \text{par})=\tfrac13", color=AMBAR).scale(1.3).move_to([0, -2.6, 0])
        fantasma = DashedVMobject(Rectangle(width=e.marco.width, height=e.marco.height, color=INK,
                                            stroke_width=2).move_to(e.marco))
        impares = e.aros([1, 3, 5], ERROR, 0.1)
        una_de = Text("Una entre tres", color=INK).scale(0.55).move_to([0, -3.5, 0])
        universo = Text("Universo nuevo", color=AMBAR, weight=BOLD).scale(0.6).move_to([0, 2.4, 0])
        self.reloj.clear_updaters()

        with self.narrar("b2"):
            # «La respuesta es un tercio»
            self.en("tercio")
            self.play(FadeOut(self.reloj), FadeOut(self.ojo_), FadeOut(self.par),
                      ReplacementTransform(otra, tercio), run_time=self.dur(0.6))
            self.sfx("exito")

            # «el mundo se ha hecho más pequeño»
            self.en("pequeno")
            self.add(fantasma)
            self.resaltar(e.marco, color=AMBAR)

            # «El uno, el tres y el cinco»
            self.en("impares")
            self.play(Create(impares), run_time=self.dur(0.5))

            # «ya no son posibles»
            self.en("fuera")
            self.play(*[e.caras[i - 1].animate.shift(UP * 1.7).fade(1) for i in (1, 3, 5)],
                      FadeOut(impares, shift=UP * 1.7), run_time=self.dur(0.7))

            # «quedan el dos, el cuatro y el seis»
            self.en("quedan")
            nuevos = {2: -1.5, 4: 0.0, 6: 1.5}
            self.play(*[e.caras[i - 1].animate.move_to([x, 0.5, 0]) for i, x in nuevos.items()],
                      FadeOut(self.aros_par), FadeOut(self.aro6),
                      e.marco.animate.stretch_to_fit_width(5.2).move_to([0, 0.5, 0]),
                      run_time=self.dur(0.8))

            # «El seis sigue siendo una cara»
            self.en("sigue")
            self.resaltar(e.caras[5], color=AMBAR)

            # «una entre tres»
            self.en("entre3")
            self.play(FadeIn(una_de), run_time=self.dur(0.4))

            # «El dado no ha cambiado»
            self.en("igual")
            self.play(Rotate(e.caras[5], TAU), run_time=self.dur(0.8))

            # «Ha cambiado el universo»
            self.en("universo")
            self.play(FadeOut(fantasma), FadeIn(universo), run_time=self.dur(0.5))
