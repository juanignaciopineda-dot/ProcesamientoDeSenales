"""Escena 10 — Se puede cortar porque cada muestra blanca es una flecha perpendicular a las demás."""
from comun.escena import *

O = np.array([-3.2, -0.3, 0.0])


class PorQueSePuedeCortar(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.bloque_uno()
        self.bloque_dos()
        self.wait(1.0)
        self.limpiar()

    def bloque_uno(self):
        pre = self.palabra("¿por qué se puede cortar?", AMBAR, 0.75).move_to([0, 3.3, 0])
        dirs = [(np.array([2.6, 0, 0]), AZUL, r"x[n]"),
                (np.array([0, 2.4, 0]), AMBAR, r"x[n-1]"),
                (np.array([-1.4, -1.2, 0]), VERDE, r"x[n-2]")]
        flechas = [Arrow(O, O + d, buff=0, color=c, stroke_width=7, max_tip_length_to_length_ratio=0.15)
                   for d, c, _ in dirs]
        rots = [MathTex(r, color=c).scale(0.7).move_to(O + d * 1.0 + (d / np.linalg.norm(d)) * 0.5)
                for d, c, r in dirs]
        cajas = [caja_tex(f"h[{k}]", c, ancho=1.5, alto=0.7, escala=0.7).move_to([3.8, y, 0])
                 for k, c, y in ((0, AZUL, 0.5), (1, AMBAR, 1.7), (2, VERDE, -0.7))]
        hilos = [Line(cajas[i].get_left(), O + dirs[i][0], color=dirs[i][1], stroke_width=2.5, stroke_opacity=0.8)
                 for i in range(3)]
        ang = RightAngle(Line(O, O + RIGHT), Line(O, O + UP), length=0.3, color=VERDE)
        yv = Arrow(O, O + np.array([2.0, 1.4, 0]), buff=0, color=SENAL, stroke_width=7,
                   max_tip_length_to_length_ratio=0.15)
        ly = MathTex("y", color=SENAL).scale(0.8).move_to(O + np.array([2.4, 1.7, 0]))
        d1 = DashedLine(O + np.array([2.0, 1.4, 0]), O + np.array([2.0, 0, 0]), color=SENAL, stroke_width=2.5)
        d2 = DashedLine(O + np.array([2.0, 1.4, 0]), O + np.array([0, 1.4, 0]), color=SENAL, stroke_width=2.5)
        pr1 = Line(O, O + np.array([2.0, 0, 0]), color=SENAL, stroke_width=9, stroke_opacity=0.55)
        pr2 = Line(O, O + np.array([0, 1.4, 0]), color=SENAL, stroke_width=9, stroke_opacity=0.55)
        fperp = formula("x[n]", r"\perp", "x[n-1]", r"\perp", r"x[n-2]", escala=0.8,
                        colores={0: AZUL, 2: AMBAR, 4: VERDE}).move_to([3.4, 2.6, 0])
        til = tilde(VERDE, 1.0).move_to([3.4, -2.6, 0])
        with self.narrar("b1"):
            # «¿Por qué se puede cortar?»
            self.en("pregunta")
            self.pop(pre)

            # «información propia»
            self.en("propia")
            self.play(LaggedStart(*[GrowArrow(f) for f in flechas], lag_ratio=0.3), *[FadeIn(r) for r in rots],
                      run_time=self.dur(1.2))

            # «no repite la de las otras»
            self.en("norepite")
            self.play(Create(ang), run_time=self.dur(0.5))

            # «solo escucha a su muestra»
            self.en("escucha")
            self.play(*[FadeIn(c) for c in cajas], *[Create(h) for h in hilos], run_time=self.dur(1.0))

            # «quitar unas no cambia lo que dicen las demás»
            self.en("quitar")
            self.play(FadeOut(flechas[2]), FadeOut(rots[2]), FadeOut(hilos[2]), FadeOut(cajas[2]),
                      run_time=self.dur(0.7))

            # «suma de varias proyecciones»
            self.en("suma")
            self.play(GrowArrow(yv), FadeIn(ly), run_time=self.dur(0.6))
            self.play(Create(d1), Create(d2), run_time=self.dur(0.5))
            self.play(Create(pr1), Create(pr2), run_time=self.dur(0.5))

            # «perpendiculares entre sí»
            self.en("perpend")
            self.pop(fperp, sonido=None)

            # «no se estorban»
            self.en("estorban")
            self.play(FadeIn(til, scale=0.6), run_time=self.dur(0.4))
            self.sfx("exito", gain=-18)

    def bloque_dos(self):
        tira = tira_blanca((1, -1, -1, 1, -1, 1, 1, -1), lado=0.52).move_to([0, 2.9, 0])
        tach = tachar(tira)
        L = Lienzo(ancho=6.0, alto=1.6, t_rango=(0, 6), v_max=1.6, centro=(-1.8, 1.0))
        t = np.linspace(0, 6, 120)
        traza_s = L.curva(t, 0.9 * serie(5, 120, 0.93), MEDIDA, 3.0)
        term = termometro(1.6, ROJO, 0.55).move_to([-6.0, 1.0, 0])
        angs = [flecha_c([4.6, 0.2, 0], 1.7, a, MEDIDA, ancho=5) for a in (12, 40, 68)]
        sal = Arrow([-1.8, 0.0, 0], [-1.8, -0.9, 0], color=INK, stroke_width=3, buff=0)
        lsal = etiqueta("salida", AMBAR, 0.5).move_to([-0.7, -0.45, 0])
        cs = caja("sensor", MEDIDA, ancho=2.2, alto=0.8, scale=0.5)
        cb = caja("blanqueador", CIAN, ancho=3.0, alto=0.8, scale=0.5)
        tb = tira_blanca((1, -1, -1, 1, -1, 1), lado=0.5)
        cad = VGroup(cs, cb, tb).arrange(RIGHT, buff=0.9).move_to([0, -2.3, 0])
        a1 = flecha(cs.get_right(), cb.get_left(), INK, 3)
        a2 = flecha(cb.get_right(), tb.get_left(), INK, 3)
        til = tilde(VERDE, 0.9).move_to([cb.get_center()[0], -3.4, 0])
        lcap = etiqueta("capítulo 11", INK, 0.45).move_to([cb.get_center()[0], -3.4, 0])
        til.move_to([cb.get_center()[0] + 1.4, -3.4, 0])
        with self.narrar("b2"):
            # «casi nada es blanco»
            self.en("noblanco")
            self.corte()
            self.play(FadeIn(tira), run_time=self.dur(0.4))
            self.play(Create(tach), run_time=0.3)

            # «el sensor tiene memoria»
            self.en("sensor")
            self.play(FadeIn(term), Create(traza_s), run_time=self.dur(1.0))

            # «se parecen unas a otras»
            self.en("parecen")
            self.play(LaggedStart(*[GrowArrow(a) for a in angs], lag_ratio=0.25), run_time=self.dur(0.8))

            # «una salida»
            self.en("salida")
            self.play(GrowArrow(sal), FadeIn(lsal), run_time=self.dur(0.5))

            # «lo convertimos en blanco»
            self.en("convertir")
            self.play(FadeIn(cs), GrowArrow(a1), FadeIn(cb), GrowArrow(a2), FadeIn(tb), run_time=self.dur(1.2))

            # «Eso ya lo sabemos hacer»
            self.en("sabemos")
            self.play(FadeIn(til, scale=0.6), run_time=self.dur(0.4))
            self.sfx("exito", gain=-18)

            # «el blanqueador del capítulo once»
            self.en("blanq")
            self.play(FadeIn(lcap), run_time=self.dur(0.4))
