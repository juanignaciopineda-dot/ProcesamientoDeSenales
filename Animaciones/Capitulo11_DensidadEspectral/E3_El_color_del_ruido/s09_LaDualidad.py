"""Escena 09 — Memoria corta, espectro ancho: la dualidad de Fourier y el espectro de líneas."""
from comun.escena import *


class LaDualidad(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.regla()
        self.extremo()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def regla(self):
        p = ParAlfa(alfa=1.0, c_auto=(-3.6, -0.6), c_esp=(3.9, -2.4))
        auto, espec, area = p.auto(), p.espec(), p.area_espec()
        base = p.L.base()
        desl = p.deslizador(centro=(-3.6, -3.55))
        self.add(base, auto, p.esp.ejes, area, espec, desl)
        with self.narrar("b1"):
            # «el área no cambia»
            self.en("area")
            self.play(p.a.animate.set_value(6.0), run_time=self.dur(2.2))
            # «la potencia sigue siendo uno»
            self.en("potuno")
            pot = MathTex(r"\text{potencia} = 1", color=AMBAR).scale(0.85).move_to([3.9, 1.5, 0])
            self.play(FadeIn(pot), run_time=self.dur(0.5))
            # «pierde en altura»
            self.en("altura")
            fl = Arrow(p.esp.p(-2.2, 1.0), p.esp.p(-2.2, 0.3), buff=0, color=ROJO, stroke_width=6)
            self.play(GrowArrow(fl), run_time=self.dur(0.4))
            # «lo gana en anchura»
            self.en("anchura")
            dobl = DoubleArrow(p.esp.p(-9, 0.55), p.esp.p(9, 0.55), buff=0, color=VERDE, stroke_width=5)
            self.play(GrowFromCenter(dobl), FadeOut(fl), run_time=self.dur(0.5))
            # «memoria corta, espectro ancho»
            self.en("corta")
            tc = Text("memoria corta ↔ espectro ancho", color=AMBAR, weight=BOLD).scale(0.55).move_to([0, 3.4, 0])
            self.play(FadeIn(tc), run_time=self.dur(0.5))
            # «memoria larga, espectro estrecho»
            self.en("larga")
            tl = Text("memoria larga ↔ espectro estrecho", color=VERDE, weight=BOLD).scale(0.55).move_to([0, 2.8, 0])
            self.play(FadeOut(dobl), p.a.animate.set_value(0.6), FadeIn(tl), run_time=self.dur(1.2))
            # «la dualidad de Fourier»
            self.en("dual")
            self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=0.3)
            td = Text("tiempo", color=SENAL, weight=BOLD).scale(0.8).move_to([-3.5, 2.4, 0])
            fr = Text("frecuencia", color=AMBAR, weight=BOLD).scale(0.8).move_to([3.5, 2.4, 0])
            dob = DoubleArrow([-1.5, 2.4, 0], [1.5, 2.4, 0], buff=0, color=INK, stroke_width=5)
            self.play(FadeIn(td), FadeIn(fr), GrowFromCenter(dob), run_time=self.dur(0.6))
            # «el pulso estrecho con espectro ancho»
            self.en("pulso")
            Lt = Lienzo(ancho=4.6, alto=2.2, t_rango=(-3, 3), v_max=1.2, centro=(-3.5, -0.4))
            ts = np.linspace(-3, 3, 400)
            pul = Lt.curva(ts, np.where(np.abs(ts) < 0.25, 1.0, 0.0), SENAL, 4)
            esp = Espectro(w_max=6, y_max=1.2, ancho=4.6, alto=2.2, centro=(3.5, -1.5))
            anch = esp.curva(lambda w: 0.8 * np.exp(-(w / 3.5) ** 2), AMBAR)
            self.play(Create(Lt.base()), Create(pul), Create(esp.ejes), Create(anch), run_time=self.dur(1.0))
            # «la memoria de un proceso»
            self.en("memproc")
            auto8 = Lt.curva(ts, np.exp(-8 * np.abs(ts)), SENAL, 4)
            esp8 = esp.curva(lambda w: tele_S(w, 8.0) * 3.2, AMBAR)
            self.play(Transform(pul, auto8), Transform(anch, esp8), run_time=self.dur(0.9))
            mem = Text("la memoria de un proceso", color=TXT, weight=BOLD).scale(0.55).move_to([0, -3.4, 0])
            self.play(FadeIn(mem), run_time=self.dur(0.4))
        self.limpiar()

    # ------------------------------------------------------------ b2
    def extremo(self):
        rng = np.random.default_rng(4)
        # los dos tiempos
        La = Lienzo(ancho=5.4, alto=1.0, t_rango=(0, 2), v_max=1.3, centro=(-3.6, 2.7))
        fases = [0, 70, 150, 250]
        sinus = VGroup(*[Lienzo(ancho=5.4, alto=0.8, t_rango=(0, 2), v_max=1.3, centro=(-3.6, 2.9 - 0.85 * i)).curva(
            np.linspace(0, 2, 150), np.cos(2 * np.pi * np.linspace(0, 2, 150) + np.deg2rad(f)), SENAL, 3)
            for i, f in enumerate(fases)])
        Lc = Lienzo(ancho=5.6, alto=2.2, t_rango=(-3, 3), v_max=1.3, centro=(-3.6, -2.0))
        tt = np.linspace(-3, 3, 300)
        coseno = Lc.curva(tt, np.cos(2 * np.pi * 0.8 * tt), AMBAR, 4)
        esp = Espectro(w_max=3, y_max=1.2, ancho=5.2, alto=2.4, centro=(3.7, -1.5))
        with self.narrar("b2"):
            # «Llevémoslo al extremo»
            self.en("extremo")
            ext = Text("memoria infinita", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, 0.4, 0])
            self.pop(ext)
            # «Una sinusoide con fase al azar»
            self.en("sinus")
            self.play(FadeOut(ext), Create(sinus), run_time=self.dur(1.2), rate_func=linear)
            # «del capítulo anterior»
            self.en("cap10")
            c10 = Text("capítulo 10", color=INK).scale(0.5).move_to([0.6, 2.0, 0])
            self.play(FadeIn(c10), run_time=self.dur(0.4))
            # «un coseno que no decae nunca»
            self.en("coseno")
            self.play(Create(Lc.base()), Create(coseno), run_time=self.dur(1.3), rate_func=linear)
            # «recuerda para siempre»
            self.en("siempre")
            sie = Arrow([-5.8, -3.45, 0], [-1.4, -3.45, 0], buff=0, color=INK, stroke_width=5)
            sie_t = Text("para siempre", color=INK).scale(0.5).move_to([-3.6, -3.78, 0])
            self.play(GrowArrow(sie), FadeIn(sie_t), run_time=self.dur(0.6))
            # «dos rayas»
            self.en("rayas")
            r1, r2 = esp.flecha(-2, 1.0, AMBAR), esp.flecha(2, 1.0, AMBAR)
            self.play(Create(esp.ejes), GrowArrow(r1), GrowArrow(r2), run_time=self.dur(0.7))
            # «dos impulsos en más y menos su frecuencia»
            self.en("impulsos")
            m1 = MathTex(r"+\omega_0", color=AMBAR).scale(0.8).move_to(esp.p(2, -0.3))
            m2 = MathTex(r"-\omega_0", color=AMBAR).scale(0.8).move_to(esp.p(-2, -0.3))
            self.play(FadeIn(m1), FadeIn(m2), run_time=self.dur(0.5))
            # «Toda la potencia en dos puntos»
            self.en("dospuntos")
            h1 = MathTex(r"\tfrac{1}{2}", color=AMBAR).scale(0.8).next_to(r1, RIGHT, buff=0.15)
            h2 = MathTex(r"\tfrac{1}{2}", color=AMBAR).scale(0.8).next_to(r2, RIGHT, buff=0.15)
            self.play(FadeIn(h1), FadeIn(h2), run_time=self.dur(0.5))
            # «espectro de líneas»
            self.en("lineas")
            li = Text("espectro de líneas", color=VERDE, weight=BOLD).scale(0.65).move_to([3.7, 1.9, 0])
            self.pop(li)
