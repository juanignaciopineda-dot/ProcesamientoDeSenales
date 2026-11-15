"""Escena 12 — Un colador ideal de frecuencias; la simetría del espectro de una señal real."""
from comun.escena import *


class ElColadorIdeal(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        c = Curva(psd_tele, x_rango=(-6, 6), y_max=1.2, ancho=8.4, alto=3.4, color=AMBAR, x_label=r"\omega") \
            .move_to([0, -0.5, 0])
        ax = c.ejes

        def ventana(a, b, color=CIAN):
            x0, x1 = ax.c2p(a, 0)[0], ax.c2p(b, 0)[0]
            r = Rectangle(width=x1 - x0, height=3.0, color=color, stroke_width=2.5).set_fill(color, 0.12)
            r.move_to([(x0 + x1) / 2, ax.c2p(0, 0)[1] + 1.5, 0])
            r.permitir_encima = True
            return r

        dens = self.palabra("¿densidad?", AMBAR, 0.8).move_to([0, 3.4, 0])
        with self.narrar("b1"):
            # «no basta para llamar densidad»
            self.en("nobasta")
            self.play(Create(ax), FadeIn(c.etiquetas), Create(c.grafica), run_time=self.dur(1.2))
            self.pop(dens)

            # «Queremos más»
            self.en("mas")
            self.resaltar(dens, color=AMBAR)

            # «cada trozo de área»
            self.en("trozo")
            tr = c.area(1.0, 2.0, AMBAR, 0.5)
            self.play(FadeIn(tr), run_time=self.dur(0.5))

            # «la potencia de ese trozo de frecuencias»
            self.en("potrozo")
            lt = etiqueta("potencia de esta banda", AMBAR, 0.5).move_to([4.2, 2.0, 0])
            at = flecha([3.2, 1.75, 0], list(ax.c2p(1.7, 0.55)), AMBAR, 3)
            self.play(FadeIn(lt), GrowArrow(at), run_time=self.dur(0.6))

            # «Para comprobarlo»
            self.en("comprobar")
            lupa_ = lupa()
            lupa_.permitir_encima = True
            lupa_.scale(0.9).move_to(ax.c2p(1.5, 0.9))
            self.play(FadeIn(lupa_, scale=0.7), run_time=0.4)

            # «un colador ideal»
            self.en("ideal")
            v1 = ventana(0.5, 2.5)
            self.play(FadeOut(lupa_), FadeIn(v1), FadeOut(lt), FadeOut(at), run_time=self.dur(0.6))
            lc = etiqueta("colador ideal", CIAN, 0.55).move_to([-3.6, 2.6, 0])
            self.pop(lc)

            # «una franja estrecha»
            self.en("franja")
            v2 = ventana(1.2, 1.8)
            self.play(Transform(v1, v2), run_time=self.dur(0.8))

            # «omega cero»
            self.en("w0")
            w0 = formula(r"\omega_0", escala=0.9, colores={0: CIAN}).move_to(ax.c2p(1.5, 0) + DOWN * 0.45)
            self.pop(w0)

            # «borra todo lo demás»
            self.en("borra")
            self.play(c.grafica.animate.set_stroke(opacity=0.2), FadeOut(lc), run_time=self.dur(0.6))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        Ls = Lienzo(ancho=8.0, alto=1.3, t_rango=(0, 1), v_max=1.3, centro=(0, 2.7))
        seno = seno_t(Ls, 5, 1.0, SENAL)
        barras = BarrasF([-5, 5], [0.9, 0.9], f_max=8, ancho=11.0, alto=2.0, centro=(0, -1.3), simetrico=True)
        eje = barras.base
        simetria = DashedLine([0, -2.4, 0], [0, 0.0, 0], color=AMBAR, stroke_width=3)
        pm5 = [etiqueta("−5", INK, 0.5).move_to([barras.x(-5), -2.7, 0]),
               etiqueta("+5", INK, 0.5).move_to([barras.x(5), -2.7, 0])]
        y0 = -2.3

        def ventana_f(f0, color=CIAN):
            r = Rectangle(width=1.1, height=2.0, color=color, stroke_width=2.5).set_fill(color, 0.12)
            r.move_to([barras.x(f0), y0 + 1.0, 0])
            return r

        with self.narrar("b2"):
            # «el espectro de una señal real es simétrico»
            self.en("simetrico")
            self.corte()
            self.play(Create(eje), Create(simetria), run_time=self.dur(1.2))

            # «Un seno de cinco hercios»
            self.en("seno5")
            self.play(Create(Ls.base()), Create(seno), run_time=self.dur(1.0), rate_func=linear)

            # «dos barras»
            self.en("barras")
            self.play(*[Create(b) for b in barras.barras], *[FadeIn(p) for p in barras.puntas], run_time=self.dur(0.7))

            # «en más cinco y en menos cinco»
            self.en("pm5")
            self.play(*[FadeIn(p) for p in pm5], run_time=self.dur(0.6))

            # «el colador también tiene que ser simétrico»
            self.en("colsim")
            cs = etiqueta("el colador también es simétrico", CIAN, 0.6).move_to([0, 1.0, 0])
            self.pop(cs)

            # «una ventanita en más omega cero»
            self.en("vpos")
            vp = ventana_f(2.0)
            lp = formula(r"+\omega_0", escala=0.8, colores={0: CIAN}).move_to([barras.x(2.0), -2.85, 0])
            self.play(FadeIn(vp), FadeIn(lp), run_time=self.dur(0.6))

            # «su reflejo en menos omega cero»
            self.en("vneg")
            vn = ventana_f(-2.0)
            ln = formula(r"-\omega_0", escala=0.8, colores={0: CIAN}).move_to([barras.x(-2.0), -2.85, 0])
            self.play(FadeIn(vn), FadeIn(ln), run_time=self.dur(0.6))
