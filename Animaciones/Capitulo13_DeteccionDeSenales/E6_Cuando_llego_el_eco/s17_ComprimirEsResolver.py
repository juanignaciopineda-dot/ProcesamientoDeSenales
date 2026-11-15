"""Escena 17 — Comprimir es resolver; y para solo detectar con ruido blanco da igual la forma."""
from comun.escena import *


def _tri(x, c=0.0):
    return np.clip(13 - np.abs(x - c), 0, None)


class ComprimirEsResolver(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        # figuras de las escenas anteriores, en miniatura
        L = Lienzo(ancho=5.0, alto=1.8, t_rango=(-14, 17), v_max=26, centro=(-3.6, 0.5))
        rect = curva_f(L, lambda x: _tri(x, 0.0) + _tri(x, 3.0), -14, 17, VERDE, 4.0, n=200)
        rbase = L.base()
        a = autocorr13(BARKER13)
        s = np.zeros(28)
        s[0:25] += a
        s[3:28] += a
        bark = Tallos([float(v) for v in s], centro=(3.6, -0.4), paso=0.17, unidad=0.1, color=AMBAR)
        lr = Text("rectangular", color=TXT).scale(0.5).move_to([-3.6, 2.0, 0])
        lb = Text("Barker", color=TXT).scale(0.5).move_to([3.6, 2.0, 0])
        mes = Text("1 ó 2", color=ERROR, weight=BOLD).scale(0.5).move_to([-3.6, -1.3, 0])
        dos = Text("2", color=VERDE, weight=BOLD).scale(0.5).move_to([3.6, -1.3, 0])
        cp = Text("compresión de pulso", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, 3.4, 0])
        pre = Text("precisión del retardo", color=INK).scale(0.65).move_to([-3.4, -2.3, 0])
        tpre = tachar(pre)
        sep = Text("separar objetos cercanos", color=VERDE, weight=BOLD).scale(0.65).move_to([3.0, -2.3, 0])
        cr = Text("comprimir = resolver", color=AMBAR, weight=BOLD).scale(0.95).move_to([0, -3.4, 0])
        # parte B
        hay = Text("¿hay señal?", color=TXT, weight=BOLD).scale(0.9).move_to([-4.0, 3.1, 0])
        Lr = Lienzo(ancho=3.0, alto=0.8, t_rango=(0, 1), v_max=1.0, centro=(-4.2, 1.7))
        rui = ruido_t(Lr, semilla=5, amp=0.7, color=RUIDO)
        blanco = Text("ruido blanco", color=RUIDO).scale(0.55).move_to([-4.2, 0.8, 0])
        pr = Tallos([1] * 13, centro=(0.6, 1.5), paso=0.2, unidad=0.5, color=SENAL)
        pb = Tallos(list(BARKER13), centro=(4.6, 1.5), paso=0.2, unidad=0.5, color=SENAL)
        igual = MathTex("=", color=VERDE).scale(1.3).move_to([2.6, 1.5, 0])
        pe = MathTex("P_e", color=ERROR).scale(0.9).move_to([2.6, 0.5, 0])
        carta = caja("solo importa la energía", AMBAR, ancho=5.2, alto=0.8, scale=0.55).move_to([0.0, -0.9, 0])
        e1 = MathTex("E", color=AMBAR).scale(1.0).move_to([0.6, 2.7, 0])
        e2 = MathTex("E", color=AMBAR).scale(1.0).move_to([4.6, 2.7, 0])
        rel = reloj().scale(0.9).move_to([-1.5, -2.8, 0])
        dq = formula("D", "=", "?", escala=1.2, colores={0: AMBAR, 2: AMBAR}).move_to([1.5, -2.8, 0])
        forma = Text("la forma cuenta", color=TXT, weight=BOLD).scale(0.65).move_to([4.6, -2.8, 0])
        with self.narrar("b1"):
            # «la razón de fondo»
            self.en("razon")
            self.play(FadeIn(rbase), Create(rect), FadeIn(lr), FadeIn(bark), FadeIn(lb), FadeIn(mes), FadeIn(dos),
                      run_time=self.dur(0.9))
            # «de la compresión de pulso»
            self.en("compresion")
            self.pop(cp)
            # «no es solo precisión en el retardo»
            self.en("precision")
            self.play(FadeIn(pre), run_time=0.3)
            self.play(Create(tpre), run_time=self.dur(0.5))
            # «es poder separar objetos cercanos»
            self.en("separar")
            self.play(FadeIn(sep), FadeIn(cr), run_time=self.dur(0.9))
            # «Y una aclaración»
            self.en("aclaracion")
            self.play(*[FadeOut(m) for m in (rbase, rect, lr, bark, lb, mes, dos, cp, pre, tpre, sep, cr)], run_time=0.4)
            # «hay o no hay señal»
            self.en("hayono")
            self.pop(hay)
            # «con ruido blanco»
            self.en("blanco")
            self.play(Create(rui), FadeIn(blanco), run_time=self.dur(0.7))
            # «el rectangular y Barker dan el mismo error»
            self.en("mismo")
            self.play(FadeIn(pr), FadeIn(pb), run_time=0.4)
            self.play(FadeIn(igual), FadeIn(pe), run_time=self.dur(0.6))
            # «Ya lo vimos»
            self.en("yavimos")
            self.play(FadeIn(carta), run_time=self.dur(0.6))
            # «solo importa la energía»
            self.en("energia")
            self.pop(e1, e2)
            # «La forma cuenta»
            self.en("forma")
            self.play(FadeOut(carta), run_time=0.3)
            self.pop(forma)
            # «cuando además hay que medir cuándo»
            self.en("cuando")
            self.play(FadeIn(rel), FadeIn(dq), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
