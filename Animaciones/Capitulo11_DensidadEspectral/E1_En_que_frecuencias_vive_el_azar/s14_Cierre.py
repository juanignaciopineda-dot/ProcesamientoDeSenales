"""Escena 14 — Cierre: resumen y el episodio siguiente («Lo que un espectro no puede hacer»)."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        L = Lienzo(ancho=4.0, alto=1.5, t_rango=(0, 4), v_max=1.0, centro=(-4.4, 2.2))
        ruido = ruido_t(L, semilla=7, amp=0.4)
        caos = espectro_ruidoso(centro=(-4.4, 0.5), ancho=3.6, alto=1.0, semilla=9, color=AZUL)
        c = Curva(psd_tele, x_rango=(-6, 6), y_max=1.2, ancho=5.2, alto=2.4, color=AMBAR, x_label=r"\omega") \
            .move_to([3.9, 1.9, 0])
        R = formula("R_{xx}(\\tau)", escala=1.0, colores={0: AZUL}).move_to([-2.8, -2.5, 0])
        S = formula("S_{xx}(j\\omega)", escala=1.0, colores={0: AMBAR}).move_to([2.8, -2.5, 0])
        with self.narrar("b1"):
            # «El ruido no tiene espectro»
            self.en("sin")
            self.play(Create(L.base()), Create(ruido), run_time=self.dur(0.8), rate_func=linear)
            self.play(Create(caos), run_time=self.dur(0.6), rate_func=linear)
            self.play(Create(tachar(caos)), run_time=0.3)
            self.sfx("error")

            # «su potencia esperada sí»
            self.en("potesp")
            self.play(Create(c.ejes), FadeIn(c.etiquetas), Create(c.grafica), run_time=self.dur(1.0))

            # «la transformada de la autocorrelación»
            self.en("transf")
            a = flecha([-1.7, -2.5, 0], [1.7, -2.5, 0])
            tr = etiqueta("transformada", INK, 0.5).move_to([0, -2.0, 0])
            self.play(FadeIn(R), GrowArrow(a), FadeIn(tr), FadeIn(S), run_time=self.dur(1.2))

            # «y su área sobre una banda»
            self.en("area")
            ba = c.area(0.8, 2.2, AMBAR, 0.55)
            self.play(FadeIn(ba), run_time=self.dur(0.6))

            # «la potencia que hay en ella»
            self.en("banda")
            self.resaltar(ba, color=AMBAR)

            # «Pero no vale cualquier curva»
            self.en("cualquiera")
            dip = c.ejes.plot(lambda w: -0.32 * np.exp(-((w - 3.0) / 0.9) ** 2), x_range=[1.6, 4.4, 0.05],
                              color=INK, stroke_width=4)
            self.play(Create(dip), run_time=self.dur(0.8))

            # «la potencia no puede ser negativa»
            self.en("negativa")
            neg = c.ejes.get_area(dip, x_range=[1.6, 4.4], color=ROJO, opacity=0.6)
            self.play(dip.animate.set_color(ROJO), FadeIn(neg), run_time=self.dur(0.7))

            # «Y eso prohíbe cosas»
            self.en("prohibe")
            sl = sello("prohibido", ROJO).move_to([4.2, -0.7, 0])
            self.pop(sl, sonido="impacto")

            # «En el próximo episodio»
            self.en("proximo")
            pr = etiqueta("próximo episodio", INK, 0.55).move_to([0, -3.35, 0])
            self.play(FadeIn(pr), run_time=self.dur(0.4))

            # «lo que un espectro no puede hacer»
            self.en("titulo_e2")
            t2 = self.palabra("Lo que un espectro no puede hacer", AMBAR, 0.62).move_to([0, -3.35, 0])
            self.play(FadeOut(pr), run_time=0.2)
            self.pop(t2)

        self.wait(1.0)
        self.limpiar()
