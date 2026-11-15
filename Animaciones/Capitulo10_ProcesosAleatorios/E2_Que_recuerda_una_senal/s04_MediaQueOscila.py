"""Escena 04 — Cuatro osciladores que arrancan a la vez (amplitudes 1, 1, 3, 3): la media oscila, 2 cos."""
from comun.escena import *


class MediaQueOscila(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        cos = CuatroEnFase()
        tab = TablaCortes(["A = 1", "A = 1", "A = 3", "A = 3"])
        estado = {"corte": None, "puntos": None}

        def dots(t):
            return VGroup(*[Dot(cos.punto(i, t), radius=0.09, color=AMBAR) for i in range(4)])

        def mover(t):
            nuevos = dots(t)
            anims = [estado["corte"].animate.set_x(float(cos.x(t)))]
            if estado["puntos"] is not None:
                anims.append(FadeOut(estado["puntos"]))
            anims.append(FadeIn(nuevos))
            estado["puntos"] = nuevos
            return anims

        L2 = Lienzo(ancho=4.0, alto=2.0, t_rango=(-0.25, 1.75), v_max=2.6, centro=(-4.6, -2.6))
        t = np.linspace(-0.25, 1.75, 200)

        with self.narrar("b1"):
            # «no tiene por qué ser así»
            self.en("no_siempre")
            plana = Line([-4.5, 0.6, 0], [4.5, 0.6, 0], color=AMBAR, stroke_width=6)
            self.play(Create(plana), run_time=0.4)
            x = cruz(ROJO, 1.0).move_to([0, 0.6, 0])
            self.pop(x)

            # «Cambiemos el experimento»
            self.en("cambio")
            self.corte()
            self.play(Create(VGroup(*cos.bases)), run_time=self.dur(0.5))

            # «arrancan a la vez»
            self.en("a_la_vez")
            self.play(Create(VGroup(*cos.curvas)), run_time=self.dur(1.5), rate_func=linear)

            # «amplitud uno»
            self.en("amp1")
            self.play(FadeIn(cos.rotulos[0:2]), run_time=0.4)

            # «amplitud tres»
            self.en("amp3")
            self.play(FadeIn(cos.rotulos[2:4]), run_time=0.4)

            # «En te igual a cero, la media es dos»
            self.en("media2")
            estado["corte"] = cos.corte(0.0)
            estado["puntos"] = dots(0.0)
            self.play(Create(estado["corte"]), FadeIn(estado["puntos"]), FadeIn(tab.armazon()),
                      FadeIn(tab.enc(0, "t = 0")),
                      FadeIn(etiqueta("t en períodos", INK, 0.45).move_to([-4.2, 3.15, 0])), run_time=self.dur(0.7))
            self.play(LaggedStart(*[FadeIn(tab.celda(0, i, s), shift=DOWN * 0.1) for i, s in enumerate(["1", "1", "3", "3"])],
                                  lag_ratio=0.2), run_time=self.dur(0.9))
            self.pop(tab.prom(0, "2"))

            # «Un cuarto de período después»
            self.en("cuarto0")
            self.play(*mover(0.25), FadeIn(tab.enc(1, "t = ¼")), run_time=self.dur(0.6))
            self.play(LaggedStart(*[FadeIn(tab.celda(1, i, "0"), shift=DOWN * 0.1) for i in range(4)], lag_ratio=0.15),
                      run_time=self.dur(0.7))

            # «la media es cero»
            self.en("media0")
            self.pop(tab.prom(1, "0"))

            # «Medio período después»
            self.en("medio")
            self.play(*mover(0.5), FadeIn(tab.enc(2, "t = ½")), run_time=self.dur(0.6))

            # «menos dos»
            self.en("menos2")
            self.play(LaggedStart(*[FadeIn(tab.celda(2, i, s), shift=DOWN * 0.1)
                                    for i, s in enumerate(["−1", "−1", "−3", "−3"])], lag_ratio=0.12),
                      run_time=self.dur(0.6))
            self.pop(tab.prom(2, "−2"))

            # «La media sube y baja»
            self.en("sube")
            base = L2.base()
            marcas = VGroup(*[Dot(L2.p(tt, v), radius=0.09, color=AMBAR) for tt, v in ((0, 2), (0.25, 0), (0.5, -2))])
            self.play(Create(base), FadeIn(marcas), run_time=0.5)
            media = L2.curva(t, 2 * np.cos(2 * np.pi * t), AMBAR, 5)
            self.play(Create(media), run_time=self.dur(1.6), rate_func=linear)

            # «de amplitud dos»
            self.en("amp2")
            f = formula("2", r"\cos", "(", "2", r"\pi", "t", ")", colores={0: AMBAR}, escala=0.75).move_to([-1.5, -2.6, 0])
            self.pop(f)

        self.wait(1.0)
        self.limpiar()
