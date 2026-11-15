"""Escena 06 — En cada frecuencia, dos procesos son dos variables; el filtro actúa por separado en cada Ω."""
from comun.escena import *


class EnCadaFrecuenciaDosVariables(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.parte_b3()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        r1 = formula("a", "=", r"C_{xx}^{-1}", "c", escala=1.3, colores={0: ESTIMACION, 2: MEDIDA}).move_to([-1.0, 1.9, 0])
        r2 = formula(r"H(\Omega)", "=", r"S_{xx}^{-1}", r"S_{yx}", escala=1.3,
                     colores={0: ESTIMACION, 2: MEDIDA}).move_to([-1.0, -0.4, 0])
        r2.shift(RIGHT * (r1[2].get_x() - r2[2].get_x()))
        l_inv = Text("matriz de covarianzas", color=AMBAR).scale(0.55).next_to(r1[2], DOWN, buff=0.25)
        l_vec = Text("vector de covarianzas cruzadas", color=AMBAR).scale(0.55).next_to(r1[3], UP, buff=0.4)
        c11 = Text("Cap. 11", color=INK).scale(0.65).move_to([5.6, 3.4, 0])
        Ly = Lienzo(ancho=2.8, alto=0.6, t_rango=(0, 1), v_max=2.5, centro=(-3.6, -2.4))
        Lx = Lienzo(ancho=2.8, alto=0.6, t_rango=(0, 1), v_max=2.5, centro=(-3.6, -3.2))
        t = np.linspace(0, 1, 90)
        y, v, x = registro_e3(90)
        ty = Ly.curva(t, y * 0.6, SENAL, 3)
        tx = Lx.curva(t, x * 0.6, MEDIDA, 3)
        paso = flecha([-1.7, -2.8, 0], [0.5, -2.8, 0], INK, 3)
        o = np.array([1.4, -3.4, 0.0])
        fy = Arrow(o, o + np.array([1.7, 1.5, 0]) * 0.9, buff=0, color=SENAL, stroke_width=6, max_tip_length_to_length_ratio=0.2)
        fx = Arrow(o, o + RIGHT * 2.0, buff=0, color=MEDIDA, stroke_width=6, max_tip_length_to_length_ratio=0.2)
        with self.narrar("b1"):
            self.en("varias")                                # «varias variables»
            self.play(FadeIn(r1[0]), FadeIn(r1[1]), run_time=0.5)
            self.en("inv")                                   # «la inversa de la matriz de covarianzas»
            self.play(FadeIn(r1[2]), FadeIn(l_inv), run_time=0.6)
            self.en("vec")                                   # «el vector de covarianzas cruzadas»
            self.play(FadeIn(r1[3]), FadeIn(l_vec), run_time=0.6)
            self.en("hmat")                                  # «la densidad de equis hace de matriz»
            self.play(FadeIn(r2[2], shift=DOWN * 0.3), run_time=0.5)
            self.en("hvec")                                  # «la cruzada de vector»
            self.play(FadeIn(r2[3], shift=DOWN * 0.3), run_time=0.5)
            self.en("igual")                                 # «la misma fórmula»
            self.play(FadeIn(r2[0]), FadeIn(r2[1]), run_time=0.5)
            self.resaltar(r2, color=AMBAR, escala=1.05)
            self.en("cap11")                                 # «el capítulo once»
            self.pop(c11)
            self.en("dosvar")                                # «dos procesos son dos variables»
            self.play(Create(ty), Create(tx), run_time=0.7)
            self.play(Create(paso), run_time=0.3)
            self.play(Create(fy), Create(fx), run_time=0.5)

    def parte_b2(self):
        L = lienzo_omega(ancho=10.0, alto=1.1, v_max=1.0, centro=(0.0, 2.2))
        cajas = rebanadas_omega(L, 7, alto=1.1)
        hs = VGroup(*[MathTex("H", color=ESTIMACION).scale(0.7).move_to(c) for c in cajas])
        om = MathTex(r"\Omega", color=INK).scale(0.8).next_to(cajas, RIGHT, buff=0.15)
        cruces = VGroup(*[cruz(ROJO, 0.22).move_to([(cajas[i].get_right()[0]), 1.3, 0]) for i in range(6)])
        Ly = Lienzo(ancho=4.0, alto=0.9, t_rango=(0, 1), v_max=2.5, centro=(-3.6, -0.4))
        Lx = Lienzo(ancho=4.0, alto=0.9, t_rango=(0, 1), v_max=2.5, centro=(-3.6, -1.7))
        t = np.linspace(0, 1, 100)
        y, v, x = registro_e3(100, 5)
        ty = Ly.curva(t, y * 0.7, SENAL, 3)
        tx = Lx.curva(t, x * 0.7, MEDIDA, 3)
        ly = MathTex("y", color=SENAL).scale(0.8).next_to(Ly.p(0, 0), LEFT, buff=0.3)
        lx = MathTex("x", color=MEDIDA).scale(0.8).next_to(Lx.p(0, 0), LEFT, buff=0.3)
        barrido = Line([-4.9, 2.9, 0], [-4.9, 1.5, 0], color=AMBAR, stroke_width=5)
        F, rt = flechas_xy(origen=(1.5, -3.0), largo=2.6, angulo=45.0)
        with self.narrar("b2"):
            self.corte()
            self.en("razon")                                 # «Hay una razón profunda»
            self.play(LaggedStart(*[FadeIn(c) for c in cajas], lag_ratio=0.1), FadeIn(om), run_time=self.dur(1.0))
            self.en("separado")                              # «el filtro actúa por separado»
            self.play(LaggedStart(*[FadeIn(h, scale=0.5) for h in hs], lag_ratio=0.12), run_time=self.dur(1.4))
            self.en("omega")                                 # «en cada omega»
            self.play(cajas[1].animate.set_fill(AMBAR, 0.35), run_time=0.3)
            self.play(cajas[1].animate.set_fill(INK, 0.06), cajas[4].animate.set_fill(AMBAR, 0.35), run_time=0.4)
            self.play(cajas[4].animate.set_fill(INK, 0.06), run_time=0.3)
            self.en("noafecta")                              # «no afecta a las demás»
            self.play(LaggedStart(*[FadeIn(c, scale=0.4) for c in cruces], lag_ratio=0.15), run_time=self.dur(1.2))
            self.en("proceso")                               # «Estimar un proceso a partir de otro»
            self.play(Create(ty), Create(tx), FadeIn(ly), FadeIn(lx), run_time=0.8)
            self.en("fxf")                                   # «frecuencia por frecuencia»
            self.play(FadeIn(barrido), run_time=0.2)
            self.play(barrido.animate(rate_func=linear).shift(RIGHT * 9.8), run_time=self.dur(2.0, 0.3))
            self.en("variable")                              # «una variable a partir de otra»
            self.play(FadeOut(barrido), Create(F.presente), Create(F.futuro), run_time=0.5)
            self.play(Create(F.sombra), Create(F.error), FadeIn(rt["x"]), FadeIn(rt["y"]), run_time=0.5)

    def parte_b3(self):
        tm = termometro(alto=2.0, color=ROJO, nivel=0.6).move_to([-5.2, 0.9, 0])
        t = np.linspace(0, 1, 120)
        rng = np.random.default_rng(3)
        cable = traza(-4.4 + t * 3.0, 0.9 + 0.35 * rng.normal(0, 1, 120), RUIDO, 2.5)
        reloj = reloj_arena().scale(0.9).move_to([5.6, 3.0, 0])
        Ll = Lienzo(ancho=4.5, alto=0.9, t_rango=(0, 1), v_max=2.5, centro=(3.2, 2.0))
        Lr = Lienzo(ancho=4.5, alto=0.9, t_rango=(0, 1), v_max=2.5, centro=(3.2, 0.0))
        lenta = Ll.curva(t, 0.6 * serie(8, 120, 0.97), SENAL, 3.5)
        rapida = Lr.curva(t, 0.5 * serie(9, 120, 0.0), RUIDO, 2.5)
        t_len = etiqueta("cambia despacio", SENAL, 0.6).move_to(Ll.p(0.5, 0) + UP * 0.8)
        t_rap = etiqueta("cambia deprisa", RUIDO, 0.6).move_to(Lr.p(0.5, 0) + UP * 0.8)
        La = lienzo_omega(ancho=8.0, alto=1.0, v_max=1.0, centro=(0.0, -2.0))
        eje = eje_omega(La, 0.0)
        interr = MathTex("?", color=AMBAR).scale(1.6).move_to([0, -1.3, 0])
        bajas = caja("bajas", AZUL, ancho=2.2, alto=0.8, scale=0.55).move_to([-2.5, -3.5, 0])
        altas = caja("altas", MAGENTA, ancho=2.2, alto=0.8, scale=0.55).move_to([2.5, -3.5, 0])
        with self.narrar("b3"):
            self.en("sensor")                                # «el sensor»
            self.corte()
            self.play(FadeIn(tm), Create(cable), run_time=0.8)
            self.en("piensa")                                # «Piénsalo antes de seguir»
            self.pop(reloj)
            self.en("lenta")                                 # «la temperatura cambia despacio»
            self.play(Create(lenta), FadeIn(t_len), run_time=0.8)
            self.en("rapido")                                # «el ruido cambia deprisa»
            self.play(Create(rapida), FadeIn(t_rap), run_time=0.8)
            self.en("preg")                                  # «¿en qué frecuencias»
            self.play(Create(eje.h), FadeIn(eje.rotulos), run_time=0.5)
            self.pop(interr)
            self.en("fiar")                                  # «te fiarías más»
            self.play(FadeIn(bajas, shift=UP * 0.2), FadeIn(altas, shift=UP * 0.2), run_time=0.5)
