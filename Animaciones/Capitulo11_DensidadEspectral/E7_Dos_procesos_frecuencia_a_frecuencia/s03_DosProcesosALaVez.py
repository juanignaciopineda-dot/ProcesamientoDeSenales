"""Escena 03 — Dos procesos a la vez: la correlación cruzada y su transformada."""
from comun.escena import *


class DosProcesosALaVez(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        t = np.linspace(0, 4, 200)
        v = 0.9 * voz_valores(200)
        d = 24
        retrasada = np.concatenate([np.zeros(d), v[:-d]])
        L1 = Lienzo(ancho=5.0, alto=1.4, t_rango=(0, 4), v_max=1.0, centro=(-2.9, 1.9))
        L2 = Lienzo(ancho=5.0, alto=1.4, t_rango=(0, 4), v_max=1.0, centro=(-2.9, 0.1))
        x = L1.curva(t, v, SENAL, 2.6)
        y = L2.curva(t, retrasada, MEDIDA, 2.6)
        pers = persona(AZUL).scale(1.1).move_to([-6.4, 1.9, 0])
        mic = microfono(CIAN).scale(1.2).move_to([-6.4, 0.1, 0])
        l_env = etiqueta("envía", AZUL, 0.55).move_to([0.8, 1.9, 0])
        l_rec = etiqueta("recibe", CIAN, 0.55).move_to([0.9, 0.1, 0])
        cap10 = caja("Cap. 10", INK, ancho=1.6, alto=0.5, scale=0.4).move_to([5.9, 3.4, 0])
        R = formula(r"R_{yx}", "(", r"\tau", ")", escala=1.1, colores={0: MEDIDA}).move_to([-3.6, -2.5, 0])
        S = formula(r"S_{yx}", "(", r"j\omega", ")", escala=1.1, colores={0: AMBAR}).move_to([3.0, -2.5, 0])
        fl = flecha([-1.6, -2.5, 0], [1.2, -2.5, 0])
        nombre = etiqueta("densidad espectral cruzada", AMBAR, 0.55).move_to([3.0, -3.4, 0])
        with self.narrar("b1"):
            # «un proceso cada vez»
            self.en("uno")
            self.play(Create(L1.base()), Create(x), run_time=self.dur(1.2), rate_func=linear)

            # «casi siempre hay dos»
            self.en("dos")
            self.play(Create(L2.base()), Create(y), run_time=self.dur(1.0), rate_func=linear)

            # «lo que se envía y lo que se recibe»
            self.en("envia")
            self.play(FadeIn(l_env), run_time=0.3)
            self.play(FadeIn(l_rec), run_time=0.3)

            # «la voz y lo que capta un micrófono lejano»
            self.en("mic")
            self.play(FadeIn(pers, scale=0.7), FadeIn(mic, scale=0.7), run_time=self.dur(0.6))
            self.sfx("pop")

            # «Del capítulo anterior»
            self.en("anterior")
            self.play(FadeIn(cap10), run_time=self.dur(0.4))

            # «la correlación cruzada»
            self.en("cruzada")
            self.pop(R)

            # «una copia desplazada del otro»
            self.en("copia")
            cop = y.copy().set_stroke(opacity=0.85)
            self.add(cop)
            self.play(cop.animate.shift(UP * 1.8), run_time=self.dur(1.2))

            # «Su transformada»
            self.en("transf")
            self.play(GrowArrow(fl), run_time=self.dur(0.5))

            # «densidad espectral cruzada»
            self.en("densidad")
            self.pop(S)
            self.play(FadeIn(nombre), run_time=0.4)

        self.wait(1.0)
        self.limpiar()
