"""Escena 08 — Conocer las reglas del ruido; estimar y detectar; el mapa del curso."""
from comun.escena import *


class EstimarYDetectar(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.bloque_tareas()
        self.bloque_mapa()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def bloque_tareas(self):
        L = Lienzo(ancho=5.0, alto=2.2, t_rango=(-3, 3), v_max=1.1, centro=(-3.3, 1.9))
        x = np.linspace(-3, 3, 140)
        campana = np.exp(-0.5 * x ** 2)

        with self.narrar("b1"):
            # «conocer sus reglas»
            self.en("reglas")
            base = L.base()
            cur = L.curva(x, campana, RUIDO, 4.0)
            lab = Text("Ruido", color=RUIDO, weight=BOLD).scale(0.55).move_to([-3.3, 3.55, 0])
            eje = eje_v7(L, 0, 1.1, t=0)
            self.play(Create(base), Create(eje), Create(cur), FadeIn(lab), run_time=self.dur(0.9))

            # «qué valores suele tomar»
            self.en("suele")
            banda_ = Rectangle(width=float(L.x(0.8) - L.x(-0.8)), height=L.alto, color=AMBAR, stroke_width=0)
            banda_.set_fill(AMBAR, 0.22).move_to([-3.3, 1.9, 0])
            self.play(FadeIn(banda_), run_time=self.dur(0.4))

            # «cuáles son raros»
            self.en("raros")
            xa, xb = np.linspace(1.8, 3, 30), np.linspace(-3, -1.8, 30)
            colas = VGroup(area_bajo(L, xa, np.exp(-0.5 * xa ** 2), ERROR, 0.6),
                           area_bajo(L, xb, np.exp(-0.5 * xb ** 2), ERROR, 0.6))
            self.play(FadeOut(banda_), FadeIn(colas), run_time=self.dur(0.4))

            # «cómo se relaciona con lo que se envió»
            self.en("relaciona")
            Ls = Lienzo(ancho=3.0, alto=1.3, t_rango=(0, 1), v_max=1.2, centro=(3.8, 1.9))
            env = seno_t(Ls, 2.0, 1.0, SENAL, 3.5)
            fl = DoubleArrow([-0.3, 1.9, 0], [1.6, 1.9, 0], color=INK, stroke_width=4, buff=0.05,
                             max_tip_length_to_length_ratio=0.2)
            le = Text("Enviada", color=SENAL, weight=BOLD).scale(0.5).move_to([3.8, 3.1, 0])
            self.play(GrowArrow(fl), Create(env), FadeIn(le), run_time=self.dur(0.8))

            # «Con esas reglas»
            self.en("con_reglas")
            self.play(cur.animate(rate_func=there_and_back).set_stroke(width=8),
                      env.animate(rate_func=there_and_back).set_stroke(width=8), run_time=self.dur(0.8))

            # «hacemos dos cosas»
            self.en("dos_cosas")
            f1 = VGroup(Circle(radius=0.3, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.25),
                        Text("1", color=AMBAR, weight=BOLD).scale(0.6)).move_to([-3.2, 0.05, 0])
            f2 = VGroup(Circle(radius=0.3, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.25),
                        Text("2", color=AMBAR, weight=BOLD).scale(0.6)).move_to([3.2, 0.05, 0])
            self.pop(f1, f2)

            # «las dos grandes tareas»
            self.en("tareas")
            c1 = RoundedRectangle(corner_radius=0.15, width=5.4, height=2.6, color=INK, stroke_width=3).move_to([-3.2, -1.6, 0])
            c2 = RoundedRectangle(corner_radius=0.15, width=5.4, height=2.6, color=INK, stroke_width=3).move_to([3.2, -1.6, 0])
            self.play(Create(c1), Create(c2), run_time=self.dur(0.6))

            # «Estimar: adivinar lo mejor posible»
            self.en("estimar")
            te = Text("Estimar", color=ESTIMACION, weight=BOLD).scale(0.7).move_to([-3.2, -0.6, 0])
            Le = Lienzo(ancho=4.4, alto=1.1, t_rango=(0, 1), v_max=1.2, centro=(-3.2, -1.9))
            tt = np.linspace(0, 1, 140)
            vera = np.sin(2 * np.pi * 2 * tt)
            real = Le.curva(tt, vera, SENAL, 3.0)
            est = Le.curva(tt, 0.9 * np.sin(2 * np.pi * 2 * tt + 0.15) + 0.04 * serie(2, 140, 0.8), ESTIMACION, 3.0)
            self.pop(te)
            self.play(Create(real), Create(est), run_time=self.dur(0.8))

            # «cuánto valía la señal»
            self.en("valia")
            q = Text("?", color=ROJO, weight=BOLD).scale(1.2).move_to([0.0, -1.9, 0])
            self.pop(q)

            # «Y detectar»
            self.en("detectar")
            td = Text("Detectar", color=VERDE, weight=BOLD).scale(0.7).move_to([3.2, -0.6, 0])
            self.pop(td)

            # «hay señal o solo ruido»
            self.en("senal_o_ruido")
            pr = Text("¿Señal?", color=TXT).scale(0.6).move_to([3.2, -1.3, 0])
            si = caja("Sí", VERDE, ancho=1.2, alto=0.7, scale=0.55).move_to([2.2, -2.2, 0])
            no = caja("No", ROJO, ancho=1.2, alto=0.7, scale=0.55).move_to([4.2, -2.2, 0])
            self.play(FadeIn(pr), run_time=0.25)
            self.play(FadeIn(si), FadeIn(no), run_time=self.dur(0.4))

            # «un uno o un cero»
            self.en("bit")
            uno = caja("1", SENAL, ancho=1.2, alto=0.7, scale=0.55).move_to([2.2, -2.2, 0])
            cero = caja("0", INK, ancho=1.2, alto=0.7, scale=0.55).move_to([4.2, -2.2, 0])
            self.play(ReplacementTransform(si, uno), ReplacementTransform(no, cero), run_time=self.dur(0.5))

    # ------------------------------------------------------------ b2
    def bloque_mapa(self):
        with self.narrar("b2"):
            # «Las dos cosas se hacen con probabilidad»
            self.en("con_prob")
            c1 = RoundedRectangle(corner_radius=0.15, width=4.4, height=2.4, color=ESTIMACION, stroke_width=3)
            c2 = RoundedRectangle(corner_radius=0.15, width=4.4, height=2.4, color=VERDE, stroke_width=3)
            tarjetas = VGroup(c1, c2).arrange(RIGHT, buff=1.4).move_to([0, 0.6, 0])
            t1 = Text("Estimar", color=ESTIMACION, weight=BOLD).scale(0.7).move_to(c1)
            t2 = Text("Detectar", color=VERDE, weight=BOLD).scale(0.7).move_to(c2)
            p = Text("P", color=AMBAR, weight=BOLD).scale(2.2).move_to([0, 0.6, 0])
            self.corte()
            self.play(FadeIn(tarjetas), FadeIn(t1), FadeIn(t2), run_time=0.3)
            self.pop(p)

            # «la materia empieza aquí»
            self.en("empieza")
            self.corte()
            mapa = Mapa7(centro=(0, 0.2))
            self.play(Create(mapa.linea), LaggedStart(*[FadeIn(c) for c in mapa.circ], lag_ratio=0.08),
                      FadeIn(VGroup(*mapa.nums)), FadeIn(VGroup(*mapa.rot)), run_time=self.dur(0.9))
            self.play(*mapa.luz(0), run_time=self.dur(0.4))

            # «construimos el lenguaje»
            self.en("lenguaje")
            leng = Text("El lenguaje", color=AMBAR, weight=BOLD).scale(0.65).move_to([float(mapa.circ[0].get_x()), 1.5, 0])
            self.pop(leng)

            # «aprendemos a estimar y a decidir»
            self.en("estimar_decidir")
            self.play(*mapa.luz(1, ESTIMACION), *mapa.luz(2, VERDE), run_time=self.dur(0.5))
            ed = Text("Estimar y decidir", color=TXT, weight=BOLD).scale(0.6).move_to([-1.0, 1.5, 0])
            self.pop(ed)

            # «y al final»
            self.en("final")
            self.resaltar(mapa.circ[6], color=AMBAR, escala=1.3, run_time=0.6)

            # «señales enteras que cambian en el tiempo»
            self.en("enteras")
            self.play(*mapa.luz(3, SENAL), *mapa.luz(4, SENAL), *mapa.luz(5, SENAL), *mapa.luz(6, SENAL),
                      run_time=self.dur(0.6))
            se = Text("Señales enteras", color=SENAL, weight=BOLD).scale(0.6).move_to([3.9, 1.5, 0])
            self.pop(se)

            # «Empecemos por lo más básico»
            self.en("basico")
            resto = [mapa.linea, leng, ed, se] + mapa.circ[1:] + mapa.nums[1:] + mapa.rot
            self.play(*[FadeOut(m) for m in resto],
                      VGroup(mapa.circ[0], mapa.nums[0]).animate.move_to([0, 0.2, 0]).scale(2.2),
                      run_time=self.dur(0.6))

            # «algo que no se puede predecir»
            self.en("impredecible")
            Lr = Lienzo(ancho=5.0, alto=1.8, t_rango=(0, 1), v_max=1.5, centro=(0, -2.2))
            cr = Lr.curva(np.linspace(0, 1, 160), serie(14, 160, 0.5), RUIDO, 3.5)
            q = Text("?", color=ROJO, weight=BOLD).scale(1.4).move_to([3.2, -2.2, 0])
            self.play(Create(cr), run_time=self.dur(0.8), rate_func=linear)
            self.pop(q)
