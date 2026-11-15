"""Escena 08 — α es a la vez la velocidad de olvido y el ancho de banda."""
from comun.escena import *


def _saltos(rng, tasa, t_max=6.0):
    t, ts = 0.0, []
    while True:
        t += rng.exponential(1.0 / tasa)
        if t >= t_max:
            return ts
        ts.append(t)


class MemoriaYAncho(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.par = ParAlfa(alfa=2.0, c_auto=(-3.6, -0.6), c_esp=(3.9, -2.4))
        self.tiempos()
        self.cuentas()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def tiempos(self):
        p = self.par
        interr = interruptor().scale(0.75).move_to([-5.9, 2.6, 0])
        dosl = MathTex(r"2\lambda", color=AMBAR).scale(1.1).next_to(interr, RIGHT, buff=0.3)
        auto, espec, mitad = p.auto(), p.espec(), p.mitad()
        base = p.L.base()
        desl = p.deslizador(centro=(-3.6, -3.55))
        with self.narrar("b1"):
            # «dos lambda»
            self.en("dosl")
            self.play(FadeIn(interr), FadeIn(dosl), run_time=self.dur(0.5))
            # «la velocidad a la que el interruptor olvida»
            self.en("olvida")
            self.play(*voltear(interr, False), Create(base), Create(auto), run_time=self.dur(0.9))
            # «disfrazada de ancho de banda»
            self.en("disfraz")
            dis = Text("¿ancho de banda?", color=MAGENTA, weight=BOLD).scale(0.55).next_to(dosl, RIGHT, buff=0.4)
            self.play(FadeIn(dis), run_time=self.dur(0.5))
            # «Aquí está»
            self.en("aqui")
            al = MathTex(r"\alpha", "=", r"2\lambda", color=TXT).scale(1.1).move_to([-1.6, 2.6, 0])
            al[0].set_color(AMBAR)
            self.play(FadeOut(dis), FadeIn(al), run_time=self.dur(0.5))
            # «la frecuencia donde el espectro cae a la mitad»
            self.en("mitad")
            self.play(Create(p.esp.ejes), Create(espec), FadeIn(mitad), run_time=self.dur(0.9))
            # «Movamos alfa»
            self.en("mover")
            self.play(FadeIn(desl), run_time=self.dur(0.4))
            self.play(p.a.animate.set_value(4.0), run_time=self.dur(1.0))
            # «las dos curvas a la vez»
            self.en("dos")
            self.play(p.a.animate.set_value(2.0), run_time=self.dur(0.9))
        self.desl = desl
        self.mitad_obj = mitad
        self.hijos = [interr, dosl, al]

    # ------------------------------------------------------------ b2
    def cuentas(self):
        p = self.par
        L = p.L
        ruido = np.random.default_rng(7)
        w8 = onda_tel(Lienzo(ancho=5.2, alto=1.0, t_rango=(0, 6), v_max=1.3, centro=(-3.6, 2.7)),
                      tiempos=_saltos(ruido, 4.0), color=AMBAR, ancho=3)
        w05 = onda_tel(Lienzo(ancho=5.2, alto=1.0, t_rango=(0, 6), v_max=1.3, centro=(-3.6, 2.7)),
                       tiempos=[3.6], color=AMBAR, ancho=3)
        self.play(*[FadeOut(m) for m in self.hijos], FadeOut(self.mitad_obj), run_time=0.3)
        with self.narrar("b2"):
            # «Con alfa igual a ocho»
            self.en("a8")
            self.play(p.a.animate.set_value(8.0), run_time=self.dur(1.3))
            # «salta muy a menudo»
            self.en("salta")
            self.play(Create(w8), run_time=self.dur(1.2), rate_func=linear)
            # «A medio segundo»
            self.en("medio")
            vl = Line(L.p(0.5, -0.45), L.p(0.5, 0.6), color=VERDE, stroke_width=3)
            m5 = MathTex(r"\tau = 0{,}5", color=VERDE).scale(0.7).move_to(L.p(0.5, -0.8) + RIGHT * 0.5)
            self.play(Create(vl), FadeIn(m5), run_time=self.dur(0.5))
            # «cero coma cero dos»
            self.en("r002")
            r = MathTex(r"R(0{,}5) = e^{-4} \approx 0{,}02", color=AMBAR).scale(0.85).move_to([-3.6, 1.2, 0])
            self.play(FadeIn(r), run_time=self.dur(0.6))
            # «casi lo ha olvidado todo»
            self.en("olvido")
            pt = Dot(L.p(0.5, 0.0183), color=VERDE, radius=0.09)
            self.play(FadeIn(pt), run_time=self.dur(0.4))
            # «cero coma dos cinco»
            self.en("s025")
            s0 = MathTex(r"S(0) = \tfrac{2}{8} = 0{,}25", color=AMBAR).scale(0.85).move_to([3.9, 2.0, 0])
            self.play(FadeIn(s0), run_time=self.dur(0.6))
            # «cae a la mitad en ocho»
            self.en("mitad8")
            mit = self.mitad_obj
            self.play(FadeIn(mit), run_time=self.dur(0.6))
            # «bajo y ancho»
            self.en("bajoancho")
            ba = Text("bajo y ancho", color=VERDE, weight=BOLD).scale(0.6).move_to([3.9, 1.4, 0])
            self.pop(ba)
            # «Con alfa igual a cero coma cinco»
            self.en("a05")
            self.play(FadeOut(VGroup(vl, m5, r, pt, s0, ba, mit)), FadeOut(w8), run_time=0.3)
            self.play(p.a.animate.set_value(0.5), run_time=self.dur(1.4))
            # «recuerda mucho»
            self.en("recuerda")
            self.play(Create(w05), run_time=self.dur(1.0), rate_func=linear)
            rec = Text("recuerda mucho", color=AMBAR, weight=BOLD).scale(0.6).move_to([-3.6, 1.2, 0])
            self.play(FadeIn(rec), run_time=self.dur(0.4))
            # «alto y estrecho»
            self.en("altoestrecho")
            mit2 = self.mitad_obj
            s4 = MathTex(r"S(0) = 4", color=AMBAR).scale(0.9).move_to([3.9, 2.4, 0])
            ae = Text("alto y estrecho", color=VERDE, weight=BOLD).scale(0.6).move_to([3.9, 1.7, 0])
            self.play(FadeIn(mit2), FadeIn(s4), FadeIn(ae), run_time=self.dur(0.6))
