"""Escena 04 — El espectro y el colador: barras, ganancia; la voz y el ruido en el eje; la pregunta."""
from comun.escena import *


class ElEspectroYElColador(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        barras = BarrasF([2, 5], [0.85, 0.7], f_max=7, ancho=5.6, alto=1.8, centro=(-3.2, 1.3),
                         rotulos=["2 Hz", "5 Hz"])
        Ls = Lienzo(ancho=5.6, alto=1.5, t_rango=(0, 1), v_max=2.2, centro=(-3.2, -2.3))
        t = np.linspace(0, 1, 260)
        suma = Ls.curva(t, np.sin(2 * np.pi * 2 * t) + np.sin(2 * np.pi * 5 * t), SENAL, 3.2)
        lento = seno_t(Ls, 2, 1.0, SENAL)
        col = colador(CIAN, 2.0, 1.6).move_to([3.7, 1.2, 0])
        g = [etiqueta("× 1", TXT, 0.55).move_to(barras.puntas[0].get_center() + UP * 0.4),
             etiqueta("× 1", TXT, 0.55).move_to(barras.puntas[1].get_center() + UP * 0.4)]
        with self.narrar("b1"):
            # «cuánto hay de cada frecuencia»
            self.en("cuanto")
            self.play(Create(barras.base), Create(Ls.base()), Create(suma), run_time=self.dur(0.6))
            self.play(*[Create(b) for b in barras.barras], *[FadeIn(p) for p in barras.puntas],
                      FadeIn(barras.rot), run_time=self.dur(0.6))

            # «el espectro»
            self.en("espectro")
            pal = self.palabra("espectro", AMBAR, 0.9).move_to([-3.2, 3.4, 0])
            self.pop(pal)

            # «dos barras»
            self.en("dosbarras")
            self.play(*[p.animate(rate_func=there_and_back).scale(1.8) for p in barras.puntas], run_time=0.6)

            # «Y un filtro actúa»
            self.en("filtro")
            self.play(FadeIn(col, scale=0.7), run_time=self.dur(0.5))
            lf = etiqueta("filtro", CIAN, 0.55).move_to([3.7, 0.0, 0])
            self.play(FadeIn(lf), run_time=0.3)

            # «multiplica cada barra por un número»
            self.en("multiplica")
            self.play(LaggedStart(*[FadeIn(x, shift=DOWN * 0.15) for x in g], lag_ratio=0.3), run_time=self.dur(0.8))

            # «su ganancia»
            self.en("ganancia")
            gl = etiqueta("ganancia", INK, 0.5).move_to([-3.2, 2.85, 0])
            self.pop(gl)

            # «cinco hercios es cero»
            self.en("cero")
            cero = etiqueta("× 0", ROJO, 0.55).move_to(g[1])
            self.play(ReplacementTransform(g[1], cero), run_time=self.dur(0.5))

            # «esa barra desaparece»
            self.en("desaparece")
            p0 = barras.barras[1].get_start()
            self.play(barras.barras[1].animate.put_start_and_end_on(p0, p0 + UP * 0.01),
                      barras.puntas[1].animate.move_to(p0), run_time=self.dur(0.7))
            self.play(FadeOut(barras.puntas[1]), run_time=0.2)

            # «queda solo el seno lento»
            self.en("solo_lento")
            self.play(ReplacementTransform(suma, lento), run_time=self.dur(1.0))

            # «Eso es el colador»
            self.en("colador")
            self.resaltar(col, color=CIAN)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        x = np.linspace(-1.9, 1.9, 80)
        bulto_v = traza(-1.4 + x / 1.9 * 1.3, -0.6 + 1.6 * np.exp(-0.5 * (x / 0.9) ** 2), AZUL, 4)
        bulto_m = traza(4.4 + x / 1.9 * 1.3, -0.6 + 1.3 * np.exp(-0.5 * (x / 0.9) ** 2), MAGENTA, 4)
        eje = Arrow([-6.6, -0.6, 0], [6.8, -0.6, 0], color=INK, stroke_width=2.5, buff=0,
                    max_tip_length_to_length_ratio=0.03)
        pers = persona(AZUL).scale(1.2).move_to([-5.7, 1.4, 0])
        tick1 = Line([-3.4, -0.7, 0], [-3.4, -0.5, 0], color=INK, stroke_width=3)
        tick2 = Line([0.6, -0.7, 0], [0.6, -0.5, 0], color=INK, stroke_width=3)
        r1 = etiqueta("300 Hz", INK, 0.5).move_to([-3.4, -1.05, 0])
        r2 = etiqueta("3.000 Hz", INK, 0.5).move_to([0.6, -1.05, 0])
        col = colador(CIAN, 1.1, 0.85).move_to([-1.4, 2.8, 0])
        banda = Rectangle(width=4.0, height=2.5, color=CIAN, stroke_width=2.5).set_fill(CIAN, 0.1)
        banda.move_to([-1.4, 0.65, 0])
        with self.narrar("b2"):
            # «Con la voz»
            self.en("voz")
            self.corte()
            self.play(FadeIn(pers), Create(eje), run_time=self.dur(0.6))

            # «un bulto»
            self.en("bulto")
            self.play(Create(bulto_v), run_time=self.dur(0.9), rate_func=linear)

            # «entre unos cientos y unos miles de hercios»
            self.en("rango")
            self.play(Create(tick1), Create(tick2), FadeIn(r1), FadeIn(r2), run_time=self.dur(0.7))

            # «Si el murmullo vive»
            self.en("murmullo")
            lm = self.palabra("murmullo", MAGENTA, 0.7).move_to([4.4, 1.5, 0])
            self.pop(lm)

            # «otras frecuencias»
            self.en("otras")
            self.play(Create(bulto_m), run_time=self.dur(0.8), rate_func=linear)

            # «el colador los separa»
            self.en("separa")
            self.play(FadeIn(col, scale=0.7), FadeIn(banda), run_time=self.dur(0.6))
            self.play(bulto_m.animate.set_stroke(opacity=0.25), lm.animate.set_opacity(0.3), run_time=self.dur(0.5))

            # «en las mismas»
            self.en("mismas")
            self.play(bulto_m.animate.shift(LEFT * 5.8).set_stroke(opacity=1),
                      lm.animate.shift(LEFT * 5.8).set_opacity(1), run_time=self.dur(1.0))

            # «no hay colador que valga»
            self.en("novale")
            self.play(Create(tachar(col)), run_time=0.4)
            self.sfx("error")

            # «Todo depende»
            self.en("depende")
            q = self.palabra("?", AMBAR, 1.4).move_to([1.9, 0.9, 0])
            self.pop(q)

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        preg = self.texto_centrado("¿Cómo calcularías el espectro", "de un ruido?", escala=0.75).move_to([0, 2.9, 0])
        L = Lienzo(ancho=3.6, alto=1.2, t_rango=(0, 3), v_max=1.0, centro=(-4.6, -1.8))
        ruido = ruido_t(L, semilla=12, amp=0.4)
        cf = caja("Fourier", AZUL, ancho=1.9, alto=0.9).move_to([0.0, -1.8, 0])
        with self.narrar("b3"):
            # «¿cómo calcularías el espectro de un ruido?»
            self.en("pregunta")
            self.corte()
            self.pop(preg)

            # «Piénsalo un momento»
            self.en("pausa")
            rel = reloj_arena(TXT).scale(1.3).move_to([0, 0.5, 0])
            self.play(FadeIn(rel), run_time=self.dur(0.4))
            self.play(Rotate(rel, angle=PI, about_point=rel.get_center()), run_time=self.dur(1.5))

            # «La respuesta obvia»
            self.en("obvia")
            self.play(FadeOut(rel), run_time=0.3)
            ob = self.palabra("respuesta obvia", AMBAR, 0.75).move_to([0, 0.5, 0])
            self.pop(ob)

            # «grabarlo»
            self.en("grabar")
            self.play(Create(L.base()), Create(ruido), run_time=self.dur(0.6), rate_func=linear)

            # «aplicarle Fourier»
            self.en("aplicar")
            a1 = flecha([-2.6, -1.8, 0], [-1.05, -1.8, 0])
            self.play(GrowArrow(a1), FadeIn(cf), run_time=self.dur(0.5))

            # «Parece fácil»
            self.en("facil")
            ti = tilde(VERDE, 0.9).move_to([2.2, -1.8, 0])
            self.play(Create(ti), run_time=0.4)

            # «No funciona»
            self.en("nofunciona")
            x = cruz(ROJO, 1.0).move_to([2.2, -1.8, 0])
            self.play(ReplacementTransform(ti, x), run_time=0.4)
            self.sfx("error")

            # «la mitad de este capítulo»
            self.en("mitad")
            pq = self.palabra("¿por qué?", AMBAR, 0.9).move_to([0, -3.4, 0])
            self.pop(pq)
