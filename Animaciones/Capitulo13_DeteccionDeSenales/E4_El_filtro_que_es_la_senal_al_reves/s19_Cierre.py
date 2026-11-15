"""Escena 19 — Cierre: repaso del filtro adaptado y gancho hacia el ruido con memoria."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "19"

    def construct(self):
        s = Tallos(S13, centro=(-5.0, 1.7), paso=0.6, unidad=0.3, color=SENAL)
        h = Tallos(H13, centro=(-2.4, 1.7), paso=0.6, unidad=0.3, color=ESTIMACION)
        giro = CurvedArrow([-4.5, 2.7, 0], [-2.9, 2.7, 0], color=AMBAR, angle=-PI / 2.5, stroke_width=4)
        aut = Tallos(AUT13, centro=(2.4, 1.7), paso=0.5, unidad=0.15, color=AMBAR)
        al = alarma13().scale(0.7).move_to([5.3, 1.9, 0])
        alin = VGroup(*[flecha_c([-5.6 + 0.65 * i, -0.4, 0], 0.55, 0, SENAL, 5) for i in range(3)])
        par = parabola_l(centro=(2.0, -0.5), ancho=3.2, alto=1.8, fondo=0.0, color=AMBAR)
        L = Lienzo(ancho=3.2, alto=0.8, t_rango=(0, 1), v_max=1.6, centro=(-3.2, -2.9))
        t = np.linspace(0, 1, 140)
        blanco = Line(L.p(0, 0), L.p(1, 0), color=RUIDO, stroke_width=4)
        memoria = L.curva(t, 0.8 * serie(11, 140, 0.95), RUIDO, 3.0)
        tri = Triangle(color=AMBAR, stroke_width=5).scale(0.5).move_to([0.9, -2.9, 0])
        adv = Text("!", color=AMBAR, weight=BOLD).scale(0.6).move_to(tri).shift(DOWN * 0.04)
        rl = reloj().scale(0.9).move_to([4.6, -2.9, 0])
        titulo_prox = self.palabra("Cuando el ruido tiene memoria", AMBAR, 0.85).move_to([0, -2.3, 0])

        with self.narrar("b1"):
            # «es la señal al revés»
            self.en("reves")
            self.play(FadeIn(s), run_time=self.dur(0.4))
            self.play(Create(giro), FadeIn(h), run_time=self.dur(0.6))

            # «en el tiempo busca parecidos»
            self.en("tiempo")
            self.play(FadeIn(aut), FadeIn(al, scale=0.7), run_time=self.dur(0.6))

            # «en la frecuencia alinea las fases»
            self.en("frec")
            self.play(LaggedStart(*[GrowArrow(a) for a in alin], lag_ratio=0.25), run_time=self.dur(0.9))

            # «ningún otro filtro»
            self.en("ninguno")
            self.play(Create(par.eje), Create(par.curva), run_time=self.dur(0.8))

            # «Pero todo esto suponía»
            self.en("pero")
            self.play(FadeIn(tri), FadeIn(adv), run_time=self.dur(0.4))

            # «ruido blanco»
            self.en("blanco")
            self.play(Create(blanco), run_time=self.dur(0.5))

            # «¿Y si el ruido tiene memoria?»
            self.en("memoria")
            self.play(Transform(blanco, memoria), run_time=self.dur(1.0))

            # «En el próximo episodio»
            self.en("proximo")
            self.play(FadeIn(rl, scale=0.7), run_time=self.dur(0.4))
            self.play(Rotate(rl.minutero, angle=-PI, about_point=rl.aro.get_center()), run_time=self.dur(0.8))

            # «cuando el ruido tiene memoria»
            self.en("titulo")
            self.play(FadeOut(VGroup(blanco, tri, adv, rl)), run_time=0.3)
            self.pop(titulo_prox)
        self.wait(1.0)
        self.limpiar()
