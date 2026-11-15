"""Escena 13 — Cierre: resumen del episodio y anuncio del E7, «Dos procesos, frecuencia a frecuencia»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        Lt = Lienzo(ancho=3.6, alto=1.1, t_rango=(0, 3), v_max=1.0, centro=(-4.6, 2.6))
        tr = traza(Lt.x(np.linspace(0, 3, 150)), Lt.y(0.8 * serie(5, 150, 0.9)), RUIDO, 3.5)
        Ee = Lienzo(ancho=2.6, alto=1.4, t_rango=(-np.pi, np.pi), v_max=6.5, centro=(-0.4, 2.6))
        ce = curva_f(Ee, psd_eco, -np.pi, np.pi, AMBAR, 4)
        mon = moneda("", AMBAR).scale(0.6).move_to([-6.2, 0.6, 0])
        bh = BloqueLTI("H", centro=(-3.6, 0.6), ancho=1.4, alto=0.9, largo=1.1, color=CIAN, escala=0.8)
        col = traza(np.linspace(-0.6, 2.2, 80), 0.6 + 0.35 * serie(5, 80, 0.9), RUIDO, 3.5)
        bi = BloqueLTI("1/H", centro=(-3.6, -1.4), ancho=1.4, alto=0.9, largo=1.1, color=AMBAR, escala=0.8)
        pla = traza(np.linspace(-0.6, 2.2, 80), -1.4 + 0.3 * serie(6, 80, 0.0), TXT, 3.0)
        fm = self.palabra("fase mínima", VERDE, 0.9).move_to([4.6, -1.4, 0])
        ok = tilde(VERDE, 0.5).move_to([4.6, -2.3, 0])
        uno = traza(np.linspace(-2.5, 2.5, 160), 1.2 + 0.7 * serie(7, 160, 0.9), SENAL, 3.5)
        dos1 = traza(np.linspace(-6.4, -0.4, 160), 1.8 + 0.35 * serie(8, 160, 0.9), SENAL, 3.5)
        dos2 = traza(np.linspace(-6.4, -0.4, 160), -0.6 + 0.35 * serie(9, 160, 0.9), RUIDO, 3.5)
        t_v = etiqueta("voz", SENAL, 0.6).move_to([-5.0, 3.1, 0])
        t_m = etiqueta("murmullo", RUIDO, 0.6).move_to([-5.0, -1.5, 0])
        pq = etiqueta("¿cuánto se parecen?", AMBAR, 0.8).move_to([4.2, 0.6, 0])
        E = Lienzo(ancho=10.0, alto=1.4, t_rango=(0, 10), v_max=1.0, centro=(0, -3.0))
        base = E.base()
        vent = VGroup(*[Rectangle(width=0.9, height=1.2, color=AMBAR, stroke_width=2.5).set_fill(AMBAR, 0.18)
                        .move_to([E.x(0.9 + 1.3 * i), -2.6, 0]) for i in range(7)])
        prox = etiqueta("Próximo episodio", INK, 0.6).move_to([0, 1.9, 0])
        a = self.palabra("Dos procesos,", TXT, 1.3).move_to([0, 0.4, 0])
        b = self.palabra("frecuencia a frecuencia", AMBAR, 1.3).move_to([0, -1.0, 0])
        with self.narrar("b1"):
            # «mirar un ruido»
            self.en("mirar")
            self.play(Create(Lt.base()), Create(tr), Create(ce), run_time=self.dur(1.0))

            # «fabricarlo con un filtro modelador»
            self.en("fabricar")
            self.play(FadeIn(mon), FadeIn(bh), Create(col), run_time=self.dur(1.0))

            # «quitarle el color con un blanqueador»
            self.en("quitar")
            self.play(FadeIn(bi), Create(pla), run_time=self.dur(1.0))

            # «y el único que se puede deshacer»
            self.en("unico")
            self.resaltar(bi, color=VERDE)

            # «fase mínima»
            self.en("fasemin")
            self.pop(fm)
            self.play(FadeIn(ok), run_time=0.3)

            # «un solo proceso»
            self.en("uno")
            self.corte()
            self.play(Create(uno), run_time=self.dur(1.0), rate_func=linear)

            # «la voz y el murmullo»
            self.en("dos")
            self.corte()
            self.play(Create(dos1), FadeIn(t_v), run_time=self.dur(0.8))
            self.play(Create(dos2), FadeIn(t_m), run_time=self.dur(0.8))

            # «cuánto se parecen»
            self.en("parecen")
            self.pop(pq)

            # «frecuencia a frecuencia»
            self.en("frec")
            self.play(Create(base), run_time=0.3)
            self.play(LaggedStart(*[FadeIn(v) for v in vent], lag_ratio=0.2), run_time=self.dur(1.6))

            # «En el próximo episodio»
            self.en("prox")
            self.wait(0.2)

            # «dos procesos, frecuencia a frecuencia»
            self.en("titulo_e7")
            self.limpiar(0.25)
            self.play(FadeIn(prox), run_time=0.3)
            self.pop(a, b)
        self.wait(1.0)
        self.limpiar()
