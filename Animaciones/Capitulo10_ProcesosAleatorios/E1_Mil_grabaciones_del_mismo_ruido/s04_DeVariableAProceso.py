"""Escena 04 — De variable aleatoria a proceso aleatorio: una regla que a cada resultado le pone una señal."""
from comun.escena import *


class DeVariableAProceso(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.regla()
        self.ensemble()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1: variable → proceso
    def regla(self):
        ys = [2.1 - 0.84 * k for k in range(6)]
        xd, xr = -5.6, -0.2                       # columna de dados y línea de números / curvas
        with self.narrar("b1"):
            # «el azar de un número»
            self.en("numero")
            recta = Line([xr, 2.5, 0], [xr, -2.5, 0], color=INK, stroke_width=2.5)
            marcas = VGroup(*[Line([xr - 0.12, y, 0], [xr + 0.12, y, 0], color=INK, stroke_width=2.5) for y in ys])
            nums = VGroup(*[Text(str(k + 1), color=INK).scale(0.5).move_to([xr + 0.6, y, 0]) for k, y in enumerate(ys)])
            self.play(Create(recta), FadeIn(marcas), FadeIn(nums), run_time=0.5)
            punto = Dot([xr, ys[1], 0], radius=0.15, color=AMBAR)
            self.play(FadeIn(punto, scale=0.5), run_time=0.2)
            for k in (4, 2):
                self.play(punto.animate.move_to([xr, ys[k], 0]), run_time=self.dur(0.4))

            # «Una variable aleatoria es una regla»
            self.en("regla")
            self.play(FadeOut(punto), run_time=0.15)
            dados = VGroup(*[dado_n(k + 1).scale(0.6).move_to([xd, y, 0]) for k, y in enumerate(ys)])
            res = etiqueta("resultados", INK, 0.55).move_to([xd, 3.15, 0])
            self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in dados], lag_ratio=0.12), FadeIn(res),
                      run_time=self.dur(1.6))

            # «a cada resultado del experimento»
            self.en("resultado")
            self.play(LaggedStart(*[d.animate(rate_func=there_and_back).scale(1.25) for d in dados], lag_ratio=0.15),
                      run_time=self.dur(1.6))

            # «le pone un número»
            self.en("pone")
            flechas = VGroup(*[flecha([xd + 0.55, y, 0], [xr - 0.3, y, 0], INK, 2.5) for y in ys])
            X = formula("X", colores={0: AMBAR}, escala=1.2).move_to([(xd + xr) / 2 + 0.3, 2.75, 0])
            self.play(LaggedStart(*[GrowArrow(f) for f in flechas], lag_ratio=0.12), run_time=self.dur(1.2))
            self.pop(X, sonido=None)

            # «Si el dado cae en la cara tres»
            self.en("tres")
            self.play(flechas[2].animate.set_color(AMBAR).set_stroke(width=5),
                      dados[2].animate.scale(1.35),
                      nums[2].animate.set_color(AMBAR).scale(1.4), run_time=self.dur(0.7))
            self.play(Indicate(nums[2], color=AMBAR, scale_factor=1.3), run_time=self.dur(0.6))

            # «un proceso aleatorio»
            self.en("proceso")
            self.play(FadeOut(recta), FadeOut(marcas), FadeOut(nums), run_time=0.3)
            self.play(flechas[2].animate.set_color(INK).set_stroke(width=2.5), dados[2].animate.scale(1 / 1.35),
                      run_time=0.25)
            bases = VGroup(*[Line([xr, y, 0], [xr + 5.9, y, 0], color=INK, stroke_width=1.5) for y in ys])
            self.play(FadeIn(bases), run_time=0.4)

            # «un paso más»
            self.en("paso")
            mas = etiqueta("un paso más", AMBAR, 0.6, BOLD).move_to([2.9, 3.15, 0])
            self.pop(mas)
            Xt = formula("X", "(t)", colores={0: AMBAR}, escala=1.2).move_to(X)
            self.play(ReplacementTransform(X, Xt), run_time=0.4)

            # «a cada resultado del experimento le pone»
            self.en("a_cada")
            self.play(LaggedStart(*[d.animate(rate_func=there_and_back).scale(1.25) for d in dados], lag_ratio=0.12),
                      run_time=self.dur(1.3))

            # «una señal entera»
            self.en("senal")
            t = np.linspace(0, 1, 160)
            curvas = VGroup(*[traza(xr + t * 5.9, y + 0.33 * np.clip(serie(40 + k, 160, 0.9), -2.1, 2.1) / 2.1 * 1.0,
                                    SENAL, 3.0) for k, y in enumerate(ys)])
            self.play(LaggedStart(*[Create(c) for c in curvas], lag_ratio=0.15), run_time=self.dur(2.2))
            self.dados, self.flechas, self.curvas, self.bases, self.mas, self.Xt, self.res = (
                dados, flechas, curvas, bases, mas, Xt, res)
            self.ys, self.xr = ys, xr

    # ---------------------------------------------------------------- b2: realización y ensemble
    def ensemble(self):
        dados, flechas, curvas, bases = self.dados, self.flechas, self.curvas, self.bases
        ys, xr = self.ys, self.xr
        with self.narrar("b2"):
            # «se llama realización»
            self.en("realizacion")
            self.play(FadeOut(self.mas), curvas[2].animate.set_stroke(AMBAR, width=6), run_time=0.4)
            rot = etiqueta("realización", AMBAR, 0.6, BOLD).move_to([2.9, 3.15, 0])
            self.pop(rot)

            # «la que ha salido esta vez»
            self.en("salido")
            esta = etiqueta("esta vez", AMBAR, 0.45).move_to([xr + 6.55, ys[2], 0])
            self.play(FadeIn(esta, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «el conjunto de todas las realizaciones posibles»
            self.en("conjunto")
            caja_ = SurroundingRectangle(curvas, color=AMBAR, buff=0.2, corner_radius=0.15, stroke_width=3)
            self.play(Create(caja_), FadeOut(esta), run_time=self.dur(0.8))

            # «cada una con su probabilidad»
            self.en("prob")
            ps = VGroup(*[etiqueta(f"p{'₁₂₃₄₅₆'[k]}", TXT, 0.55).move_to([xr + 6.9, y, 0]) for k, y in enumerate(ys)])
            self.play(FadeOut(caja_), LaggedStart(*[FadeIn(p, scale=0.6) for p in ps], lag_ratio=0.12),
                      run_time=self.dur(1.2))

            # «se llama el ensemble»
            self.en("ensemble")
            ens = self.palabra("ensemble", AMBAR, 1.0).move_to([2.9, 3.15, 0])
            self.play(FadeOut(rot), run_time=0.15)
            self.pop(ens)

            # «mil grabaciones del mismo fenómeno»
            self.en("mil")
            self.play(FadeOut(ps), FadeOut(dados), FadeOut(flechas), FadeOut(self.res), FadeOut(self.Xt),
                      run_time=0.3)
            rng = np.random.default_rng(8)
            t = np.linspace(0, 1, 160)
            extras, desp = [], []
            for i in range(34):
                off = float(rng.uniform(-2.2, 2.2))
                c = traza(xr + t * 5.9, off + 0.33 * np.clip(serie(100 + i, 160, 0.9), -2.1, 2.1) / 2.1,
                          SENAL, 2.2, 0.55)
                extras.append(c)
                desp.append(off)
            self.play(LaggedStart(*[Create(c) for c in extras], lag_ratio=0.05), run_time=self.dur(2.6))

            # «una encima de otra»
            self.en("encima")
            self.play(FadeOut(bases), run_time=0.2)
            corr = LEFT * 2.65
            anims = [c.animate.shift(DOWN * off + corr).stretch(2.6, 1, about_point=ORIGIN)
                     for c, off in zip(extras, desp)]
            anims += [c.animate.shift(DOWN * y + corr).stretch(2.6, 1, about_point=ORIGIN)
                      for c, y in zip(curvas, ys)]
            anims.append(ens.animate.move_to([0, 3.15, 0]))
            self.play(*anims, run_time=self.dur(1.8), rate_func=smooth)
