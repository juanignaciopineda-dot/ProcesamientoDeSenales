"""Escena 18 — La receta para detectar, en cinco pasos, con sus variantes."""
from comun.escena import *

YS = [2.5, 1.4, 0.3, -0.8, -1.9]
TXT_PASOS = ["1 · señal y ruido", "2 · blanquear", "3 · filtro adaptado", "4 · muestrear en el pico", "5 · umbral"]
COL = [TXT, CIAN, AMBAR, AMBAR, AMBAR]


class LaReceta(EscenaCurso):
    ESCENA = "18"

    def construct(self):
        cuaderno = RoundedRectangle(corner_radius=0.2, width=6.4, height=6.0, color=INK, stroke_width=2,
                                    stroke_opacity=0.6).move_to([-3.4, 0.3, 0])
        receta = etiqueta("receta", AMBAR, 0.8, BOLD).move_to([-3.4, 3.65, 0])
        pasos = [caja(TXT_PASOS[i], COL[i], ancho=5.4, alto=0.8, scale=0.55).move_to([-3.4, YS[i], 0]) for i in range(5)]
        etq_s = etiqueta("señal", SENAL, 0.5, BOLD).move_to([1.2, 2.8, 0])
        etq_r = etiqueta("ruido", RUIDO, 0.5, BOLD).move_to([2.6, 2.8, 0])
        Lm = Lienzo(ancho=3.6, alto=0.9, t_rango=(0, 80), v_max=2.0, centro=(4.6, 1.4))
        mem = Lm.curva(np.arange(80), serie(9, 80, 0.9), RUIDO, 3)
        prior = etiqueta("prior", AMBAR, 0.6, BOLD).move_to([1.6, -1.2, 0])
        fa = MathTex(r"P_{FA}\ \text{tolerada}", color=ERROR).scale(0.9).move_to([4.6, -1.2, 0])
        # variante: no sé cuándo llega → la salida tiene un pico
        Lp = Lienzo(ancho=4.6, alto=1.5, t_rango=(0, 8), v_max=1.0, centro=(3.7, -3.3))
        vals = np.array([0.1, 0.15, 0.1, 0.2, 0.15, 0.55, 1.0, 0.45, 0.15, 0.1, 0.12, 0.08])
        tt = np.linspace(0.3, 7.7, len(vals))
        pico = Lp.curva(tt, vals, SENAL, 4)
        base = Lp.base()
        etq_cuando = etiqueta("¿cuándo llega?", INK, 0.45).move_to([5.3, -2.1, 0])
        maxi = MathTex(r"\max", color=AMBAR).scale(0.9).move_to([Lp.x(tt[6]), Lp.y(1.0) + 0.4, 0])
        umb = DashedLine(Lp.p(0.0, 0.55), Lp.p(8.0, 0.55), color=ERROR, stroke_width=3)
        umb_alto = DashedLine(Lp.p(0.0, 0.85), Lp.p(8.0, 0.85), color=ERROR, stroke_width=3)
        with self.narrar("b1"):
            # «Si tuvieras que resolver un problema real»
            self.paso("problema", cuaderno, t=0.6)
            # «la receta es esta»
            self.paso("receta", receta, t=0.5)
            # «Identifica qué es señal y qué es ruido»
            self.en("paso1")
            self.play(FadeIn(pasos[0]), FadeIn(etq_s), FadeIn(etq_r), run_time=self.dur(0.7))
            # «Si el ruido tiene memoria»
            self.paso("memoria", Create(mem), t=0.8)
            # «blanquéalo»
            self.paso("paso2", pasos[1], t=0.6)
            # «Correlaciona con la señal»
            self.paso("paso3", pasos[2], t=0.6)
            # «con un filtro adaptado»
            self.en("adaptado")
            self.resaltar(pasos[2], color=AMBAR, run_time=0.5)
            # «Muestrea en el pico»
            self.paso("paso4", pasos[3], t=0.6)
            # «Compara con un umbral»
            self.paso("paso5", pasos[4], t=0.6)
            # «la probabilidad a priori»
            self.paso("prior", prior, t=0.5)
            # «una falsa alarma tolerada»
            self.paso("fa", fa, t=0.6)
            # «Y si no sabes cuándo llega»
            self.en("cuando")
            self.play(FadeIn(etq_cuando), FadeIn(base), Create(pico), run_time=self.dur(0.9))
            # «usa el máximo»
            self.paso("maximo", maxi, t=0.5)
            # «sube el umbral»
            self.en("sube")
            self.play(Create(umb), run_time=0.3)
            self.play(Transform(umb, umb_alto), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
