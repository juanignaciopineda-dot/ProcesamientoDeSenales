"""Escena 18 — Cierre: repaso del capítulo y el título del siguiente, «¿Cuál es el mejor filtro?»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "18"

    def construct(self):
        c = Curva(psd_tele, x_rango=(-6, 6), y_max=1.2, ancho=3.8, alto=1.9, color=AMBAR, x_label=r"\omega") \
            .move_to([-4.6, 1.9, 0])
        n1 = formula(r"S_{xx}(j\omega)", escala=0.8, colores={0: AMBAR}).move_to([-4.6, 0.2, 0])
        fz = flecha_c([-0.4, 1.5, 0], 1.3, 35, AMBAR, ancho=6)
        n2 = formula(r"S_{yx}(j\omega)", escala=0.8, colores={0: AMBAR}).move_to([0.2, 0.2, 0])
        l_c = etiqueta("cuánto comparten", INK, 0.5).move_to([0.2, -0.5, 0])
        gam = formula(r"\gamma_{yx}", escala=1.1, colores={0: AMBAR}).move_to([4.4, 2.6, 0])
        L = Lienzo(ancho=3.6, alto=1.3, t_rango=(0, 1), v_max=1.0, centro=(4.6, 1.2))
        f = lambda u: 0.15 + 0.7 * np.exp(-((u - 0.3) / 0.1) ** 2) + 0.45 * np.exp(-((u - 0.75) / 0.12) ** 2)
        rho_c = curva_f(L, f, 0, 1, AMBAR, 4.0)
        rho_l = formula(r"\rho(\omega)", escala=0.8, colores={0: AMBAR}).move_to([4.6, 0.2, 0])
        col = colador(CIAN, 1.6, 1.3).move_to([-1.0, -1.5, 0])
        q = self.palabra("?", AMBAR, 1.4).move_to([1.0, -1.5, 0])
        tit = self.palabra("¿Cuál es el mejor filtro?", AMBAR, 0.85).move_to([0.0, -3.2, 0])
        cap = etiqueta("Capítulo 12", INK, 0.6).move_to([-5.4, -3.2, 0])
        with self.narrar("b1"):
            # «la densidad espectral»
            self.en("psd")
            self.play(Create(c.ejes), FadeIn(c.etiquetas), Create(c.grafica), FadeIn(n1), run_time=self.dur(1.0))

            # «dónde vive la potencia»
            self.en("donde")
            self.play(FadeIn(c.area(-6, 6, AMBAR, 0.35)), run_time=self.dur(0.6))

            # «la cruzada»
            self.en("cruzada")
            self.play(GrowArrow(fz), FadeIn(n2), run_time=self.dur(0.6))

            # «cuánto comparten dos señales»
            self.en("comparten")
            self.play(FadeIn(l_c), run_time=self.dur(0.4))

            # «la coherencia»
            self.en("coh")
            self.pop(gam)

            # «un rho por frecuencia»
            self.en("rho")
            self.play(Create(L.base()), Create(rho_c), FadeIn(rho_l), run_time=self.dur(1.0))

            # «la pregunta de fondo»
            self.en("pregunta")
            self.play(FadeIn(col, scale=0.7), run_time=self.dur(0.5))
            self.pop(q)

            # «cuál es el mejor filtro»
            self.en("titulo_c12")
            self.play(FadeIn(cap), run_time=0.3)
            self.pop(tit)

        self.wait(1.0)
        self.limpiar()
