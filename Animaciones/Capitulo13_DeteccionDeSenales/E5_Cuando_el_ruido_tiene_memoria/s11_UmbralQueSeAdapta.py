"""Escena 11 — Un umbral que se adapta a la lluvia, y el aviso: el filtro hereda el error de lo estimado."""
from comun.escena import *


class UmbralQueSeAdapta(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.radar()
        self.aviso()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def radar(self):
        n = 48
        x = datos_celdas(n=n)
        u = umbral_local(x, 2.6)
        L = Lienzo(ancho=11.0, alto=3.0, t_rango=(0, n - 1), v_max=6.0, centro=(0.0, -1.0))
        ks = np.arange(n)
        base = L.base()
        traza_ = L.curva(ks, x, RUIDO, 3)
        fijo = Line(L.p(0, 2.6), L.p(n - 1, 2.6), color=ESTIMACION, stroke_width=4)
        adapt = L.curva(ks, u, ESTIMACION, 5)
        falsas = VGroup(*[Dot(L.p(k, x[k]), radius=0.1, color=ERROR) for k in ks if x[k] > 2.6 and 20 <= k < 36])
        zona = Rectangle(width=L.x(35.5) - L.x(19.5), height=3.4, stroke_width=0).set_fill(RUIDO, 0.12)
        zona.move_to([(L.x(35.5) + L.x(19.5)) / 2, L.y(0) + 1.55, 0])
        sigma = MathTex(r"\sigma^2 = ?", color=AMBAR).scale(0.9).move_to([5.4, 3.3, 0])
        ant = antena(TXT).scale(0.8).move_to([-5.8, 2.2, 0])
        nube = nube_lluvia(INK).scale(0.9).move_to([L.x(27.5) - 0.4, 2.7, 0])
        k0 = 27
        celda = Rectangle(width=L.x(1) - L.x(0), height=3.4, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.25)
        celda.move_to([L.x(k0), L.y(0) + 1.55, 0])
        izq = Rectangle(width=L.x(7) - L.x(0), height=3.4, stroke_width=0).set_fill(AMBAR, 0.1)
        izq.move_to([L.x(k0 - 3.5 - 0.0) - 0.0, L.y(0) + 1.55, 0])
        der = izq.copy().move_to([L.x(k0 + 4.5 + 0.0) - 0.0, L.y(0) + 1.55, 0])
        l_izq = Text("sin avión", color=INK).scale(0.45).move_to([L.x(k0 - 3.5), L.y(0) - 0.35, 0])
        l_der = Text("sin avión", color=INK).scale(0.45).move_to([L.x(k0 + 4.5), L.y(0) - 0.35, 0])
        cfar = Text("CFAR", color=ESTIMACION, weight=BOLD).scale(0.6).move_to([5.8, 1.4, 0])
        perd = Text("pérdida: un par de dB", color=ERROR).scale(0.6).move_to([0, -3.5, 0])

        with self.narrar("b1"):
            # «lo único que no conocemos»
            self.en("unico")
            self.play(FadeIn(sigma, shift=UP * 0.1), run_time=self.dur(0.5))

            # «la varianza del ruido»
            self.en("var")
            self.play(Create(base), Create(traza_), run_time=self.dur(1.2))

            # «un problema con el umbral»
            self.en("problema")
            self.play(Create(fijo), run_time=self.dur(0.7))

            # «un radar donde llueve»
            self.en("radar")
            self.play(FadeIn(ant), FadeIn(nube), run_time=self.dur(0.8))

            # «el ruido es mayor»
            self.en("mayor")
            self.play(FadeIn(zona), run_time=self.dur(0.6))

            # «un umbral fijo»
            self.en("fijo")
            self.resaltar(fijo, color=AMBAR, escala=1.0)

            # «falsas alarmas sin parar»
            self.en("falsas")
            self.play(LaggedStart(*[GrowFromCenter(d) for d in falsas], lag_ratio=0.2), run_time=self.dur(1.2))

            # «recalcular el umbral»
            self.en("recalcular")
            self.play(fijo.animate.set_stroke(opacity=0.25), Create(adapt), run_time=self.dur(1.2))

            # «las celdas vecinas»
            self.en("celdas")
            self.play(FadeIn(celda), FadeIn(izq), FadeIn(der), run_time=self.dur(0.8))

            # «donde no hay avión»
            self.en("noavion")
            self.play(FadeIn(l_izq), FadeIn(l_der), run_time=self.dur(0.5))

            # «Un umbral que se adapta»
            self.en("adapta")
            self.play(FadeOut(falsas), FadeIn(cfar), run_time=self.dur(0.6))

            # «un par de decibelios»
            self.en("decibelios")
            self.pop(perd)
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def aviso(self):
        ws = np.linspace(0, np.pi, 80)
        rng = np.random.default_rng(21)
        L = lienzo_w(ancho=9.0, alto=3.0, base_y=-2.2)
        eje = eje_w(L)
        ideal = d_ruido(ws, 0.6)
        est_larga = ideal * (1 + 0.12 * np.convolve(rng.normal(0, 1, 80), np.ones(7) / 7, mode="same") * 2.0)
        est_corta = ideal * (1 + 0.5 * np.convolve(rng.normal(0, 1, 80), np.ones(4) / 4, mode="same") * 2.0)
        est_corta = np.clip(est_corta, 0.02, 1.15)
        c_ideal = L.curva(ws, ideal, INK, 3)
        c_larga = L.curva(ws, est_larga, RUIDO, 4)
        c_corta = L.curva(ws, est_corta, RUIDO, 4)

        def entre(est, color):
            arriba = np.column_stack([L.x(ws), L.y(np.maximum(est, ideal)), np.zeros(len(ws))])
            abajo = np.column_stack([L.x(ws[::-1]), L.y(np.minimum(est, ideal)[::-1]), np.zeros(len(ws))])
            m = VMobject(stroke_width=0, stroke_opacity=0).set_fill(color, 0.55)
            m.set_points_as_corners(np.vstack([arriba, abajo]))
            return m

        a_larga = entre(est_larga, ERROR)
        a_corta = entre(est_corta, ERROR)
        av = aviso_triangulo(AMBAR).scale(1.2).move_to([-5.8, 2.9, 0])
        filtro = caja("filtro", ESTIMACION, ancho=2.0, alto=0.8, scale=0.55).move_to([1.4, 2.9, 0])
        err_t = Text("error", color=ERROR, weight=BOLD).scale(0.6).move_to([-2.2, 2.9, 0])
        err_a = flecha([-1.55, 2.9, 0], filtro.get_left() + LEFT * 0.03, ERROR)
        est_t = Text("blanqueador estimado", color=RUIDO).scale(0.5).move_to([4.0, 1.8, 0])
        reg_largo = traza(np.linspace(-6.0, -1.0, 80), -3.3 + 0.28 * ruido_ar(80, 0.6, 3), color=RUIDO, ancho=3)
        reg_corto = traza(np.linspace(-6.0, -4.4, 24), -3.3 + 0.28 * ruido_ar(24, 0.6, 3), color=RUIDO, ancho=3)

        with self.narrar("b2"):
            # «Un aviso»
            self.en("aviso")
            self.corte()
            self.pop(av)

            # «hereda el error»
            self.en("hereda")
            self.play(FadeIn(filtro), FadeIn(err_t), GrowArrow(err_a), run_time=self.dur(0.8))

            # «lo que se ha estimado»
            self.en("estimado")
            self.play(Create(eje.base), FadeIn(eje.rotulos), Create(c_ideal), Create(c_larga), Create(reg_largo),
                      FadeIn(est_t), run_time=self.dur(1.2))

            # «nunca es perfecto»
            self.en("perfecto")
            self.play(FadeIn(a_larga), run_time=self.dur(0.6))

            # «cuanto más corto el registro»
            self.en("corto")
            self.play(ReplacementTransform(reg_largo, reg_corto), run_time=self.dur(0.9))

            # «peor»
            self.en("peor")
            self.play(ReplacementTransform(c_larga, c_corta), ReplacementTransform(a_larga, a_corta),
                      run_time=self.dur(1.0))
