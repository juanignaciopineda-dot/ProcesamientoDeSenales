"""Escena 07 — Ec. 2: el símbolo fija la frecuencia de partida del chirp (el dato es el desplazamiento)."""
from comun.escena import *
from comun.figuras_lora import *


class ElDatoEsElDesplazamiento(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.partida()
        self.desplazada()
        self.ecuacion()
        self.wait(1.0)
        self.limpiar()

    def partida(self):
        P = self.P = PlanoTF(centro=(-1.2, 0.2), ancho=7.0, alto=5.0, escala=0.5)
        q = Text("?", color=AMBAR, weight=BOLD).scale(2.0).move_to(P.marco)
        s = self.s = ValueTracker(0)
        rampa = self.rampa = always_redraw(lambda: P.rampa(s.get_value(), grosor=6))

        def _punto():
            d = Dot(P.p(0, s.get_value() / M7), radius=0.13, color=AMBAR)
            d.permitir_encima = True      # arranca pegado al «0» del eje
            return d

        punto = self.punto = always_redraw(_punto)
        rot = self.rot = MathTex("s", "=", color=TXT).scale(1.5).move_to([4.3, 2.2, 0])
        rot[0].set_color(AMBAR)
        num = self.num = Integer(0, group_with_commas=False, color=AMBAR).scale(1.5).next_to(rot, RIGHT, buff=0.2)
        num.add_updater(lambda m: m.set_value(round(s.get_value())).next_to(rot, RIGHT, buff=0.2))
        ct = self.ct = cota(P.p(1, 0) + RIGHT * 0.3, P.p(1, S_EJEMPLO / M7) + RIGHT * 0.3, "20", AMBAR, RIGHT, 0.6)
        tope = self.tope = Dot(P.p((M7 - S_EJEMPLO) / M7, 1), radius=0.13, color=CIAN)
        salto = self.salto = P.salto(S_EJEMPLO, color=CIAN)
        with self.narrar("b1"):
            # «¿Y dónde va el dato?»
            self.en("donde")
            self.play(FadeIn(P), run_time=0.4)
            self.pop(q)
            # «En el punto de partida»
            self.en("partida")
            self.play(FadeOut(q), run_time=0.25)
            self.pop(punto)
            # «El símbolo cero»
            self.en("s0")
            self.play(Create(rampa), FadeIn(rot), FadeIn(num), run_time=self.dur(0.8))
            # «El símbolo veinte» / «veinte escalones más arriba»
            self.en("s20")
            self.resaltar(num, color=AMBAR, escala=1.2, run_time=self.dur(0.4))
            self.en("escal")
            self.play(s.animate.set_value(S_EJEMPLO), run_time=self.dur(1.2))
            self.play(FadeIn(ct), run_time=self.dur(0.4))
            # «La rampa sube igual»
            self.en("igual")
            luz = P.rampa(S_EJEMPLO, color=TXT, grosor=9)[0]
            self.play(Create(luz), run_time=self.dur(0.8))
            self.play(FadeOut(luz), run_time=0.3)
            # «llega al tope»
            self.en("tope")
            self.pop(tope)
            # «vuelve a cero»
            self.en("vuelve")
            self.play(Create(salto), run_time=self.dur(0.7))
            # «hasta completar el símbolo»
            self.en("completa")
            luz2 = P.rampa(S_EJEMPLO, color=TXT, grosor=9)[1]
            self.play(Create(luz2), run_time=self.dur(0.6))
            self.play(FadeOut(luz2), run_time=0.3)

    def desplazada(self):
        P, s = self.P, self.s
        porta = Text("Chirp = Portadora", color=TXT, weight=BOLD).scale(0.56).move_to([4.6, 0.3, 0])
        info = Text("Dato = Desplazamiento", color=AMBAR, weight=BOLD).scale(0.56).move_to([4.6, -0.7, 0])
        P3 = PlanoTF(centro=(0.3, -0.2), ancho=11.4, alto=4.4, n=3, escala=0.5)
        div = VGroup(P3.division(1), P3.division(2))
        rs = [P3.rampa(v, i, grosor=6) for i, v in enumerate((0, 32, 80))]
        ns = [MathTex(f"s={v}", color=AMBAR).scale(1.2).move_to(P3.p(i + 0.5, 1) + UP * 0.5)
              for i, v in enumerate((0, 32, 80))]
        with self.narrar("b2"):
            # «la misma rampa, desplazada»
            self.en("misma")
            self.play(FadeOut(self.ct), FadeOut(self.tope), FadeOut(self.salto), run_time=0.3)
            t = (self.margen() - 0.3) / 2
            self.play(s.animate.set_value(100), run_time=t)
            self.play(s.animate.set_value(S_EJEMPLO), run_time=t)
            # «el chirp hace de portadora»
            self.en("porta")
            self.pop(porta)
            # «la información está en el desplazamiento»
            self.en("info")
            self.pop(info)
            # «Aquí van»
            self.en("aqui")
            self.num.clear_updaters()
            self.rampa.clear_updaters()
            self.punto.clear_updaters()
            self.play(*[FadeOut(m) for m in (porta, info, self.rot, self.num, self.rampa, self.punto, P)],
                      run_time=self.dur(0.5))
            # «tres símbolos seguidos»
            self.en("tres")
            self.play(FadeIn(P3), FadeIn(div), run_time=self.dur(0.6))
            # «cero», «treinta y dos», «ochenta»
            for marca, r, n in zip(("c0", "c32", "c80"), rs, ns):
                self.en(marca)
                self.play(Create(r), FadeIn(n), run_time=self.dur(0.5))

    def ecuacion(self):
        ec = Text("Ec. 2", color=INK, weight=BOLD).scale(0.65).move_to([-5.9, 2.9, 0])
        f = MathTex(r"c(nT_s+kT)", "=", r"\frac{1}{\sqrt{2^{SF}}}", r"\exp\!\Big(j2\pi\,\big[", "(s+k)",
                    r"\bmod 2^{SF}", r"\big]\,\frac{k}{2^{SF}}\Big)", color=TXT).scale(1.05).move_to([0, 1.5, 0])
        f[4].set_color(AMBAR)
        f[5].set_color(CIAN)
        centro = np.array([3.6, -1.7, 0])
        circ = Circle(radius=1.2, color=INK, stroke_width=2).move_to(centro)
        fle = Arrow(centro, centro + RIGHT * 1.2, color=SENAL, stroke_width=6, buff=0,
                    max_tip_length_to_length_ratio=0.25)
        e1 = Text("Energía = 1", color=VERDE, weight=BOLD).scale(0.85).move_to([-3.2, -1.7, 0])
        with self.narrar("b3"):
            # «La ecuación dos»
            self.en("ec2")
            self.corte()
            self.play(FadeIn(ec), FadeIn(f[0]), FadeIn(f[1]), run_time=self.dur(0.6))
            # «Una exponencial compleja»
            self.en("exp")
            self.play(FadeIn(f[3]), FadeIn(f[6]), run_time=self.dur(0.6))
            # «una flecha que gira»
            self.en("flecha")
            self.play(FadeIn(circ), GrowArrow(fle), run_time=0.4)
            self.play(Rotate(fle, angle=1.5 * TAU, about_point=centro, rate_func=linear),
                      run_time=max(0.5, self.margen() - 0.2))
            # «el símbolo más el índice de la muestra»
            self.en("smask")
            self.pop(f[4], sonido=None)
            self.play(Rotate(fle, angle=1.0 * TAU, about_point=centro, rate_func=linear),
                      run_time=max(0.5, self.margen() - 0.2))
            # «la vuelta a cero»
            self.en("mod")
            self.pop(f[5], sonido=None)
            self.play(Rotate(fle, angle=1.0 * TAU, about_point=centro, rate_func=linear),
                      run_time=max(0.5, self.margen() - 0.2))
            # «un factor delante»
            self.en("factor")
            self.pop(f[2], sonido=None)
            # «energía uno»
            self.en("e1")
            self.pop(e1)
