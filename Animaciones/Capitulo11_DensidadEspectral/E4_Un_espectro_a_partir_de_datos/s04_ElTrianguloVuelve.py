"""Escena 04 — Einstein, Wiener y Khinchin, y el triángulo del episodio 2 que vuelve."""
from comun.escena import *

TIEMPOS = [x - 8 for x in cambios_tel(4, 16.0)]


class ElTrianguloVuelve(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.laboratorio()
        self.camino()
        self.triangulo()
        self.wait(1.0)
        self.limpiar()

    def laboratorio(self):
        L = Lienzo(ancho=11.0, alto=1.6, t_rango=(-8, 8), v_max=1.4, centro=(0, 3.0))
        onda = onda_tel(L, TIEMPOS, 1, SENAL, 4.0).set_stroke(opacity=0.25)
        dentro = onda_tel(L, TIEMPOS, nivel_en(-5, TIEMPOS), SENAL, 4.5, t0=-5, t1=5)
        marco = marco_t(L, -5, 5, 1.4, AMBAR, 0.12)
        marco_g = marco_t(L, -8, 8, 1.4, AMBAR, 0.12)
        w = np.linspace(-8, 8, 161)
        vals = psd_tele(w) * periodograma_blanco(31, 161) * 0.9
        P = Lienzo(ancho=6.4, alto=3.2, t_rango=(-8, 8), v_max=2.4, centro=(3.6, -3.0))
        f = lambda x: np.interp(x, w, vals)
        ej = ejes_L(P, 0, 2.3)
        pg = curva_f(P, f, -8, 8, MEDIDA, 3.5, n=161)
        area_pg = area_f(P, f, -8, 8, AMBAR, 0.35, n=161)
        pila = VGroup(*[curva_f(P, lambda x, s=s: np.interp(x, w, psd_tele(w) * periodograma_blanco(40 + s, 161) * 0.9),
                                -8, 8, MEDIDA, 1.6).set_stroke(opacity=0.3) for s in range(14)])
        suave = curva_f(P, psd_tele, -8, 8, AMBAR, 5, n=161)
        e10 = MathTex(r"E=\int x^2\,dt=10", color=TXT).scale(0.8).move_to([-4.4, 1.0, 0])
        p1 = MathTex(r"\frac{10}{10\,\mathrm{s}}=1", color=TXT).scale(0.9).move_to([-4.6, -0.5, 0])
        ok1 = tilde(VERDE, 0.4).move_to([-2.8, -0.5, 0])
        etq = MathTex(r"\tfrac{1}{2\pi}\cdot\mathrm{area}=1", color=AMBAR).scale(0.7).move_to([3.6, -0.9, 0])
        lim = MathTex(r"T\to\infty", color=AMBAR).scale(0.9).move_to([-4.4, 1.7, 0])
        s_lab = MathTex(r"S_{xx}(j\omega)", color=AMBAR).scale(0.8).move_to([5.6, -1.7, 0])
        ewk = formula(r"S_{xx}(j\omega)", "=", r"\lim_{T\to\infty}", r"\frac{1}{2T}", r"E\!\left[|X_T(j\omega)|^2\right]",
                      escala=0.85, colores={0: AMBAR, 4: MEDIDA}).move_to([-1.0, 0.45, 0])
        with self.narrar("b1"):
            self.en("e10")
            self.play(Create(L.base()), FadeIn(onda), FadeIn(dentro), FadeIn(marco), FadeIn(e10), run_time=self.dur(0.8))
            self.en("p1")
            self.play(FadeIn(p1), run_time=0.4)
            self.pop(ok1)
            self.en("area1")
            self.play(Create(ej), Create(pg), FadeIn(area_pg), run_time=self.dur(0.9))
            self.play(FadeIn(etq), run_time=0.3)
            self.en("da_uno")
            self.resaltar(etq)
            self.en("esperanza")
            self.play(FadeOut(e10), FadeOut(p1), FadeOut(ok1), FadeOut(area_pg), FadeOut(etq),
                      FadeIn(pila), run_time=self.dur(0.6))
            self.play(FadeOut(pila), ReplacementTransform(pg, suave), run_time=self.dur(0.8))
            self.en("limite")
            self.play(ReplacementTransform(marco, marco_g), FadeOut(dentro), FadeIn(lim), run_time=self.dur(0.9))
            self.en("densidad")
            self.play(FadeIn(s_lab), run_time=0.3)
            self.resaltar(suave, color=AMBAR, escala=1.05)
            self.en("ewk")
            self.play(LaggedStart(*[FadeIn(ewk[i]) for i in range(5)], lag_ratio=0.5), run_time=self.dur(2.8))

    def camino(self):
        lab = caja("laboratorio", MEDIDA, ancho=3.4).move_to([-4.3, 2.4, 0])
        aut = caja("autocorrelación", SENAL, ancho=3.8).move_to([4.3, 2.4, 0])
        f1 = flecha([-4.3, 1.9, 0], [-1.2, 0.2, 0], MEDIDA)
        f2 = flecha([4.3, 1.9, 0], [1.2, 0.2, 0], SENAL)
        C = Lienzo(ancho=3.4, alto=1.8, t_rango=(-8, 8), v_max=1.3, centro=(0, -0.8))
        ej_c = ejes_L(C, 0, 1.2)
        curva = curva_f(C, psd_tele, -8, 8, AMBAR, 5)
        ok = tilde(VERDE, 0.6).move_to([2.8, -0.8, 0])
        L = Lienzo(ancho=11.0, alto=1.8, t_rango=(-8, 8), v_max=1.4, centro=(0, 2.4))
        marco = marco_t(L, -5, 5, 1.4, AMBAR, 0.12)
        e_m = MathTex("-T", color=AMBAR).scale(0.8).move_to(L.p(-5, -1.4) + DOWN * 0.38)
        e_p = MathTex("T", color=AMBAR).scale(0.8).move_to(L.p(5, -1.4) + DOWN * 0.38)
        interr = MathTex("?", color=ROJO).scale(2.6).move_to([0, -0.4, 0])
        U = Lienzo(ancho=11.0, alto=1.4, t_rango=(-8, 8), v_max=1.4, centro=(0, 0.7))

        def rect(a, b, color, op):
            p, q = U.p(a, -0.55), U.p(b, 0.55)
            return Rectangle(width=q[0] - p[0], height=q[1] - p[1], color=color, stroke_width=3).set_fill(color, op).move_to(
                [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2, 0])
        fijo = rect(-5, 5, SENAL, 0.25)
        mov = rect(-2, 8, AMBAR, 0.25)
        com = rect(-2, 5, VERDE, 0.7)
        e_fijo = MathTex(r"x(\sigma)", color=SENAL).scale(0.8).move_to(U.p(-5.5, 0) + UP * 1.1)
        e_mov = MathTex(r"x(\sigma-\tau)", color=AMBAR).scale(0.8).move_to(U.p(5.5, 0) + UP * 1.1)
        e2 = etiqueta("como en el episodio 2", INK, 0.5).move_to([0, -1.5, 0])
        with self.narrar("b2"):
            self.en("lab")
            self.corte()
            self.play(FadeIn(lab), FadeIn(aut), Create(f1), Create(f2), run_time=self.dur(0.8))
            self.en("mismo")
            self.play(Create(ej_c), Create(curva), run_time=self.dur(0.7))
            self.pop(ok)
            self.en("finita")
            self.corte()
            self.play(Create(L.base()), FadeIn(marco), FadeIn(e_m), FadeIn(e_p), run_time=self.dur(0.6))
            self.en("antes")
            self.pop(interr)
            self.en("vuelve")
            self.play(FadeOut(interr), FadeOut(L.base()), ReplacementTransform(marco, fijo), FadeOut(e_m), FadeOut(e_p),
                      FadeIn(e2), run_time=self.dur(0.7))
            self.en("copia")
            self.play(FadeIn(mov), FadeIn(e_fijo), FadeIn(e_mov), run_time=self.dur(0.6))
            self.en("dentro")
            self.resaltar(fijo, color=SENAL)
            self.en("solapan")
            self.play(FadeIn(com), run_time=self.dur(0.6))

    def triangulo(self):
        U = Lienzo(ancho=11.0, alto=1.4, t_rango=(-15, 15), v_max=1.4, centro=(0, 2.5))
        V = Lienzo(ancho=11.0, alto=2.6, t_rango=(-15, 15), v_max=1.25, centro=(0, -0.9))
        d = ValueTracker(-10.0)

        def rect(a, b, color, op, sw=3):
            p, q = U.p(a, -0.55), U.p(b, 0.55)
            return Rectangle(width=q[0] - p[0], height=q[1] - p[1], color=color, stroke_width=sw).set_fill(color, op).move_to(
                [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2, 0])

        fijo = rect(-5, 5, SENAL, 0.25)
        mov = always_redraw(lambda: rect(d.get_value() - 5, d.get_value() + 5, AMBAR, 0.25))

        def comun_():
            x = d.get_value()
            a, b = max(-5, x - 5), min(5, x + 5)
            return rect(a, b, VERDE, 0.7, 0) if b - a > 0.05 else VMobject()
        com = always_redraw(comun_)
        ej_v = ejes_L(V, -0.1, 1.2)
        tri = V.curva([-10, 0, 10], [0, 1, 0], AMBAR, 5)
        e2 = etiqueta("episodio 2 · escena 08", INK, 0.5).move_to([4.6, 3.75, 0])
        ok_e2 = tilde(VERDE, 0.4).move_to([2.2, 3.75, 0])
        f = formula(r"R_{xx}(\tau)", r"\cdot", r"\text{triángulo}(\tau)", escala=0.9, colores={2: AMBAR}).move_to([-1.2, -3.3, 0])
        tach = Line(f[0].get_corner(DL) + DL * 0.05, f[0].get_corner(UR) + UR * 0.05, color=ROJO, stroke_width=6)
        doc = documento(INK).scale(0.9).move_to([5.3, -3.0, 0])
        doc_t = etiqueta("apunte en profundidad", INK, 0.45).move_to([5.3, -3.75, 0])
        E = Lienzo(ancho=3.0, alto=1.0, t_rango=(-6, 6), v_max=1.2, centro=(5.3, -3.3))
        ej_e = ejes_L(E, 0, 1.1)
        pr = MathTex("?", color=AMBAR).scale(1.2).move_to([5.3, -2.9, 0])
        fl_e = flecha([1.6, -3.3, 0], [3.6, -3.3, 0], AMBAR)
        with self.narrar("b3"):
            self.en("rects")
            self.corte()
            self.add(com)
            self.play(Create(U.base()), FadeIn(fijo), FadeIn(mov), Create(ej_v), run_time=self.dur(0.9))
            self.en("triangulo")
            self.play(d.animate(rate_func=linear).set_value(10.0), Create(tri, rate_func=linear), run_time=self.dur(1.7))
            self.en("dos_eps")
            self.play(FadeIn(e2), run_time=0.3)
            self.pop(ok_e2)
            self.en("finita2")
            self.resaltar(fijo, color=SENAL)
            self.en("nor")
            self.play(FadeIn(f[0]), run_time=0.3)
            self.play(Create(tach), run_time=0.3)
            self.en("portri")
            self.play(FadeOut(tach), FadeIn(f[1]), FadeIn(f[2]), run_time=self.dur(0.6))
            self.en("apunte")
            self.play(FadeIn(doc), FadeIn(doc_t), run_time=self.dur(0.5))
            self.en("importante")
            self.resaltar(f, color=AMBAR)
            self.en("alespectro")
            self.play(FadeOut(doc), FadeOut(doc_t), Create(fl_e), Create(ej_e), run_time=self.dur(0.6))
            self.pop(pr)
        com.clear_updaters()
        mov.clear_updaters()
