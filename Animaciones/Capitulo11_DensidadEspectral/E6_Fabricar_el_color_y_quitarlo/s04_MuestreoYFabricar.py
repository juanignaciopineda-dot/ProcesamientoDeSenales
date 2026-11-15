"""Escena 04 — Muestreo para procesos y la pregunta de fabricar ruido con un espectro dado."""
from comun.escena import *


def pico(w):
    w = np.asarray(w, dtype=float)
    return 0.08 + 0.85 * np.exp(-((w - 0.166) / 0.011) ** 2)


def banda_b(w):
    """Espectro nulo por encima de B = 2."""
    w = np.asarray(w, dtype=float)
    return np.where(np.abs(w) < 2.0, 0.95 * (1 - (w / 2.0) ** 2) + 0.05, 0.0)


def senal(t):
    t = np.asarray(t, dtype=float)
    return 0.55 * np.sin(2 * np.pi * 0.28 * t) + 0.3 * np.sin(2 * np.pi * 0.5 * t + 1.0)


class MuestreoYFabricar(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        E = Lienzo(ancho=5.0, alto=1.8, t_rango=(0, 0.5), v_max=1.0, centro=(-3.0, 2.2))
        ej = ejes_L(E, 0, 1.05)
        pk = curva_f(E, pico, 0.0, 0.5, AMBAR, 5, n=300)
        raya = Line(E.p(0.166, 0), E.p(0.166, 0.93), color=AMBAR, stroke_width=8)
        Lt = Lienzo(ancho=5.0, alto=1.6, t_rango=(0, 6), v_max=1.0, centro=(-3.0, -0.4))
        seno = seno_t(Lt, 1.0, 0.8, AMBAR, 3.5)
        ciclo = DoubleArrow(Lt.p(0.25, 1.0), Lt.p(1.25, 1.0), color=CIAN, stroke_width=3, buff=0,
                            max_tip_length_to_length_ratio=0.2)
        t_hace = etiqueta("hace unos episodios", INK, 0.55).move_to([3.4, 1.2, 0])
        t_ss = self.palabra("Señales y Sistemas", CIAN, 0.8).move_to([0, 3.2, 0])
        Lr = Lienzo(ancho=5.0, alto=1.7, t_rango=(0, 4), v_max=1.0, centro=(-2.2, 0.9))
        ruido = ruido_t(Lr, semilla=11, amp=0.8)
        ok = tilde(VERDE, 0.9).move_to([1.6, 0.9, 0])
        muestreo = self.palabra("muestreo", AMBAR, 1.4).move_to([0, 3.0, 0])
        Eb = Lienzo(ancho=5.0, alto=1.8, t_rango=(-6, 6), v_max=1.0, centro=(-3.6, 1.2))
        ejb = ejes_L(Eb, 0, 1.05)
        cb = curva_f(Eb, banda_b, -6, 6, SENAL, 5, n=240)
        lb1 = MathTex("B", color=ERROR).scale(0.8).move_to(Eb.p(2, 0) + [0, -0.4, 0])
        lb2 = MathTex("-B", color=ERROR).scale(0.8).move_to(Eb.p(-2, 0) + [0, -0.4, 0])
        f2b = formula(">", "2B", r"\;\text{muestras por segundo}", escala=0.8, colores={1: AMBAR}).move_to([3.9, 1.2, 0])
        Ls = Lienzo(ancho=8.0, alto=1.9, t_rango=(0, 8), v_max=1.0, centro=(0, -2.0))
        tt = np.linspace(0.3, 7.7, 20)
        puntos = VGroup(*[Dot(Ls.p(x, float(senal(x))), radius=0.09, color=AMBAR) for x in tt])
        curva_s = Ls.curva(np.linspace(0, 8, 240), senal(np.linspace(0, 8, 240)), SENAL, 4)
        with self.narrar("b1"):
            # «Un pico marcado en un espectro»
            self.en("pico")
            self.corte()
            self.play(Create(ej), Create(pk), run_time=self.dur(0.9))

            # «algo que se repite»
            self.en("repite")
            self.play(Create(Lt.base()), Create(seno), run_time=self.dur(1.0), rate_func=linear)
            self.play(GrowFromCenter(ciclo), run_time=0.4)

            # «las rayas de la sinusoide»
            self.en("rayas")
            self.play(ReplacementTransform(pk, raya), run_time=self.dur(0.7))

            # «de hace unos episodios»
            self.en("hace")
            self.play(FadeIn(t_hace), run_time=0.4)

            # «Otra herramienta de Señales y Sistemas»
            self.en("otra")
            self.corte()
            self.pop(t_ss)

            # «sobrevive al azar»
            self.en("sobrevive")
            self.play(Create(Lr.base()), Create(ruido), run_time=self.dur(1.0), rate_func=linear)
            self.pop(ok)

            # «teorema del muestreo»
            self.en("muestreo")
            self.corte()
            self.pop(muestreo)

            # «no tiene frecuencias por encima de be»
            self.en("banda")
            self.play(Create(ejb), Create(cb), run_time=self.dur(1.0))
            self.play(FadeIn(lb1), FadeIn(lb2), run_time=0.4)

            # «más de dos be muestras por segundo»
            self.en("dosb")
            self.play(FadeIn(f2b), Create(Ls.base()), run_time=self.dur(0.6))
            self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.3) for p in puntos], lag_ratio=0.12), run_time=self.dur(1.6))

            # «reconstruirla»
            self.en("reconstruir")
            self.play(Create(curva_s), run_time=self.dur(1.2), rate_func=linear)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        E = Lienzo(ancho=5.0, alto=1.8, t_rango=(-6, 6), v_max=1.0, centro=(-3.6, 2.2))
        ej = ejes_L(E, 0, 1.05)
        cb = curva_f(E, banda_b, -6, 6, AMBAR, 5, n=240)
        lb1 = MathTex("B", color=ERROR).scale(0.8).move_to(E.p(2, 0) + [0, -0.4, 0])
        Ls = Lienzo(ancho=8.0, alto=1.9, t_rango=(0, 8), v_max=1.0, centro=(-1.4, -1.6))
        tt = np.linspace(0, 8, 240)
        v = 0.45 * np.sin(2 * np.pi * 0.28 * tt) + 0.3 * np.sin(2 * np.pi * 0.5 * tt + 1.0) + 0.15 * np.sin(2 * np.pi * 0.7 * tt + 2.0)
        proc = Ls.curva(tt, v, RUIDO, 3.5)
        ks = np.linspace(0.4, 7.6, 18)
        vk = [float(np.interp(k, tt, v)) for k in ks]
        puntos = VGroup(*[Dot(Ls.p(k, y), radius=0.09, color=AMBAR) for k, y in zip(ks, vk)])
        rec = Ls.curva(tt, v + 0.04 * np.sin(2 * np.pi * 0.9 * tt), AMBAR, 3.0)
        t_real = etiqueta("cada realización", INK, 0.6).move_to([4.6, -0.2, 0])
        x_real = cruz(ROJO, 0.5).move_to([4.6, -0.9, 0])
        ec = formula("E", r"\big[", r"(x-\hat x)^2", r"\big]", "=", "0", escala=1.0,
                     colores={2: ERROR}).move_to([4.2, 1.6, 0])
        ok = tilde(VERDE, 0.6).move_to([6.6, 1.6, 0])
        with self.narrar("b2"):
            # «Con procesos pasa lo mismo»
            self.en("procesos")
            self.corte()
            self.play(Create(Ls.base()), Create(proc), run_time=self.dur(1.2), rate_func=linear)

            # «la densidad espectral vale cero por encima de be»
            self.en("cero")
            self.play(Create(ej), Create(cb), FadeIn(lb1), run_time=self.dur(1.0))

            # «las muestras bastan»
            self.en("bastan")
            self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.3) for p in puntos], lag_ratio=0.1), run_time=self.dur(1.5))

            # «No se reconstruye cada realización»
            self.en("norecon")
            self.play(FadeIn(t_real), Create(x_real), run_time=self.dur(0.6))

            # «punto a punto»
            self.en("punto")
            self.play(Create(rec), run_time=self.dur(1.2), rate_func=linear)

            # «el error tiene potencia cero»
            self.en("error")
            self.play(FadeIn(ec), run_time=self.dur(1.0))

            # «en la práctica eso es lo mismo»
            self.en("igual")
            self.pop(ok)

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        E = Lienzo(ancho=5.0, alto=1.8, t_rango=(-6, 6), v_max=1.2, centro=(-3.0, 2.0))
        ej = ejes_L(E, 0, 1.2)
        c = curva_f(E, psd_tele, -6, 6, AMBAR, 5)
        lupa_ = lupa(TXT).scale(1.6).move_to(E.p(0, 0.7))
        t_fab = self.palabra("fabricar", AMBAR, 1.2).move_to([3.8, 2.4, 0])
        alt = altavoz(TXT).scale(1.4).move_to([-5.0, -1.2, 0])
        Ef = Lienzo(ancho=2.8, alto=1.4, t_rango=(-6, 6), v_max=1.2, centro=(-1.8, -1.2))
        cf = curva_f(Ef, lambda w: 0.2 + 0.8 * np.exp(-((np.asarray(w) - 3) / 1.5) ** 2) + 0.5 * np.exp(-((np.asarray(w) + 2) / 1.2) ** 2),
                     -6, 6, AMBAR, 4)
        ejf = ejes_L(Ef, 0, 1.2)
        ant = antena(TXT).scale(1.1).move_to([-5.0, -1.2, 0])
        proc = caja("proceso", RUIDO, ancho=2.0, alto=0.9, scale=0.6).move_to([3.0, -1.2, 0])
        flecha_p = flecha([-0.2, -1.2, 0], [1.9, -1.2, 0], INK, 3)
        cf2 = curva_f(Ef, lambda w: 0.9 - 0.7 * np.exp(-((np.asarray(w)) / 2.2) ** 2) + 0.2 * np.sin(np.asarray(w)) ** 2,
                      -6, 6, AMBAR, 4)
        preg = etiqueta("¿cómo fabrico un ruido con este espectro?", TXT, 0.6).move_to([0, -3.3, 0])
        with self.narrar("b3"):
            # «usado el espectro para mirar»
            self.en("mirar")
            self.corte()
            self.play(Create(ej), Create(c), run_time=self.dur(0.8))
            self.play(FadeIn(lupa_), run_time=0.4)

            # «También sirve para fabricar»
            self.en("fabricar")
            self.play(FadeOut(lupa_), run_time=0.3)
            self.pop(t_fab)

            # «probar un altavoz»
            self.en("altavoz")
            self.play(FadeIn(alt), run_time=self.dur(0.6))

            # «un ruido de una forma concreta»
            self.en("forma")
            self.play(Create(ejf), Create(cf), run_time=self.dur(0.9))

            # «el ruido de un canal de comunicaciones»
            self.en("canal")
            self.play(FadeOut(alt), FadeIn(ant), run_time=self.dur(0.7))

            # «necesitas generar un proceso»
            self.en("generar")
            self.play(GrowArrow(flecha_p), FadeIn(proc), run_time=self.dur(0.7))

            # «la densidad espectral que tú elijas»
            self.en("elijas")
            self.play(ReplacementTransform(cf, cf2), run_time=self.dur(1.2))

            # «¿Cómo se consigue?»
            self.en("como")
            self.pop(preg)
