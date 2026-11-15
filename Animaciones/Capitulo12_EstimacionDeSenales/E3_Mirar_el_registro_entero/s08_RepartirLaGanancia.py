"""Escena 08 — Las tres cuentas, la curva H(Ω), cómo reparte la ganancia y por qué tira hacia la media."""
from comun.escena import *


class RepartirLaGanancia(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.parte_b3()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        cas = VGroup(*[RoundedRectangle(corner_radius=0.12, width=3.9, height=1.8, color=INK, stroke_width=2.5)
                       .set_fill(INK, 0.08).move_to([x, 2.4, 0]) for x in (-4.2, 0.0, 4.2)])
        cab = [MathTex(t, color=AMBAR).scale(0.8).move_to([x, 2.95, 0])
               for x, t in zip((-4.2, 0.0, 4.2), (r"\Omega=0", r"\Omega=\pi/2", r"\Omega=\pi"))]
        frs = [MathTex(t, color=TXT).scale(0.9).move_to([x - 0.9, 2.0, 0])
               for x, t in zip((-4.2, 0.0, 4.2), (r"\frac{16}{17}", r"\frac{1{,}88}{2{,}88}", r"\frac{1}{2}"))]
        res = [MathTex(t, color=ESTIMACION).scale(0.9).move_to([x + 0.9, 2.0, 0])
               for x, t in zip((-4.2, 0.0, 4.2), (r"=0{,}94", r"=0{,}65", r"=0{,}5"))]
        L = lienzo_omega(ancho=9.0, alto=3.8, v_max=1.1, centro=(0.0, -1.5))
        eje = eje_omega(L, 1.1, escala=0.75)
        curva = curva_f(L, h_wiener, 0.0, np.pi, AMBAR, 5, n=200)
        puntos = [Dot(L.p(w, h_wiener(w)), radius=0.1, color=AMBAR) for w in (0.0, np.pi / 2, np.pi)]
        verde = area_f(L, h_wiener, 0.0, 0.8, VERDE, 0.3)
        golpe = VGroup(DashedLine(L.p(0, 1.0), L.p(np.pi / 2, 1.0), color=INK, stroke_width=3),
                       DashedLine(L.p(np.pi / 2, 1.0), L.p(np.pi / 2, 0.0), color=INK, stroke_width=3),
                       DashedLine(L.p(np.pi / 2, 0.0), L.p(np.pi, 0.0), color=INK, stroke_width=3))
        t = np.linspace(0, 1, 120)
        Ll = Lienzo(ancho=3.4, alto=0.7, t_rango=(0, 1), v_max=2.5, centro=(-3.2, -3.5))
        Lr = Lienzo(ancho=3.4, alto=0.7, t_rango=(0, 1), v_max=2.5, centro=(3.2, -3.5))
        lenta = Ll.curva(t, 1.6 * serie(8, 120, 0.97), SENAL, 3.5)
        rapida = Lr.curva(t, 0.8 * serie(9, 120, 0.0), RUIDO, 2.5)
        self.L, self.curva, self.eje, self.puntos = L, curva, eje, puntos
        self.todo_b1 = VGroup(cas, *cab, *frs, *res, golpe, lenta, rapida, verde)
        with self.narrar("b1"):
            self.en("cuentas")                               # «Hacemos las cuentas»
            self.play(LaggedStart(*[FadeIn(c) for c in cas], lag_ratio=0.15), run_time=self.dur(0.8))
            self.en("f0")                                    # «En frecuencia cero»
            self.play(FadeIn(cab[0]), run_time=0.3)
            self.en("c0")                                    # «dieciséis entre diecisiete»
            self.play(FadeIn(frs[0]), run_time=0.4)
            self.en("r94")                                   # «cero coma nueve cuatro»
            self.play(FadeIn(res[0]), run_time=0.4)
            self.en("pm")                                    # «En pi medios»
            self.play(FadeIn(cab[1]), run_time=0.3)
            self.en("c1")                                    # «uno coma ocho ocho entre dos coma ocho ocho»
            self.play(FadeIn(frs[1]), run_time=0.5)
            self.en("r65")                                   # «cero coma seis cinco»
            self.play(FadeIn(res[1]), run_time=0.4)
            self.en("p")                                     # «En pi:»
            self.play(FadeIn(cab[2]), run_time=0.3)
            self.en("c2")                                    # «uno entre dos»
            self.play(FadeIn(frs[2]), run_time=0.4)
            self.en("r5")                                    # «cero coma cinco»
            self.play(FadeIn(res[2]), run_time=0.4)
            self.en("suave")                                 # «Un filtro suave»
            self.play(Create(eje.h), Create(eje.v), FadeIn(eje.rotulos), run_time=0.4)
            self.play(*[FadeIn(p, scale=2) for p in puntos], Create(curva), run_time=self.dur(1.0))
            self.en("bajas")                                 # «casi todo en las frecuencias bajas»
            self.play(FadeIn(verde), run_time=0.5)
            self.en("golpe")                                 # «sin cortar de golpe»
            self.play(Create(golpe), run_time=0.5)
            self.play(FadeOut(golpe), run_time=0.4)
            self.en("despacio")                              # «La temperatura cambia despacio»
            self.play(Create(lenta), run_time=0.7)
            self.en("deprisa")                               # «el ruido, deprisa»
            self.play(Create(rapida), run_time=0.7)

    def parte_b2(self):
        L = self.L
        bandas = VGroup(*[DashedLine(L.p(w, 0), L.p(w, 1.1), color=INK, stroke_width=2)
                          for w in (np.pi / 3, 2 * np.pi / 3)])
        v_s = ventana(L, 0.0, np.pi / 3, 1.1, AZUL, 0.2)
        v_r = ventana(L, 2 * np.pi / 3, np.pi, 1.1, MAGENTA, 0.2)
        t_s = Text("señal", color=SENAL).scale(0.65).move_to(L.p(np.pi / 6, 1.25) + UP * 0.1)
        t_r = Text("ruido", color=RUIDO).scale(0.65).move_to(L.p(5 * np.pi / 6, 1.25) + UP * 0.1)
        pasa = flecha([-6.0, 2.4, 0], [-1.2, 2.4, 0], MEDIDA, 5)
        l_uno = MathTex(r"H\approx 1", color=AMBAR).scale(0.8).next_to(pasa, UP, buff=0.15)
        pared = muro(alto=1.0, ancho=0.35, color=ROJO).move_to([3.4, 2.4, 0])
        corta = flecha([0.8, 2.4, 0], [3.1, 2.4, 0], MEDIDA, 5)
        l_cero = MathTex(r"H\to 0", color=AMBAR).scale(0.8).move_to([2.0, 3.1, 0])
        et = MathTex(r"H(\Omega)", color=AMBAR).scale(0.9).move_to(L.p(1.55, 1.05) + UP * 0.5)
        with self.narrar("b2"):
            self.play(FadeOut(self.todo_b1), run_time=0.4)
            self.en("reparte")                               # «repartir la ganancia»
            self.play(FadeIn(et), run_time=0.4)
            self.resaltar(self.curva, color=AMBAR, escala=1.03)
            self.en("banda")                                 # «cuánta señal hay en cada banda»
            self.play(Create(bandas), run_time=0.5)
            self.en("domina")                                # «Donde la señal domina»
            self.play(FadeIn(v_s), FadeIn(t_s), run_time=0.4)
            self.en("uno")                                   # «se acerca a uno y deja pasar»
            self.play(Create(pasa), FadeIn(l_uno), run_time=0.6)
            self.en("manda")                                 # «Donde manda el ruido»
            self.play(FadeIn(v_r), FadeIn(t_r), run_time=0.4)
            self.en("cero")                                  # «se acerca a cero y corta»
            self.play(Create(corta), FadeIn(pared), FadeIn(l_cero), run_time=0.6)
        self.b2 = VGroup(bandas, v_s, v_r, t_s, t_r, pasa, l_uno, pared, corta, l_cero, et)

    def parte_b3(self):
        L = self.L
        uno = DashedLine(L.p(0, 1.0), L.p(np.pi, 1.0), color=INK, stroke_width=2.5)
        l_uno = MathTex("1", color=INK).scale(0.6).next_to(L.p(0, 1.0), LEFT, buff=0.15)
        Lt = Lienzo(ancho=9.0, alto=1.6, t_rango=(0, 1), v_max=2.2, centro=(0.0, -3.3))
        t = np.linspace(0, 1, 140)
        y, v, x = registro_e3(140, 7)
        base_t = Lt.base()
        ty = Lt.curva(t, 0.75 * y, SENAL, 3.5)
        yh = Lt.curva(t, 0.75 * 0.55 * y, ESTIMACION, 3.5)
        yh2 = Lt.curva(t, 0.75 * 0.9 * y, ESTIMACION, 3.5)
        ok = tilde(VERDE, 0.6).move_to([6.2, -2.4, 0])
        tiran = VGroup(*[Arrow(Lt.p(tt, 0.75 * 0.9 * y[int(tt * 139)]) , Lt.p(tt, 0.75 * 0.5 * y[int(tt * 139)]),
                               buff=0, color=INK, stroke_width=4, max_tip_length_to_length_ratio=0.35)
                         for tt in (0.12, 0.32, 0.55, 0.78)])
        c10 = Text("Cap. 10", color=INK).scale(0.65).move_to([6.0, 3.4, 0])
        i1 = int(0.32 * 139)
        duda = Text("?", color=AMBAR, weight=BOLD).scale(1.3).move_to([-6.0, -3.0, 0])
        with self.narrar("b3"):
            self.play(FadeOut(self.b2), run_time=0.3)
            self.en("nunca")                                 # «la ganancia nunca llega a uno»
            self.play(Create(uno), FadeIn(l_uno), run_time=0.5)
            self.en("amplitud")                              # «menos amplitud»
            self.play(Create(base_t), Create(ty), run_time=0.7)
            self.play(Create(yh), run_time=0.7)
            self.en("noerror")                               # «No es un error»
            self.pop(ok)
            self.en("tira")                                  # «tira hacia la media»
            self.play(LaggedStart(*[GrowArrow(a) for a in tiran], lag_ratio=0.2), run_time=self.dur(1.0))
            self.en("cap10")                                 # «la predicción del capítulo diez»
            self.pop(c10)
            self.en("duda")                                  # «cuando duda»
            self.pop(duda)
            self.en("info")                                  # «Cuanta más información tiene»
            self.play(FadeOut(duda), ReplacementTransform(yh, yh2), run_time=self.dur(1.0))
            self.en("menos")                                 # «menos tira»
            self.play(*[a.animate.scale(0.3) for a in tiran], run_time=0.5)
