"""Escena 13 — Primera sorpresa: un espectro plano obliga a media cero."""
from comun.escena import *


class LaPrimeraSorpresa(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.esp = Espectro(w_max=3.2, y_max=1.5, ancho=5.6, alto=2.4, centro=(-3.6, -2.0), x_label=r"\omega")
        self.pregunta()
        self.respuesta()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def pregunta(self):
        esp = self.esp
        titulo_ = Text("primera sorpresa", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, 3.4, 0])
        plano = esp.curva(lambda w: 0.9, AMBAR, a=-np.pi, b=np.pi)
        mu5 = MathTex(r"\mu = 5", color=SENAL).scale(1.1).move_to([-3.6, 1.7, 0])
        self.cajas = VGroup(caja("sí", INK, ancho=2.6, alto=0.8, scale=0.6),
                            caja("no", INK, ancho=2.6, alto=0.8, scale=0.6),
                            caja("depende", INK, ancho=2.6, alto=0.8, scale=0.6)).arrange(DOWN, buff=0.3).move_to([4.3, 1.2, 0])
        media = MathTex(r"\text{media}", r"\to", r"\text{impulso en el origen}", color=SENAL).scale(0.7).move_to([4.0, -1.0, 0])
        self.imp = esp.flecha(0, 1.3, SENAL)
        with self.narrar("b1"):
            # «Primera sorpresa»
            self.en("primera")
            self.pop(titulo_)
            # «un ruido de espectro plano»
            self.en("plano")
            self.play(Create(esp.ejes), Create(plano), run_time=self.dur(0.8))
            # «media cinco»
            self.en("cinco")
            self.pop(mu5)
            # «Sí, no, ¿depende?»
            self.en("opciones")
            self.play(LaggedStart(*[FadeIn(c) for c in self.cajas], lag_ratio=0.3), run_time=self.dur(1.2))
            # «lo que sabemos de la media»
            self.en("media")
            self.play(FadeIn(media), run_time=self.dur(0.6))
            # «un impulso en el origen»
            self.en("impulso")
            self.play(GrowArrow(self.imp), run_time=self.dur(0.6))
        self.plano = plano
        self.vars = (titulo_, mu5, media)

    # ------------------------------------------------------------ b2
    def respuesta(self):
        esp = self.esp
        self.play(*[FadeOut(m) for m in self.vars], run_time=0.3)
        d1 = oculta(formula(r"D_{xx}", "=", r"S_{xx}", "-", r"2\pi \mu^2 \delta(\omega)").scale(0.95)).move_to([-3.2, 3.2, 0])
        d2 = oculta(formula("=", "K", "-", r"2\pi \cdot 25 \cdot \delta(\omega)").scale(0.95)).move_to([-3.0, 2.2, 0])
        self.add(d1, d2)
        with self.narrar("b2"):
            # «La respuesta es no»
            self.en("no")
            ok = tilde().scale(0.8).next_to(self.cajas[1], RIGHT, buff=0.2)
            self.play(self.cajas[1][0].animate.set_stroke(VERDE, width=5), FadeIn(ok), run_time=self.dur(0.5))
            # «plano a altura ka»
            self.en("ka")
            kk = MathTex("K", color=AMBAR).scale(0.9).move_to(esp.p(-3.2, 0.9) + LEFT * 0.0 + UP * 0.35)
            self.play(FadeIn(kk), run_time=self.dur(0.4))
            # «la densidad de las fluctuaciones sería»
            self.en("dens")
            self.play(*revelar(d1[0], d1[1]), run_time=self.dur(0.5))
            # «el espectro menos el impulso de la media»
            self.en("menos")
            self.play(*revelar(d1[2], d1[3], d1[4]), run_time=self.dur(0.8))
            # «ka menos dos pi por veinticinco»
            self.en("kmenos")
            self.play(*revelar(*d2), run_time=self.dur(0.8))
            # «en el origen»
            self.en("origen")
            self.play(self.imp.animate.set_stroke(opacity=0.35), run_time=self.dur(0.5))
            # «apunta hacia abajo»
            self.en("abajo")
            aba = Arrow(esp.p(0, 0), esp.p(0, -0.9), buff=0, color=ROJO, stroke_width=8, max_tip_length_to_length_ratio=0.25)
            self.play(GrowArrow(aba), run_time=self.dur(0.5))
            # «una densidad negativa»
            self.en("neg")
            sel = sello("densidad negativa", ROJO).move_to([4.2, -2.8, 0])
            self.pop(sel)
            # «Imposible»
            self.en("imposible")
            cr = cruz(ROJO, 1.0).move_to(esp.p(0, -0.9) + DOWN * 0.3)
            self.sfx("error")
            self.play(FadeIn(cr), run_time=self.dur(0.4))
            # «la media sea cero»
            self.en("mu0")
            mu0 = MathTex(r"\mu = 0", color=VERDE).scale(1.3).move_to([4.2, -1.2, 0])
            self.pop(mu0)
