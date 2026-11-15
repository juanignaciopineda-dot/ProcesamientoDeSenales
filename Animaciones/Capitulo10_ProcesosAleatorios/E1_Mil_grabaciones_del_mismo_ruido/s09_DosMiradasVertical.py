"""Escena 09 — Los cuatro osciladores desfasados; congelar el tiempo da una variable aleatoria."""
from comun.escena import *


class DosMiradasVertical(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.cos = CuatroCosenos()
        self.presentar()
        self.leer()
        self.variable()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1: cuatro osciladores
    def presentar(self):
        cos = self.cos
        rng = np.random.default_rng(6)
        xs = [-5.5 + 2.2 * k for k in range(6)]
        grid = VGroup(*[generador(float(rng.uniform(0.5, 1.0)), float(rng.choice([1.0, 1.5, 2.0, 2.5, 3.0])),
                                  float(rng.uniform(0, 6.28))).move_to([x, y, 0])
                        for y in (2.55, 0.95) for x in xs])
        self.gens = VGroup(*[generador(1.0, 1.0, np.deg2rad(f) + np.pi / 2, 1.5, 1.0).move_to([-5.9, cos.yc(i), 0])
                             for i, f in enumerate(cos.FASES)])
        gens = self.gens
        with self.narrar("b1"):
            self.play(LaggedStart(*[FadeIn(g, scale=0.7) for g in grid], lag_ratio=0.05), run_time=self.dur(1.2))

            # «simplifiquemos la nave»
            self.en("simple")
            self.play(*[ReplacementTransform(grid[k], gens[k]) for k in range(4)],
                      *[FadeOut(grid[k]) for k in range(4, 12)], run_time=self.dur(1.2))

            # «la misma amplitud»
            self.en("amp")
            t_amp = formula("A=1", color=AMBAR, escala=1.5).move_to([-1.5, 1.2, 0])
            self.pop(t_amp)

            # «la misma frecuencia»
            self.en("frec")
            t_frec = Text("misma frecuencia", color=AMBAR, weight=BOLD).scale(0.75).move_to([-1.5, -0.6, 0])
            self.pop(t_frec)

            # «uno arranca en cero grados» … «otro en doscientos setenta»
            for marca, i in (("f0", 0), ("f90", 1), ("f180", 2), ("f270", 3)):
                self.en(marca)
                self.pop(cos.rotulos[i], sonido=None)

            # «Elegimos uno al azar»
            self.en("elegimos")
            aro = RoundedRectangle(corner_radius=0.15, width=1.75, height=1.25, color=AMBAR, stroke_width=5)
            aro.move_to(gens[2])
            self.play(FadeIn(aro), run_time=0.15)
            for k in (0, 3, 1):
                self.play(aro.animate.move_to(gens[k]), run_time=0.3, rate_func=linear)
                self.sfx("tick", gain=-20)

            # «probabilidad un cuarto»
            self.en("cuarto")
            self.cuartos = VGroup(*[Text("¼", color=AMBAR, weight=BOLD).scale(0.9).move_to([-4.65, cos.yc(i), 0])
                                    for i in range(4)])
            self.play(FadeOut(aro), LaggedStart(*[FadeIn(c, scale=0.5) for c in self.cuartos], lag_ratio=0.15),
                      run_time=self.dur(1.0))

            # «las cuatro realizaciones»
            self.en("cosenos")
            self.play(FadeOut(t_amp), FadeOut(t_frec), run_time=0.25)
            self.play(LaggedStart(*[AnimationGroup(Create(cos.bases[i]), Create(cos.curvas[i])) for i in range(4)],
                                  lag_ratio=0.25), run_time=self.dur(3.0))

    # ---------------------------------------------------------------- b2: congelar el tiempo
    def leer(self):
        cos = self.cos
        self.lecturas = VGroup()
        with self.narrar("b2"):
            self.play(FadeOut(self.gens), FadeOut(self.cuartos), run_time=0.35)

            # «leer de dos maneras»
            self.en("dos")
            b1 = VGroup(Circle(0.27, color=AMBAR, stroke_width=3), Text("1", color=AMBAR, weight=BOLD).scale(0.4))
            b2 = VGroup(Circle(0.27, color=INK, stroke_width=3), Text("2", color=INK, weight=BOLD).scale(0.4))
            b1.move_to([-6.5, 3.55, 0])
            b2.move_to([-5.8, 3.55, 0])
            self.pop(b1, b2)

            # «congela el tiempo»
            self.en("congela")
            t0 = formula("t=0", color=AMBAR, escala=1.1).move_to([float(cos.x(0)), 3.55, 0])
            self.pop(t0)

            # «mira hacia abajo»
            self.en("baja")
            corte = cos.corte(0)
            self.play(Create(corte), run_time=self.dur(2.2), rate_func=linear)

            # «las cuatro grabaciones»
            self.en("cuatro_grab")
            self.play(LaggedStart(*[c.animate(rate_func=there_and_back).set_stroke(AMBAR, width=7)
                                    for c in cos.curvas], lag_ratio=0.25), run_time=self.dur(2.4))

            # «vale uno», «vale cero», «menos uno», «otra vez cero»
            for marca, i, txt in (("v1", 0, "1"), ("v0a", 1, "0"), ("vm1", 2, "−1"), ("v0b", 3, "0")):
                self.en(marca)
                p = cos.punto(i, 0.0)
                d = Dot(p, radius=0.11, color=AMBAR)
                con = DashedLine(p, [6.05, p[1], 0], color=INK, dash_length=0.1, stroke_width=2)
                lab = Text(txt, color=AMBAR, weight=BOLD).scale(0.9).move_to([6.5, p[1], 0])
                self.lecturas.add(d, con, lab)
                self.play(FadeIn(d, scale=0.4), Create(con), run_time=0.3)
                self.pop(lab, sonido=None)
            self.corte0, self.t0, self.badges = corte, t0, VGroup(b1, b2)

    # ---------------------------------------------------------------- b3: de las cuatro al número
    def variable(self):
        cos = self.cos
        etiquetas = [m for m in self.lecturas if isinstance(m, Text)]
        xs = {1: 2.6, 0: 0.0, -1: -2.6}
        with self.narrar("b3"):
            # «un número por cada realización»
            self.en("numeros")
            valores = [1, 0, -1, 0]
            fichas = []
            for etq, v in zip(etiquetas, valores):
                fichas.append(VGroup(Square(0.75, color=AZUL, stroke_width=3).set_fill(AZUL, 0.25),
                                     Text("−1" if v < 0 else str(v), color=TXT, weight=BOLD).scale(0.6)))
                fichas[-1].move_to(etq)
            resto = [m for m in self.mobjects if m is not self.camera.frame]
            self.play(*[FadeOut(m) for m in resto], run_time=0.3)
            recta = Line([-4.2, -1.4, 0], [4.2, -1.4, 0], color=INK, stroke_width=3)
            marcas = VGroup(*[Line([x, -1.52, 0], [x, -1.28, 0], color=INK, stroke_width=3) for x in xs.values()])
            nums = VGroup(*[Text("−1" if v < 0 else str(v), color=INK).scale(0.6).move_to([x, -1.95, 0])
                            for v, x in xs.items()])
            self.play(Create(recta), FadeIn(marcas), FadeIn(nums), *[FadeIn(f) for f in fichas], run_time=0.4)
            altura = {1: 0, 0: 0, -1: 0}
            destinos = []
            for v in valores:
                destinos.append(np.array([xs[v], -0.85 + 0.85 * altura[v], 0]))
                altura[v] += 1
            self.play(*[f.animate.move_to(d) for f, d in zip(fichas, destinos)], run_time=self.dur(1.6))

            # «Uno, con probabilidad un cuarto»
            self.en("b1")
            l1 = Text("¼", color=AMBAR, weight=BOLD).scale(1.0).move_to([xs[1], -0.85 + 0.75, 0])
            self.pop(l1)

            # «Cero, con probabilidad un medio»
            self.en("b0")
            l0 = Text("½", color=AMBAR, weight=BOLD).scale(1.0).move_to([xs[0], -0.85 + 0.85 + 0.75, 0])
            self.pop(l0)

            # «sale en dos de las cuatro»
            self.en("dos_de_cuatro")
            self.play(fichas[1].animate(rate_func=there_and_back).scale(1.25),
                      fichas[3].animate(rate_func=there_and_back).scale(1.25), run_time=self.dur(0.8))

            # «Menos uno, con probabilidad un cuarto»
            self.en("bm1")
            lm = Text("¼", color=AMBAR, weight=BOLD).scale(1.0).move_to([xs[-1], -0.85 + 0.75, 0])
            self.pop(lm)

            # «una variable aleatoria discreta»
            self.en("vad")
            X0 = formula("X(0)", color=AMBAR, escala=1.4).move_to([5.3, -1.4, 0])
            self.pop(X0)

            # «equis de cero»
            self.en("x0")
            self.resaltar(X0, color=AMBAR, escala=1.2)

            # «tal cual»
            self.en("tal_cual")
            ok = tilde(VERDE, 0.9).next_to(X0, UP, buff=0.25)
            self.pop(ok)

            # «su escalera»
            self.en("escalera")
            E = Lienzo(ancho=3.0, alto=2.0, t_rango=(-2, 2), v_max=1.0, centro=(5.2, 1.7))
            E.cy = 1.7
            px = [-2, -1, -1, 0, 0, 1, 1, 2]
            py = [0, 0, 0.25, 0.25, 0.75, 0.75, 1.0, 1.0]
            esc = traza([float(E.x(x)) for x in px], [E.cy - 1.0 + y * 2.0 for y in py], AMBAR, 4.5)
            self.play(Create(esc), run_time=self.dur(0.8), rate_func=linear)

            # «su media, su varianza»
            self.en("media_var")
            mu = formula(r"\mu", color=AMBAR, escala=1.3).move_to([4.4, 0.25, 0])
            sg = formula(r"\sigma^2", color=AMBAR, escala=1.3).move_to([6.0, 0.25, 0])
            self.pop(mu, sg)
