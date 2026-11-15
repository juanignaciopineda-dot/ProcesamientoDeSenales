"""Escena 14 — Segunda sorpresa: en tiempo continuo, el espectro plano tiene área infinita."""
from comun.escena import *


class LaSegundaSorpresa(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        self.esp = Espectro(w_max=6, y_max=1.5, ancho=9.0, alto=2.6, centro=(0.0, -1.2), x_label=r"\omega")
        self.infinita()
        self.idealizacion()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def infinita(self):
        esp = self.esp
        tit = Text("segunda sorpresa", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, 3.4, 0])
        cont = Text("tiempo continuo", color=INK).scale(0.6).move_to([0, 2.7, 0])
        plano = esp.curva(lambda w: 1.0, AMBAR)
        t_pi = VGroup(MathTex(r"-\pi", color=INK).scale(0.7).move_to(esp.p(-1.2, -0.28)),
                      MathTex(r"\pi", color=INK).scale(0.7).move_to(esp.p(1.2, -0.28)),
                      Line(esp.p(-1.2, -0.08), esp.p(-1.2, 0.08), color=INK, stroke_width=3),
                      Line(esp.p(1.2, -0.08), esp.p(1.2, 0.08), color=INK, stroke_width=3))
        flechas = VGroup(Arrow(esp.p(-5.6, 1.2), esp.p(-6.0, 1.2), buff=0, color=INK, stroke_width=5),
                         Arrow(esp.p(5.6, 1.2), esp.p(6.0, 1.2), buff=0, color=INK, stroke_width=5))
        a1 = esp.area(plano, -2.2, 2.2, AMBAR, 0.4)
        a2 = esp.area(plano, -5.8, 5.8, AMBAR, 0.4)
        l1 = MathTex(r"-1.000", color=AMBAR).scale(0.65).move_to(esp.p(-2.2, -0.3))
        l2 = MathTex(r"1.000", color=AMBAR).scale(0.65).move_to(esp.p(2.2, -0.3))
        m1 = MathTex(r"-1.000.000", color=AMBAR).scale(0.6).move_to(esp.p(-5.5, -0.3))
        m2 = MathTex(r"1.000.000", color=AMBAR).scale(0.6).move_to(esp.p(5.4, -0.3))
        r2000 = MathTex(r"\text{área} = 2.000", color=AMBAR).scale(0.9).move_to([0, 2.1, 0])
        r2m = MathTex(r"\text{área} = 2.000.000", color=AMBAR).scale(0.9).move_to([0, 2.1, 0])
        rinf = MathTex(r"\text{área} = \infty", color=ROJO).scale(1.1).move_to([0, 2.1, 0])
        with self.narrar("b1"):
            # «Segunda sorpresa»
            self.en("segunda")
            self.pop(tit)
            # «en tiempo continuo»
            self.en("continuo")
            self.play(FadeIn(cont), Create(esp.ejes), run_time=self.dur(0.6))
            # «no se acaba en pi»
            self.en("pi")
            self.play(FadeIn(t_pi), run_time=self.dur(0.6))
            # «hasta el infinito»
            self.en("inf")
            self.play(Create(flechas), run_time=self.dur(0.5))
            # «altura uno»
            self.en("alt1")
            self.play(Create(plano), run_time=self.dur(0.7))
            # «hasta mil radianes por segundo»
            self.en("mil")
            self.play(FadeIn(a1), FadeIn(l1), FadeIn(l2), run_time=self.dur(0.6))
            # «área dos mil»
            self.en("a2000")
            self.play(FadeIn(r2000), run_time=self.dur(0.5))
            # «Hasta un millón»
            self.en("millon")
            self.play(ReplacementTransform(a1, a2), FadeOut(l1), FadeOut(l2), FadeIn(m1), FadeIn(m2),
                      FadeOut(r2000), run_time=self.dur(0.8))
            # «dos millones»
            self.en("dosmill")
            self.play(FadeIn(r2m), run_time=self.dur(0.5))
            # «área infinita»
            self.en("areainf")
            self.play(ReplacementTransform(r2m, rinf), run_time=self.dur(0.5))
            # «potencia infinita»
            self.en("potinf")
            pinf = MathTex(r"\text{potencia} = \infty", color=ROJO).scale(1.1).move_to([0, -3.4, 0])
            self.pop(pinf)
            # «no puede existir»
            self.en("noexiste")
            sel = sello("no existe", ROJO).move_to([4.8, 2.6, 0])
            self.pop(sel)
        self.sel = sel
        self.limp = VGroup(tit, cont, t_pi, flechas, a2, m1, m2, rinf, pinf)

    # ------------------------------------------------------------ b2
    def idealizacion(self):
        esp = self.esp
        plano = esp.curva(lambda w: 1.0, AMBAR)
        self.play(FadeOut(self.limp), FadeOut(self.sel), run_time=0.3)
        dirac = Arrow([-5.6, 1.4, 0], [-5.6, 3.2, 0], buff=0, color=AZUL, stroke_width=8, max_tip_length_to_length_ratio=0.25)
        dir_t = MathTex(r"\delta(t)", color=AZUL).scale(0.9).next_to(dirac, RIGHT, buff=0.2)
        ideal = Text("idealización", color=VERDE, weight=BOLD).scale(0.65).move_to([0, 3.2, 0])
        res = resistencia().scale(0.9).move_to([-5.2, 2.6, 0])
        res_t = Text("ruido térmico", color=INK).scale(0.5).next_to(res, DOWN, buff=0.2)
        bill = Text("billones de Hz", color=AMBAR, weight=BOLD).scale(0.6).move_to([0, 2.1, 0])
        ap = caja("aparato", AZUL, ancho=2.2, alto=0.8, scale=0.55).move_to([5.0, 2.6, 0])
        ven = Rectangle(width=esp.p(2.4)[0] - esp.p(-2.4)[0], height=2.9, color=VERDE, stroke_width=3)
        ven.set_fill(VERDE, 0.1).move_to(esp.p(0, 0.65))
        ven.permitir_encima = True
        with self.narrar("b2"):
            # «aun así lo usamos»
            self.en("usamos")
            self.play(Create(esp.ejes), Create(plano), run_time=self.dur(0.6))
            # «el impulso de Dirac»
            self.en("dirac")
            self.play(GrowArrow(dirac), FadeIn(dir_t), run_time=self.dur(0.6))
            # «una idealización cómoda»
            self.en("ideal")
            self.pop(ideal)
            # «buenos resultados»
            self.en("buenos")
            ok = tilde().scale(0.8).next_to(ideal, RIGHT, buff=0.3)
            self.play(FadeIn(ok), run_time=self.dur(0.4))
            # «El ruido térmico de una resistencia»
            self.en("termico")
            self.play(FadeOut(VGroup(dirac, dir_t)), Create(res), FadeIn(res_t), run_time=self.dur(0.7))
            # «billones de hercios»
            self.en("billones")
            self.play(FadeIn(bill), run_time=self.dur(0.5))
            # «Cualquier aparato real»
            self.en("aparato")
            self.play(FadeIn(ap), run_time=self.dur(0.5))
            # «corta mucho antes»
            self.en("corta")
            self.play(FadeIn(ven), run_time=self.dur(0.6))
            # «indistinguible del blanco»
            self.en("indist")
            ok2 = tilde().scale(0.9).move_to(esp.p(0, 1.45))
            self.play(FadeIn(ok2), run_time=self.dur(0.5))
