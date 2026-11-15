"""Escena 18 — El promediador que no ve nada: con (1, −2, 1) el promediador es perpendicular a la señal."""
from comun.escena import *


class LaSorpresa(EscenaCurso):
    ESCENA = "18"

    def construct(self):
        pal = self.palabra("sorpresa", AMBAR, 0.9).move_to([0, 3.3, 0])
        s = Tallos([1, -2, 1], centro=(-3.5, 1.1), paso=0.8, unidad=0.35, color=SENAL)
        v_s = valores_sobre13(s)
        e6 = MathTex(r"E=6", color=AMBAR).scale(1.0).move_to([-0.6, 1.1, 0])
        l_det = etiqueta("detectable", VERDE, 0.5).move_to([1.8, 1.1, 0])
        ok = tilde(VERDE, 0.8).move_to([3.2, 1.1, 0])
        pr = Tallos([1, 1, 1], centro=(-3.5, -1.0), paso=0.8, unidad=0.35, color=ESTIMACION)
        suma0 = MathTex(r"1-2+1=0", color=TXT).scale(1.2).move_to([0.6, -1.0, 0])
        pl = plano_c(centro=(5.3, -0.2), radio=0.9)
        fs = flecha_c(pl.o, 1.3, 0, SENAL, 6)
        fh = flecha_c(pl.o, 1.3, 90, ESTIMACION, 6)
        recto = RightAngle(Line(pl.o, pl.o + RIGHT), Line(pl.o, pl.o + UP), length=0.3, color=AMBAR, quadrant=(1, 1))
        cos0 = MathTex(r"\cos^2 90^\circ=0", color=AMBAR).scale(0.8).move_to([5.3, -1.8, 0])
        oj = ojo(TXT).scale(0.8).move_to([4.8, 2.1, 0])
        q0 = MathTex(r"Q(0)", r"=0{,}5", color=TXT).scale(1.2).move_to([-3.0, -2.7, 0])
        q0[1].set_color(ERROR)
        mon = moneda("", AMBAR).scale(0.8).move_to([0.2, -2.7, 0])
        # segundo bloque
        sue = Tallos([0, -2, 0], centro=(-3.5, 1.5), paso=0.8, unidad=0.35, color=ESTIMACION)
        s2 = Tallos([1, -2, 1], centro=(-3.5, 1.5), paso=0.8, unidad=0.35, color=SENAL)
        terc = MathTex(r"\frac46=0{,}667", r"\ (-1{,}76\ \mathrm{dB})", color=TXT).scale(1.0).move_to([2.2, 1.5, 0])
        mor = self.palabra("moraleja", AMBAR, 0.9).move_to([0, 3.3, 0])
        L = Lienzo(ancho=5.0, alto=2.4, t_rango=(0, 1), v_max=1.0, centro=(-3.0, -2.1))
        cur = curva_f(L, lambda x: np.cos(np.asarray(x) * np.pi / 2) ** 2, 0.0, 1.0, AMBAR, 4.0)
        eje = L.base(INK, 2.0)
        l0 = MathTex(r"0^\circ", color=INK).scale(0.6).move_to(L.p(0, 0) + DOWN * 0.35)
        l90 = MathTex(r"90^\circ", color=INK).scale(0.6).move_to(L.p(1, 0) + DOWN * 0.35)
        cero = Dot(L.p(1, 0), radius=0.12, color=ERROR)
        pr2 = Tallos([1, 1, 1], centro=(4.6, -1.7), paso=0.7, unidad=0.35, color=ESTIMACION)
        s3 = Tallos([1, -2, 1], centro=(4.6, 0.1), paso=0.7, unidad=0.3, color=SENAL)
        x_pr = cruz(ROJO, 1.0).move_to(pr2)
        dos = caja("episodio 1: dos mediciones", INK, ancho=4.2, alto=0.6, scale=0.38).move_to([4.6, -3.4, 0])

        with self.narrar("b1"):
            # «una sorpresa»
            self.en("sorpresa")
            self.pop(pal)

            # «uno, menos dos, uno»
            self.en("pulso")
            self.play(FadeIn(s), FadeIn(v_s), run_time=self.dur(0.6))

            # «energía seis»
            self.en("e6")
            self.play(Write(e6), run_time=self.dur(0.6))

            # «tan detectable»
            self.en("detectable")
            self.play(FadeIn(l_det), Create(ok), run_time=self.dur(0.5))

            # «mira al promediador»
            self.en("mira")
            self.play(FadeIn(pr), run_time=self.dur(0.6))

            # «uno menos dos, más uno, cero»
            self.en("suma0")
            self.play(Write(suma0), run_time=self.dur(1.2))

            # «perpendicular a la señal»
            self.en("perp")
            self.play(FadeIn(pl), GrowArrow(fs), GrowArrow(fh), run_time=self.dur(0.7))
            self.play(Create(recto), run_time=0.3)

            # «coseno cero»
            self.en("cos0")
            self.play(Write(cos0), run_time=self.dur(0.7))

            # «No ve nada»
            self.en("nada")
            self.play(FadeIn(oj), run_time=0.3)
            self.play(oj.animate.stretch(0.12, 1), run_time=self.dur(0.4))

            # «cu de cero»
            self.en("q0")
            self.play(Write(q0[0]), run_time=self.dur(0.5))

            # «tirar una moneda»
            self.en("moneda")
            self.play(Write(q0[1]), FadeIn(mon, scale=1.3), run_time=self.dur(0.7))

        with self.narrar("b2"):
            # «La muestra suelta»
            self.en("suelta")
            self.corte()
            self.play(FadeIn(s2), FadeIn(sue), run_time=self.dur(0.6))

            # «dos tercios»
            self.en("tercios")
            self.play(Write(terc), run_time=self.dur(1.6))

            # «Moraleja»
            self.en("moraleja")
            self.pop(mor)

            # «cualquier desalineación con la señal cuesta»
            self.en("cuesta")
            self.play(Create(eje), FadeIn(l0), FadeIn(l90), run_time=self.dur(0.5))
            self.play(Create(cur), run_time=self.dur(1.4))

            # «puede costarlo todo»
            self.en("todo")
            self.play(FadeIn(cero, scale=2.0), run_time=self.dur(0.4))
            self.sfx("error", gain=-18)

            # «Promediar no siempre es buena idea»
            self.en("promediar")
            self.play(FadeIn(s3), FadeIn(pr2), run_time=self.dur(0.5))
            self.play(Create(x_pr), run_time=0.3)

            # «las dos mediciones»
            self.en("dos")
            self.play(FadeIn(dos), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
