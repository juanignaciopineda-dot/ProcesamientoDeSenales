"""Escena 06 — El eco del sensor: x[n] = 0,6 x[n−1] + w[n], correlaciones 0,6 · 0,36 · 0,22 y un espectro de bajas."""
from comun.escena import *


class ElEcoDelSensor(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        term = termometro(1.7, ROJO, 0.6).move_to([-6.0, 2.3, 0])
        t_sensor = etiqueta("sensor", INK, 0.5).next_to(term, DOWN, buff=0.15)
        f = formula("x[n]", "=", num_tex(0.6), "x[n-1]", "+", "w[n]", escala=1.1,
                    colores={0: SENAL, 3: SENAL, 5: RUIDO}).move_to([0.2, 3.1, 0])
        puntos = fila_puntos(7, ancho=5.6, centro=(-1.5, 1.4), color=SENAL, radio=0.1)
        hilos = hilos_entre(puntos, INK, 3)
        t60 = etiqueta("× 0,6", AMBAR, 0.55).move_to([-3.7, 1.9, 0])
        T = Tallos([1, 0.6, 0.36, 0.22, 0.13, 0.08], centro=(-3.0, -2.5), paso=0.8, unidad=1.7, color=AMBAR, indices=True)
        rot_k = etiqueta("distancia", INK, 0.45).move_to([-3.0, -3.55, 0])
        e1 = etiqueta("0,6", AMBAR, 0.55).move_to(T.pos(1) + UP * 0.35)
        e2 = formula(num_tex(0.6), r"\cdot", num_tex(0.6), "=", num_tex(0.36), escala=0.85).move_to([1.5, -0.6, 0])
        e3 = etiqueta("0,22", AMBAR, 0.55).move_to(T.pos(3) + UP * 0.35)
        E = Lienzo(ancho=4.0, alto=2.0, t_rango=(-np.pi, np.pi), v_max=6.5, centro=(4.6, -1.9))
        ej = ejes_L(E, 0, 6.5)
        c = curva_f(E, psd_eco, -np.pi, np.pi, AMBAR, 5)
        t_bajas = etiqueta("frecuencias bajas", INK, 0.5).move_to([4.6, -3.45, 0])
        with self.narrar("b1"):
            # «sensor de temperatura»
            self.en("sensor")
            self.play(FadeIn(term), FadeIn(t_sensor), run_time=self.dur(0.6))

            # «La salida es»
            self.en("salida")
            self.play(FadeIn(f[0:2]), run_time=self.dur(0.6))

            # «cero coma seis veces la salida anterior más una moneda nueva»
            self.en("ecuacion")
            self.play(FadeIn(f[2:4]), run_time=self.dur(1.0))
            self.play(FadeIn(f[4:6]), run_time=0.6)

            # «una moneda nueva»
            self.en("nueva")
            self.resaltar(f[5], color=RUIDO)

            # «arrastra el sesenta por ciento de la anterior»
            self.en("arrastra")
            self.play(LaggedStart(*[FadeIn(p) for p in puntos], lag_ratio=0.15), run_time=self.dur(1.0))
            self.play(Create(hilos), FadeIn(t60), run_time=self.dur(0.8))

            # «Las vecinas se parecen cero coma seis»
            self.en("vecinas")
            self.play(Create(T.base), FadeIn(T.ks), FadeIn(rot_k), FadeIn(T.palito(0)), run_time=0.5)
            self.play(FadeIn(T.palito(1)), FadeIn(e1), run_time=self.dur(0.6))

            # «cero coma seis al cuadrado, cero coma tres seis»
            self.en("dos")
            self.play(FadeIn(e2), FadeIn(T.palito(2)), run_time=self.dur(0.8))

            # «a tres, cero coma dos dos»
            self.en("tres")
            self.play(FadeIn(T.palito(3)), FadeIn(e3), run_time=self.dur(0.6))

            # «Memoria que se borra poco a poco»
            self.en("memoria")
            self.play(FadeIn(T.palito(4)), FadeIn(T.palito(5)), run_time=self.dur(0.7))

            # «concentrado en las frecuencias bajas»
            self.en("bajas")
            self.play(Create(ej), Create(c), FadeIn(t_bajas), run_time=self.dur(1.2))
        self.wait(1.0)
        self.limpiar()
