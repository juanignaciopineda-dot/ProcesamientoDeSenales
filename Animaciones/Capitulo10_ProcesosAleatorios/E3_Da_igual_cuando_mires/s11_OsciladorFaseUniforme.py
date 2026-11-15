"""Escena 11 — Oscilador con fase uniforme: la media es cero (la integral de un coseno en una vuelta)."""
from comun.escena import *


class OsciladorFaseUniforme(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1: la nave con infinitos osciladores
    def parte_b1(self):
        rng = np.random.default_rng(3)
        xs = [-5.2 + 1.45 * k for k in range(7)]
        filas = [2.7, 1.6, 0.5]
        gens = [[generador(1.0, 1.0, float(rng.uniform(0, 6.28)), 1.3, 0.9).move_to([x, y, 0]) for x in xs] for y in filas]
        circ = Circle(radius=1.0, color=INK, stroke_width=3).move_to([4.6, -1.6, 0])
        pts = VGroup(*[Dot(circ.point_at_angle(k * TAU / 14), radius=0.07, color=AMBAR) for k in range(14)])

        with self.narrar("b1"):
            # «la nave»
            self.en("nave")
            self.play(LaggedStart(*[FadeIn(g, scale=0.7) for g in gens[0] + gens[1]], lag_ratio=0.04), run_time=self.dur(0.9))

            # «infinitos osciladores»
            self.en("infinitos")
            self.play(LaggedStart(*[FadeIn(g, scale=0.7) for g in gens[2]], lag_ratio=0.05), run_time=self.dur(0.7))

            # «la misma frecuencia»
            self.en("frec")
            mf = etiqueta("misma frecuencia", AMBAR, 0.5, BOLD).move_to([5.7, 2.65, 0])
            mf.permitir_fuera = True
            self.play(FadeIn(mf), *[g.seno.animate(rate_func=there_and_back).set_stroke(AMBAR, width=5)
                                    for fila in gens for g in fila], run_time=self.dur(1.0))

            # «omega cero»
            self.en("omega")
            f = formula("X(t)", "=", r"\square", r"\cos\!\big(", r"\omega_0 t", "+", r"\square", r"\big)",
                        escala=1.0).move_to([-3.4, -2.1, 0])
            f[4].set_color(AMBAR)
            self.play(FadeIn(f), run_time=self.dur(0.7))

            # «la fase se reparte»
            self.en("fase")
            self.play(Create(circ), LaggedStart(*[FadeIn(p, scale=0.4) for p in pts], lag_ratio=0.05), run_time=self.dur(0.9))
            th = MathTex(r"\Theta", color=AMBAR).scale(1.0).move_to(f[6])
            self.play(ReplacementTransform(f[6], th), run_time=0.3)

            # «toda la vuelta»
            self.en("vuelta")
            c0 = circ.get_center()
            radio = Line(c0, circ.point_at_angle(0), color=AMBAR, stroke_width=4)
            self.add(radio)
            self.play(Rotate(radio, angle=TAU, about_point=c0), run_time=self.dur(1.3), rate_func=linear)

            # «de cero a trescientos sesenta grados»
            self.en("grados")
            g = MathTex(r"\Theta\ \text{uniforme en}\ [0^\circ, 360^\circ)", color=TXT).scale(0.65).move_to([4.3, -3.4, 0])
            self.play(FadeIn(g), run_time=0.4)

            # «La amplitud»
            self.en("amp")
            a = MathTex("A", color=AMBAR).scale(1.0).move_to(f[2])
            self.play(ReplacementTransform(f[2], a), run_time=0.3)

            # «independiente de la fase»
            self.en("indep")
            ind = Text("A independiente de Θ", color=INK).scale(0.5).move_to([-3.4, -3.3, 0])
            self.play(FadeIn(ind, shift=UP * 0.1), run_time=0.4)

            # «Los cuatro osciladores desfasados»
            self.en("cuatro_osc")
            aros = VGroup(*[RoundedRectangle(corner_radius=0.12, width=1.45, height=1.05, color=AMBAR, stroke_width=4).move_to(gens[0][k])
                            for k in (0, 1, 2, 3)])
            self.play(LaggedStart(*[Create(r) for r in aros], lag_ratio=0.15), run_time=self.dur(0.8))

            # «una versión pequeña de esto»
            self.en("pequena")
            vp = etiqueta("versión pequeña", AMBAR, 0.55, BOLD).move_to([-2.3, 3.75, 0])
            self.play(FadeIn(vp, shift=DOWN * 0.1), run_time=0.4)

            # «¿Sigue siendo estacionario?»
            self.en("pregunta")
            q = Text("¿WSS?", color=AMBAR, weight=BOLD).scale(0.9).move_to([0.9, -2.1, 0])
            self.pop(q)
        self.limpiar()

    # ---------------------------------------------------------------- b2: la media, integral de un coseno
    def parte_b2(self):
        L = Lienzo(ancho=8.0, alto=2.6, t_rango=(0, 2), v_max=1.25, centro=(-1.6, 1.9))
        fases = [k * 45 for k in range(8)]
        curvas = [coseno(L, f, 1.0, SENAL, 2.6) for f in fases]
        t_c = 0.15
        circ = Circle(radius=0.95, color=INK, stroke_width=3).move_to([5.0, 1.9, 0])
        pts = [Dot(circ.point_at_angle(np.deg2rad(f)), radius=0.08, color=AMBAR) for f in fases]

        with self.narrar("b2"):
            # «un instante cualquiera»
            self.en("cualquiera")
            base = L.base()
            corte = L.vertical(t_c, AMBAR, 3.5)
            self.play(Create(base), *[Create(c) for c in curvas], run_time=self.dur(0.6))
            self.play(Create(corte), run_time=0.3)

            # «el promedio de los cosenos»
            self.en("promedio")
            dots = VGroup(*[Dot(L.p(t_c, float(np.cos(2 * np.pi * t_c + np.deg2rad(f)))), radius=0.09, color=AMBAR) for f in fases])
            self.play(FadeIn(dots, scale=0.5), run_time=self.dur(0.6))

            # «todas las fases posibles»
            self.en("todas")
            self.play(Create(circ), *[FadeIn(p, scale=0.4) for p in pts], run_time=self.dur(0.8))

            # «Con cuatro fases»
            self.en("cuatro")
            self.play(*[pts[k].animate.scale(1.8) for k in (0, 2, 4, 6)], *[pts[k].animate.set_opacity(0.25) for k in (1, 3, 5, 7)],
                      run_time=self.dur(0.6))

            # «sumábamos cuatro valores»
            self.en("sumabamos")
            sig = MathTex(r"\sum", color=AMBAR).scale(2.0).move_to([-1.6, -0.9, 0])
            self.pop(sig)

            # «Con infinitas, integramos»
            self.en("integramos")
            integ = MathTex(r"\int", color=AMBAR).scale(2.0).move_to(sig)
            self.play(ReplacementTransform(sig, integ), *[p.animate.set_opacity(1.0) for p in pts], run_time=self.dur(0.7))
            self.play(*[FadeOut(m) for m in (base, corte, dots, circ, *pts, *curvas)], integ.animate.move_to([-5.9, 0.6, 0]),
                      run_time=0.4)

            # «la integral de un coseno»
            self.en("integral")
            L2 = Lienzo(ancho=8.0, alto=3.0, t_rango=(0, 1), v_max=1.2, centro=(0.3, 0.6))
            base2 = L2.base()
            cur = coseno(L2, 0, 1.0, SENAL, 5)
            self.play(Create(base2), Create(cur), run_time=self.dur(1.0))

            # «una vuelta completa»
            self.en("completa")
            br = BraceBetweenPoints(L2.p(1, -1.25), L2.p(0, -1.25), color=AMBAR)
            lbl = MathTex(r"0 \to 2\pi", color=AMBAR).scale(0.8).next_to(br, DOWN, buff=0.1)
            self.play(Create(br), FadeIn(lbl), run_time=self.dur(0.7))

            # «por encima del eje»
            self.en("encima")
            tt = np.linspace(0, 1, 120)
            vv = np.cos(2 * np.pi * tt)

            def area(mask, color):
                piezas = VGroup()
                idx = np.where(mask)[0]
                grupos = np.split(idx, np.where(np.diff(idx) != 1)[0] + 1)
                for gr in grupos:
                    if len(gr) < 2:
                        continue
                    arriba = [L2.p(tt[i], vv[i]) for i in gr]
                    poli = Polygon(*arriba, L2.p(tt[gr[-1]], 0), L2.p(tt[gr[0]], 0), stroke_width=0)
                    poli.set_fill(color, 0.5)
                    piezas.add(poli)
                return piezas

            ar_pos = area(vv > 0, VERDE)
            self.play(FadeIn(ar_pos), run_time=self.dur(0.6))

            # «por debajo»
            self.en("debajo")
            ar_neg = area(vv < 0, ROJO)
            self.play(FadeIn(ar_neg), run_time=self.dur(0.6))

            # «La media es cero»
            self.en("media0")
            m0 = MathTex(r"\mu_X(t) = 0", color=AMBAR).scale(1.2).move_to([0.3, -2.9, 0])
            self.pop(m0)
