"""Escena 12 — Fase mínima (el factor cuya inversa no explota) y el límite de blanquear: no se blanquea lo que no existe."""
from comun.escena import *


def espectro_hueco(w):
    """Espectro con una banda vacía: potencia solo para |Ω| < 1,2."""
    w = np.asarray(w, dtype=float)
    return np.where(np.abs(w) < 1.2, 1.0 - 0.5 * (w / 1.2) ** 2, 0.0)


class FaseMinimaYElLimite(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        b1 = caja("(2, 1) / √5", SENAL, ancho=3.0, alto=0.9, scale=0.6).move_to([-3.5, 2.8, 0])
        b2 = caja("(1, 2) / √5", AMBAR, ancho=3.0, alto=0.9, scale=0.6).move_to([3.5, 2.8, 0])
        ok = tilde(VERDE, 0.5).move_to([-5.8, 2.8, 0])
        x2 = cruz(ROJO, 0.7).move_to([5.8, 2.8, 0])
        c21 = MathTex(r"(\,\mathbf{2}\,,\;1\,)", color=AMBAR).scale(1.4).move_to([-3.5, 1.2, 0])
        gr = Underline(c21[0][2], color=AMBAR)
        fase = self.palabra("fase mínima", AMBAR, 1.2).move_to([0, -0.4, 0])
        rel = reloj(TXT).scale(1.2).move_to([-4.2, -2.0, 0])
        rel.permitir_encima = True
        t_causal = VGroup(tilde(VERDE, 0.4), etiqueta("causal", TXT, 0.65)).arrange(RIGHT, buff=0.25).move_to([0.3, -2.0, 0])
        t_estable = VGroup(tilde(VERDE, 0.4), etiqueta("estable", TXT, 0.65)).arrange(RIGHT, buff=0.25).move_to([3.4, -2.0, 0])
        fl = flecha([-1.0, -3.3, 0], [1.2, -3.3, 0], AMBAR, 4)
        cap = etiqueta("Cap. 12", AMBAR, 0.7).move_to([2.6, -3.3, 0])
        with self.narrar("b1"):
            # «hay uno cuya inversa no explota»
            self.en("uno")
            self.play(FadeIn(b1), FadeIn(b2), run_time=self.dur(0.6))
            self.play(FadeIn(ok), FadeIn(x2), run_time=0.5)

            # «el coeficiente grande primero»
            self.en("grande")
            self.play(FadeIn(c21), run_time=self.dur(0.6))
            self.play(Create(gr), run_time=0.4)

            # «factor de fase mínima»
            self.en("fase")
            self.pop(fase)

            # «el único que permite blanquear en tiempo real»
            self.en("tiempo")
            self.play(FadeIn(rel), run_time=0.5)
            self.play(Rotate(rel.minutero, angle=-TAU, about_point=rel.aro.get_center()), run_time=self.dur(1.2))

            # «causal y estable»
            self.en("causal")
            self.play(FadeIn(t_causal), run_time=0.4)
            self.play(FadeIn(t_estable), run_time=0.4)

            # «En el próximo capítulo»
            self.en("proximo")
            self.play(GrowArrow(fl), FadeIn(cap), run_time=self.dur(0.6))

            # «una pieza central»
            self.en("central")
            self.resaltar(fase, color=VERDE, escala=1.15, run_time=0.8)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        mu = muro(2.4, 0.5, ROJO).move_to([-6.2, 1.2, 0])
        t_lim = etiqueta("límite", ROJO, 0.6).move_to([-6.2, -0.5, 0])
        E = Lienzo(ancho=5.0, alto=2.0, t_rango=(-np.pi, np.pi), v_max=1.5, centro=(-2.6, 1.3))
        ej = ejes_L(E, 0, 1.5)
        cs = curva_f(E, espectro_hueco, -np.pi, np.pi, RUIDO, 5, n=300)
        vacia = Rectangle(width=E.x(np.pi) - E.x(1.2), height=2.0, color=ROJO, stroke_width=0).set_fill(ROJO, 0.25)
        vacia.move_to([(E.x(np.pi) + E.x(1.2)) / 2, 1.3, 0])
        t_nada = etiqueta("nada de potencia", ROJO, 0.55).move_to([E.x(2.2), 2.6, 0])
        t_nada.permitir_encima = True
        Eg = Lienzo(ancho=5.0, alto=2.0, t_rango=(-np.pi, np.pi), v_max=1.5, centro=(4.0, 1.3))
        ejg = ejes_L(Eg, 0, 1.5)
        dash = DashedLine(Eg.p(-np.pi, 1.0), Eg.p(np.pi, 1.0), color=TXT, stroke_width=3)
        cg = curva_f(Eg, lambda w: np.minimum(1.0 / np.maximum(espectro_hueco(w), 0.04) * 0.5, 1.45), -np.pi, np.pi, AMBAR, 5, n=300)
        t_inf = MathTex(r"\infty", color=ROJO).scale(1.6).move_to([Eg.x(2.4) + 0.6, 3.1, 0])
        sin = etiqueta("no se puede blanquear lo que no existe", TXT, 0.75).move_to([0, -1.9, 0])
        x = cruz(ROJO, 1.4).move_to([4.0, 1.3, 0])
        fl = flecha([-1.0, -3.0, 0], [1.2, -3.0, 0], AMBAR, 4)
        cap = etiqueta("Cap. 12", AMBAR, 0.7).move_to([2.6, -3.0, 0])
        nombre = MathTex("?", color=AMBAR).scale(2.0).move_to([5.0, -3.0, 0])
        with self.narrar("b2"):
            # «un límite que ningún blanqueador puede saltarse»
            self.en("limite")
            self.corte()
            self.play(FadeIn(mu), FadeIn(t_lim), run_time=self.dur(0.8))

            # «Si el proceso no tiene»
            self.en("si")
            self.play(Create(ej), Create(cs), run_time=self.dur(1.0))

            # «nada de potencia en toda una banda»
            self.en("nada")
            self.play(FadeIn(vacia), FadeIn(t_nada), run_time=self.dur(0.8))

            # «dejarlo plano»
            self.en("plano")
            self.play(Create(ejg), Create(dash), run_time=self.dur(0.8))

            # «multiplicar esa banda por infinito»
            self.en("infinito")
            self.play(Create(cg), run_time=self.dur(1.0))
            self.pop(t_inf)

            # «No se puede blanquear lo que no existe»
            self.en("noexiste")
            self.play(Create(x), run_time=0.4)
            self.pop(sin)

            # «En el capítulo que viene»
            self.en("cap")
            self.play(GrowArrow(fl), FadeIn(cap), run_time=self.dur(0.6))

            # «tendrá nombre propio»
            self.en("nombre")
            self.pop(nombre)
