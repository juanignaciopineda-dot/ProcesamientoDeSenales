"""Escena 10 — Autocovarianza de la moneda (un impulso) y el sensor de temperatura con memoria (× 0,6 por paso)."""
from comun.escena import *


class ImpulsoYSensor(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        pal = Palitos(range(0, 7), [1, 0, 0, 0, 0, 0, 0], ancho=4.6, alto=2.2, v_max=1.0, centro=(-3.8, 1.5))
        L = Lienzo(ancho=4.4, alto=2.4, t_rango=(0, 1), v_max=3.6, centro=(4.6, 0.6))
        t = np.linspace(0, 1, 240)
        v = 1.3 * serie(41, 240, 0.95)
        senal = L.curva(t, v, SENAL, 3.2)
        with self.narrar("b1"):
            # «solo se parece a sí misma»
            self.en("solo_igual")
            c = formula("C", escala=0.9, colores={0: AMBAR}).move_to([-6.3, 2.7, 0])
            self.play(FadeIn(pal.base), FadeIn(pal.eje), FadeIn(c), run_time=self.dur(0.6))

            # «en el mismo instante»
            self.en("mismo")
            m0 = Dot(pal.pos(0, 0), radius=0.1, color=AMBAR)
            self.play(FadeIn(m0, scale=2), run_time=0.4)

            # «un pico solitario»
            self.en("pico")
            self.play(Create(pal.tallos[0]), FadeIn(pal.puntos[0]), run_time=self.dur(0.6))

            # «un impulso»
            self.en("impulso")
            w = self.palabra("impulso", AMBAR, 1.0).move_to([-3.8, 3.3, 0])
            self.pop(w)

            # «un tercer ejemplo»
            self.en("tercero")
            tercer = etiqueta("tercer ejemplo", INK, 0.6).move_to([4.6, 3.3, 0])
            self.play(FadeIn(tercer), run_time=0.4)

            # «un sensor de temperatura»
            self.en("sensor")
            term = termometro(1.6, ROJO, 0.55).move_to([1.4, 0.9, 0])
            tt = Text("20 °C", color=TXT, weight=BOLD).scale(0.55).move_to([1.4, -0.5, 0])
            self.play(FadeIn(term), FadeIn(tt), Create(L.base()), run_time=self.dur(0.6))
            self.play(Create(senal), run_time=self.dur(1.2), rate_func=linear)

            # «Media, veinte grados»
            self.en("media20")
            media = L.base(AMBAR, 5)
            mu = formula(r"\mu", "=", "20", colores={0: AMBAR}, escala=0.9).move_to([5.9, 2.15, 0])
            self.play(Create(media), run_time=0.4)
            self.pop(mu)

            # «Varianza, cuatro»
            self.en("var4")
            banda = Rectangle(width=L.ancho, height=2 * 2 / 3.6 * L.alto / 2, stroke_width=0).set_fill(AMBAR, 0.15)
            banda.move_to(L.p(0.5, 0))
            s2 = formula(r"\sigma^{2}", "=", "4", colores={0: AMBAR}, escala=0.9).move_to([4.6, -1.15, 0])
            self.play(FadeIn(banda), run_time=0.4)
            self.pop(s2)

            # «con memoria»
            self.en("con_memoria")
            self.play(senal.animate.set_stroke(width=5), run_time=0.4)

            # «dos muestras seguidas»
            self.en("seguidas")
            va = L.vertical(t[110], AMBAR, 3, mitad=1.25)
            vb = L.vertical(t[122], TXT, 3, mitad=1.25)
            self.play(Create(va), Create(vb), run_time=0.4)

            # «dos coma cuatro»
            self.en("c1")
            c1 = formula("C[1]", "=", "2{,}4", escala=0.95).move_to([-3.8, -1.0, 0])
            self.pop(c1)

            # «dos pasos de separación»
            self.en("dos_pasos")
            self.play(vb.animate.set_x(float(L.x(t[134]))), run_time=0.5)

            # «uno coma cuatro cuatro»
            self.en("c2")
            c2 = formula("C[2]", "=", "1{,}44", escala=0.95).move_to([-3.8, -1.9, 0])
            self.pop(c2)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        filas = [("C[0]", "4"), ("C[1]", "2{,}4"), ("C[2]", "1{,}44")]
        ys = [1.6, 0.4, -0.8]
        nums = [formula(a, "=", b, escala=1.0).move_to([-5.6, y, 0]) for (a, b), y in zip(filas, ys)]
        divs = [formula(r"\div 4", escala=0.9, color=INK).move_to([-3.3, y, 0]) for y in ys]
        rhos = [formula(s, escala=1.2, colores={0: AMBAR}).move_to([-1.6, y, 0]) for s, y in zip(["1", "0{,}6", "0{,}36"], ys)]
        rho_t = formula(r"\rho", escala=1.0, colores={0: AMBAR}).move_to([-1.6, 2.6, 0])
        a1 = flecha([-0.2, ys[0] - 0.25, 0], [-0.2, ys[1] + 0.25, 0], AMBAR, 3)
        a2 = flecha([-0.2, ys[1] - 0.25, 0], [-0.2, ys[2] + 0.25, 0], AMBAR, 3)
        l1 = formula(r"\times 0{,}6", escala=0.8, colores={0: AMBAR}).move_to([1.0, (ys[0] + ys[1]) / 2, 0])
        l2 = formula(r"\times 0{,}6", escala=0.8, colores={0: AMBAR}).move_to([1.0, (ys[1] + ys[2]) / 2, 0])
        L = Lienzo(ancho=4.2, alto=2.4, t_rango=(0, 1), v_max=3.0, centro=(4.9, -1.0))
        t = np.linspace(0, 1, 200)
        v = np.where(t < 0.3, 1.3 + 0.1 * np.sin(40 * t), 1.3 * np.exp(-1.6 * (t - 0.3)))
        with self.narrar("b2"):
            # «¿Qué quieren decir esos números?»
            self.en("pregunta")
            self.corte()
            self.play(LaggedStart(*[FadeIn(n, shift=RIGHT * 0.2) for n in nums], lag_ratio=0.2), run_time=self.dur(0.8))

            # «Divide entre la varianza»
            self.en("divide")
            self.play(LaggedStart(*[FadeIn(d) for d in divs], lag_ratio=0.15), run_time=self.dur(0.6))

            # «el coeficiente de correlación»
            self.en("rho")
            self.play(FadeIn(rho_t), LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in rhos], lag_ratio=0.2),
                      run_time=self.dur(1.0))

            # «cero coma seis entre muestras seguidas»
            self.en("r1")
            self.play(rhos[1].animate(rate_func=there_and_back).scale(1.35), run_time=0.6)

            # «cero coma tres seis»
            self.en("r2")
            self.play(rhos[2].animate(rate_func=there_and_back).scale(1.35), run_time=0.6)

            # «con dos pasos de separación»
            self.en("sep2")
            marco = SurroundingRectangle(VGroup(nums[2], rhos[2]), color=INK, buff=0.15, stroke_width=2)
            self.play(Create(marco), run_time=0.4)

            # «En cada paso»
            self.en("cada_paso")
            self.play(FadeOut(marco), GrowArrow(a1), FadeIn(l1), run_time=0.5)

            # «se multiplica por cero coma seis»
            self.en("por06")
            self.play(GrowArrow(a2), FadeIn(l2), run_time=0.5)

            # «Si ahora hace calor»
            self.en("calor")
            term = termometro(1.7, ROJO, 0.85).move_to([4.9, 1.6, 0])
            self.play(FadeIn(term), Create(L.base()), run_time=self.dur(0.6))
            fija = L.curva(t[:61], v[:61], SENAL, 4)
            self.play(Create(fija), run_time=self.dur(0.8), rate_func=linear)

            # «probablemente también»
            self.en("tambien")
            sigue = L.curva(t[60:], v[60:], SENAL, 4)
            self.play(Create(sigue), run_time=self.dur(1.2), rate_func=linear)

            # «cada vez es menos seguro»
            self.en("menos_seguro")
            ta = t[60:]
            k = 1.4 * (ta - 0.3) / 0.7
            sup = [L.p(x, y) for x, y in zip(ta, v[60:] + k)]
            inf = [L.p(x, y) for x, y in zip(ta[::-1], (v[60:] - k)[::-1])]
            banda = Polygon(*sup, *inf, stroke_width=0).set_fill(AMBAR, 0.2)
            self.play(FadeIn(banda), run_time=self.dur(1.2))
