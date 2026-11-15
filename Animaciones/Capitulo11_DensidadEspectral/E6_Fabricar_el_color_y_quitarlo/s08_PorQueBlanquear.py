"""Escena 08 — Blanquear un ruido coloreado: para qué sirve y cómo es el filtro blanqueador."""
from comun.escena import *


class PorQueBlanquear(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        g, b, ent, sal = cadena_bloques("blanco", "H", "coloreado", centro=(-1.0, 2.7), color=CIAN)
        vuelta = CurvedArrow([2.4, 2.1, 0], [-4.6, 2.1, 0], angle=-TAU / 6, color=AMBAR, stroke_width=4)
        c12 = etiqueta("Cap. 12", AMBAR, 0.55).move_to([5.0, 3.5, 0])
        c13 = etiqueta("Cap. 13", AMBAR, 0.55).move_to([5.0, 2.8, 0])
        Lc = Lienzo(ancho=3.6, alto=1.2, t_rango=(0, 3), v_max=1.0, centro=(-4.4, -0.2))
        trc = traza(Lc.x(np.linspace(0, 3, 150)), Lc.y(0.8 * serie(5, 150, 0.9)), RUIDO, 3.5)
        Ec = Lienzo(ancho=2.6, alto=1.4, t_rango=(-np.pi, np.pi), v_max=6.5, centro=(-4.4, -1.9))
        cc = curva_f(Ec, psd_eco, -np.pi, np.pi, RUIDO, 4)
        Lb = Lienzo(ancho=3.6, alto=1.2, t_rango=(0, 3), v_max=1.0, centro=(4.4, -0.2))
        trb = traza(Lb.x(np.linspace(0, 3, 150)), Lb.y(0.8 * serie(6, 150, 0.0)), TXT, 3.0)
        Eb = Lienzo(ancho=2.6, alto=1.4, t_rango=(-np.pi, np.pi), v_max=6.5, centro=(4.4, -1.9))
        cb = Eb.curva(np.array([-np.pi, np.pi]), np.array([2.0, 2.0]), TXT, 4)
        flecha_c = flecha([-1.7, -0.9, 0], [1.7, -0.9, 0], AMBAR, 4)
        q = MathTex("?", color=AMBAR).scale(2.5).move_to([0, 1.2, 0])
        c_est = caja("estimar", ESTIMACION, ancho=2.6, alto=1.0, scale=0.65).move_to([-3.2, 0.4, 0])
        c_det = caja("detectar", ESTIMACION, ancho=2.6, alto=1.0, scale=0.65).move_to([3.2, 0.4, 0])
        ok1 = VGroup(tilde(VERDE, 0.4), etiqueta("ruido blanco", TXT, 0.55)).arrange(RIGHT, buff=0.25).move_to([-3.2, -0.9, 0])
        ok2 = VGroup(tilde(VERDE, 0.4), etiqueta("ruido blanco", TXT, 0.55)).arrange(RIGHT, buff=0.25).move_to([3.2, -0.9, 0])
        t_bl = self.palabra("blanquear", AMBAR, 1.0).move_to([-3.4, -2.5, 0])
        fl = flecha([-1.4, -2.5, 0], [-0.2, -2.5, 0], INK, 3)
        t_ap = etiqueta("aplicar lo que ya sabemos", TXT, 0.6).move_to([3.2, -2.5, 0])
        with self.narrar("b1"):
            # «el camino contrario»
            self.en("contrario")
            self.play(FadeIn(g), run_time=self.dur(0.7))
            self.play(Create(vuelta), run_time=self.dur(0.6))

            # «los dos capítulos siguientes»
            self.en("siguientes")
            self.play(FadeIn(c12), FadeIn(c13), run_time=0.5)

            # «un ruido coloreado»
            self.en("coloreado")
            self.play(Create(Lc.base()), Create(trc), Create(Ec.base()), Create(cc), run_time=self.dur(1.2))

            # «convertirlo en blanco»
            self.en("blanco")
            self.play(GrowArrow(flecha_c), run_time=0.4)
            self.play(Create(Lb.base()), Create(trb), Create(Eb.base()), Create(cb), run_time=self.dur(1.2))

            # «¿Para qué?»
            self.en("paraque")
            self.corte()
            self.pop(q)

            # «estimación y de detección»
            self.en("est")
            self.play(FadeOut(q), FadeIn(c_est), FadeIn(c_det), run_time=self.dur(0.7))

            # «solución conocida cuando el ruido es blanco»
            self.en("conocida")
            self.play(FadeIn(ok1), FadeIn(ok2), run_time=self.dur(0.8))

            # «La estrategia»
            self.en("estrategia")
            self.play(GrowArrow(fl), run_time=0.4)

            # «blanquear primero»
            self.en("primero")
            self.pop(t_bl)

            # «lo que ya sabemos»
            self.en("sabemos")
            self.play(FadeIn(t_ap), run_time=self.dur(0.6))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        blq = BloqueLTI("1/H", centro=(-3.0, 3.0), ancho=1.8, alto=1.0, largo=1.2, color=AMBAR)
        t_nom = self.palabra("blanqueador", AMBAR, 0.9).move_to([3.0, 3.0, 0])
        F = formula(r"|H_w|^2", "=", r"\frac{\sigma_w^2}{S_{xx}}", escala=1.2, colores={0: AMBAR}).move_to([0, 1.5, 0])
        Es = Lienzo(ancho=3.2, alto=1.6, t_rango=(-np.pi, np.pi), v_max=6.5, centro=(-4.4, -1.4))
        cs = curva_f(Es, psd_eco, -np.pi, np.pi, RUIDO, 4)
        Eg = Lienzo(ancho=3.2, alto=1.6, t_rango=(-np.pi, np.pi), v_max=6.5, centro=(0, -1.4))
        cg = curva_f(Eg, lambda w: 1.0 / psd_eco(w) * 3.0, -np.pi, np.pi, AMBAR, 4)
        Ep = Lienzo(ancho=3.2, alto=1.6, t_rango=(-np.pi, np.pi), v_max=6.5, centro=(4.4, -1.4))
        cp = Ep.curva(np.array([-np.pi, np.pi]), np.array([3.0, 3.0]), TXT, 4)
        por = MathTex(r"\times", color=INK).scale(1.0).move_to([-2.2, -1.4, 0])
        ig = MathTex("=", color=INK).scale(1.0).move_to([2.2, -1.4, 0])
        t_s = etiqueta("ruido", RUIDO, 0.5).move_to([-4.4, -2.7, 0])
        t_g = etiqueta("blanqueador", AMBAR, 0.5).move_to([0, -2.7, 0])
        t_p = etiqueta("plano", TXT, 0.5).move_to([4.4, -2.7, 0])
        zona = area_f(Eg, lambda w: 1.0 / psd_eco(w) * 3.0, -np.pi, -2.2, AMBAR, 0.5)
        zona2 = area_f(Eg, lambda w: 1.0 / psd_eco(w) * 3.0, 2.2, np.pi, AMBAR, 0.5)
        zb = area_f(Es, psd_eco, -0.7, 0.7, RUIDO, 0.5)
        g, b, ent, sal = cadena_bloques("blanco", "H", "coloreado", centro=(-1.0, 3.2), color=CIAN)
        g2, b2, ent2, sal2 = cadena_bloques("coloreado", "1/H", "blanco", centro=(-1.0, 1.4), color=AMBAR)
        with self.narrar("b2"):
            # «se llama blanqueador»
            self.en("nombre")
            self.corte()
            self.play(FadeIn(blq), run_time=self.dur(0.6))
            self.pop(t_nom)

            # «una constante dividida entre la densidad espectral»
            self.en("formula")
            self.play(FadeIn(F[0:2]), run_time=self.dur(0.6))
            self.play(FadeIn(F[2]), run_time=self.dur(1.0))

            # «Amplifica donde el ruido tiene poca potencia»
            self.en("amplifica")
            self.play(Create(Es.base()), Create(cs), FadeIn(t_s), run_time=self.dur(0.8))
            self.play(Create(Eg.base()), Create(cg), FadeIn(t_g), run_time=self.dur(1.0))
            self.play(FadeIn(zb), FadeIn(zona), FadeIn(zona2), run_time=0.5)

            # «atenúa donde tiene mucha»
            self.en("atenua")
            self.play(zb.animate.set_fill(RUIDO, 0.15), zona.animate.set_fill(AMBAR, 0.15),
                      zona2.animate.set_fill(AMBAR, 0.15), run_time=0.5)
            za = area_f(Eg, lambda w: 1.0 / psd_eco(w) * 3.0, -0.7, 0.7, AMBAR, 0.5)
            self.play(FadeIn(za), run_time=0.5)

            # «hasta dejarlo plano»
            self.en("plano")
            self.play(FadeIn(por), run_time=0.3)
            self.play(FadeIn(ig), Create(Ep.base()), Create(cp), FadeIn(t_p), run_time=self.dur(1.0))

            # «convertía blanco en coloreado»
            self.en("convertia")
            self.corte()
            self.play(FadeIn(g), run_time=self.dur(0.8))

            # «el blanqueador es su inverso»
            self.en("inverso")
            self.play(FadeIn(g2), run_time=self.dur(0.8))
