"""Escena 10 — Con gaussianas, la media condicional es la recta y la varianza de cada rebanada es el error."""
from comun.escena import *
from comun.figuras_c8e4 import *

MU_X, SIG_Y = 0.8, float(np.sqrt(0.8))     # media condicional = 0,8 · x; varianza de cada rebanada 0,8
CUBO = 2.2                                  # cuánto se estira la campana (unidades del eje por unidad de densidad)


class LasGaussianas(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.elipse_y_rebanadas()
        self.una_recta()
        self.lo_lineal()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ utilidades
    def campana(self, ax, x0, color=AMBAR, opacidad=0.28):
        """Campana de Y dado X = x0, tumbada sobre la rebanada (nace en la línea vertical x = x0)."""
        ys = np.linspace(MU_X * x0 - 3 * SIG_Y, MU_X * x0 + 3 * SIG_Y, 60)
        dens = gaussiana(ys, MU_X * x0, SIG_Y)
        pts = [ax.c2p(x0 + CUBO * d, y) for d, y in zip(dens, ys)]
        cerrada = pts + [ax.c2p(x0, ys[-1]), ax.c2p(x0, ys[0])]
        m = VMobject(stroke_color=color, stroke_width=3).set_fill(color, opacidad)
        m.set_points_as_corners(np.array(cerrada))
        return m

    # ------------------------------------------------------------ b1
    def elipse_y_rebanadas(self):
        ax, etq = ejes([-6, 6, 2], [-5, 5, 2], ancho=6.4, alto=5.0, x_label=r"\text{Lectura}", y_label=r"\text{Temperatura}")
        g = VGroup(ax, etq).move_to([-3.4, -0.3, 0])
        self.ax = ax
        rng = np.random.default_rng(5)
        yv = rng.normal(0, 2.0, 150)
        xv = yv + rng.normal(0, 1.0, 150)
        nube = VGroup(*[Dot(ax.c2p(x, y), radius=0.045, color=SENAL).set_opacity(0.85)
                        for x, y in zip(xv, yv) if abs(x) < 5.8 and abs(y) < 4.8])
        L = np.linalg.cholesky(np.array([[5.0, 4.0], [4.0, 4.0]]))
        th = np.linspace(0, TAU, 120)
        el = np.array([2.0 * L @ np.array([np.cos(t), np.sin(t)]) for t in th])
        elipse = VMobject(stroke_color=TXT, stroke_width=3).set_fill(opacity=0)
        elipse.set_points_as_corners(np.array([ax.c2p(a, b) for a, b in el] + [ax.c2p(*el[0])]))
        xs3 = (-3.0, 0.0, 3.0)
        franjas = VGroup(*[Rectangle(width=abs(ax.c2p(0.5, 0)[0] - ax.c2p(0, 0)[0]), height=abs(ax.c2p(0, 5)[1] - ax.c2p(0, -5)[1]),
                                     stroke_width=0).set_fill(MEDIDA, 0.2).move_to(ax.c2p(x, 0)) for x in xs3])
        campanas = VGroup(*[self.campana(ax, x) for x in xs3])
        centros = VGroup(*[Dot(ax.c2p(x, MU_X * x), radius=0.11, color=ESTIMACION) for x in xs3])
        recta = Line(ax.c2p(-5.5, -MU_X * 5.5), ax.c2p(5.5, MU_X * 5.5), color=ESTIMACION, stroke_width=5)
        t_rec = Text("Recta de pendiente 0,8", color=ESTIMACION).scale(0.55).move_to([3.5, 2.6, 0])
        anchos = VGroup(*[DoubleArrow(ax.c2p(x - 0.5, MU_X * x - SIG_Y), ax.c2p(x - 0.5, MU_X * x + SIG_Y), buff=0,
                                      color=TXT, stroke_width=3, tip_length=0.15) for x in xs3])
        v08 = Text("Varianza 0,8", color=TXT).scale(0.6).move_to([3.5, 1.4, 0])
        # las dos campanitas del principio
        cb = Axes(x_range=[-3, 3], y_range=[0, 0.5], x_length=2.0, y_length=1.0)
        cb_a = cb.plot(lambda x: gaussiana(x, 0, 1), x_range=[-3, 3], color=SENAL, stroke_width=4).move_to([2.9, 2.6, 0])
        cb_r = cb.plot(lambda x: gaussiana(x, 0, 1), x_range=[-3, 3], color=RUIDO, stroke_width=4).move_to([5.6, 2.6, 0])
        t_a = Text("Temperatura", color=SENAL).scale(0.5).next_to(cb_a, DOWN, buff=0.2)
        t_r = Text("Ruido", color=RUIDO).scale(0.5).next_to(cb_r, DOWN, buff=0.2)
        mas = MathTex("+", color=TXT).scale(1.1).move_to([4.25, 2.6, 0])
        ok = tilde(VERDE, 0.5).move_to([4.25, 1.4, 0])
        # la franja que viaja
        tr = ValueTracker(-4.0)
        viaja = always_redraw(lambda: VGroup(
            Rectangle(width=franjas[0].width, height=franjas[0].height, stroke_width=0).set_fill(VERDE, 0.2)
            .move_to(ax.c2p(tr.get_value(), 0)),
            self.campana(ax, tr.get_value(), VERDE, 0.3),
            Dot(ax.c2p(tr.get_value(), MU_X * tr.get_value()), radius=0.11, color=VERDE)))

        with self.narrar("b1"):
            # «El segundo caso es el gaussiano»
            self.en("gauss")
            self.corte()
            self.play(Create(ax), FadeIn(etq), run_time=self.dur(1.0))

            # «Si la temperatura y el ruido»
            self.en("dosg")
            self.play(Create(cb_a), FadeIn(t_a), FadeIn(mas), Create(cb_r), FadeIn(t_r), run_time=self.dur(1.2))

            # «son gaussianos»
            self.en("songauss")
            self.play(FadeIn(ok, scale=0.4), run_time=self.dur(0.4))

            # «la nube de puntos»
            self.en("nube")
            self.play(FadeOut(cb_a), FadeOut(cb_r), FadeOut(t_a), FadeOut(t_r), FadeOut(mas), FadeOut(ok),
                      run_time=self.dur(0.3))
            self.play(LaggedStart(*[FadeIn(d, scale=0.3) for d in nube], lag_ratio=0.02), run_time=self.dur(1.5))

            # «elipse inclinada»
            self.en("elipse")
            self.play(Create(elipse), run_time=self.dur(1.2))

            # «rebanadas verticales»
            self.en("rebanadas")
            self.play(FadeIn(franjas), run_time=self.dur(0.8))

            # «cada rebanada es una campana»
            self.en("campanas")
            self.play(LaggedStart(*[FadeIn(c) for c in campanas], lag_ratio=0.3), run_time=self.dur(1.2))

            # «Sus centros caen»
            self.en("centros")
            self.play(LaggedStart(*[FadeIn(d, scale=0.3) for d in centros], lag_ratio=0.3), run_time=self.dur(0.9))

            # «sobre una recta»
            self.en("recta")
            self.play(Create(recta), run_time=self.dur(0.8))

            # «la del cero coma ocho»
            self.en("r08")
            self.play(FadeIn(t_rec), run_time=self.dur(0.5))

            # «Y todas las campanas»
            self.en("todas")
            self.resaltar(*campanas, color=AMBAR, escala=1.04)

            # «el mismo ancho»
            self.en("ancho")
            self.play(*[Create(a) for a in anchos], run_time=self.dur(0.7))

            # «varianza cero coma ocho»
            self.en("v08")
            self.play(FadeIn(v08), run_time=self.dur(0.5))

            # «marque lo que marque el termómetro»
            self.en("marque")
            self.play(FadeOut(franjas), FadeOut(campanas), FadeOut(centros), FadeOut(anchos), run_time=self.dur(0.3))
            self.add(viaja)
            self.play(tr.animate.set_value(4.0), run_time=self.dur(1.4))
            self.play(tr.animate.set_value(-1.0), run_time=self.dur(0.9))
        viaja.clear_updaters()
        self.cosas = VGroup(v08, t_rec)
        self.viaja, self.recta, self.nube, self.elipse_m, self.franjas = viaja, recta, nube, elipse, franjas

    # ------------------------------------------------------------ b2
    def una_recta(self):
        ax = self.ax
        c1 = formula(r"E[Y\,|\,X]", "=", r"\text{Recta}", escala=1.2, colores={0: SENAL, 2: ESTIMACION}).move_to([3.7, 2.9, 0])
        ok = tilde(VERDE, 0.45).move_to([1.7, 2.0, 0])
        t_ok = Text("La del episodio 3", color=VERDE).scale(0.55).move_to([4.1, 2.0, 0])
        caja1 = caja("Mejor posible", VERDE, ancho=3.8, alto=0.8).move_to([3.7, 0.9, 0])
        caja2 = caja("Mejor lineal", AMBAR, ancho=3.8, alto=0.8).move_to([3.7, -0.5, 0])
        igual = MathTex("=", color=TXT).scale(1.3).move_to([3.7, 0.2, 0])
        nada = Text("No se pierde nada", color=VERDE).scale(0.6).move_to([3.7, -1.5, 0])
        vv = Text("Varianza = 0,8", color=TXT).scale(0.6).move_to([3.7, -2.3, 0])
        er = Text("Error de la recta = 0,8", color=ERROR).scale(0.6).move_to([3.7, -3.1, 0])
        cs = VGroup(*[self.campana(ax, x) for x in (-3.0, 0.0, 3.0)])

        with self.narrar("b2"):
            # fuera lo de la escena anterior y vuelven las campanas
            self.play(FadeOut(self.cosas), FadeOut(self.viaja), FadeIn(cs), run_time=0.3)

            # «la media condicional ya es una recta»
            self.en("condrec")
            self.play(*[FadeIn(c1[i]) for i in range(len(c1))], run_time=self.dur(0.9))

            # «la misma que da la fórmula»
            self.en("misma")
            self.play(FadeIn(ok, scale=0.4), FadeIn(t_ok), run_time=self.dur(0.6))

            # «La mejor estimación posible»
            self.en("posible")
            self.play(FadeIn(caja1, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «la mejor estimación lineal»
            self.en("lineal")
            self.play(FadeIn(caja2, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «son la misma»
            self.en("igual")
            self.pop(igual)

            # «no se pierde nada»
            self.en("nada")
            self.play(FadeIn(nada), run_time=self.dur(0.5))

            # «la varianza de cada rebanada»
            self.en("varreb")
            self.resaltar(*cs, color=AMBAR, escala=1.04)

            # «cero coma ocho»
            self.en("v08")
            self.play(FadeIn(vv), run_time=self.dur(0.5))

            # «el error de la recta»
            self.en("errrecta")
            self.play(FadeIn(er), run_time=self.dur(0.6))

    # ------------------------------------------------------------ b3
    def lo_lineal(self):
        filtro = caja("Filtro lineal", AMBAR, ancho=3.8, alto=1.0).move_to([-3.6, 2.2, 0])
        flecha_c = flecha([-1.4, 2.2, 0], [0.8, 2.2, 0], INK, 4)
        caps = Text("Capítulos 10 a 13", color=TXT).scale(0.65).move_to([3.4, 2.2, 0])
        xs = np.linspace(-3, 3, 80)
        cb_g = traza(-3.6 + xs * 0.45, -0.6 + 1.5 * gaussiana(xs, 0, 1) * 1.4, RUIDO, 4)
        base = Line([-5.2, -0.6, 0], [-2.0, -0.6, 0], color=INK, stroke_width=2)
        mezcla = 0.55 * gaussiana(xs, -0.8, 0.8) + 0.45 * gaussiana(xs, 1.3, 0.6)
        cb_t = traza(-3.6 + xs * 0.45, -0.6 + 1.5 * mezcla * 1.4, RUIDO, 4)
        t_g = Text("Ruido gaussiano", color=RUIDO).scale(0.55).move_to([-3.6, -1.2, 0])
        t_n = Text("Ruido no gaussiano", color=RUIDO).scale(0.55).move_to([-3.6, -1.2, 0])
        opt = Text("Lineal = óptimo", color=VERDE).scale(0.7).move_to([3.2, -0.2, 0])
        ok = tilde(VERDE, 0.5).next_to(opt, LEFT, buff=0.2)
        mejor = Text("Lo mejor entre las rectas", color=ESTIMACION).scale(0.7).move_to([3.2, -0.2, 0])
        chips = VGroup(*[caja(t, SENAL if i == 0 else (RUIDO if i == 1 else MEDIDA), ancho=3.3, alto=0.8)
                         for i, t in enumerate(("Medias", "Varianzas", "Covarianzas"))]).arrange(RIGHT, buff=0.4).move_to([0, -3.0, 0])

        with self.narrar("b3"):
            # «resto de la materia»
            self.en("resto")
            self.corte()
            self.play(FadeIn(filtro), Create(flecha_c), FadeIn(caps), run_time=self.dur(1.0))

            # «filtros lineales»
            self.en("filtros")
            self.resaltar(filtro, color=AMBAR, escala=1.08)

            # «El ruido suele ser gaussiano»
            self.en("ruido")
            self.play(Create(base), Create(cb_g), FadeIn(t_g), run_time=self.dur(0.9))

            # «lo lineal ya es lo óptimo»
            self.en("optimo")
            self.play(FadeIn(ok, scale=0.4), FadeIn(opt), run_time=self.dur(0.6))

            # «Cuando no lo es»
            self.en("noes")
            self.play(ReplacementTransform(cb_g, cb_t), ReplacementTransform(t_g, t_n), FadeOut(opt), FadeOut(ok),
                      run_time=self.dur(0.9))

            # «lo mejor que se puede hacer»
            self.en("mejor")
            self.play(FadeIn(mejor), run_time=self.dur(0.6))

            # «medias, varianzas y covarianzas»
            self.en("tres")
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in chips], lag_ratio=0.3), run_time=self.dur(1.2))
