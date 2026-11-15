"""Escena 11 — Deshacer un borrón: el filtro inverso 1/G amplifica el ruido donde G es pequeño."""
from comun.escena import *


class ElBorron(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.parte_b3()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        ent = MathTex("y[n]", color=SENAL).scale(0.9).move_to([-5.6, 1.0, 0])
        a1 = flecha([-4.8, 1.0, 0], [-3.7, 1.0, 0], INK, 3)
        G = caja("G", AZUL, ancho=1.4, alto=1.0, scale=0.7).move_to([-3.0, 1.0, 0])
        a2 = flecha([-2.3, 1.0, 0], [-0.75, 1.0, 0], INK, 3)
        suma = VGroup(Circle(radius=0.32, color=TXT, stroke_width=3.5).set_fill(FONDO, 1),
                      MathTex("+", color=TXT).scale(0.8)).move_to([-0.4, 1.0, 0])
        v = MathTex("v[n]", color=RUIDO).scale(0.9).move_to([-0.4, -0.5, 0])
        av = Arrow([-0.4, -0.2, 0], [-0.4, 0.65, 0], buff=0, color=RUIDO, stroke_width=3.5,
                   max_tip_length_to_length_ratio=0.3)
        a3 = flecha([0.1, 1.0, 0], [1.7, 1.0, 0], INK, 3)
        sal = MathTex("x[n]", color=MEDIDA).scale(0.9).move_to([2.5, 1.0, 0])
        foto_m = foto(INK, nitida=False).scale(1.1).move_to([-5.0, -2.1, 0])
        tm = termometro(alto=1.3, color=ROJO, nivel=0.5).move_to([-2.8, -2.0, 0])
        l_prom = Text("promediador (½, ½)", color=AMBAR).scale(0.45).next_to(G, DOWN, buff=0.25)
        media = formula("r[n]", "=", r"\frac{y[n]+y[n-1]}{2}", escala=1.2,
                        colores={0: SENAL}).move_to([2.9, -2.1, 0])
        self.b1 = VGroup(ent, a1, G, a2, suma, v, av, a3, sal, foto_m, tm, l_prom, media)
        with self.narrar("b1"):
            self.en("otro")                                  # «Otro caso»
            self.play(FadeIn(ent), Create(a1), run_time=0.5)
            self.en("sistema")                               # «emborronada por un sistema»
            self.play(FadeIn(G, shift=RIGHT * 0.3), Create(a2), run_time=0.6)
            self.en("ruido")                                 # «ruido»
            self.play(FadeIn(suma), FadeIn(v), Create(av), Create(a3), FadeIn(sal), run_time=0.7)
            self.en("foto")                                  # «una foto movida»
            self.play(FadeIn(foto_m), run_time=0.5)
            self.en("inercia")                               # «un sensor con inercia»
            self.play(FadeIn(tm), run_time=0.5)
            self.en("sencillo")                              # «el emborronador más sencillo»
            self.resaltar(G, color=AMBAR)
            self.en("prom")                                  # «el promediador de dos muestras»
            self.play(FadeIn(l_prom), run_time=0.5)
            self.en("media")                                 # «la media de la temperatura de ahora y la anterior»
            self.play(FadeIn(media[0]), FadeIn(media[1]), run_time=0.4)
            self.play(FadeIn(media[2]), run_time=0.6)

    def parte_b2(self):
        L = lienzo_omega(ancho=5.6, alto=6.0, v_max=1.1, centro=(-3.2, -2.2))
        eje = eje_omega(L, 1.15)
        curva = curva_f(L, g_prom, 0.0, np.pi, SENAL, 5, n=200)
        pts = [(0.0, "1"), (np.pi / 2, "0,71"), (0.9 * np.pi, "0,16"), (np.pi, "0")]
        dots = [Dot(L.p(w, float(g_prom(w))), radius=0.1, color=AMBAR) for w, _ in pts]
        txts = [Text(t, color=AMBAR, weight=BOLD).scale(0.5) for _, t in pts]
        txts[0].next_to(dots[0], UP, buff=0.2)
        txts[1].next_to(dots[1], UR, buff=0.3)
        txts[2].next_to(dots[2], UL, buff=0.3)
        txts[3].next_to(dots[3], RIGHT, buff=0.25)
        t_g = MathTex(r"|G(\Omega)|", color=SENAL).scale(1.0).move_to([-5.0, 2.0, 0])
        altas = ventana(L, 0.78 * np.pi, np.pi, 1.15, ROJO, 0.18)
        altas.permitir_encima = True
        L2 = lienzo_omega(ancho=5.0, alto=6.0, v_max=8.5, centro=(4.0, -2.2))
        eje2 = eje_omega(L2, 8.3)
        inv = curva_f(L2, lambda w: h_inverso(w, 8.0), 0.0, np.pi, AMBAR, 5, n=300)
        t_i = MathTex(r"\frac{1}{|G|}", color=AMBAR).scale(1.1).move_to([2.2, 2.2, 0])
        preg = Text("¿?", color=AMBAR, weight=BOLD).scale(1.0).move_to([0.3, 0.9, 0])
        flecha_i = flecha([-0.15, -0.6, 0], [1.4, -0.6, 0], AMBAR, 4)
        inverso = formula("1", "/", "G", escala=1.2, colores={0: AMBAR, 1: AMBAR, 2: AMBAR}).move_to([0.5, -0.1, 0])
        self.L, self.L2, self.dots, self.inv, self.altas = L, L2, dots, inv, altas
        self.eje, self.eje2 = eje, eje2
        with self.narrar("b2"):
            self.corte()
            self.en("g1")                                    # «Su ganancia es uno»
            self.play(Create(eje.h), Create(eje.v), FadeIn(eje.rotulos), FadeIn(t_g), run_time=0.4)
            self.play(Create(curva), FadeIn(dots[0], scale=2), FadeIn(txts[0]), run_time=self.dur(1.0))
            self.en("g71")                                   # «cero coma siete uno en pi medios»
            self.play(FadeIn(dots[1], scale=2), FadeIn(txts[1]), run_time=0.3)
            self.en("g16")                                   # «cero coma uno seis en cero coma nueve pi»
            self.play(FadeIn(dots[2], scale=2), FadeIn(txts[2]), run_time=0.3)
            self.en("g0")                                    # «cero en pi»
            self.play(FadeIn(dots[3], scale=2), FadeIn(txts[3]), run_time=0.3)
            self.en("altas")                                 # «las altas casi desaparecen»
            self.play(FadeIn(altas), run_time=0.5)
            self.en("ingenua")                               # «La idea ingenua»
            self.pop(preg)
            self.en("inverso")                               # «uno entre ge»
            self.play(FadeOut(preg), FadeIn(inverso), Create(flecha_i), run_time=0.5)
            self.en("contrario")                             # «lo contrario»
            self.play(Create(eje2.h), Create(eje2.v), FadeIn(eje2.rotulos), FadeIn(t_i), run_time=0.4)
            self.play(Create(inv), run_time=self.dur(1.0))
        self.izq = VGroup(inverso, flecha_i)

    def parte_b3(self):
        L2 = self.L2
        w9 = 0.9 * np.pi
        guia_i = DashedLine(self.L.p(w9, 0), self.L.p(w9, 1.15), color=AMBAR, stroke_width=3)
        guia_d = DashedLine(L2.p(w9, 0), L2.p(w9, 8.3), color=AMBAR, stroke_width=3)
        dp = Dot(L2.p(w9, 6.39), radius=0.1, color=ROJO)
        t639 = MathTex(r"\times 6{,}39", color=ROJO).scale(0.8).next_to(dp, LEFT, buff=0.2)
        t41 = Text("potencia del ruido × 41", color=ROJO).scale(0.65).move_to([3.6, 3.3, 0])
        barra = Rectangle(width=0.6, height=0.45, color=INK, stroke_width=0).set_fill(INK, 0.9).move_to([-3.0 + 0.3, -3.5, 0])
        grande = Rectangle(width=3.6, height=0.45, color=RUIDO, stroke_width=0).set_fill(RUIDO, 0.9).move_to([-3.0 + 1.8, -3.5, 0])
        l_r = Text("ruido", color=RUIDO).scale(0.65).next_to(grande, RIGHT, buff=0.25)
        inf = Arrow(L2.p(np.pi, 7.0), L2.p(np.pi, 8.4), buff=0, color=ROJO, stroke_width=6, max_tip_length_to_length_ratio=0.4)
        t_inf = MathTex(r"\infty", color=ROJO).scale(1.0).next_to(inf, UP, buff=0.1)
        with self.narrar("b3"):
            self.en("desastre")                              # «con ruido, eso es un desastre»
            self.play(self.inv.animate.set_color(ROJO), self.eje2.h.animate.set_color(INK), run_time=0.5)
            self.en("en09")                                  # «En cero coma nueve pi»
            self.play(Create(guia_i), Create(guia_d), run_time=0.5)
            self.en("x639")                                  # «seis coma tres nueve»
            self.play(FadeIn(dp, scale=2), FadeIn(t639), run_time=0.4)
            self.en("x41")                                   # «la potencia se multiplica por unos cuarenta y uno»
            self.pop(t41)
            self.en("ahi")                                   # «Pero ahí»
            self.resaltar(self.dots[2], color=AMBAR, escala=1.6)
            self.en("nollego")                               # «la señal casi no llegó»
            self.play(self.dots[2].animate.set_color(ROJO), run_time=0.4)
            self.en("por6")                                  # «lo que estamos multiplicando por seis»
            self.play(FadeIn(barra), run_time=0.3)
            self.play(Transform(barra, grande), run_time=self.dur(1.2))
            self.en("esruido")                               # «es el ruido»
            self.play(FadeIn(l_r), run_time=0.4)
            self.en("gcero")                                 # «donde la ganancia de ge es cero»
            self.resaltar(self.dots[3], color=ROJO, escala=1.6)
            self.en("infinito")                              # «habría que multiplicar por infinito»
            self.play(GrowArrow(inf), FadeIn(t_inf), run_time=0.5)
