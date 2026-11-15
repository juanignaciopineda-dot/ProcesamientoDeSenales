"""Escena 15 — PeroNoEsAutomatico: ergódico se suele suponer, pero hay procesos estacionarios donde una grabación no dice nada."""
from comun.escena import *


class PeroNoEsAutomatico(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        L = Lienzo(ancho=10.0, alto=3.2, t_rango=(0, 8), v_max=2.0, centro=(0, 0.3))
        t = np.linspace(0, 8, 260)
        larga = L.curva(t, 0.6 * serie(41, 260, 0.96), SENAL, 4.5)
        pila = pila_de_curvas(Lienzo(ancho=10.0, alto=3.2, t_rango=(0, 8), v_max=2.0, centro=(0, 0.3)), 10,
                              semilla=9, a=0.95, puntos=200, opacidad=0.4, ancho=2.2, escala=0.6)
        base = L.base()
        llana = L.curva(t, 0.45 + 0 * t, SENAL, 4.5)
        term = termometro().scale(0.9).move_to([-6.2, 2.9, 0])
        se_suele = sello("se suele suponer", AMBAR).scale(0.9).move_to([0, 3.2, 0])
        pruebas = etiqueta("salvo pruebas en contra", INK, 0.6).move_to([0, -2.9, 0])
        pero = etiqueta("pero…", ROJO, 1.2, BOLD).move_to([0, 3.2, 0])
        estac = sello("estacionario", VERDE).scale(0.9).move_to([-4.4, 3.2, 0])
        largar = Arrow(L.p(0, -1.55), L.p(8, -1.55), color=VERDE, buff=0, stroke_width=5)

        with self.narrar("b1"):
            # «una grabación larga»
            self.en("larga")
            self.play(Create(base), Create(larga), run_time=self.dur(1.6), rate_func=linear)

            # «el ensemble entero»
            self.en("entero")
            self.play(LaggedStart(*[FadeIn(c) for c in pila], lag_ratio=0.05), run_time=self.dur(1.2))

            # «datos reales»
            self.en("reales")
            self.pop(term)

            # «se suele dar por supuesto»
            self.en("supuesto")
            self.pop(se_suele, sonido="impacto")

            # «pruebas en contra»
            self.en("pruebas")
            self.play(FadeIn(pruebas), run_time=0.5)

            # «no es automático»
            self.en("noauto")
            self.play(FadeOut(se_suele, shift=DOWN * 0.3), run_time=0.3)
            self.pop(pero, sonido="error")

            # «perfectamente estacionarios»
            self.en("estac")
            self.play(*[c.animate.set_stroke(opacity=0.0) for c in pila], run_time=0.4)
            self.pop(estac, sonido="impacto")

            # «por larga que sea»
            self.en("sea")
            self.play(Create(largar), run_time=self.dur(1.6))

            # «no dice casi nada»
            self.en("nada")
            self.play(ReplacementTransform(larga, llana), run_time=self.dur(1.0))
        self.wait(1.0)
        self.limpiar()
