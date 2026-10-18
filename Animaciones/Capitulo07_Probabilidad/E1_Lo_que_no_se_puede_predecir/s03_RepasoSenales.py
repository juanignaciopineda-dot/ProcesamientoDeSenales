"""Escena 03 — Repaso de señales: qué es una señal, continua y discreta, muestrear."""
from comun.escena import *


class RepasoSenales(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.t = np.linspace(0, 2, 260)
        self.L = Lienzo(ancho=7.6, alto=2.6, t_rango=(0, 2), v_max=1.3, centro=(1.2, -0.3))
        self.bloque_senal()
        self.bloque_discreta()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def bloque_senal(self):
        L, t = self.L, self.t
        voz = 0.95 * voz_valores(260)
        tension = 0.9 * np.sin(2 * np.pi * 3 * t) + 0.25 * np.sin(2 * np.pi * 8 * t)
        temp = 0.75 * np.sin(2 * np.pi * 0.6 * t + 0.5) + 0.2 * np.sin(2 * np.pi * 1.3 * t)
        self.v_actual = voz

        with self.narrar("b1"):
            # «un repaso»
            self.en("repaso")
            rel = reloj().scale(0.8)
            tit = Text("Señales y Sistemas", color=TXT, weight=BOLD).scale(0.8)
            cab = VGroup(rel, tit).arrange(RIGHT, buff=0.35).move_to([0, 3.3, 0])
            rel.save_state()
            self.pop(rel)

            # «muy por encima»
            self.en("encima")
            enc = Text("Muy por encima", color=INK).scale(0.5).move_to([0, 2.65, 0])
            self.play(FadeIn(enc, shift=UP * 0.1), run_time=self.dur(0.4))

            # «Señales y Sistemas»
            self.en("sys")
            self.pop(tit)

            # «Una señal es algo que cambia con el tiempo»
            self.en("senal")
            self.base = L.base()
            self.c = L.curva(t, voz, SENAL, 4.0)
            self.eje = eje_v7(L, -1.3, 1.3)
            self.play(Create(self.base), Create(self.eje), run_time=0.3)
            self.play(Create(self.c), run_time=self.dur(1.0), rate_func=linear)

            # «y lleva información»
            self.en("info")
            inf = Text("Lleva información", color=AMBAR).scale(0.55).move_to([1.2, -2.3, 0])
            self.play(FadeIn(inf, shift=UP * 0.1), run_time=self.dur(0.4))

            # «la voz que capta un micrófono»
            self.en("microfono")
            mic = microfono(AMBAR).scale(1.0).move_to([-5.7, 1.3, 0])
            l_mic = Text("Voz", color=TXT).scale(0.5).next_to(mic, RIGHT, buff=0.25)
            self.pop(VGroup(mic, l_mic))

            # «la tensión en un cable»
            self.en("cable")
            ray = rayo(AMBAR).scale(0.8).move_to([-5.7, -0.2, 0])
            l_ray = Text("Tensión", color=TXT).scale(0.5).next_to(ray, RIGHT, buff=0.25)
            c2 = L.curva(t, tension, SENAL, 4.0)
            self.play(FadeIn(ray), FadeIn(l_ray), ReplacementTransform(self.c, c2), run_time=self.dur(0.6))
            self.c, self.v_actual = c2, tension

            # «la temperatura de una habitación»
            self.en("habitacion")
            ter = termometro(1.3, ROJO, 0.6).move_to([-5.7, -1.8, 0])
            l_ter = Text("Temperatura", color=TXT).scale(0.5).next_to(ter, RIGHT, buff=0.25)
            c3 = L.curva(t, temp, SENAL, 4.0)
            self.play(FadeIn(ter), FadeIn(l_ter), ReplacementTransform(self.c, c3), run_time=self.dur(0.6))
            self.c, self.v_actual = c3, temp

            # «es una función»
            self.en("funcion")
            fx = formula("x", "(", "t", ")", colores={0: SENAL, 2: AMBAR}, escala=1.3).move_to([4.6, 1.9, 0])
            self.pop(fx)

            # «a cada instante le toca un valor»
            self.en("valor")
            cur = Cursor7(L, t, temp, AMBAR, t_ini=0.1)
            self.play(FadeIn(cur), run_time=0.25)
            self.play(cur.barrer(0.1, 1.5), run_time=self.dur(1.6), rate_func=smooth)
            self.viejos = [cab, enc, inf, mic, l_mic, ray, l_ray, ter, l_ter, fx, cur]

    # ------------------------------------------------------------ b2
    def bloque_discreta(self):
        L, t = self.L, self.t
        v = self.v_actual

        with self.narrar("b2"):
            # «un valor en cada instante»
            self.en("cont")
            lab1 = Text("Continuo", color=SENAL, weight=BOLD).scale(0.65).move_to([-3.6, 3.1, 0])
            self.play(*[FadeOut(m) for m in self.viejos], FadeIn(lab1), run_time=0.4)

            # «sin huecos»
            self.en("sin_huecos")
            self.play(self.c.animate(rate_func=there_and_back).set_stroke(width=8), run_time=self.dur(0.8))

            # «cada cierto tiempo»
            self.en("cada")
            ks = np.linspace(0.125, 1.875, 15)
            ticks = VGroup(*[Line(L.p(k, -1.3), L.p(k, 1.3), color=INK, stroke_width=1.6, stroke_opacity=0.7) for k in ks])
            self.play(LaggedStart(*[Create(m) for m in ticks], lag_ratio=0.08), run_time=self.dur(0.9))

            # «mil veces por segundo»
            self.en("mil")
            cada = Text("1.000 veces por segundo", color=AMBAR).scale(0.55).move_to([1.2, -2.3, 0])
            self.pop(cada)

            # «una lista de números»
            self.en("lista")
            puntos = VGroup(*[Dot([float(L.x(k)), float(L.y(np.interp(k, t, v))), 0], radius=0.07, color=AMBAR) for k in ks])
            nums = VGroup(*[Text(num(float(np.interp(k, t, v))), color=TXT).scale(0.5) for k in ks[:5]])
            nums.arrange(DOWN, buff=0.3).move_to([6.2, 0.3, 0])
            pts = Text("⋮", color=INK).scale(0.7).next_to(nums, DOWN, buff=0.15)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in puntos], lag_ratio=0.05),
                      LaggedStart(*[FadeIn(n) for n in nums], FadeIn(pts), lag_ratio=0.1), run_time=self.dur(1.2))

            # «tiempo discreto»
            self.en("discreto")
            lab2 = Text("Discreto", color=AMBAR, weight=BOLD).scale(0.65).move_to([3.4, 3.1, 0])
            self.play(FadeOut(self.c), FadeOut(ticks), run_time=0.3)
            self.pop(lab2)

            # «la que manejan los ordenadores»
            self.en("ordenador")
            pc = ordenador().scale(1.3).move_to([-4.6, -2.5, 0])
            self.pop(pc)

            # «Pasar de una a otra»
            self.en("pasar")
            fl = Arrow([-2.2, 3.1, 0], [2.3, 3.1, 0], color=INK, stroke_width=4, buff=0.05)
            self.play(GrowArrow(fl), run_time=self.dur(0.5))

            # «muestrear»
            self.en("muestrear")
            pal = Text("Muestrear", color=AMBAR, weight=BOLD).scale(0.55).move_to([0, 3.62, 0])
            self.pop(pal)
