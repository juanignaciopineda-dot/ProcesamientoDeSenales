"""Escena 01 — Gancho: grabar diez veces más no baja el temblor del espectro."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        L1 = Lienzo(ancho=9.0, alto=1.4, t_rango=(0, 10), v_max=2.6, centro=(1.2, 2.8))
        P = Lienzo(ancho=10.0, alto=3.2, t_rango=(0, 1), v_max=5.0, centro=(-0.6, -2.7))
        t = np.linspace(0, 10, 400)
        larga = L1.curva(t, 0.8 * serie(5, 400, 0.0), RUIDO, 2.6)
        corta = L1.curva(t[:40], 0.8 * serie(5, 400, 0.0)[:40], RUIDO, 2.6)
        t1s = etiqueta("1 s", INK, 0.55).move_to([-4.2, 3.7, 0])
        t10s = etiqueta("10 s", INK, 0.55).move_to([-4.2, 3.7, 0])
        pc = ordenador(INK).scale(0.8).move_to([-5.7, 2.8, 0])
        ok = tilde(VERDE, 0.5).move_to([-4.65, 2.8, 0])
        verdadero = P.curva([0, 1], [1, 1], SENAL, 5)
        b1 = bosque_f(P, periodograma_blanco(7, 90), MEDIDA, 2.4)
        b2 = bosque_f(P, periodograma_blanco(8, 320), MEDIDA, 2.2)
        tope = DashedLine(P.p(0, 3), P.p(1, 3), color=ROJO, stroke_width=3.5)
        no_baja = etiqueta("no baja", ROJO, 0.55).move_to([5.7, -1.74, 0])
        metodo = etiqueta("el método", ROJO, 0.55).move_to([5.7, -0.9, 0])
        x = cruz(ROJO, 2.2).move_to(P.p(0.5, 2.2))
        suave = bosque_f(P, periodograma_blanco(9, 320, 60), ESTIMACION, 4.5)
        ok2 = tilde(VERDE, 0.7).move_to([5.7, -1.4, 0])
        with self.narrar("b1"):
            self.en("mas")
            self.play(Create(L1.base()), Create(corta), FadeIn(t1s), run_time=self.dur(0.5))
            self.play(FadeOut(corta), Create(larga), ReplacementTransform(t1s, t10s), run_time=self.dur(0.8))
            self.en("espectro")
            self.play(Create(P.base()), Create(verdadero), Create(b1), run_time=self.dur(1.0))
            self.en("temblor")
            self.play(ReplacementTransform(b1, b2), Create(tope), FadeIn(no_baja), run_time=self.dur(1.0))
            self.en("aparato")
            self.play(FadeIn(pc), run_time=0.3)
            self.pop(ok)
            self.en("trampa")
            self.pop(x)
            self.play(FadeIn(metodo), run_time=0.3)
            self.en("arreglo")
            self.play(FadeOut(x), FadeOut(b2), FadeOut(tope), FadeOut(no_baja), FadeOut(metodo),
                      Create(suave), run_time=self.dur(0.9))
            self.pop(ok2)
        self.wait(0.8)
        self.limpiar()
