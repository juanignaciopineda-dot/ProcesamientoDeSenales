"""Escena 03 — Decidir no es estimar: hipótesis y probabilidades a priori."""
from comun.escena import *
from comun.figuras_c9e1 import *


class NoEsUnBit(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.pregunta()
        self.nombres()
        self.a_priori()
        self.wait(1.0)
        self.limpiar()

    def pregunta(self):
        with self.narrar("b1"):
            # «En el capítulo anterior»
            self.en("anterior")
            cap = Text("Capítulo 8", color=TXT, weight=BOLD).scale(1.1)
            sub = Text("Estimación", color=INK).scale(0.6).next_to(cap, DOWN, buff=0.3)
            self.pop(cap)
            self.play(FadeIn(sub, shift=UP * 0.15), run_time=self.dur(0.4))
            esquina = etiqueta("Capítulo 8", INK, 0.5).to_corner(UL, buff=0.45)

            # «Por un canal se envían»
            self.en("canal")
            K = canal9(centro=(-0.8, 1.6), ancho=7.0)
            self.canal = K
            self.play(ReplacementTransform(cap, esquina), FadeOut(sub), FadeIn(K), run_time=self.dur(0.6))
            bits = [bit9(b, lado=0.45) for b in (0, 1, 0)]
            for i, b in enumerate(bits):
                b.move_to(K.p_ent() + RIGHT * 0.3)
            self.play(LaggedStart(*[Succession(FadeIn(b, run_time=0.15),
                                               b.animate(run_time=0.6).move_to(K.caja.get_left() + LEFT * 0.3)
                                               .set_opacity(0))
                                    for b in bits], lag_ratio=0.45), run_time=self.dur(1.4))
            self.remove(*bits)

            # «recibes un uno»
            self.en("recibe")
            rec = bit9(1, color=MEDIDA, lado=0.55).move_to(K.p_sal() + RIGHT * 0.45)
            self.play(FadeIn(rec, shift=RIGHT * 0.3), run_time=self.dur(0.4))

            # «cero coma setenta y nueve»
            self.en("est")
            b0 = bit9(0, lado=0.6).move_to([-3.4, -0.7, 0])
            b1 = bit9(1, lado=0.6).move_to([1.8, -0.7, 0])
            est = Text("0,79", color=ESTIMACION, weight=BOLD).scale(0.9).move_to([-0.8, -0.7, 0])
            preg = Text("?", color=ESTIMACION, weight=BOLD).scale(0.6).next_to(est, UP, buff=0.2)
            self.play(FadeIn(b0), FadeIn(b1), run_time=self.dur(0.3))
            self.pop(est, preg)

            # «no es un bit»
            self.en("nobit")
            self.play(Create(tachar(est)), run_time=self.dur(0.4))
            self.sfx("error", gain=-20)

            # «El receptor de tu móvil»
            self.en("movil")
            mov = movil7().move_to([5.4, 1.6, 0])
            self.play(FadeIn(mov, shift=LEFT * 0.3), rec.animate.move_to([4.25, 1.6, 0]), run_time=self.dur(0.5))

            # «tiene que elegir»
            self.en("elegir")
            e0 = bit9(0, lado=0.55).move_to([4.8, -0.3, 0])
            e1 = bit9(1, lado=0.55).move_to([6.0, -0.3, 0])
            f0 = Arrow(mov.get_bottom(), e0.get_top(), color=INK, buff=0.1, stroke_width=3,
                       max_tip_length_to_length_ratio=0.25)
            f1 = Arrow(mov.get_bottom(), e1.get_top(), color=INK, buff=0.1, stroke_width=3,
                       max_tip_length_to_length_ratio=0.25)
            self.play(GrowArrow(f0), GrowArrow(f1), FadeIn(e0), FadeIn(e1), run_time=self.dur(0.6))

            # «Eso es decidir»
            self.en("decidir")
            dec = self.palabra("Decidir", ESTIMACION, 1.2).move_to([0, -2.3, 0])
            self.pop(dec)

            # «el tema de este capítulo»
            self.en("tema")
            tema = etiqueta("Pruebas de hipótesis", TXT, 0.6).move_to([0, -3.2, 0])
            self.play(FadeIn(tema, shift=UP * 0.2), run_time=self.dur(0.4))

    def nombres(self):
        with self.narrar("b2"):
            # «Pongamos nombres»
            self.en("limpia")
            self.corte()
            rec = VGroup(Text("Recibido", color=MEDIDA).scale(0.55), bit9(1, color=MEDIDA, lado=0.5))
            rec.arrange(RIGHT, buff=0.25)
            self.rec = rec
            arriba = rec.copy().move_to([0, 3.3, 0])
            rec.scale(1.8).move_to([0, 0.4, 0])
            self.pop(rec)
            preg = Text("¿Qué se envió?", color=ESTIMACION, weight=BOLD).scale(0.7).next_to(rec, DOWN, buff=0.5)
            self.play(FadeIn(preg, shift=UP * 0.15), run_time=self.dur(0.4))

            # «se llama hipótesis»
            self.en("hip")
            hip = self.palabra("Hipótesis", ESTIMACION, 0.9).move_to([0, 2.25, 0])
            self.play(rec.animate.become(arriba), FadeOut(preg), run_time=self.dur(0.5))
            self.pop(hip)

            # «hache cero»
            self.en("h0")
            h0 = casilla_h9("H_0", "· Se envió 0", C0).move_to([-3.3, 0.9, 0])
            self.h0 = h0
            self.pop(h0)

            # «se envió un cero»
            self.en("env0")
            b = bit9(0, lado=0.4).move_to(h0.get_right() + RIGHT * 0.35)
            self.add(b)
            self.play(b.animate.shift(RIGHT * 1.3).set_opacity(0), run_time=self.dur(0.7))
            self.remove(b)

            # «hache uno»
            self.en("h1")
            h1 = casilla_h9("H_1", "· Se envió 1", C1).move_to([3.3, 0.9, 0])
            self.h1 = h1
            self.pop(h1)

            # «Solo una es verdad»
            self.en("una")
            ok = tilde(VERDE, 0.55).move_to([0, 0.9, 0])
            ok.permitir_encima = True
            tapa = Text("?", color=ESTIMACION, weight=BOLD).scale(0.9).move_to(ok)
            self.play(Create(ok), run_time=self.dur(0.3))
            self.pop(tapa)
            self.una = VGroup(ok, tapa)

            # «Tenemos dos cosas»
            self.en("dos")
            hu0 = DashedVMobject(RoundedRectangle(corner_radius=0.12, width=5.2, height=1.0, color=INK,
                                                  stroke_width=2.5), num_dashes=40).move_to([-3.3, -1.4, 0])
            hu1 = hu0.copy().move_to([3.3, -1.4, 0])
            self.huecos = VGroup(hu0, hu1)
            self.play(Create(hu0), Create(hu1), run_time=self.dur(0.5))

            # «un dato»
            self.en("dato")
            dato = Text("Dato: recibido 1", color=MEDIDA).scale(0.5).move_to(hu0)
            self.pop(dato)

            # «antes de mirar»
            self.en("antes")
            antes = Text("Lo que sabíamos antes", color=ESTIMACION).scale(0.5).move_to(hu1)
            self.pop(antes)

    def a_priori(self):
        with self.narrar("b3"):
            # «el setenta por ciento»
            self.en("p0")
            t0 = Text("70 %", color=C0, weight=BOLD).scale(0.6).next_to(self.h0, DOWN, buff=0.25)
            self.pop(t0)

            # «un uno el treinta»
            self.en("p1")
            t1 = Text("30 %", color=C1, weight=BOLD).scale(0.6).next_to(self.h1, DOWN, buff=0.25)
            self.pop(t1)

            # «probabilidades a priori»
            self.en("apriori")
            ap = Text("A priori", color=ESTIMACION, weight=BOLD).scale(0.55).move_to([0, t0.get_y(), 0])
            m0 = MathTex(r"p_0 = 0{,}7", color=C0).scale(0.8).move_to(t0)
            m1 = MathTex(r"p_1 = 0{,}3", color=C1).scale(0.8).move_to(t1)
            self.play(FadeOut(self.una), run_time=self.dur(0.2))
            self.play(ReplacementTransform(t0, m0), ReplacementTransform(t1, m1), FadeIn(ap),
                      run_time=self.dur(0.6))

            # «antes de recibir nada»
            self.en("nada")
            self.play(self.rec.animate.fade(0.7), run_time=self.dur(0.5))

            # «cómo es el canal»
            self.en("canal")
            K = canal9(centro=(0, -3.15), ancho=4.6, escala=0.6)
            self.play(FadeIn(K, shift=UP * 0.2), run_time=self.dur(0.5))

            # «una de cada diez veces»
            self.en("diez")
            b = bit9(0, lado=0.36).move_to(K.p_ent() + RIGHT * 0.25)
            self.add(b)
            self.play(b.animate.move_to(K.caja.get_left() + LEFT * 0.25).set_opacity(0), run_time=self.dur(0.5))
            self.remove(b)
            b2 = bit9(1, color=ERROR, lado=0.36).move_to(K.caja.get_right() + RIGHT * 0.25)
            self.play(FadeIn(b2), run_time=self.dur(0.2))
            self.play(b2.animate.move_to(K.p_sal() + LEFT * 0.25), run_time=self.dur(0.4))
            diez = Text("10 %", color=ERROR, weight=BOLD).scale(0.5).next_to(K.caja, UP, buff=0.15)
            self.pop(diez)
