"""Escena 16 — Cuándo usar cada versión: filtrar en tiempo real, predecir para adelantarse, suavizar con la grabación."""
from comun.escena import *


class CuandoUsarCada(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        rel = reloj().scale(1.5).move_to([0, 3.0, 0])
        cr = colador(CIAN, 1.6, 1.3).move_to([-4.5, 1.1, 0])
        Lc = Lienzo(ancho=2.8, alto=0.9, t_rango=(0, 1), v_max=1.5, centro=(-4.5, -0.4))
        t = np.linspace(0, 1, 80)
        ruidosa = Lc.curva(t, 0.8 * serie(23, 80, 0.5), MEDIDA, 3)
        base_c = Lc.base()
        t_fil = self.palabra("filtrar", VERDE, 0.8).move_to([-4.5, -1.6, 0])
        v_l = etiqueta("en tiempo real", INK, 0.5).move_to([-4.5, -2.3, 0])

        sal = Arrow([-1.3, 1.2, 0], [1.3, 1.2, 0], color=AMBAR, buff=0, stroke_width=7, max_tip_length_to_length_ratio=0.15)
        ctrl = engranaje(INK).scale(0.9).move_to([0, -0.1, 0])
        t_pre = self.palabra("predecir", AMBAR, 0.8).move_to([0, -1.6, 0])
        p_l = etiqueta("antes de que pase", INK, 0.5).move_to([0, -2.3, 0])

        gr = disco(INK).scale(1.1).move_to([4.5, 1.1, 0])
        esp = reloj_arena().scale(1.0).move_to([4.5, -0.2, 0])
        t_sua = self.palabra("suavizar", VERDE, 0.8).move_to([4.5, -1.6, 0])
        mej = formula(r"0{,}686", escala=0.9, colores={0: VERDE}).move_to([4.5, -2.6, 0])
        marco = SurroundingRectangle(mej, color=VERDE, buff=0.18, stroke_width=3.5)

        with self.narrar("b1"):
            # «cuándo necesitas la respuesta»
            self.en("cuando")
            self.corte()
            self.play(FadeIn(rel, scale=0.7), run_time=self.dur(0.6))

            # «Si limpias una señal»
            self.en("limpias")
            self.play(FadeIn(cr, scale=0.7), run_time=self.dur(0.5))

            # «a medida que llega»
            self.en("llega")
            self.play(Create(base_c), Create(ruidosa), run_time=self.dur(1.2))

            # «en tiempo real, filtras»
            self.en("filtras")
            self.pop(t_fil)
            self.play(FadeIn(v_l), run_time=self.dur(0.3))

            # «adelantarte»
            self.en("adelantar")
            self.play(GrowArrow(sal), run_time=self.dur(0.6))

            # «un control que actúa»
            self.en("control")
            self.play(FadeIn(ctrl, scale=0.7), run_time=self.dur(0.5))
            self.play(Rotate(ctrl, angle=PI / 3), run_time=self.dur(0.6))

            # «predices»
            self.en("predices")
            self.pop(t_pre)
            self.play(FadeIn(p_l), run_time=self.dur(0.3))

            # «la grabación entera»
            self.en("grab")
            self.play(FadeIn(gr, scale=0.7), run_time=self.dur(0.5))

            # «puedes esperar»
            self.en("espera")
            self.play(FadeIn(esp, scale=0.7), run_time=self.dur(0.4))

            # «suavizas»
            self.en("suavizas")
            self.pop(t_sua)

            # «lo mejor que se puede hacer»
            self.en("mejor")
            self.play(FadeIn(mej), Create(marco), run_time=self.dur(0.6))

        self.wait(1.0)
        self.limpiar()
